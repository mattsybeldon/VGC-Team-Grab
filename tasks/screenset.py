'''
Screen Capture Configuration
Written by: Matt Sybeldon (bearsfan092) with heavy references from pyimagesearch

This allows the user to select the region to monitor. They should have the monitor region open and visible.
The function will take a screenshot and display that screenshot. The user should then click on the upper left corner.
Then they should drag to the lower right corner. The points will be returned
'''

from PIL import ImageGrab
import numpy as np
import argparse
import cv2
from tasks import grab_screen

from win32api import GetSystemMetrics

from ctypes import windll, Structure, c_ulong, byref

class point(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

refPt = []

def return_position():
    pt = point()
    windll.user32.GetCursorPos(byref(pt))
    return{"x": pt.x, "y": pt.y}

def mouse_click(event, x, y, flags, params):

    global refPt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))


def configure_screen():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    screen_img = grab_screen.return_screen_grab(0, 0, width, height)
    cv2.namedWindow("Click and drag to the corners! LU to DR")
    cv2.setMouseCallback("Click and drag to the corners! LU to DR", mouse_click)

    while True:
        cv2.imshow("Click and drag to the corners! LU to DR", screen_img)
        cv2.waitKey(1) & 0xFF

        if len(refPt) == 2:
            cv2.destroyAllWindows()
            return refPt


