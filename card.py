import pygame

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.default_image = pygame.transform.smoothscale(pygame.image.load(f"cards/default_mode/{color}_{value}.png"), (80, 120))
        self.default_rect = self.default_image.get_rect()
        self.blind_image = pygame.transform.smoothscale(pygame.image.load(f"cards/color_blind_mode/{color}_{value}.png"), (80, 120))
        self.blind_rect = self.blind_image.get_rect()
    
    def move(self, dx, dy):
        self.default_rect.x += dx
        self.default_rect.y += dy
        self.blind_rect.x += dx
        self.blind_rect.y += dy
    
    def set_position(self, x, y):
        self.default_rect.x = x
        self.default_rect.y = y
        self.blind_rect.x = x
        self.blind_rect.y = y