import pygame
import settings

pygame.init()


class Button():
    def __init__(self, x, y, width, height, ButtonColor, Text, TextColor):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttoncolor = ButtonColor
        if(self.buttoncolor==(0,255,0)):
            self.hovercolor = tuple(map(lambda i, j: i - j, self.buttoncolor, (0,35,0)))
        else:
            self.hovercolor = tuple(map(lambda i, j: i - j, self.buttoncolor, (35,35,35)))
        self.text = Text
        self.textcolor = TextColor
        self.clicked = False
        font_size = min(self.rect.width // len(self.text), self.rect.height // 2)
        self.font =pygame.font.Font('assets\\fonts\\RONORGERIONDEMO-Regular.otf', font_size)

    def draw(self,sorting=False):
        action = False
        pygame.draw.rect(settings.WINDOW, self.buttoncolor, self.rect, 0, 3)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(settings.WINDOW,self.hovercolor, self.rect, 0, 3)
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        if(sorting):
            pygame.draw.rect(settings.WINDOW,(127,127,127), self.rect, 0, 3)            
        text_surface = self.font.render(self.text, True, self.textcolor)
        text_rect = text_surface.get_rect(center=self.rect.center)
        settings.WINDOW.blit(text_surface, text_rect)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action