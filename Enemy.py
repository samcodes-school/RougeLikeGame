# import pygame
#
# class Enemy(pygame.sprite.Sprite): #The enemy class
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.surf = pygame.image.load("Bat.png")
#         self.surf = pygame.transform.scale(self.surf, (30, 30))
#         self.surf.set_colorkey((0, 0, 0))
#         self.rect=self.surf.get_rect()
#         self.x=300
#         self.y=200
#         self.direction=1
#         self.width=20
#         self.height=20
#         self.health=50
#
#     def draw(self):
#         screen.blit(self.surf, (self.x, self.y))
#
#     def movement(self):
#         self.x+=5*self.direction
#         if self.x>500:
#             self.direction=-1
#         if self.x<5:
#             self.direction=1