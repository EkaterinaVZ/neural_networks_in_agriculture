# neural_networks_in_agriculture
automation in agriculture
## Description
The set allows to classify the tomatoes according to their ripeness level for the further automation of the sorting process.
The first set allows to classify the insects.

## Dataset(tomatoes)
High quality data set of images that contains tomatoes. The set allows to classify the tomatoes according to their ripeness level for the further automation of the sorting process. The following types of tomatoes are included (according to their ripeness level): ripe and unripe.

<p>Folders Training and Test contain all images used for training and testing</p>
<p><a href= "https://www.dropbox.com/s/xr9korqevso13dn/train.zip?dl=0">train</a></p>
<p><a href= "https://www.dropbox.com/s/jobbumuysmfpzoz/ezyzip.zip?dl=0">test</a></p>

## Dataset(insects)
High quality data set of images that contains insect species. The set allows to classify the insects. Extending of dataset volume and adding of the additional classes will make use of the set for the insect-pest detecting on the agricultural plants or for the automatically insect classification and insect census. At the moment three classes of insects are included: ants(Formicidae), colorado beetle(Leptinotarsa decemlineata), ladybug(Coccinellidae).

<p>Folders Training and Test contain all images used for training and testing</p>
<p><a href= "https://www.dropbox.com/s/2rxrttiyekd6mkr/train2.zip?dl=0">train</a></p>
<p><a href= "https://www.dropbox.com/s/cs2v7xfl0h14fvr/test2.zip?dl=0">test</a></p>

## Dataset properties(tomatoes)

Total number of images: 2026.

Training set size: 1520 images.

Test set size: 506 images.

Number of classes: 2 (ripe_tomatoes, unripe_tomatoes).

Image size: 224x224 pixels.

Filename format: ripe_tomatoes.index.jpg(e.g. ripe_tomatoes.0.jpg), unripe_tomatoes.index.jpg(e.g. ripe_tomatoes.19.jpg)

Ripe and unripe tomatoes belong to two different classes.

## Dataset properties(insects)

Total number of images: 1512.

Training set size: 1134 images.

Test set size: 378 images.

Number of classes: 3 (ants, colorado_beetle, ladybug).

Image size: 224x224 pixels.

Filename format: ants.index.jpg(e.g. ants.0.jpg), colorado_beetle.index.jpg(e.g. ladybug.19.jpg),

Ants, colorado beetles, ladybugs belong to three different classes.

## Repository structure(tomatoes)

Folders Training and Test contain all images used for training and testing.

Ripe and unripe tomatoes belong to two different classes. The main part of images was unloaded using a script (code), then the images were checked and selected in manual way. Small part of the data consists of prepared photographs. It is a convenient tool for classifying fruits into ripe and unripe. If needed the additional required data (and classes) can be added to the set to expand the use of classification.


## Repository structure(insects)

Folders Training and Test contain all images used for training and testing.

Insects belong to three different classes. The main part of images was unloaded using a script (code), then the images were checked and selected in manual way. Small part of the data consists of prepared photographs. It is a convenient tool for classifying fruits into ripe and unripe. If needed the additional required data (and classes) can be added to the set to expand the use of classification.

## Team members:
Project-manager: Alexander Lebede
Product-manager: Ekaterina Zheriborova
Developer: Sofia Moriy
Disainer: Inessa Babiy, Alexey Podlyagin
