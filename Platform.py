import pygame
from pygame.locals import *
import Collision

##I would have liked to test this, but I don't know how to integrate it into the main code.

class Platform(Rect):
    def __init__(self,xPos,yPos,width):
        self.left = xPos
        self.top = yPos
        self.width = width
        self.height = 20

    def floorTime(self,character):
        if Collision.collideTop(character,self):
            character.bottom = self.top

    def wallTime(self,character):
        if Collision.collideLeft(character,self):
            character.right = self.left

        if Collision.collideRight(character,self):
            character.left = self.left + self.width