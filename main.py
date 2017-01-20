import cv2
import numpy as np
from tasks import grab_screen
from tasks import screenset
from Preprocessing import resize_top_screen


print('Waiting for screen selection region. Click upper left corner and drag to lower right.')

capture_coords = screenset.configure_screen()
left = capture_coords[0][0]
upper = capture_coords[0]

print(capture_coords)

#Body loop starts here
while True:

    grab_screen.return_screen_grab()


# img_resize = resize_top_screen.resize_3ds(img, 400, 240)
#
# cv2.imshow('Screen', img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()