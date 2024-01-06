import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour, passthrough): ## Making our platforms. Sprite for groups.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.colour = colour
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.passthrough = passthrough



platforms = pygame.sprite.Group() # Grouping
platform = Platform(0, 300, 200, 50, (128, 0, 32), False) # Instantiating a rough floor
platformTwo = Platform(400, 200, 50, 20, (128, 0, 32), False)
platformThree = Platform(100, 250, 50, 20, (128, 128, 128), False)

platformList = [platform, platformTwo, platformThree]

def drawPlatforms(screen): # Drawing
    platforms.add(platformList) # Adding to group

    platforms.update() # Drawing and updating the group (platforms)
    platforms.draw(screen)

    #     platformLocations = []
    #     for platform in platforms:
    #         platformLocations.append(platform.rect.top)