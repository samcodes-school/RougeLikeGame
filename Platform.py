import pygame
from pygame.locals import *
import Collision as c

##I would have liked to test this, but I don't know how to integrate it into the main code.

#Use this to have a small platform
class Platform(Rect):
    def __init__(self,xPos,yPos,):
        self.left = xPos
        self.top = yPos
        self.width = 80
        self.height = 20

#This is code to turn the platform into a floor
    def floorTime(self,character):
      if c.collideTop(character.rect,self):
        character.rect.bottom = self.top

    def drawPlatform(self,screen):
        pygame.draw.rect(screen,(240,48,64),self)


#This is for anything larger than the platforms
class Wall(Rect):
    def __init__(self,xPos,yPos,width,height):
        self.left = xPos
        self.top = yPos
        self.width = width
        self.height = height