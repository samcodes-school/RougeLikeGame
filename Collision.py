import pygame
from Platforms import Platform
from Player import Player

# collidepoint instead of colliderect because colliderect wouldn't work for the walls
# I am running two if statements because I expect that what will happen without them is that it will phase through the floor if the wrong corner is touching the wall
#
# #If we get code for hitboxes into the IntelliJ, then that would allow us to just use those for collision instead of
#trying to figure out how to do it with sprites
#Later on, if the screen is centered on the character, we can cut out all of the extra logic and just have a point or
#two for the computer to check

def collideRight(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(groundRect , groundRect.right , charRect.bottom))

    if collision == True:
        return collision

def collideLeft(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(groundRect , groundRect.left , charRect.bottom))

    if collision == True:
        return collision

def collideTop(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(groundRect , charRect.left , groundRect.top))

    if collision == True:
        return collision

def collideBottom(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(groundRect , charRect.left , groundRect.bottom))

    if collision == True:
        return collision
