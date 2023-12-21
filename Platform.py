import pygame
from pygame.locals import *
import Collision

##I would have liked to test this, but I don't know how to integrate it into the main code.

#Use this to have a small platform
class Platform(Rect):
    def __init__(self,xPos,yPos,):
        self.left = xPos
        self.top = yPos
        self.width = 80
        self.height = 20


#This is for anything larger than the platforms
class Wall(Rect):
    def __init__(self,xPos,yPos,width,height):
        self.left = xPos
        self.top = yPos
        self.width = width
        self.height = height