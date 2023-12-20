import pygame
import time
import os

pygame.init()
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption('Side Scroll-Test')

clock = pygame.time.Clock()

image = pygame.image.load('curling-stone-emoji-2048x1534-1ec3cb7w.png')
image1 = pygame.image.load('IMG_20231212_214709_407.png')
image2 =
done = False
win.blit(image, (0, 0))
win.blit(image1, (500, 0))

while not done:
    pygame.display.flip()
    print("tick " + str(pygame.time.get_ticks()))
    time.sleep(1)

    run = True
    speed = 30
    while run:
        clock.tick(speed)
        image -= 1.4
        image1 -= 1.4

        if image < image.get_width() * -1:
            image = image
        if image1 < image1.get_width() * -1:
            image1 = image1.get_width()

def redrawWindow():
    win.blit(image, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
