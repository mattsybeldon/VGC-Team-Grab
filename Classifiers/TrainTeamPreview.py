'''
Training script for the team preview classifier
Written by: Matt Sybeldon (bearsfan092)

This script is meant to obtain the scores using template matching and establish a SVM classifier to separate between the
scores. An accuracy estimate is obtained using five fold cross validation. The final classifier is trained with
all data.

This is the first stage in a multi stage classifier where the team preview screen is identified. The next phase is to
find Pokemon, and the last stage is to identify the specific Pokemon
'''

import numpy as np
from Features import TemplateMatch
from os import listdir
from os.path import isfile, join
import cv2

from sklearn import svm
from sklearn.cross_validation import cross_val_score

def return_tp_classifier():
    #Return only the files
    positiveFiles = [f for f in listdir('Training/TeamPreview/Positive') if isfile(join('Training/TeamPreview/Positive', f))]
    negativeFiles = [f for f in listdir('Training/TeamPreview/Negative') if isfile(join('Training/TeamPreview/Negative', f))]

    template_path = 'Training\TeamPreview/template.png'

    #Initialize scores
    positive_scores = np.empty([len(positiveFiles), 1], dtype = float)
    negative_scores = np.empty([len(negativeFiles), 1], dtype = float)

    #Build up labels
    all_labels = np.append(np.ones((len(positive_scores), 1)), np.zeros((len(negative_scores), 1)))

    template_img = cv2.imread(template_path, 0)

    for i in xrange(0, len(positiveFiles) - 1):
        img = cv2.imread('Training/TeamPreview/Positive' + '/' + positiveFiles[i], 0)
        positive_scores[i] = TemplateMatch.returnMatchScore(img, template_img)

    for i in xrange(0, len(positiveFiles) - 1):
        img = cv2.imread('Training/TeamPreview/Negative' + '/' + negativeFiles[i], 0)
        negative_scores[i] = TemplateMatch.returnMatchScore(img, template_img)

    all_scores = np.append(positive_scores, negative_scores)
    all_scores = np.reshape(all_scores, (len(all_scores), 1))

    classifier = svm.SVC()

    cv_scores = cross_val_score(classifier, all_scores, all_labels, cv = 5)
    print('Estimated accuracy for Team Preview: ' + str(np.mean(cv_scores)))

    classifier.fit(all_scores, all_labels)

    return(classifier)








