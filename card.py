import pygame

class Card:
    def __init__(self, value, color, color_blind_mode=False):
        self.value = value
        self.color = color
        if not color_blind_mode:
            self.image_path = f"cards/defalut_mode/{color}_{value}.png"
        else:
            self.image_path = f"cards/color_blind_mode/{color}_{value}.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.smoothscale(self.image, (80, 120))
        self.rect = self.image.get_rect()
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y