import pygame

# class Arrow(pygame.sprite.Sprite): #A sample arrow class for ranged attacks
#   def __init__(self, x, y, direction): #We would take the x, y and direction of the player
#     pygame.sprite.Sprite.__init__(self)
#     self.x=x
#     self.y=y
#     self.direction=direction
#     #Some sort of drawing code
#   def movement(self):
#     self.x+=10*self.direction
#     if self.x>500:
#       self.kill()
#     if self.x<0:
#       self.kill()

class Enemy(pygame.sprite.Sprite): #The enemy class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Bat.png")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=300
        self.y=200
        self.direction=1
        self.width=20
        self.height=20
        self.health=50

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))

    def movement(self):
        self.x+=5*self.direction
        if self.x>500:
            self.direction=-1
        if self.x<5:
            self.direction=1

class Player(pygame.sprite.Sprite): #Making our player class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("penguin.JPG")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.x = 200
        self.y = 200
        self.vel = 5
        self.direction=1
        self.dashCooldown=0
        self.attackCooldown=0
        self.isJump = False
        self.jumpCount = 7
        self.health=100

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

    def jump(self): #Jumping
        keys=pygame.key.get_pressed()
        if self.isJump==False and self.y==200:
            if keys[pygame.K_w]:
                self.isJump=True
        else:
            if self.jumpCount >= -7:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5 #Parabola
                self.jumpCount -= 1
            else:
                self.jumpCount = 7
                self.isJump = False

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

    def draw(self): #Drawing the player (at the moment it is a rectangle)
        screen.blit(self.surf, (self.x, self.y))

    def takeDamage(self, sprite):
        if self.x==sprite.x and self.y==sprite.y:
            self.health-=10
            print(self.health)

    def update(self): #Updates the cooldown
        if self.dashCooldown>0:
            self.dashCooldown-=10
        if self.attackCooldown>0:
            self.attackCooldown-=10

pygame.init() #Setup
screen = pygame.display.set_mode((700, 350))
pygame.display.set_caption("First Game")
enemyList=pygame.sprite.Group()
player=Player() #Instantiating the player
enemy=Enemy() #Instantiating the enemy
enemyList.add(enemy)
clock=pygame.time.Clock()

running = True

while running: #The game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.keys() #Calling all of the things the player can do
    player.jump()
    player.attack(enemyList)
    for sprite in enemyList:
        sprite.movement()
    for sprite in enemyList:
        player.takeDamage(sprite)
    screen.fill((0,0,0))
    player.draw() #Drawing the player
    for sprite in enemyList:
        sprite.draw()
    pygame.display.update() #And updating the screen
    clock.tick(40)
    player.update()

pygame.quit()