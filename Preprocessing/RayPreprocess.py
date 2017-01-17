'''
Used for slicing out Ray's footage
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join

negativeDirectory = 'D:\Documents\Repos\VGC-Team-Grab\Training\Raw\Ray\Negative'
positiveDirectory = 'D:\Documents\Repos\VGC-Team-Grab\Training\Raw\Ray\Positive'

negativeTarget = 'D:\Documents\Repos\VGC-Team-Grab\Training\TeamPreview\Negative'
positiveTarget = 'D:\Documents\Repos\VGC-Team-Grab\Training\TeamPreview\Positive'

positiveFiles = [f for f in listdir(positiveDirectory) if isfile(join(positiveDirectory, f))]
negativeFiles = [f for f in listdir(negativeDirectory) if isfile(join(negativeDirectory, f))]


for i in positiveFiles:
    img = cv2.imread(positiveDirectory + '/' + i , 0)
    smallImg = img[135:489, 323:914]
    cv2.imwrite(positiveTarget + '/' + i, smallImg)

for i in negativeFiles:
    img = cv2.imread(negativeDirectory + '/' + i, 0)
    smallImg = img[135:489, 323:914]
    cv2.imwrite(negativeTarget + '/' + i, smallImg)

