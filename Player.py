import pygame
from Platforms import Platform
screen = pygame.display.set_mode((700, 350))

class Player(pygame.sprite.Sprite):  # Making our player class

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("penguin.JPG")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
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
        self.isColliding = False
        self.health=100
        self.invincibility=0
        self.blocking=False
        self.activeWeapon="Sword"
        self.damage=10

        self.g = 5

    def keys(self): #Making the controls
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d] and self.x<670: #Adding boundaries
            self.x+=self.vel
            self.direction=1
        elif keys[pygame.K_a] and self.x>5:
            self.x-=self.vel
            self.direction=-1
        if keys[pygame.K_s] and self.dashCooldown<=0: #Dashing and boundaries
            if self.x<100 and self.direction==-1:
                self.x+=(self.x*self.direction)
            elif self.x>570 and self.direction==1:
                self.x+=((670-self.x)*self.direction)
            else:
                self.x+=(100*self.direction)
            self.dashCooldown=250

    def jump(self):  # Jumping
        keys = pygame.key.get_pressed()

        # TO DO:
        # EVERYTIME A COLLISION HAPPENS, SWITCH STARTINGPOS TO THE Y-COORD READ DURING COLLISION
        if self.isColliding == False and self.isJump == False: # Gravity if not jumping. THROW ISCOLLIDING HERE TO FIX
            self.isGravity = True
            self.y += self.g
            if self.isColliding == True: ## Switch to isColliding
                self.isGravity = False

        # if self.startingPos == 1 and self.isGravity is False: ## startingPos is set to 1 at the start. Acts as a starter method.
        #     self.startingPos = self.y # For collision and jump detection
        #     print(self.startingPos)
        #     print(self.isJump)

        if self.isJump == False and self.isColliding == True: ## If on ground, and not jumping
            if keys[pygame.K_SPACE]:
                self.isJump = True # Jump
        else:
            if self.isJump == True: # Jumping
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5  # Parabola
                self.jumpCount -= 1

                if self.isColliding == True: ## Once landed, stop jumping.
                    self.jumpCount = 7
                    self.isJump = False
                    self.startingPos = 1


        # if self.y > 200: # boundary
        #     self.y = 200

# import pygame
# class Player(pygame.sprite.Sprite): #Making our player class
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.surf = pygame.image.load("penguin.JPG")
#         self.surf = pygame.transform.scale(self.surf, (30, 30))
#         self.surf.set_colorkey((0, 0, 0))
#         self.rect = self.surf.get_rect()
#         self.vel = 5
#         self.direction=1
#         self.dashCooldown=0
#         self.attackCooldown=0
#         self.isJump = False
#         self.jumpCount = 7

    def weapons(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.activeWeapon="Sword"
        if keys[pygame.K_2]:
            self.activeWeapon="Bow"

    def attack(self, group, ranged, list): #A bit finnicky - probably not the best but it works
        left, middle, right=pygame.mouse.get_pressed()
        if left and self.attackCooldown==0:
            if self.activeWeapon=="Sword":
                print("Sword attack")
                for sprite in group:
                    if sprite.x>self.x and self.x+100>sprite.x and self.direction==1:
                        sprite.health-=self.damage
                        print(sprite.health)
                    if sprite.x<self.x and self.x-100<sprite.x and self.direction==-1:
                        sprite.health-=self.damage
                        print(sprite.health)
                self.attackCooldown=250
            elif self.activeWeapon=="Bow":
                print("Bow attack")
                arrow=ranged(self.x, self.y, self.direction)
                list.add(arrow)
                self.attackCooldown=250
        elif right:
            self.blocking=True
        elif not right:
            self.blocking=False

    def draw(self): #Drawing the player (at the moment it is a rectangle)
        screen.blit(self.surf, self.rect)
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def update(self): #Updates the cooldown
        if self.dashCooldown>0:
            self.dashCooldown-=10
        if self.attackCooldown>0:
            self.attackCooldown-=10
        if self.invincibility>0:
            self.invincibility-=10
        self.rect.x=self.x
        self.rect.y=self.y
        if self.health<=0:
            print("Game Over")
            pygame.quit()