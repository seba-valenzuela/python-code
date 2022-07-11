import pygame
from pygame.locals import *

class SimpleText():
    def __init__(self, window, loc, value, textColor):
        pygame.font.init() # starts up pygame's font system
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.textColor = textColor
        self.text = None
        self.setValue(value) # set the initial text for drawing

    def setValue(self, newText):
        if self.text == newText:
            return # exit this function, discontinue the rest of it
        
        self.text = newText
        # render has 3 parameters: the text to display, 
        # whether or not you want it anti-aliased, and the font color
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)