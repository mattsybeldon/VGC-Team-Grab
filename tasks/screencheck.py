'''
Check screen for team preview using trained classifier
Written by: Matt Sybeldon (bearsfan092)

Given a trained SVM classifier, this allows the team preview screen to be identified. Returns a true or false
'''

import cv2
import numpy as np
from Features import TemplateMatch

def is_team_preview(classifier, img, template_img):
    score = TemplateMatch.returnMatchScore(img, template_img)

    tp_flag = bool(classifier.predict(score))

    return(tp_flag)