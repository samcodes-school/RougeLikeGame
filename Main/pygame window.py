import pygame
import time


pygame.init()
win = pygame.display.set_mode((1000, 900))
pygame.display.set_caption('Side Scroller')

image = pygame.image.load('Dead_cells_cover_art.png')
image1 = pygame.image.load('IMG_20231212_214709_407.png')
done = False
win.blit(image, (0, 0))
win.blit(image1, (500, 0))

clock = pygame.time.Clock()

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
            image = image.get_width()

        if image1 < image1.get_width() * -1:
            image1 = image1.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
