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
lvZeroPlatform = Platform(0, 300, 200, 50, (128, 0, 32), False) # Instantiating a rough floor
lvZeroPlatformTwo = Platform(255, 275, 50, 10, (128, 0, 32), False)
lvZeroPlatformThree = Platform(380, 250, 50, 10, (128, 0, 32), False)
lvZeroPlatformFour = Platform(500, 225, 200, 125, (128, 0, 32), False)

lvZeroPlatformList = [lvZeroPlatform, lvZeroPlatformTwo, lvZeroPlatformThree, lvZeroPlatformFour] #Index 0 in levelList

lvOnePlatform = Platform(0, 275, 150, 75, (129,0,31), False)
lvOnePlatformTwo = Platform(150, 300, 400, 50, (129,0,31), False)
lvOnePlatformThree = Platform(550, 275, 150, 75, (129,0,31), False)
lvOnePlatformFour = Platform(300, 250, 100, 10, (129,0,31), False)
#Maybe some enemies in the depression?
lvOnePlatformList = [lvOnePlatform, lvOnePlatformTwo, lvOnePlatformThree, lvOnePlatformFour] #Index 1 in levelList

lvEvilPlatform = Platform(0, 300, 700, 50, (130,0,30), False)
lvEvilPlatformTwo = Platform(0, 250, 20, 10, (130,0,30), False)
lvEvilPlatformThree = Platform(400, 250, 100, 10, (130,0,30), False)
lvEvilPlatformFour = Platform(680, 200, 20,10, (130,0,30), False)
lvEvilPlatformFive = Platform(200, 200, 100, 10, (130,0,30), False)
lvEvilPlatformSix = Platform(0, 150, 20, 10, (130,0,30), False)
lvEvilPlatformSeven = Platform(400, 150, 100, 10, (130,0,30), False)
lvEvilPlatformEight = Platform(680, 100, 20,10, (130,0,30), False)
lvEvilPlatformNine = Platform(200, 100, 100, 10, (130,0,30), False)
#this would continue
#The evil level Jack talked about, casters on all of the 20-wide platforms
lvEvilPlatformList = [lvEvilPlatform, lvEvilPlatformTwo, lvEvilPlatformThree,
                      lvEvilPlatformFour, lvEvilPlatformFive, lvEvilPlatformSix,
                      lvEvilPlatformSeven, lvEvilPlatformEight, lvEvilPlatformNine] #Index 2 in LevelList

lvImBeingForcedToMakeThesePlatform = Platform(0,300,700,50,(131,0,29),False)
lvOhGodSomeoneHelpMePlatformTwo = Platform(0,200,100,10,(131,0,29),False)
lvPleaseStopThisMadmanPlatformThree = Platform(600,200,100,10,(131,0,29),False)
#this is just to meet Jack's platform quota
lvQuotaPlatformList = [lvImBeingForcedToMakeThesePlatform,lvOhGodSomeoneHelpMePlatformTwo,
                       lvPleaseStopThisMadmanPlatformThree] #Index 3 in LevelList

lvBossPlatform = Platform(0, 300, 700, 50, (132,0,28), False)
lvBossPlatformTwo = Platform(0, 0, 700, 50, (132,0,28), False)
#also draw a hexagon
#syntax for hexagon will be something along the lines
# "pygame.draw.polygon(window,(131,0,29),((200,75),(203,71),(208,71),(211,75),(208,79),(203,79)))"
lvBossPlatformList = [lvBossPlatform, lvBossPlatformTwo]

levelList = [lvZeroPlatformList,lvOnePlatformList,lvEvilPlatformList, lvQuotaPlatformList, lvBossPlatformList]
#With this we can use a 2d array and iterate through that to determine the level maybe.
#That's your problem, I haven't done any coding since the collision that we aren't using and I won't start now

def drawPlatforms(screen, level): # Drawing
    platforms.add(levelList[level]) # Adding to group

    platforms.update() # Drawing and updating the group (platforms)
    platforms.draw(screen)

    #     platformLocations = []
    #     for platform in platforms:
    #         platformLocations.append(platform.rect.top)