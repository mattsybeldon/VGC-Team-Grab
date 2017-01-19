import cv2
import numpy as np
from tasks import grab_screen
from Preprocessing import resize_top_screen

img = grab_screen.return_screen_grab(0,72,625,447) #We'll make this better later.

img_resize = resize_top_screen.resize_3ds(img, 400)

cv2.imshow('Screen', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()