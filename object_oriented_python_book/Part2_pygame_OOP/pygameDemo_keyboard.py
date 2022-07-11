from pathlib import Path
import pygame
from pygame.locals import *
import sys
import random

# This program uses the pygame library to create a window, 
# load an image, and move that image around the screen

# if the python is overlapping the penguin, 
# a message will print in the terminal (frame rate is 30 frames/second)

BASE_PATH = Path(__file__).resolve().parent
pathToSnake = str(BASE_PATH) + '/media/python.png'
pathToPenguin = str(BASE_PATH) + '/media/linux_penguin.jpeg'

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
SNAKE_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - SNAKE_WIDTH_HEIGHT 
MAX_HEIGHT = WINDOW_HEIGHT - SNAKE_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Load assets: image(s), sound(s), etc.
snakeImage = pygame.image.load(pathToSnake)
targetImage = pygame.image.load(pathToPenguin)
# 5 - Initialize variables
snakeX = random.randrange(MAX_WIDTH) 
snakeY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(snakeX, snakeY, SNAKE_WIDTH_HEIGHT, SNAKE_WIDTH_HEIGHT)
# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    # for every "EVENT": this means only check ONCE every time the key is pressed
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if user pressed key
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         snakeX = snakeX - N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_RIGHT:
        #         snakeX = snakeX + N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_UP:
        #         snakeY = snakeY - N_PIXELS_TO_MOVE
        #     elif event.key == pygame.K_DOWN:
        #         snakeY = snakeY + N_PIXELS_TO_MOVE
        
    # For a continuous key press, use THIS INSTEAD of the elif block above:
    # by putting this outside of the FOR LOOP, 
    # it will update at the pace of the frame rate
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]: # moving left
        snakeX = snakeX - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:  # moving right
        snakeX = snakeX + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_UP]:  # moving up
        snakeY = snakeY - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_DOWN]:  # moving down
        snakeY = snakeY + N_PIXELS_TO_MOVE

    
    # 8 - Do any "per frame" actions
    # Check if the snake rectangle is colliding with the target
    snakeRect = pygame.Rect(snakeX, snakeY, 
                            SNAKE_WIDTH_HEIGHT, SNAKE_WIDTH_HEIGHT)
    if snakeRect.colliderect(targetRect):
        print('Snake is touching the target')

    # 9 - Clear the window (black background)
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(snakeImage, (snakeX, snakeY))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND) # make pygame wait