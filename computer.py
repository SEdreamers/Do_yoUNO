import pygame
from player import Player
class Computer(Player):
    
    def __init__(self, screen, deck):
        super().__init__("name", screen, deck)
        self.screen = screen
        self.screen_size = (screen.get_width(), screen.get_height())
        # Get the dimensions of the computer's image
        self.computer_width = self.screen_size[0] / 3.333
        self.computer_height = self.screen_size[1] / 5
        # Load the computer's image
        self.computer_image = pygame.image.load("images/gray.jpg")
        self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))
    
    # card 그리기 추가하기
    def draw(self, i):
        # Set the position of the computer's image on the right side of the screen
        computer_x = self.screen_size[0] - self.computer_width
        computer_y = 0
        self.screen.blit(self.computer_image, (computer_x, computer_y + i * self.computer_height))
