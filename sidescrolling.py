import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1920, 900))
pygame.display.set_caption('Side Scroll-Test')

clock = pygame.time.Clock()
keys = pygame.key.get_pressed()

bg = pygame.image.load('curling-stone-emoji-2048x1534-1ec3cb7w.png').convert()
bg1 = pygame.image.load('IMG_20231212_214709_407.png').convert()
bg2 = pygame.image.load('Ducati_side_shadow-fs8.png').convert()
bg.blit(bg, (1000, 900))
bg.blit(bg1, (1620, 000))
bg.blit(bg2, (0, 000))


tiles = math.ceil(1000 / bg.get_width())+1
tiles1 = math.ceil(1000 / bg1.get_width())+1
tiles2 = math.ceil(1000 / bg2.get_width())+1

scroll = 0


# def __init__(self):
#     self.x = 200
#     self.y = 200
#     self.width = 20
#     self.height = 20
#     self.vel = 5
#     self.direction = 1
#     self.dashCooldown = 0
#     self.isJump = False
#     self.jumpCount = 7
#     self.startingPos = 1
#     self.isGravity = False
#
#     self.g = 5


while keys[pygame.K_d]:
    clock.tick(30)
    i = 0

    while i < tiles:
        # def keys(self):  # Making the controls
        #     keys = pygame.key.get_pressed()
        #       self.x += self.vel
        #       self.direction = 1
        screen.blit(bg, (bg.get_width()*i+scroll, 0))
        i += 1
        scroll -= 6
        if abs(scroll) > bg.get_width():
            scroll = 0

        pygame.display.update()
