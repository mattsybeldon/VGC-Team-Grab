'''
Corner detection using ORB
Written by: Matt Sybeldon (bearsfan092)
Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html#orb

This is for general corner feature generation. At the time of writing, this is for testing the detection of the team
preview screen. This may be useful for other purposes such as finding whether a Pokemon is present or not, but this has
not been investigated yet.
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

def returnCornersORB(srcImgPath):
    img = cv2.imread(srcImgPath, 0)

    orb = cv2.ORB(70) #70 points to find the level features seems to work well

    keypoints = orb.detect(img, None)
    keypoints, descriptors = orb.compute(img, keypoints)

    return keypoints
