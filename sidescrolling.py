import pygame
import time
import os

pygame.init()
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption('Side Scroll-Test')

bg = pygame.image.load(os.path.join('curling-stone-emoji-2048x1534-1ec3cb7w.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

image = pygame.image.load('curling-stone-emoji-2048x1534-1ec3cb7w.png')
#image1 = pygame.image.load('IMG_20231212_214709_407.png')
done = False
win.blit(image, (0, 0))
#win.blit(image1, (500, 0))

clock = pygame.time.Clock()

while not done:
    pygame.display.flip()
    print("tick " + str(pygame.time.get_ticks()))
    time.sleep(1)

    run = True
    speed = 30
    while run:
        clock.tick(speed)
        bgX -= 1.4
        #image1 -= 1.4

        if bgX < bg.get_width() * -1:
            bgX = bg
        #if image1 < image1.get_width() * -1:
            #image1 = image1.get_width()

def redrawWindow():
    win.blit(bg, (bgX, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
