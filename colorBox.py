import pygame

class ColorBox:
    def __init__(self, name, block_width, block_height, color_blind_mode):
        self.name = name
        if not color_blind_mode:
            self.image = pygame.transform.smoothscale(pygame.image.load("color_boxs/default_mode/" + self.name + "_box"+".png"), (block_width, block_height))
        else:
            self.image = pygame.transform.smoothscale(pygame.image.load("color_boxs/color_blind_mode/" + self.name + "_box"+".png"), (block_width, block_height))
        self.rect = self.image.get_rect()