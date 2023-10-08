import pygame

pygame.init()


#Settings
WIDTH, HEIGHT = 1280, 640
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualiser")
WindowIcon = pygame.image.load("Assets\\WindowIcon48.png").convert_alpha()
pygame.display.set_icon(WindowIcon)
FPS = 60
font = pygame.font.Font('assets\\fonts\\RONORGERIONDEMO-Regular.otf', 12)