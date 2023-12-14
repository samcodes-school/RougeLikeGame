import pygame
class Player(pygame.sprite.Sprite):  # Making our player class

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("penguin.JPG")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.x = 200
        self.y = 200
        self.width = 20
        self.height = 20
        self.vel = 5
        self.direction = 1
        self.dashCooldown = 0
        self.attackCooldown=0
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
        if self.y <= self.startingPos and self.isJump == False: # Gravity if not jumping. THROW IF-COLLIDING HERE TO FIX
            self.isGravity = True
            self.y += self.g
            if self.y == self.startingPos:
                self.isGravity = False

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
    def attack(self, group):
        left, middle, right=pygame.mouse.get_pressed()
        if left and self.attackCooldown==0:
            print("Left mouse")
            for sprite in group: #Perhaps we could do a separate sprite for the sword and then rotate the sword when the mouse is clicked and if the sword sprite is touching the enemy sprite it deals damage
                #if self.x+25>sprite.x or self.x-25<sprite.x: We are missing some way to detect if a sprite is a certain distance away
                sprite.health-=10
                print(sprite.health)
                if sprite.health<=0:
                    sprite.kill()
            self.attackCooldown=250
    def takeDamage(self, sprite):
        if self.x==sprite.x and self.y==sprite.y:
            self.health-=10
            print(self.health)

    def update(self):  # Updates the cooldown
        if self.dashCooldown > 0:
            self.dashCooldown -= 10
        if self.attackCooldown>0:
            self.attackCooldown-=10