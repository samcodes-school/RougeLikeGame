import pygame
screen=pygame.display.set_mode((700, 350))

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Arrow.png")
        self.surf=pygame.transform.scale(self.surf, (15, 5))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=x
        self.y=y+10
        self.direction=direction
        self.damage=5

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def movement(self, group):
        self.x+=10*self.direction
        if self.x>700:
            self.kill()
        if self.x<0:
            self.kill()
        for sprite in group:
            if pygame.sprite.collide_rect(self, sprite):
                sprite.health-=self.damage
                print(sprite.health)
                self.kill()
        self.rect.x=self.x
        self.rect.y=self.y

class enemyArrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load("Arrow.png")
        self.surf=pygame.transform.scale(self.surf, (15, 5))
        self.surf.set_colorkey((0, 0, 0))
        self.rect=self.surf.get_rect()
        self.x=x
        self.y=y+10
        self.direction=direction
        self.damage=5

    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        pygame.draw.rect(screen, ((255, 0, 0)), self.rect, 2)

    def movement(self, group):
        self.x+=10*self.direction
        if self.x>700:
            self.kill()
        if self.x<0:
            self.kill()
        for sprite in group:
            if pygame.sprite.collide_rect(self, sprite):
                if sprite.invincibility==0:
                    if sprite.blocking:
                        sprite.health-=(self.damage/2)
                    else:
                        sprite.health-=self.damage
                    print(sprite.health)
                    sprite.invincibility=250
                self.kill()
        self.rect.x=self.x
        self.rect.y=self.y