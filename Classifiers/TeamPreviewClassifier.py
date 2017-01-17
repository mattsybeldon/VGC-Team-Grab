'''
Team Previewer Classifier
Written by: Matt Sybeldon (bearsfan092)

This classifier is the first stage in a multi-stage process. In this part, the team preview screen needs to be detected.
This is so we don't scan meaningless screens such as screen transitions or battles (although I might add battle support
later... would be interesting to see the subselections of 4, but not even Showdown provides that info).

This is a relatively simple problem since the classes are Team Preview vs. not Team Preview. For now, I'm trying a SVM
classifier using corners as features. Those level markers should work pretty nice for that purpose since they're regular
'''

from Features import cornerORB
from os import listdir
from os.path import isfile, join
import cv2

#Return only the files
positiveFiles = [f for f in listdir('../Training/TeamPreview/Positive') if isfile(join('../Training/TeamPreview/Positive', f))]
negativeFiles = [f for f in listdir('../Training/TeamPreview/Negative') if isfile(join('../Training/TeamPreview/Negative', f))]

for i in positiveFiles:
    positiveFeatures = cornerORB.returnCornersORB('../Training/TeamPreview/Positive/' + i)

for j in negativeFiles:
    negativeFeatures = cornerORB.returnCornersORB('../Training/TeamPreview/Negative/' + j)







