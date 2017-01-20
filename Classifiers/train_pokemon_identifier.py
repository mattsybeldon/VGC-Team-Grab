'''
Nearest Neighbor Classifier for Pokemon Identification
Written by: Matt Sybeldon

This generates the nearest neighbor classifier for finding the Pokemon in the region of interest. We use nearest
neighbor because there's like a bajillion Pokemon at this point, so that means a bajillion labels. How annoying.
'''

import numpy as np
import os
from os import listdir
from os.path import isfile, join
from Features import hog_feature

from sklearn import neighbors

def pokemon_classifier():
    sprite_directory = '../sprites/'
    sprite_files =  [f for f in listdir(sprite_directory) if isfile(join(sprite_directory, f))]

    labels = []
    features = []

    for i in xrange(0, len(sprite_files) - 1):
        current_label = os.path.basename(sprite_files[i])
        name, extension = os.path.splitext(current_label)
        labels.append(int(os.path.basename(name)))
        features.append(hog_feature.return_hog_feature(sprite_directory + sprite_files[i]))

    features = np.asarray(features).astype(float)
    labels = np.asarray(labels).astype(int)

    knn_classifier = neighbors.KNeighborsClassifier(1, weights = 'uniform')
    knn_classifier.fit(features, labels)

    return(knn_classifier)