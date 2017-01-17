'''
This script is a mass sprite download script from Trainer Tower. DO NOT USE WITHOUT PERMISSION FROM TRAINER TOWER.
It's their bandwidth, so be nice :)

Written by : Matt Sybeldon (bearsfan092)
'''
from requests import get

def download(url,  fileName):
    with open(fileName, "wb") as file:
        response = get(url)
        file.write(response.content)


numPokemon = 802

imgSrc = 'https://i0.wp.com/www.serebii.net/pokedex-sm/icon/'

for i in range(1, numPokemon):

    if i < 10:
        currentUrl = imgSrc + '00' + str(i) + '.png'
    elif i < 100:
            currentUrl = imgSrc + '0' + str(i) + '.png'
    else:
        currentUrl = imgSrc + str(i) + '.png'
    download(currentUrl, 'sprites/' + str(i) + '.png')