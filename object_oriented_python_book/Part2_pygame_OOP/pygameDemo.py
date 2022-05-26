from pathlib import Path
import pygame
from pygame.locals import *
import sys
import random

BASE_PATH = Path(__file__).resolve().parent
pathToSnake = str(BASE_PATH) + '/images/python.png'
pathToPenguin = str(BASE_PATH) + '/images/linux_penguin.jpeg'

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
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
ballX = random.randrange(MAX_WIDTH) 
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, SNAKE_WIDTH_HEIGHT, SNAKE_WIDTH_HEIGHT)
# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos # Could do this if we needed it
              # Check if the click was in the rect of the ball
              # If so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, SNAKE_WIDTH_HEIGHT, SNAKE_WIDTH_HEIGHT)
    # 8 - Do any "per frame" actions
    # 9 - Clear the window
    window.fill(BLACK)
    # 10 - Draw all window elements
    # draw snake at position 100 across (x) and 200 down (y)
    window.blit(snakeImage, (ballX, ballY))
    # 11 - Update the window
    pygame.display.update()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)