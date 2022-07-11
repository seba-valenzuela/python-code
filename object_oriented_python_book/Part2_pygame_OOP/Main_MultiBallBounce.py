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
N_BALLS = 6

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # do any "per frame" actions
    # update the coordinates, etc. of the ball
    for oBall in ballList:
        oBall.update()
    # color the window black
    window.fill(BLACK)
    # draw the ball
    for oBall in ballList:
        oBall.draw()
    # update the display
    pygame.display.update()
    # wait a bit
    clock.tick(FRAMES_PER_SECOND)