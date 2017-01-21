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

def return_pkmn_imgs(screen_img):
    imgs = [screen_img[38:70, 68:100]]
    imgs.append(screen_img[93:125, 68:100])
    imgs.append(screen_img[143:175, 68:100])

    imgs.append(screen_img[38:70, 124:156])
    imgs.append(screen_img[93:125, 124:156])
    imgs.append(screen_img[143:175, 124:156])

    imgs.append(screen_img[38:70, 248:280])
    imgs.append(screen_img[93:125, 248:280])
    imgs.append(screen_img[143:175, 248:280])

    imgs.append(screen_img[38:70, 304:336])
    imgs.append(screen_img[93:125, 304:336])
    imgs.append(screen_img[143:175, 304:336])

    return imgs