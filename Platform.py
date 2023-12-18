import pygame
from pygame.locals import *
import Collision

class Platform(Rect):
    def __init__(self,xPos,yPos,width):
        self.left = xPos
        self.top = yPos
        self.width = width
        self.height = 20

    def floorTime(self,faller):
        if Collision.collideTop(faller,self):
            faller.bottom = self.top