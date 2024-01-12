# An old testing site. Worked on by Tommy and Alex, before collision was passed onto Jack.

#Sprite Collision
#To do collision between sprites you have to update the self.rect values for x and y once the player has moved
# self.rect.x=self.x
# self.rect.y=self.y

#Then you can check if the self.rect values for the player is touching something else, like a sprite
# if pygame.sprite.collide_rect(self, sprite) and self.invincibility==0:
#     self.health-=10