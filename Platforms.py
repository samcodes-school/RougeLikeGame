import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height): ## Making our platforms. Sprite for groups.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        colour = (128, 0, 32)
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



platforms = pygame.sprite.Group() # Grouping
platform = Platform(0, 300, 200, 50) # Instantiating a rough floor
platformTwo = Platform (400, 200, 50, 20)

platformList = [platform, platformTwo]

def drawPlatforms(screen): # Drawing
    platforms.add(platformList) # Adding to group

    platforms.update() # Drawing and updating the group (platforms)
    platforms.draw(screen)

    #     platformLocations = []
    #     for platform in platforms:
    #         platformLocations.append(platform.rect.top)