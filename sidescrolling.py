#Programmer: Sammy Beamish
# Completed: SCRAPPED
# An old test version of sidescrolling. Could never figure it out, so it was dropped.

import math
import pygame

pygame.init()

clock = pygame.time.Clock()

FrameHeight = 800
FrameWidth = 1800

screen = pygame.display.set_mode((FrameWidth, FrameHeight))

bg = pygame.image.load("Arrow.png").convert()
bg2 = pygame.image.load("Bat.png").convert()

keys = pygame.key.get_pressed()
scroll = 0
tiles = math.ceil(FrameWidth / bg.get_width()) + 1


if keys[pygame.K_d]:
    Walk = 1

else:
    Walk = 0

    # MAIN LOOP
    while Walk == 1:
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
