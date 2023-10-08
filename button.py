import pygame
import settings

pygame.init()


class Button():
    def __init__(self,image,x,y,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        action = False

        #draw button on screen
        settings.WINDOW.blit(self.image,(self.rect.x,self.rect.y))

        #Get Mouse Position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            #ButtonHoverAnimationHere!!!!!!!!!
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action 