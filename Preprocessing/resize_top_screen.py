'''
Screen resizing script
Written by: Matt Sybeldon (bearsfan092)

This script serves to resize any input images too 800x240, which is the native resolution of the 3DS screens. This is
to make some consistent scan points for picking up each of the Pokemon and assigning them to a team instead of grid
searching the whole screen.
'''

import cv2
import numpy as np

def resize_3ds(img, target_width, target_height):
    height, width = img.shape

    #We are going to assume that aspect ratio is approximately correct. If not, your image looks bad anyway and go away

    x_scale_factor = float(target_width)/width
    y_scale_factor = float(target_height)/height

    if x_scale_factor < 1:
        print('Warning: Target image is smaller than 3DS resolution.')

    output_img = cv2.resize(img, (0,0), fx = x_scale_factor, fy = y_scale_factor)

    return(output_img)