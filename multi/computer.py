import pygame
from multi.player import Player
from gameUI import GameUI
from card import Card
import time
import json
import lobby


class Computer(Player):
    def __init__(self, screen, deck, i, region, character):
        super().__init__("Computer" + str(i), screen, deck, region, character)

        try:
            with open('setting_data.json') as game_file:
                self.data = json.load(game_file)
        except:
            self.data = {
                "color_blind_mode": False,
                "size": (800, 600),
                "Total_Volume": 0.3,
                "Background_Volume": 0.3,
                "Sideeffect_Volume": 0.3,
                "player_numbers": 3,
                "me": 'player',
                "c1name": 'computer1',
                "c2name": 'computer2',
                "c3name": 'computer3',
                "c4name": 'computer4',
                "c5name": 'computer5',
                "unclicked_list": []
            }

        self.screen = screen
        self.screen_size = (screen.get_width(), screen.get_height())
        # Get the dimensions of the computer's image
        self.computer_width = self.screen_size[0] / 3.333
        self.computer_height = self.screen_size[1] / 5
        # Load the computer's image
        self.computer_image = pygame.image.load("images/gray.jpg")
        self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))
        self.backcard_image = pygame.image.load("images/card.png")
        self.backcard_image = pygame.transform.scale(self.backcard_image,
                                                     (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))

        # create a skip icon
        self.skip_icon = pygame.image.load("images/skip.png")
        self.skip_icon = pygame.transform.scale(self.skip_icon, (self.computer_width / 4, self.computer_width / 4))
        self.skip_rect = self.skip_icon.get_rect()

        font = pygame.font.SysFont("arial", self.screen_size[0] // 40, True)
        # create computer name
        self.c1name = font.render(self.data["c1name"], True, 'GREEN')  ## 이름 받는 부분
        self.c1name_rect = self.c1name.get_rect()

        self.c2name = font.render(self.data["c2name"], True, 'GREEN')  ## 이름 받는 부분
        self.c2name_rect = self.c2name.get_rect()

        self.c3name = font.render(self.data["c3name"], True, 'GREEN')  ## 이름 받는 부분
        self.c3name_rect = self.c3name.get_rect()

        self.c4name = font.render(self.data["c4name"], True, 'GREEN')  ## 이름 받는 부분
        self.c4name_rect = self.c4name.get_rect()

        self.c5name = font.render(self.data["c5name"], True, 'GREEN')  ## 이름 받는 부분
        self.c5name_rect = self.c4name.get_rect()

    # card 그리기 추가하기
    def draw(self, i):  ## 컴퓨터 플레이어 수만큼 호출
        # Set the position of the computer's image on the right side of the screen
        computer_x = self.screen_size[0] - self.computer_width
        computer_y = 0
        self.screen.blit(self.computer_image, (computer_x, computer_y + i * self.computer_height))

        N = Player.count_cards(self)
        for x in range(N):
            self.screen.blit(self.backcard_image,
                             (computer_x + x * self.computer_height * 0.1, computer_y + i * self.computer_height))

        # 컴퓨터 이름 화면에 띄우는 부분.
        if self.data["unclicked_list"][i] == 0:
            self.c1name_rect.x, self.c1name_rect.y = computer_x, i * self.computer_height
            self.screen.blit(self.c1name, self.c1name_rect)
        elif self.data["unclicked_list"][i] == 1:
            self.c2name_rect.x, self.c2name_rect.y = computer_x, i * self.computer_height
            self.screen.blit(self.c2name, self.c2name_rect)
        elif self.data["unclicked_list"][i] == 2:
            self.c3name_rect.x, self.c3name_rect.y = computer_x, i * self.computer_height
            self.screen.blit(self.c3name, self.c3name_rect)
        elif self.data["unclicked_list"][i] == 3:
            self.c4name_rect.x, self.c4name_rect.y = computer_x, i * self.computer_height
            self.screen.blit(self.c4name, self.c4name_rect)
        elif self.data["unclicked_list"][i] == 4:
            self.c5name_rect.x, self.c5name_rect.y = computer_x, i * self.computer_height
            self.screen.blit(self.c5name, self.c5name_rect)

        # print("남은 카드 수:" + str(Player.count_cards(self)))  ##컴퓨터 플레이어의 남은 카드 장수 출력. game.py에서 test로 출력가능. 이 부분 생략.

    def skip_draw(self, i):  # draw the skip icon
        skip_x = self.screen_size[0] - self.computer_width + self.computer_width // 2
        skip_y = i * self.computer_height + self.computer_height // 2
        self.skip_rect.centerx = skip_x
        self.skip_rect.centery = skip_y
        self.screen.blit(self.skip_icon, self.skip_rect)

