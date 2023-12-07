import pygame
import time
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 900))
# image=pygame.image.load ('Hades_cover_art.jpg')
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    print("tick " + str(pygame.time.get_ticks()))
    time.sleep(1)
