import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from SimpleText import *
from SimpleButton import *

BASE_PATH = Path(__file__).resolve().parent
pathToButtonUp = str(BASE_PATH) + '/media/restartUp.png'
pathToButtonDown = str(BASE_PATH) + '/media/restartDown.png'

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# initialize pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT) # this is the image moving across the screen
oFrameCountLabel = SimpleText(window, (60, 20),
                        'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), pathToButtonUp, pathToButtonDown)

frameCounter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0
    
    oBall.update()
    frameCounter = frameCounter + 1
    oFrameCountDisplay.setValue(str(frameCounter))

    window.fill(BLACK)

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)