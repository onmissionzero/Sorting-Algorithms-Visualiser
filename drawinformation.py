import pygame
import math

pygame.init()

class DrawInformation:
    SIDE_PAD = 500
    TOP_PAD = 125
    def __init__(self,lst):
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        diff = (self.max_val-self.min_val if self.max_val-self.min_val!=0 else 1)
        self.block_width = round((pygame.display.Info().current_w - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((pygame.display.Info().current_h - self.TOP_PAD) // (diff))
        self.start_x = (self.SIDE_PAD // 2) + 75

