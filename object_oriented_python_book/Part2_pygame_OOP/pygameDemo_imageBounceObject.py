# pygame demo 4(b) - one image, bounce around the window using rects
# this works BETTER than "...imageBounce.py"
# because it uses the boundaries of the image

# also includes AUDIO!

# 1 - Import packages
from pathlib import Path
import pygame
from pygame.locals import *
import sys
import random

BASE_PATH = Path(__file__).resolve().parent
pathToBall = str(BASE_PATH) + '/media/trixie.png'
pathToMeow = str(BASE_PATH) + '/media/meow.wav'

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load(pathToBall)
meowSound = pygame.mixer.Sound(pathToMeow)

# 5 - Initialize variables
# Set this variable equal to a rectangle object of this image
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width 
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height 
ballRect.left = random.randrange(MAX_WIDTH) 
ballRect.top = random.randrange(MAX_HEIGHT) 
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH): 
        xSpeed = -xSpeed # reverse X direction
        # Play the "meow" wav file
        meowSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction
        # Play the "meow" wav file
        meowSound.play()
    
    # Update the ball's rectangle using the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    
    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
 
    # 10 - Draw the window elements
    window.blit(ballImage, ballRect) 
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)