'''
Screen resizing script
Written by: Matt Sybeldon (bearsfan092)

This script serves to resize any input images too 800x240, which is the native resolution of the 3DS screens. This is
to make some consistent scan points for picking up each of the Pokemon and assigning them to a team instead of grid
searching the whole screen.
'''

import cv2
import numpy as np

def resize_3ds(img):
    height, width = img.shape

    if height == 240 and width == 800: #If you were a good person who actually checked their source...
        return(img)

    #We are going to assume that aspect ratio is approximately correct. If not, your image looks bad anyway and go away

    scale_factor = 240/height

    output_img = cv2.resize(img, (0,0), fx = scale_factor, fy = scale_factor)

    return(output_img)