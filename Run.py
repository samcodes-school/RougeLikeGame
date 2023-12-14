import pygame
from Player import Player
from Enemy import Enemy

## SETUP ##
pygame.init()
screen = pygame.display.set_mode((700, 350))
pygame.display.set_caption("Rougelike")

player = Player()  # Instantiating the player
clock = pygame.time.Clock()

def drawShapes():
    pygame.draw.rect(screen, (255, 255, 255), (0, 200, 700, 200))

def draw(): #Drawing the player (at the moment it is a rectangle)
    screen.blit(player.surf, (player.x, player.y))
def draw(self):
    screen.blit(self.surf, (self.x, self.y))

enemy=Enemy()
enemyList=pygame.sprite.group()
enemyList.add(enemy)
## RUNNING ##
running = True
while running:  # The game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawShapes()
    player.keys()  # Calling all of the things the player can do
    player.jump()
    player.attack(enemyList)
    for sprite in enemyList:
        sprite.movement()
    for sprite in enemyList:
        player.takeDamage(sprite)
    screen.fill((0, 0, 0))
    player.draw()  # Drawing the player
    for sprite in enemyList:
        sprite.draw()
    pygame.display.update()  # And updating the screen
    clock.tick(60)
    player.update()

pygame.quit()
