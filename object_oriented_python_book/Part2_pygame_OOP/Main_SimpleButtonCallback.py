from curses import window
import pygame
from pathlib import Path
from pygame.locals import *
from SimpleButton import *
import sys

BASE_PATH = Path(__file__).resolve().parent
pathToButtonUp = str(BASE_PATH) + '/media/buttonUp.png'
pathToButtonDown = str(BASE_PATH) + '/media/buttonDown.png'

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')

# Define a class with a method to be used as a "callback"
class CallBackTest():

    def myMethod(self):
        print('User pressed Button C, called myMethod of the CallBackTest object')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oCallBackTest = CallBackTest()

oButtonA = SimpleButton(window, (25, 30), 
                        pathToButtonUp, pathToButtonDown)

oButtonB = SimpleButton(window, (150, 30), 
                        pathToButtonUp, pathToButtonDown,
                        callBack = myCallBackFunction)

oButtonC = SimpleButton(window, (275, 30), 
                        pathToButtonUp, pathToButtonDown,
                        callBack = oCallBackTest.myMethod)

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if the method 'handleEvent' for object 'button A'
        # returns True, print this...
        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    counter = counter + 1

    window.fill(GRAY)

    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
