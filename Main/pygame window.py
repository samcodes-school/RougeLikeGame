import pygame
import time
import sys
import os
import math

pygame.init()
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption('Side Scroller')

image = pygame.image.load('Dead_cells_cover_art.png')
image1 = pygame.image.load('IMG_20231212_21409_407.png')
done = False
win.blit(image, (0, 0))



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    print("tick " + str(pygame.time.get_ticks()))
    time.sleep(1)
