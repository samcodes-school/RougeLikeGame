import pygame
from pygame.locals import *
import Collision

## MOVE STUFF TO PLAYER.PY (under a function??)
## USE SELF.G FOR GRAVITY
## PLAYER COORDS FOR BOTTOM/SIDE


pygame.init()

window = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()

rectangleOne = Rect(200,500,300,50)
rectangleTwo = Rect(200,200,50,50)
rectangleThree = Rect(500,200,50,300)

gravity = 3
momentum = 2

run = True

while run:

    clock.tick(60.0)

    #I have no idea how to fix the stretching
    rectangleTwo.bottom += gravity
    rectangleTwo.right += momentum

    #I don't know how I could simplify this
    collide1 = Collision.collideTop(rectangleTwo,rectangleOne)
    collide2 = Collision.collideLeft(rectangleTwo,rectangleThree)

    if collide1:
        rectangleTwo.bottom = rectangleOne.top
        gravity = 0

    else:
        gravity = 3

    if collide2:
        rectangleTwo.right = rectangleThree.left
        momentum = 0

    else:
        momentum = 2

    pygame.draw.rect(window,(240,48,64),rectangleOne)
    pygame.draw.rect(window,(128,255,224),rectangleTwo)
    pygame.draw.rect(window,(192,32,16),rectangleThree)

    pygame.display.update()