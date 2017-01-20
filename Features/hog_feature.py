'''
Histogram of Oriented Gradients Feature Generator
Written by: Matt Sybeldon (bearsfan092)

This script is meant to generate the histogram of oriented gradients feature vectors. This is mainly used to detect if
there is a Pokemon within a subregion of the screen or not.
'''

import numpy as np
import cv2

def return_hog_feature(img_file):

    img = cv2.imread(img_file, 0)
    gradient_x = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gradient_y = cv2.Sobel(img, cv2.CV_32F, 0, 1)

    magnitude, angle = cv2.cartToPolar(gradient_x, gradient_y)

    bins = np.int32(16 * angle /(2*np.pi))

    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = magnitude[:10, :10], magnitude[10:, :10], magnitude[:10, 10:], magnitude[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), 16) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)

    return hist