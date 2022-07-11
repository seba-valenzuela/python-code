import sys
from pathlib import Path

import pygame
import pygwidgets
from pygame.locals import *

# Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent
pathToImage = str(BASE_PATH) + '/trixie.png'
pathToMeow = str(BASE_PATH) + '/meow.wav'


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oImage = pygwidgets.Image(window, (340,180), pathToImage)
oTextButton = pygwidgets.TextButton(window, (370, 500), 'This is Trixie!', soundOnClick=pathToMeow)
oDisplayText = pygwidgets.DisplayText(window, (300, 100), 'Meet Trix...', textColor=(255,255,255), fontSize=70)
oDisplayText2 = pygwidgets.DisplayText(window, (100, 80), 'Enter text here:', textColor=(255,255,255), fontSize=40)
oInputText = pygwidgets.InputText(window, (10, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if oTextButton.handleEvent(event):
            #this doesn't work, but without this you couldn't click the button
            oTextButton.playSoundOnClick 
        if oInputText.handleEvent(event):
            userText = oInputText.getValue() # gets user's text after they press Enter
            print(userText)

    # Make each widget visible
    oDisplayText.draw()
    oDisplayText2.draw()
    oImage.draw()
    oTextButton.draw()
    oInputText.draw()
    

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
