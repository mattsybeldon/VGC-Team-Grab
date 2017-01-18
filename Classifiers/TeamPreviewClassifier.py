'''
NOTE: DEFUNCT. NO LONGER USING CORNER DETECTION. SEE TrainTeamPreview.py which is what is being used atm
Team Previewer Classifier
Written by: Matt Sybeldon (bearsfan092)

This classifier is the first stage in a multi-stage process. In this part, the team preview screen needs to be detected.
This is so we don't scan meaningless screens such as screen transitions or battles (although I might add battle support
later... would be interesting to see the subselections of 4, but not even Showdown provides that info).

This is a relatively simple problem since the classes are Team Preview vs. not Team Preview.
Definitely want to use template matching since the bottom box is mostly invariant. Then we can use a linear SVM
classifier.
'''

import numpy as np
from Features import TemplateMatch
from os import listdir
from os.path import isfile, join
import cv2

#Return only the files
positiveFiles = [f for f in listdir('../Training/TeamPreview/Positive') if isfile(join('../Training/TeamPreview/Positive', f))]
negativeFiles = [f for f in listdir('../Training/TeamPreview/Negative') if isfile(join('../Training/TeamPreview/Negative', f))]

#Initialize scores
positiveScores = np.empty([len(positiveFiles), 1], dtype = float)
negativeScores = np.empty([len(negativeFiles), 1], dtype = float)


for i in xrange(0, len(positiveFiles) - 1):
    positiveScores[i] = cornerORB.returnCornersORB('../Training/TeamPreview/Positive/' + i)

for i in xrange(0, len(positiveFiles) - 1):
    negativeScores[i[]] = cornerORB.returnCornersORB('../Training/TeamPreview/Negative/' + j)







