import pygame

#collidepoint instead of colliderect because colliderect wouldn't work for the walls
#I am running two if statements because I expect that what will happen without them is that it will phase through the floor if the wrong corner is touching the wall

def collideRight(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(charRect , groundRect.right , charRect.bottom))

    if collision == True:
        return collision

    else:
        collision = (pygame.Rect.collidepoint(charRect , groundRect.right , charRect.top))

        if collision == True:
            return collision

def collideLeft(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(charRect , groundRect.left , charRect.bottom))

    if collision == True:
        return collision

    else:
        collision = (pygame.Rect.collidepoint(charRect , groundRect.left , charRect.top))

        if collision == True:
            return collision

def collideTop(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(charRect , charRect.left , groundRect.top))

    if collision == True:
        return collision

    else:
        collision = (pygame.Rect.collidepoint(charRect , charRect.right , groundRect.top))

        if collision == True:
            return collision

def collideBottom(charRect,groundRect):

    collision = (pygame.Rect.collidepoint(charRect , charRect.left , groundRect.bottom))

    if collision == True:
        return collision

    else:
        collision = (pygame.Rect.collidepoint(charRect , charRect.right , groundRect.bottom))

        if collision == True:
            return collision

