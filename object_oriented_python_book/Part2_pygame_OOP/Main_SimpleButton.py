import pygame
from pygame.locals import *
from pathlib import Path
from SimpleButton import *
import sys

BASE_PATH = Path(__file__).resolve().parent
pathToButtonUp = str(BASE_PATH) + '/media/buttonUp.png'
pathToButtonDown = str(BASE_PATH) + '/media/buttonDown.png'

# Define Constraints
GRAY = (128, 128, 128)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# Initialize pygame, window, clock
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# create instances of SimpleButton
oButtonA = SimpleButton(window, (25, 30), pathToButtonUp, pathToButtonDown)
oButtonB = SimpleButton(window, (150, 30), pathToButtonUp, pathToButtonDown)
oButtonC = SimpleButton(window, (275, 30), pathToButtonUp, pathToButtonDown)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if oButtonA.handleEvent(event):
            print('User has clicked the button A')
        elif oButtonB.handleEvent(event):
            print('User has clicked the button B')
        elif oButtonC.handleEvent(event):
            print('User has clicked the button C')

    window.fill(GRAY)

    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()


    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)