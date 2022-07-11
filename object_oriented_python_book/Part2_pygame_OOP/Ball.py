# 1 - Import packages
from pathlib import Path
import pygame
from pygame.locals import *
import random

BASE_PATH = Path(__file__).resolve().parent
pathToBall = str(BASE_PATH) + '/media/trixie.png'
pathToMeow = str(BASE_PATH) + '/media/meow.wav'

# Ball class
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        # 4 - Load assets: image(s), sound(s), etc.
        self.image = pygame.image.load(pathToBall)
        self.meowSound = pygame.mixer.Sound(pathToMeow)
        # Set this variable equal to a rectangle object of this image
        # a rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero,
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        # print("X Speed:", self.xSpeed)
        self.ySpeed = random.choice(speedsList)
        # print("Y Speed:", self.ySpeed)

    def update(self):
        # Check for hitting a wall. If so, change that directions
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
            self.meowSound.play()
        
        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
            self.meowSound.play()

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

