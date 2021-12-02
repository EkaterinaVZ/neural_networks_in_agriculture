import os
import re
import shutil

from PIL import Image
from bs4 import BeautifulSoup
from icrawler import Parser

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from icrawler.builtin import GoogleImageCrawler
# Названия Каталогов = параметр поиска в Google
param1 = 'ants'
param2 = 'ladybug'

count = 1000


class GoogleParser(Parser):
    def parse(self, response):
        soup = BeautifulSoup(
            response.content.decode('utf-8', 'ignore'), 'lxml')
        image_divs = soup.find_all(name='script')
        for div in image_divs:
            txt = str(div)
            if 'AF_initDataCallback' not in txt:
                continue
            if 'ds:0' in txt or 'ds:1' not in txt:
                continue
            uris = re.findall(r'http[^\[]*?\.(?:jpg)', txt)
            return [{'file_url': uri} for uri in uris]


class DataCreator:
    # Каталог с данными для обучения, проверки, тестирования
    TRAIN_DIR_NAMES = ['train', 'test']
    # Часть набора данных для проверки
    DATA_PORTION = [50, 25, 25]

    def __init__(self, quantity, param1, param2, uploads=True):
        self.param = [param1, param2]
        self.quantity = quantity
        self.uploads = uploads

    def run(self):
        self.uploads_images()

    def uploads_images(self):
        if self.uploads:
            for i in self.param:
                # if i == self.param[0] or i == self.param[2]:
                #     color = 'red'
                #     i = i
                # else:
                #     color = 'yellow'
                #     i = i
                google_crawler = GoogleImageCrawler(storage={'root_dir': i}, parser_cls=GoogleParser)
                google_crawler.crawl(keyword=i, filters=dict(date=((2013, 1, 1), (2020, 8, 30))),
                                     max_num=self.quantity)

        self.create_directory()

    def correct_to_jpeg(self, path):
        for i in range(500):
            print(i)
        dirs = os.listdir(path)
        for dir in dirs:
            path_dir = os.path.join(path, dir)
            images = os.listdir(path_dir)
            for im_name in images:
                path_im = os.path.join(path_dir, im_name)
                im = Image.open(path_im)
                im.convert('RGB').save(path_im, "JPEG")

    def create_directory(self):
        for param in self.param:
            for dirpath, dirnames, filenames in os.walk(param):
                for i, file in enumerate(filenames):
                    print(i)
                    shutil.move(dirpath + "\\" + file, dirpath + "\\" + param + "." + str(i) + ".jpg")
        for name in self.TRAIN_DIR_NAMES:
            if os.path.exists(name):
                shutil.rmtree(name)
            os.makedirs(name)
            os.makedirs(os.path.join(name, self.param[0]))
            os.makedirs(os.path.join(name, self.param[1]))
        self.rename()
        for param in self.param:
            for dir_name in self.TRAIN_DIR_NAMES:
                self.copy_images(param, dir_name)

    def copy_images(self, param, dir_name):

        for dirpath, dirnames, filenames in os.walk(param):
            if dir_name == self.TRAIN_DIR_NAMES[0]:
                start, end = 0, round(len(filenames) * 3 / 4)
            elif dir_name == self.TRAIN_DIR_NAMES[1]:
                start = round(len(filenames) * 3 / 4)
                end = len(filenames)

            for file in filenames[start:end]:
                try:
                    shutil.copy2(os.path.join(param + "/" + file),
                                 os.path.join(dir_name, param))
                except Exception as ex:
                    print(f"FileNotFoundError {ex}")

        path = os.path.join(os.getcwd(), 'train')
        self.correct_to_jpeg(path)

        path = os.path.join(os.getcwd(), 'test')
        self.correct_to_jpeg(path)

    def rename(self):
        for param in self.param:
            for dirpath, dirnames, filenames in os.walk(param):
                for file in filenames:
                        shutil.move(dirpath + "\\" + file, dirpath + "\\" + param + "." + file)


data = Data_Creator(count, param1, param2, uploads=True)
data.run()
