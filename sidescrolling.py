import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption('Side Scroll-Test')

clock = pygame.time.Clock()

bg = pygame.image.load('curling-stone-emoji-2048x1534-1ec3cb7w.png').convert()
bg1 = pygame.image.load('IMG_20231212_214709_407.png').convert()
bg2 = pygame.image.load('Ducati_side_shadow-fs8.png').convert()
bg.blit(bg, (0, 0))
bg.blit(bg1, (500, 0))
bg.blit(bg2, (100, 0))

scroll = 0

tiles = math.ceil(1000 / bg.get_width())+1
tiles1 = math.ceil(1000 / bg1.get_width())+1
tiles2 = math.ceil(1000 / bg2.get_width())+1


#def keys(self):
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_d]:

while 1:
    clock.tick(30)
    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width()*i+scroll, 0))
        i += 1
        scroll -= 6

        if abs(scroll) > bg.get_width():
            scroll = 0

        pygame.display.update()



#done = False

#while not done:
    #pygame.display.flip()
    #print("tick " + str(pygame.time.get_ticks()))
    #time.sleep(1)

    #run = True
    #speed = 30
    #while run:
        #clock.tick(speed)

    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #done = True
