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
lvOnePlatform = Platform(0, 300, 200, 50, (128, 0, 32), False) # Instantiating a rough floor
lvOnePlatformTwo = Platform(255, 275, 50, 10, (128, 0, 32), False)
lvOnePlatformThree = Platform(380, 250, 50, 10, (128, 0, 32), False)
lvOnePlatformFour = Platform(500, 225, 200, 125, (128, 0, 32), False)

lvOnePlatformList = [lvOnePlatform, lvOnePlatformTwo, lvOnePlatformThree, lvOnePlatformFour]

lvTwoPlatform = Platform(0, 225, 200, 100, (129,0,31), False)
lvTwoPlatformTwo = Platform(200, 300, 300, 50, (129,0,31), False)
lvTwoPlatformThree = Platform(500, 225, 200, 100, (129,0,31), False)
lvTwoPlatformFour = Platform(400, 250, 100, 10, (129,0,31), False)
#Maybe some enemies in the depression?
lvTwoPlatformList = [lvTwoPlatform, lvTwoPlatformTwo, lvTwoPlatformThree, lvTwoPlatformFour]

lvThreePlatform = Platform(0, 300, 700, 50, (130,0,30), False)
lvThreePlatformTwo = Platform(0, 250, 20, 10, (130,0,30), False)
lvThreePlatformThree = Platform(500, 250, 100, 10, (130,0,30), False)
lvThreePlatformFour = Platform(680, 200, 20,10, (130,0,30), False)
lvThreePlatformFive = Platform(300, 300, 100, 10, (130,0,30), False)
#this would continue
#The evil level Jack talked about, casters on all of the 20-wide platforms
lvThreePlatformList = [lvThreePlatform, lvThreePlatformTwo, lvThreePlatformThree, lvThreePlatformFour, lvThreePlatformFive]

lvQuotaPlatform = Platform(0,300,700,50,(131,0,29),False)
lvQuotaPlatformTwo = Platform(0,200,100,10,(131,0,29),False)
lvQuotaPlatformThree = Platform(600,200,100,10,(131,0,29),False)
#this is just to meet Jack's platform quota
lvFourPlatformList = [lvQuotaPlatform,lvQuotaPlatformTwo,lvQuotaPlatformThree]

lvBossPlatform = Platform(0, 300, 700, 50, (132,0,28), False)
lvBossPlatformTwo = Platform(0, 0, 700, 50, (132,0,28), False)
#also draw a hexagon
#syntax for hexagon will be something along the lines "pygame.draw.polygon(window,(131,0,29),((200,75),(203,71),(208,71),(211,75),(208,79),(203,79)))"
lvBossPlatformList = [lvBossPlatform, lvBossPlatformTwo]

levelList = [lvOnePlatformList,lvTwoPlatformList,lvThreePlatformList, lvFourPlatformList, lvBossPlatformList]
#With this we can use a 2d array and iterate through that to determine the level maybe.
#That's your problem, I haven't done any coding since the collision that we aren't using and I won't start now

def drawPlatforms(screen): # Drawing
    platforms.add(lvOnePlatformList) # Adding to group

    platforms.update() # Drawing and updating the group (platforms)
    platforms.draw(screen)

    #     platformLocations = []
    #     for platform in platforms:
    #         platformLocations.append(platform.rect.top)