import pygame
from pygame.locals import *

class SimpleButton():

    STATE_IDLE = 'idle' # button is up, mouse not over button
    STATE_ARMED = 'armed' # button is down, mouse over button
    STATE_DISARMED = 'disarmed' # clicked down on button, rolled off

    def __init__(self, window, loc, up, down, callBack=None): # set callBack equal to None
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
        self.callBack = callBack # if there is a callback, it will be a METHOD

        # Get the rect of the button (to see if the mouse is over the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        # set THIS button's state to 'idle'
        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # This method will return True if user clicks the button
        # Normally returns False

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # If the event is NOT one of these 3 mouse events...
            return False

        # This will return True if the eventObj position is within the bounds of the rectangle
        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        # ** THIS IS CALLED A 'STATE MACHINE' **
        # if the state is 'idle'
        if self.state == SimpleButton.STATE_IDLE:
            # if the button is DOWN and the mouse is within the rectangle:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                # set the button state to 'armed'
                self.state = SimpleButton.STATE_ARMED
                print(self.state)
        
        # if the state is 'armed'
        elif self.state == SimpleButton.STATE_ARMED:
            # if the button is UP and the mouse is within the rectangle:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE # reset the state to 'idle'
                print(self.state)
                if self.callBack != None: # if there IS a callback,
                    self.callBack() # Call the METHOD () associated with the 'callBack' var
                return True # this indicates the button has been CLICKED

            # if the mouse is MOVED and NOT within the rectangle:
            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                # Set the state to 'disarmed'
                self.state = SimpleButton.STATE_DISARMED
                print(self.state)
        
        # FIXED! This was missing, so when state was "disarmed" you wouldn't be able to use the button anymore
        elif self.state == SimpleButton.STATE_DISARMED:
            self.state = SimpleButton.STATE_IDLE
            print(self.state)

    def draw(self):
        # draw the button's current appearance in the window
        # if the state is 'armed', draw the button DOWN
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        
        else:
            # otherwise, draw the button UP
            self.window.blit(self.surfaceUp, self.loc)