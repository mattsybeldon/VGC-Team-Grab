'''
Pokemon Detector Training Script
Written by: Matt Sybeldon (bearsfan092)

Maybe defunct. Depends on how robust we want to make this.

This script uses the sprites as well as numerous junk images to train a classifier to determine if the block contains
a Pokemon or not. This is the second stage of the cascaded classifier. The first stage lets us know if we're on Team
Preview in the first place. Once this stage detects something, we will pass it off onto the next stage that will
identify the specific Pokemon.

Trying a linear classifier first with a histogram of oriented gradients. Might have to upgrade to a neural network.

Cross validation estimate obtained using 10 folds
'''

import numpy as np
from Features import hog_feature
from os import listdir
from os.path import isfile, join
import cv2

from sklearn import svm
from sklearn.cross_validation import cross_val_score

def return_pokemon_classifier():
    # Return only the files
    positive_files = [f for f in listdir('../sprites/') if isfile(join('../sprites/', f))]
    positive_scores = np.empty((len(positive_files), 64), dtype = float)

    negative_files = [f for f in listdir('../sprites/negative/') if isfile(join('../sprites/negative/', f))]
    negative_scores = np.empty((len(positive_files), 64), dtype = float)

    #Assemble labels
    all_labels = np.append(np.ones((len(positive_scores), 1)), np.zeros((len(negative_scores), 1)))

    for i in xrange(0, len(positive_scores) - 1):
        positive_scores[i, :] = hog_feature.return_hog_feature(positive_files[i])

    for i in xrange(0, len(negative_scores) - 1):
        negative_scores[i, :] = hog_feature.return_hog_feature(negative_files[i])

    #Combine scores
    all_scores = np.append(positive_scores, negative_scores)

    classifier = svm.SVC()

    cv_scores = cross_val_score(classifier, all_scores, all_labels, cv=10)
    print('Estimated accuracy for Pokemon detection: ' + str(np.mean(cv_scores)))

    classifier.fit(all_scores, all_labels)

    return classifier
