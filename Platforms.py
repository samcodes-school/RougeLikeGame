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

    def drawPlatforms(self, screen): # Drawing
        platforms = pygame.sprite.Group() # Grouping
        platform = Platform(0, 300, 700, 50) # Instantiating a rough floor
        platforms.add(platform) # Adding to group

        platforms.update() # Drawing and updating the group (platforms)
        platforms.draw(screen)
        return platforms

    #     platformLocations = []
    #     for platform in platforms:
    #         platformLocations.append(platform.rect.top)