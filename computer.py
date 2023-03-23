import pygame
from player import Player
from gameUI import GameUI
from card import Card

class Computer(Player):
    def __init__(self, screen, deck, i):
        super().__init__("Computer" + str(i), screen, deck)
        self.screen = screen
        self.screen_size = (screen.get_width(), screen.get_height())
        # Get the dimensions of the computer's image
        self.computer_width = self.screen_size[0] / 3.333
        self.computer_height = self.screen_size[1] / 5
        # Load the computer's image
        self.computer_image = pygame.image.load("images/gray.jpg")
        self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))
        self.backcard_image = pygame.image.load("images/card.png")
        self.backcard_image = pygame.transform.scale(self.backcard_image, (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))
        
        # create a skip icon
        self.skip_icon = pygame.image.load("images/skip.png")
        self.skip_icon = pygame.transform.scale(self.skip_icon, (self.computer_width / 4, self.computer_width / 4))
        self.skip_rect = self.skip_icon.get_rect()

    # card 그리기 추가하기
    def draw(self, i):      ## 컴퓨터 플레이어 수만큼 호출
        # Set the position of the computer's image on the right side of the screen
        computer_x = self.screen_size[0] - self.computer_width
        computer_y = 0
        self.screen.blit(self.computer_image, (computer_x, computer_y + i * self.computer_height))

        # print(i)

        N = Player.count_cards(self)
        for x in range(N):
            self.screen.blit(self.backcard_image,(computer_x+ x*self.computer_height*0.1, computer_y+ i * self.computer_height))
        # print("남은 카드 수:" + str(Player.count_cards(self)))  ##컴퓨터 플레이어의 남은 카드 장수 출력. game.py에서 test로 출력가능. 이 부분 생략. 
    
    def skip_draw(self, i): # draw the skip icon
        skip_x = self.screen_size[0] - self.computer_width + self.computer_width // 2
        skip_y = i * self.computer_height + self.computer_height // 2
        self.skip_rect.centerx = skip_x
        self.skip_rect.centery = skip_y
        self.screen.blit(self.skip_icon, self.skip_rect)
        
        
        