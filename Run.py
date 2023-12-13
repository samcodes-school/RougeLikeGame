import pygame
from Player import Player

def drawShapes():
    pygame.draw.rect(screen, (255, 255, 255), (0, 200, 700, 200))


## SETUP ##
pygame.init()
screen = pygame.display.set_mode((700, 350))
pygame.display.set_caption("Rougelike")

player = Player()  # Instantiating the player
clock = pygame.time.Clock()

## RUNNING ##
running = True
while running:  # The game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawShapes()
    player.keys()  # Calling all of the things the player can do
    player.jump()
    screen.fill((0, 0, 0))
    player.draw()  # Drawing the player
    pygame.display.update()  # And updating the screen
    clock.tick(60)
    player.update()

pygame.quit()
