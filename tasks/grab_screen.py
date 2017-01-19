'''
Screen grab script
Written by: Matt Sybeldon (bearsfan092)

This script just grabs the screen according to the parameters file and outputs an image. Pretty straightforward.
'''

from PIL import ImageGrab
import numpy as np
import cv2

def return_screen_grab(left, upper, right, lower):
    screenshot = ImageGrab.grab(bbox=(left, upper, right, lower))  # bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    img = np.array(screenshot)  # this is the array obtained from conversion
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img_gray
