'''
Top Level for Team Recorder
Written by: Matt Sybeldon (bearsfan092)

This is the script to run in order to continuously monitor some gameplay feed. This might be the output of some video
monitor like for a 3DS capture card or for a homebrewed N3DS. It could also monitor other sources such as Youtube videos.

When you run this script, a screenshot of your screen will be taken and displayed. Click and hold in the upperleft corner
and drag to the lower right corner according to the video source you want to capture. This sets the capture region for
the rest of the script.

This works in two stages. The team preview screen needs to be detected first. If that is found, then the slots where the
Pokemon would be are examined. From there, the detector will assign labels to each slot and record them in an external
file. Upon successful detection, the script will enter a sleep mode to let the rest of Team Preview expire.
'''

import cv2
import time
from tasks import grab_screen
from tasks import screenset
from tasks import screencheck
from tasks import record_teams
from Classifiers import TrainTeamPreview
from Classifiers import train_pokemon_identifier
from Preprocessing import resize_top_screen
from Features import hog_feature

print('Waiting for screen selection region. Click upper left corner and drag to lower right.')

capture_coords = screenset.configure_screen()
left = capture_coords[0][0]
upper = capture_coords[0][1]
right = capture_coords[1][0]
lower = capture_coords[1][1]

print(left)
print(upper)
print(right)
print(lower)

print(capture_coords)

#Get the first stage classifier for team preview
print('Loading and training team preview screen classifier...')
tp_classifier = TrainTeamPreview.return_tp_classifier()
print('Done.')

#Get the nearest neighbor classifier for the Pokemon
print('Loading and training Pokemon identifier...')
pkmn_classifier = train_pokemon_identifier.pokemon_classifier()
print('Done.')

#Get template for team preview detection
print('Loading team preview template...')
template_img = cv2.imread('Training/TeamPreview/template.png', 0)
template_img = resize_top_screen.resize_3ds(template_img, 400, 45)
print('Done')

#Body loop starts here
while True:

    #Look at screen region of interest
    #img = grab_screen.return_screen_grab()
    img = cv2.imread('Training/TeamPreview/Positive/1.png', 0)

    #Resize it to the native 3DS resolution for consistency
    img_resize = resize_top_screen.resize_3ds(img, 400, 240)

    #Check if team preview screen.
    tp_flag = screencheck.is_team_preview(tp_classifier, img_resize, template_img)

    if tp_flag == True:
        #Function to extract list of the twelve Pokemon images
        pkmn_imgs = grab_screen.return_pkmn_imgs(img_resize)

        pkmn_labels = []
        #Function to extract list of Pokemon names based on list of Pokemon images
        for i in xrange(0, 12):
            pkmn_hog = hog_feature.return_hog_feature(pkmn_imgs[i])
            pkmn_labels.append(str(pkmn_classifier.predict(pkmn_hog.reshape(1, -1))))

        print(pkmn_labels)
        #Write out team file
        record_teams.write_team_file(pkmn_labels)

        #Sleep for three minutes
        print('Teams recorded. Sleeping for three minutes...')
        time.sleep(180)

    else:
        print('yarrr')
        #Sleep for five seconds
        time.sleep(5)