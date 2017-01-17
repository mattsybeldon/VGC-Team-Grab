#Extracts individual sprites from master sprite sheet

import numpy as np
import cv2
import matplotlib

imgPath = 'D:\Documents\Repos\VGC-Video-Stats\spritesheet.png'

pkmnCols = 15 #Pokemon per row in sheet
pkmnRows = 77 #Number of columns, staying in first palette

sheetImg = cv2.imread(imgPath)
pxRows, pxCols, depth = sheetImg.shape #Should be 2543x976

pkmnWidth = pxCols/pkmnCols
pkmnHeight = pxRows/pkmnRows

print(pkmnWidth)
print(pkmnHeight)

for i in range(0, pkmnCols):
    for j in range(0, pkmnRows):
        currentImg = sheetImg[1+j*pkmnHeight:(j+1)*pkmnHeight, 1 + i*pkmnWidth:(i+1)*pkmnWidth,:]
        cv2.imshow('Current', currentImg)
        saveString = 'col' + str(i) + 'row' + str(j)
        cv2.imwrite('sprites/' + saveString + '.png', currentImg)

cv2.destroyAllWindows()

