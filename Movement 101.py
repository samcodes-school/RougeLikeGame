import pygame

class Player(pygame.sprite.Sprite):  # Making our player class

    def __init__(self):
        self.x = 200
        self.y = 200
        self.width = 20
        self.height = 20
        self.vel = 5
        self.direction = 1
        self.dashCooldown = 0
        self.isJump = False
        self.jumpCount = 7
        self.startingPos = 1
        self.isGravity = False

        self.g = 5

    def keys(self):  # Making the controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.x < 670:  # Adding boundaries EVENTUALLY NOT NEEDED
            self.x += self.vel
            self.direction = 1
        elif keys[pygame.K_a] and self.x > 5:
            self.x -= self.vel
            self.direction = -1
        if keys[pygame.K_s] and self.dashCooldown <= 0:  # Dashing and boundaries
            if self.x < 100 and self.direction == -1:
                self.x += (self.x * self.direction)
            elif self.x > 570 and self.direction == 1:
                self.x += ((670 - self.x) * self.direction)
            else:
                self.x += (100 * self.direction)
            self.dashCooldown = 250

    def jump(self):  # Jumping
        keys = pygame.key.get_pressed()

# TO DO:
        # EVERYTIME A COLLISION HAPPENS, SWITCH STARTINGPOS TO THE Y-COORD READ DURING COLLISION
        if self.y <= self.startingPos and self.isJump == False: # Gravity if not jumping
            self.isGravity = True
            self.y += self.g
            if self.y == self.startingPos:
                self.isGravity = False # Switch this around for collisions. Can't be = 200

        if self.startingPos == 1 and self.isGravity is False:
            self.startingPos = self.y # For collision and jump detection
            print(self.startingPos)

        if self.isJump == False and self.y == self.startingPos:
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.isJump == True:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5  # Parabola
                self.jumpCount -= 1

                if self.y == self.startingPos:
                    self.jumpCount = 7
                    self.isJump = False
                    self.startingPos = 1


        if self.y > 200: # boundary
            self.y = 200

    def draw(self):  # Drawing the player (at the moment it is a rectangle)
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.x, self.y, self.width, self.height))

    def update(self):  # Updates the cooldown
        if self.dashCooldown > 0:
            self.dashCooldown -= 10


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
