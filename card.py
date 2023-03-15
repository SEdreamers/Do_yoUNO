import pygame

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.image_path = f"cards/{color}_{value}.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (90, 120))
        self.rect = self.image.get_rect()
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y