import pygame
from Player import player
import Platforms
from Platforms import platformList

import Enemy
# ENEMY STUFF IS COMMENTED OUT

## SETUP ##
pygame.init()
screen = pygame.display.set_mode((700, 350))
pygame.display.set_caption("Rougelike")
bg_image = pygame.image.load("CityBackground")

clock = pygame.time.Clock()

def draw(): #Drawing the player (at the moment it is a rectangle)
    screen.blit(player.surf, (player.x, player.y))

# def draw(self):
#     screen.blit(self.surf, (self.x, self.y))

# enemy=Enemy()
# enemyList=pygame.sprite.group()
# enemyList.add(enemy)

## RUNNING ##
running = True
while running:  # The game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg_image, (0, 0))
    pygame.display.update()
    #
    # for i in range(len(platformList)): # COLLISION CHECK. NOT MODULARIZED, JUST IN CASE.
    #     if player.rect.colliderect(platformList[i]):
    #         collisionCheck = True
    #     else:
    #         collisionCheck = False
    #
    #     while collisionCheck:
    #         if (platformList[i].rect.x <= player.x <= platformList[i].rect.x + platformList[i].rect.width and
    #                 platformList[i].rect.y <= player.rect.y <= platformList[i].rect.y + platformList[i].rect.height):
    #                 player.isColliding = True
    #                 player.platform = i
    #         else:
    #             player.isColliding = False

    player.keys()  # Calling all of the things the player can do
    player.jump()
    player.verticalCollisions()
    player.horizontalCollisions()
    player.gravity()

    # player.attack(enemyList)
    # for sprite in enemyList:
    #     sprite.movement()
    # for sprite in enemyList:
    #     player.takeDamage(sprite)


    draw()  # Drawing the player
    Platforms.drawPlatforms(screen)

# for sprite in enemyList:
    #     sprite.draw()
    pygame.display.update()  # And updating the screen
    clock.tick(60)
    player.update()

pygame.quit()

# import pygame



#ALEX CODE

# #Setup
# pygame.init()
# screen = pygame.display.set_mode((700, 350))
#
# from Player import Player
# from Arrow import Arrow
# from Arrow import enemyArrow
# from Enemy import basicEnemy
# from Enemy import archerEnemy
# from Enemy import Knight
#
# pygame.display.set_caption("First Game")
#
# enemyList=pygame.sprite.Group()
# arrowList=pygame.sprite.Group()
# enemyArrowList=pygame.sprite.Group()
# archerList=pygame.sprite.Group()
# playerGroup=pygame.sprite.Group()
# basicEnemyList=pygame.sprite.Group()
# knightList=pygame.sprite.Group()
#
# player=Player(200, 200) #Instantiating the player
# enemy=basicEnemy(500, 200) #Instantiating the enemy
# archer=archerEnemy(500, 200)
# knight=Knight(600, 200)
#
# playerGroup.add(player)
# basicEnemyList.add(enemy)
# archerList.add(archer)
# knightList.add(knight)
#
# for sprite in basicEnemyList:
#     enemyList.add(sprite)
# for sprite in archerList:
#     enemyList.add(sprite)
# for sprite in knightList:
#     enemyList.add(sprite)
#
# clock=pygame.time.Clock()
#
# running = True
#
# while running: #The game loop
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     player.keys() #Calling all of the things the player can do
#     player.jump()
#     player.weapons()
#     player.attack(enemyList, Arrow, arrowList)
#
#     for sprite in enemyList: #Enemy movement
#         sprite.movement(player)
#
#     for sprite in arrowList: #Player arrow movement
#         sprite.movement(enemyList)
#
#     for sprite in enemyArrowList: #Enemy arrow movement
#         sprite.movement(playerGroup)
#
#     for sprite in basicEnemyList: #Basic enemy attacks
#         sprite.attack(playerGroup)
#
#     for sprite in knightList:
#         sprite.attack(playerGroup)
#
#     for sprite in archerList: #Enemy archer attacks
#         sprite.attack(enemyArrow, enemyArrowList)
#
#     screen.fill((0,0,0))
#
#     player.draw() #Drawing the player
#
#     for sprite in enemyList:
#         sprite.draw()
#
#     for sprite in arrowList:
#         sprite.draw()
#
#     for sprite in enemyArrowList:
#         sprite.draw()
#
#     player.update()
#     pygame.display.update() #And updating the screen
#     clock.tick(40)
#
# pygame.quit()