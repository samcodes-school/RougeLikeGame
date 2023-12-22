import pygame
screen=pygame.display.set_mode((700, 350))

class archerEnemy(pygame.sprite.Sprite): #Enemy archer
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Bat.png")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=x
        self.y=y
        self.direction=1
        self.width=20
        self.height=20
        self.health=50
        self.attackCooldown=0

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def movement(self, sprite):
        if self.x>sprite.x:
            self.direction=-1
        else:
            self.direction=1
        if self.health<=0:
            self.kill()
        if self.attackCooldown>0:
            self.attackCooldown-=10
        self.rect.x=self.x
        self.rect.y=self.y

    def attack(self, ranged, list):
        if self.attackCooldown==0:
            arrow=ranged(self.x, self.y, self.direction)
            list.add(arrow)
            self.attackCooldown=500
class basicEnemy(pygame.sprite.Sprite): #The enemy class
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Bat.png")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=x
        self.y=y
        self.direction=1
        self.width=20
        self.height=20
        self.health=50
        self.attackCooldown=0
        self.damage=10

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def movement(self, sprite):
        self.x+=3*self.direction
        if self.x>sprite.x:
            self.direction=-1
        else:
            self.direction=+1
        self.rect.x=self.x
        self.rect.y=self.y
        if self.attackCooldown>0:
            self.attackCooldown-=10
        if self.health<=0:
            self.kill()

    def attack(self, group):
        for sprite in group:
            if pygame.sprite.collide_rect(self, sprite) and sprite.invincibility==0:
                if sprite.blocking:
                    sprite.health-=(self.damage/2)
                else:
                    sprite.health-=self.damage
                sprite.invincibility=250
                self.attackCooldown=250
                print(sprite.health)
class Knight(pygame.sprite.Sprite): #Knight class
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Knight.png")
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=x
        self.y=y
        self.direction=1
        self.width=20
        self.height=20
        self.health=100
        self.attackCooldown=0
        self.damage=20

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def movement(self, sprite):
        if self.x-sprite.x>150 or sprite.x-self.x>150:
            self.x+=5*self.direction
        else:
            self.x+=3*self.direction
        if self.x>sprite.x:
            self.direction=-1
        else:
            self.direction=+1
        self.rect.x=self.x
        self.rect.y=self.y
        if self.attackCooldown>0:
            self.attackCooldown-=10
        if self.health<=0:
            self.kill()

    def attack(self, group):
        for sprite in group:
            if pygame.sprite.collide_rect(self, sprite) and sprite.invincibility==0:
                if sprite.blocking:
                    sprite.health-=(self.damage/2)
                else:
                    sprite.health-=self.damage
                sprite.invincibility=250
                self.attackCooldown=250
                print(sprite.health)