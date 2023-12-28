import math
import pygame

pygame.init()

clock = pygame.time.Clock()

FrameHeight = 800
FrameWidth = 1800

screen = pygame.display.set_mode((FrameWidth, FrameHeight))

bg = pygame.image.load("Arrow.png").convert()
bg2 = pygame.image.load("Bat.png").convert()

# DEFINING MAIN VARIABLES IN SCROLLING
scroll = 0

# CHANGE THE BELOW 1 TO UPPER NUMBER IF YOU GET BUFFERING OF THE IMAGE
tiles = math.ceil(FrameWidth / bg.get_width()) + 1

# MAIN LOOP
while 1:
    # THIS WILL MANAGE THE SPEED OF
    # THE SCROLLING IN PYGAME
    clock.tick(33)

    # APPENDING THE IMAGE TO THE BACK
    # OF THE SAME IMAGE
    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width()*i + scroll, 0))
        i += 1
    # FRAME FOR SCROLLING
    scroll -= 6

    # RESET THE SCROLL FRAME
    if abs(scroll) > bg.get_width():
        scroll = 0
    # CLOSING THE FRAME OF SCROLLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
