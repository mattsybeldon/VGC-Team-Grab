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
    imgs = [screen_img[31:82, 53:109]]
    imgs.append(screen_img[83:134, 53:109])
    imgs.append(screen_img[135:186, 53:109])

    imgs.append(screen_img[31:82, 111:167])
    imgs.append(screen_img[83:134, 111:167])
    imgs.append(screen_img[135:186, 111:167])

    imgs.append(screen_img[31:82, 233:289])
    imgs.append(screen_img[83:134, 233:289])
    imgs.append(screen_img[135:186, 233:289])

    imgs.append(screen_img[31:82, 291:347])
    imgs.append(screen_img[83:134, 291:347])
    imgs.append(screen_img[135:186, 291:347])

    return imgs