'''
Template Matching Script
Written by: Matt Sybeldon (bearsfan092)

This function performs template matching using the bottom bar in the team preview screen. The maximum score is returned
as the key feature for ultimate classification.

Uses the input image and template images directly
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join

def returnMatchScore(img, template_img):

    scores = cv2.matchTemplate(img, template_img, 5)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(scores)

    top_left = max_loc

    width, height = template_img.shape[::-1]

    bottom_right = (top_left[0] + width, top_left[1] + height)

    return(max_val)

