# Use this with Ball.py class

from curses import window
import pygame
from pygame.locals import *
import sys
import random
from Ball import *

# Define Constraints
BLACK = (0,0,0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oBall2 = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # do any "per frame" actions
    # update the coordinates, etc. of the ball
    oBall.update()
    oBall2.update()
    # color the window black
    window.fill(BLACK)
    # draw the ball
    oBall.draw()
    oBall2.draw()
    # update the display
    pygame.display.update()
    # wait a bit
    clock.tick(FRAMES_PER_SECOND)