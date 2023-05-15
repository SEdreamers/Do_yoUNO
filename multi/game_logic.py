import pygame
import main
import hand
from deck import Deck
from human import Human
from computer import Computer
from gameUI import GameUI
import gameoverUI
from card import Card
from player import Player
import innersetting
import time
import json
import math
import copy
import random

import pickle


# 게임의 상태를 저장할 클래스
class GameState:
    def __init__(self, score, level):
        self.score = score
        self.level = level


# # 게임의 초기 상태
# initial_state = GameState(0, 1)

# self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip, self.start_time

# # 게임의 상태를 저장하는 함수
# def save_game_state(state, filename):
#     with open(filename, 'wb') as file:
#         pickle.dump(state, file)

# # 게임의 상태를 불러오는 함수
# def load_game_state(filename):
#     with open(filename, 'rb') as file:
#         state = pickle.load(file)
#     return state

# # 게임의 상태를 저장할 파일명
# save_filename = 'game_state.pickle'

# # 게임의 상태를 저장
# save_game_state(initial_state, save_filename)

# # 게임의 상태를 불러옴
# loaded_state = load_game_state(save_filename)

# # 불러온 상태 출력
# print("Loaded State - Score: {}, Level: {}".format(loaded_state.score, loaded_state.level))


class GameLogic:
    def __init__(self, screen_width, screen_height, color_blind_mode, numberofPlayers, character,
                 deck, players, turn_num, reverse, region='E'):
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        # font = pygame.font.SysFont("arial", self.screen_size[0] // 42, True, True)
        self.color_blind_mode = color_blind_mode
        self.numberofPlayers = numberofPlayers
        self.character = character

        # Set up the game screen
        self.screen = pygame.display.set_mode(self.screen_size)
        background_image = pygame.image.load("images/green.jpg")
        background_image = pygame.transform.scale(background_image, self.screen_size)
        self.running = True

        self.deck = deck
        self.players = players

        # combo
        self.combo = 0
        self.region = region
        # Load the image
        self.combo_image = pygame.image.load('images/combo.jpg')
        self.combo_image = pygame.transform.scale(self.combo_image,
                                                  (self.screen_size[0] / 3.333, self.screen_size[0] / 3.333))
        self.combo_rect = self.combo_image.get_rect()
        self.combo_rect.x = self.screen_size[0] * 0.55
        self.combo_rect.y = self.screen_size[1] * 0.27
        # # Set up the Deck
        # self.deck = Deck(self.screen_size[0], self.screen_size[1])
        # self.deck.shuffle()

        # Draw the Deck image on the screen(back)
        self.back_card = Card(0, "back", self.screen_width, self.screen_height)
        # create the uno button
        self.uno_btn = pygame.image.load("images/uno_btn.png")
        self.uno_btn = pygame.transform.scale(self.uno_btn, (self.screen_size[0] / 12.5, self.screen_size[0] * 0.054))
        self.uno_rect = self.uno_btn.get_rect()
        self.uno_rect.x = self.screen_size[0] * 0.55
        self.uno_rect.y = self.screen_size[1] * 0.27

        # turn, reverse, skip, start time 세팅
        self.turn_num = turn_num
        self.reverse = reverse
        self.skip = False
        self.start_time = -1

        self.clicked_uno = []
        self.random_delay = []
        self.clicked_uno_player = False

        self.firstDeck = Deck(self.screen_size[0], self.screen_size[1])
        self.lst = self.firstDeck.showlist()
        not_first_top_list = [x for x in self.lst if
                              "reverse" or "draw2" or "draw4" or "wild" or "wild_draw4" or "wild_swap" in x]

        # print(not_first_top_list)
        self.top_card = self.deck.pop()

        # 시작 카드(top_card) 동작 처리
        if self.top_card.value == 'skip':
            self.turn_num = self.top_card.skip_action(self.turn_num, len(self.players), self.reverse)
            self.skip = True
        elif self.top_card.value == 'reverse':
            self.reverse = self.top_card.reverse_action(self.reverse)
        elif self.top_card.value == 'draw2' or self.top_card.value == 'draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num - 1, int(self.top_card.value[4]),
                                      self.reverse)
        elif self.top_card.color == 'black':
            colors = ['red', 'yellow', 'green', 'blue']
            random_color = random.choice(colors)
            self.top_card.color = random_color
            if self.top_card.value == 'wild_draw2' or self.top_card.value == 'wild_draw4':
                self.top_card.draw_action(self.deck, self.players, self.turn_num - 1, int(self.top_card.value[9]),
                                          self.reverse)

        # Game 너비, 높이 기본 배경 설정

        if region == "D":
            self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), self.color_blind_mode, self.uno_btn,
                                 region)
        else:
            self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), self.color_blind_mode, self.uno_btn)


        self.move = pygame.mixer.Sound('soundeffect-move.mp3')  ## 효과음 추가(move)
        ##innersetting.py의 Setting class
        self.set = innersetting.Setting(self.screen_width, self.screen_height, self.color_blind_mode, self.players,
                                        self.turn_num, self.top_card, self.back_card, self.reverse, self.skip,
                                        self.start_time, self.move)

        self.back_card_pos = [self.screen_size[0] * 0.2, self.screen_size[1] * 0.2]
        self.top_card_pos = [self.screen_size[0] * 0.4, self.screen_size[1] * 0.2]


    def save_play(self):
        # 실행중이던 세팅 설정을 딕셔너리 형태로 저장
        with open('game_data.json', 'w') as game_data_file:
            json.dump(self.data, game_data_file)
    def stop(self):
        self.running = False
    def run(self):
        pygame.init()

        with open('setting_data.json') as game_file:
            data = json.load(game_file)
            tvol = data["Total_Volume"]
            bvol = data["Background_Volume"]
            svol = data["Sideeffect_Volume"]

        pygame.mixer.music.set_volume(tvol)
        pygame.mixer.init()
        pygame.mixer.music.load('unogame.mp3')
        pygame.mixer.music.play(-1, 3)  ## 무한번 반복, 음악의 3초 지점부터 재생

        if self.skip:  # 시작 카드가 skip 카드인 경우
            self.GameUI.display(self.players, self.turn_num - 1, self.top_card, self.back_card, self.reverse, self.skip,
                                self.start_time, self.clicked_uno_player)
            self.skip = False
        else:
            self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip,
                                self.start_time, self.clicked_uno_player)

        try:
            with open('game_data.json', 'w') as play_data_file:
                json.dump(self.data, play_data_file)
        except:
            print("No file created yet!")

        self.turn_num = 0
        while self.running:
            # Human turn인지 Computer turn인지 구분
            if self.turn_num == 0:  # Human turn
                print('Human turn:' + str(self.turn_num))
                is_draw = self.handle_events()
                if not is_draw:  # 카드를 낸 경우만
                    if len(self.players[self.turn_num].hand.cards) == 1:  # 직전에 카드를 내어 카드가 2장에서 1장이 된 경우
                        # 다른 플레이어가 현재 플레이어보다 uno버튼을 빠르게 눌렀거나 아무도 누르지 않은 경우 현재 플레이어에게 1장 강제 부여
                        try:
                            if self.clicked_uno[0] != self.players[self.turn_num].name:
                                self.players[self.turn_num].hand.cards.append(self.deck.pop())
                        except:
                            self.players[self.turn_num].hand.cards.append(self.deck.pop())

                    self.update()
            else:  # Computer turn
                print('Computer turn:' + str(self.turn_num))
                self.auto_handling()  ## 자동으로 카드 가져가거나 내도록

                if len(self.players[self.turn_num].hand.cards) == 1:  # 직전에 카드를 내어 카드가 2장에서 1장이 된 경우
                    # 다른 플레이어가 현재 플레이어보다 uno버튼을 빠르게 눌렀거나 아무도 누르지 않은 경우 현재 플레이어에게 1장 강제 부여
                    try:
                        if self.clicked_uno[0] != self.players[self.turn_num].name:
                            self.players[self.turn_num].hand.cards.append(self.deck.pop())
                    except:
                        self.players[self.turn_num].hand.cards.append(self.deck.pop())

                self.update()
            self.render()
            # print(self.clicked_uno)

            # 게임 오버 판별
            if self.players[self.turn_num].hand.is_empty():
                game_over = gameoverUI.GameOverUI(self.screen_size[0], self.screen_size[1],
                                                  self.players[self.turn_num].name, self.color_blind_mode)

                if self.turn_num == 0:
                    try:
                        with open('story_mode_data.json') as story_mode_data_file:
                            data = json.load(story_mode_data_file)
                            unlocked_regions = data['unlocked_regions']  # 저장된 값 불러오기
                            rg = f"region{chr(ord(self.region) + 1)}"
                            if rg not in unlocked_regions:
                                unlocked_regions.append(rg)
                                data = {
                                    "unlocked_regions": unlocked_regions
                                }
                        with open('story_mode_data.json', 'w') as story_mode_data_file:
                            json.dump(data, story_mode_data_file)
                    except:
                        pass

                while True:
                    game_over.display()  # 게임 오버 화면 불러오기
                    pygame.display.flip()

            self.clicked_uno_player = None
            # combo true일 때는 turn 안 넘기기
            if self.combo == 0:
                # turn 전환
                if not self.reverse:
                    self.turn_num += 1
                    if self.turn_num >= len(self.players):
                        self.turn_num = 0
                else:
                    self.turn_num -= 1
                    if self.turn_num < 0:
                        self.turn_num = len(self.players) - 1
        pygame.quit()

    # function is responsible for handling user input and events
    def handle_events(self):
        self.set_random_delay()

        self.start_time = pygame.time.get_ticks()  # 타이머 시작 시간
        game_paused = False
        # for animation
        move_speed = 5
        self.card_clicked = None
        deck_x = self.screen_size[0] / 20
        deck_y = self.screen_size[0] / 2
        temp = -self.screen_size[0] / 40 + self.screen_size[0] / 12.5

        # set position
        self.hand_card_pos_temp = [deck_x + (len(self.players[0].hand.cards) - 1) * temp, deck_y]
        self.hand_card_pos = [temp + self.hand_card_pos_temp[0], self.hand_card_pos_temp[1]]

        # set rect
        self.back_card.set_position(self.screen_size[0] * 0.2, self.screen_size[1] * 0.2)
        self.players[0].hand.cards[len(self.players[0].hand.cards) - 1].set_position(self.hand_card_pos_temp[0],
                                                                                     self.hand_card_pos_temp[1])
        self.back_rect = self.back_card.rect
        self.hand_rect = self.players[0].hand.cards[len(self.players[0].hand.cards) - 1].rect

        # set distance
        back_to_hand = math.dist(self.back_card_pos, self.hand_card_pos) / move_speed
        hand_to_deck = math.dist(self.hand_card_pos_temp, self.top_card_pos) / move_speed

        start_time = None
        start_time2 = pygame.time.get_ticks()
        delay_time = 3

        clock = pygame.time.Clock()
        self.clicked_uno = []
        fps = 500
        while self.running:
            count_down = self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse,
                                             self.skip, self.start_time, self.clicked_uno_player)  # 타이머 시간 업데이트

            if count_down <= 0:  # 제한 시간 내에 카드를 내지 못한 경우
                start_time = pygame.time.get_ticks()
                self.players[self.turn_num].hand.cards.append(self.deck.pop())  # 카드 한장 강제 부여
                self.card_clicked = self.back_card

            elapsed_time = (pygame.time.get_ticks() - start_time2) / 1000
            if int(elapsed_time) > delay_time:
                elapsed_time = delay_time

            if len(self.players[
                       self.turn_num].hand.cards) == 2:  # 현재 플레이어의 카드가 2장 남았을 때 각 컴퓨터 플레이어는 랜덤하게 설정된 시간에 따라 clicked_uno에 append됨
                for idx, t in enumerate(self.random_delay):
                    if int(elapsed_time) == t and self.players[idx + 1].name not in self.clicked_uno:
                        self.clicked_uno.append(self.players[idx + 1].name)
                        if len(self.clicked_uno) == 1:  # uno버튼을 첫번째로 누른 플레이어가 현재 플레이어면
                            self.clicked_uno_player = self.players[idx + 1].name
                            self.render()

            if game_paused == True: pass
            # Calculate the interpolation ratio
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if self.screen_size[0] / 66.667 < pos[0] < self.screen_size[0] / 16.667 and self.screen_size[1] / 37.5 < \
                        pos[1] < self.screen_size[1] / 17.143:
                    GameUI.exit_flag = 1
                else:
                    GameUI.exit_flag = 0
                if event.type == pygame.QUIT:
                    self.save_play()
                    self.running = False
                # keyboard handling
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Pause!")
                        game_paused = True
                        # pygame.mixer.music.pause()    ##잠시 음악 중단 - 넣을 필요 없음(setting들어가서 볼륨 얼마나 조절되는지 확인하기 위해;)

                        # font = pygame.font.SysFont("arial", self.screen_width // 40, True)
                        # surface = pygame.Surface((size[0] / 1.5, size[1] / 1.5))
                        # text_surface = font.render("Setting", True, (255, 0, 0))
                        # surface.fill((255, 255, 255))
                        # surface.blit(text_surface, (surface.get_width() / 3, surface.get_height() / 8))
                        # self.screen.blit(surface, (size[0] / 6, size[1] / 6))
                        # pygame.display.update()
                        # pygame.time.delay(15000)

                        self.set.run(self.screen_width, self.screen_height)



                    elif event.key == pygame.K_q:
                        self.running = False
                        main.main(self.screen_size[0], self.screen_size[1], self.color_blind_mode)
                    if not GameUI.backcard_uno_flag:
                        if event.key == pygame.K_LEFT:
                            GameUI.cur_card -= 1
                            if GameUI.cur_card < 0:
                                GameUI.cur_card = 0
                            self.render()
                        elif event.key == pygame.K_RIGHT:
                            GameUI.cur_card += 1
                            if GameUI.cur_card > len(self.players[0].hand.cards) - 1:
                                GameUI.cur_card = len(self.players[0].hand.cards) - 1
                            self.render()
                        elif event.key == 13:  ## press entered
                            entered_card = self.players[0].hand.cards[GameUI.cur_card]
                            if entered_card.can_play_on(self.top_card):
                                # skip 2번 방지
                                self.skip_flag = 0
                                self.card_clicked = entered_card
                                start_time = pygame.time.get_ticks()
                                self.top_card = entered_card
                                self.deck.append(self.top_card)
                                self.players[self.turn_num].hand.cards.remove(entered_card)
                                self.update()
                                if GameUI.cur_card > len(self.players[0].hand.cards) - 1:
                                    GameUI.cur_card = len(self.players[0].hand.cards) - 1
                                    self.render()
                            if self.top_card.color == 'black':
                                self.render()
                                play = True
                                while play:
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                            pos = pygame.mouse.get_pos()
                                            # print(pos)
                                            if self.screen_size[0] / 4 < pos[0] < self.screen_size[0] / 3.448 and \
                                                    self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                                self.top_card.color = 'blue'
                                                self.render()
                                                play = False
                                            elif self.screen_size[0] / 2.41 < pos[0] < self.screen_size[0] / 2.1978 and \
                                                    self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                                self.top_card.color = 'green'
                                                self.render()
                                                play = False
                                            elif self.screen_size[0] / 1.72 < pos[0] < self.screen_size[0] / 1.61 and \
                                                    self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                                self.top_card.color = 'red'
                                                self.render()
                                                play = False
                                            elif self.screen_size[0] / 1.333 < pos[0] < self.screen_size[0] / 1.266 and \
                                                    self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                                self.top_card.color = 'yellow'
                                                self.render()
                                                play = False
                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_RIGHT:
                                                GameUI.color_flag += 1
                                                GameUI.color_flag %= 4
                                                self.render()
                                            elif event.key == pygame.K_LEFT:
                                                GameUI.color_flag -= 1
                                                GameUI.color_flag %= 4
                                                self.render()
                                            elif event.key == 13:
                                                if GameUI.color_flag == 0:
                                                    self.top_card.color = 'blue'
                                                elif GameUI.color_flag == 1:
                                                    self.top_card.color = 'green'
                                                elif GameUI.color_flag == 2:
                                                    self.top_card.color = 'red'
                                                elif GameUI.color_flag == 3:
                                                    self.top_card.color = 'yellow'
                                                self.render()
                                                play == False
                                                return False
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        if GameUI.backcard_uno_flag:
                            GameUI.backcard_uno_flag = 0
                        else:
                            GameUI.backcard_uno_flag = 1
                        self.render()
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if GameUI.backcard_uno_flag == 1:
                            GameUI.backcard_uno_flag = 2
                        elif GameUI.backcard_uno_flag == 2:
                            GameUI.backcard_uno_flag = 1
                        self.render()
                    if event.key == 13 and GameUI.backcard_uno_flag == 1:
                        self.card_clicked = self.back_card
                        start_time = pygame.time.get_ticks()
                        self.players[self.turn_num].hand.cards.append(self.deck.pop())
                    elif event.key == 13 and GameUI.backcard_uno_flag == 2:  # uno 버튼 눌렀을 때
                        if len(self.players[self.turn_num].hand.cards) == 2:
                            if self.players[self.turn_num].name not in self.clicked_uno:
                                self.clicked_uno.append(self.players[self.turn_num].name)
                                if len(self.clicked_uno) == 1:  # uno버튼을 첫번째로 누른 플레이어가 현재 플레이어면
                                    self.clicked_uno_player = self.players[self.turn_num].name
                                    self.render()

                # mouse handling
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    # print(pos)
                    if self.back_card.rect.collidepoint(pos):
                        self.card_clicked = self.back_card
                        start_time = pygame.time.get_ticks()
                        self.players[self.turn_num].hand.cards.append(self.deck.pop())

                    clicked_sprites = [s for s in self.players[self.turn_num].hand.cards if s.rect.collidepoint(pos)]

                    for sprite in clicked_sprites:
                        if sprite.can_play_on(self.top_card):
                            self.skip_flag = 0
                            self.card_clicked = sprite
                            start_time = pygame.time.get_ticks()
                            self.top_card = sprite
                            self.deck.append(self.top_card)
                            self.players[self.turn_num].hand.cards.remove(sprite)
                    if self.top_card.color == 'black':
                        self.render()
                        play = True
                        while play:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    self.save_play()
                                    play = False
                                    self.running = False
                            if count_down <= 0:  # 제한 시간 내에 카드를 내지 못한 경우
                                start_time = pygame.time.get_ticks()
                                self.players[self.turn_num].hand.cards.append(self.deck.pop())  # 카드 한장 강제 부여
                                self.card_clicked = self.back_card
                                play = False
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    pos = pygame.mouse.get_pos()

                                    # print(pos)
                                    if self.screen_size[0] / 4 < pos[0] < self.screen_size[0] / 3.448 and \
                                            self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                        self.top_card.color = 'blue'
                                        self.render()
                                        play = False
                                    elif self.screen_size[0] / 2.41 < pos[0] < self.screen_size[0] / 2.1978 and \
                                            self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                        self.top_card.color = 'green'
                                        self.render()
                                        play = False
                                    elif self.screen_size[0] / 1.72 < pos[0] < self.screen_size[0] / 1.61 and \
                                            self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                        self.top_card.color = 'red'
                                        self.render()
                                        play = False
                                    elif self.screen_size[0] / 1.333 < pos[0] < self.screen_size[0] / 1.266 and \
                                            self.screen_size[1] / 2 < pos[1] < self.screen_size[1] / 1.807:
                                        self.top_card.color = 'yellow'
                                        self.render()
                                        play = False

                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RIGHT:
                                        GameUI.color_flag += 1
                                        GameUI.color_flag %= 4
                                        self.render()
                                    elif event.key == pygame.K_LEFT:
                                        GameUI.color_flag -= 1
                                        GameUI.color_flag %= 4
                                        self.render()
                                    elif event.key == 13:
                                        if GameUI.color_flag == 0:
                                            self.top_card.color = 'blue'
                                        elif GameUI.color_flag == 1:
                                            self.top_card.color = 'green'
                                        elif GameUI.color_flag == 2:
                                            self.top_card.color = 'red'
                                        elif GameUI.color_flag == 3:
                                            self.top_card.color = 'yellow'
                                        self.render()
                                        play == False
                                        return False

                    if self.uno_rect.collidepoint(pos):  # uno 버튼이 클릭된 경우

                        if len(self.players[self.turn_num].hand.cards) == 2:
                            if self.players[self.turn_num].name not in self.clicked_uno:

                                self.clicked_uno.append(self.players[self.turn_num].name)

                                if len(self.clicked_uno) == 1:  # uno버튼을 첫번째로 누른 플레이어가 현재 플레이어면
                                    self.clicked_uno_player = self.players[self.turn_num].name
                                    self.render()
                        # print(clicked_uno)
                    # exit 버튼이 클릭 된 경우
                    if self.screen_size[0] / 66.667 < pos[0] < self.screen_size[0] / 16.667 and self.screen_size[
                        1] / 37.5 < pos[1] < self.screen_size[1] / 17.143:
                        self.running = False
                        main.main(self.screen_size[0], self.screen_size[1], self.color_blind_mode)

            global svol
            with open('setting_data.json') as game_file:
                data = json.load(game_file)
                tvol = data["Total_Volume"]
                bvol = data["Background_Volume"]
                svol = data["Sideeffect_Volume"]

            if self.card_clicked is not None:
                running = True
                while running:
                    if self.card_clicked is self.back_card:
                        elapsed_time = pygame.time.get_ticks() - start_time
                        ratio = min(elapsed_time / back_to_hand, 1)
                        current_pos = self.card_clicked.rect.center
                        new_pos = self.hand_card_pos
                        self.card_clicked.rect.center = (current_pos[0] + (new_pos[0] - current_pos[0]) * ratio,
                                                         current_pos[1] + (new_pos[1] - current_pos[1]) * ratio)
                        self.screen.blit(self.card_clicked.default_image, self.card_clicked.rect)
                        pygame.display.flip()
                        clock.tick(fps)

                        self.move = pygame.mixer.Sound('soundeffect-move.mp3')  ## 효과음 추가(move)
                        self.move.set_volume(svol)
                        self.move.play()

                        if ratio == 1:
                            running = False
                            return True
                    else:
                        elapsed_time = pygame.time.get_ticks() - start_time
                        ratio = min(elapsed_time / hand_to_deck, 1)
                        current_pos = self.card_clicked.rect.center
                        new_pos = self.top_card_pos
                        self.card_clicked.rect.center = (current_pos[0] + (new_pos[0] - current_pos[0]) * ratio,
                                                         current_pos[1] + (new_pos[1] - current_pos[1]) * ratio)
                        self.screen.blit(self.card_clicked.default_image, self.card_clicked.rect)
                        pygame.display.flip()
                        clock.tick(fps)

                        self.move = pygame.mixer.Sound('soundeffect-move.mp3')  ## 효과음 추가(move)
                        self.move.set_volume(svol)
                        self.move.play()

                        if ratio == 1:
                            running = False
                            return False

    def auto_handling(self):  ## 자동으로 카드 가져가거나 내도록
        self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip,
                            self.start_time, self.clicked_uno_player)  # 타이머 안뜨게 화면 업데이트

        self.set_random_delay()
        start_time2 = pygame.time.get_ticks()

        self.clicked_uno = []

        start_time = None
        self.card_clicked = None
        move_speed = 5
        clock = pygame.time.Clock()
        fps = 1000
        # set computer position
        computer_width = self.screen_size[0] / 3.333
        computer_height = self.screen_size[1] / 5
        computer_x = self.screen_size[0] - computer_width
        computer_y = 0
        self.card_len = Player.count_cards(self.players[self.turn_num])
        self.computer_pos_temp = [computer_x + self.card_len * computer_height * 0.1,
                                  computer_y + self.turn_num * computer_height]
        self.computer_pos = [computer_x + (self.card_len + 1) * computer_height * 0.1,
                             computer_y + self.turn_num * computer_height]
        back_to_com = math.dist(self.back_card_pos, self.computer_pos) / move_speed
        com_to_deck = math.dist(self.computer_pos_temp, self.top_card_pos) / move_speed

        hand_card_list = [s for s in self.players[self.turn_num].hand.cards]

        can_play = False
        for element in hand_card_list:
            if element.can_play_on(self.top_card):
                can_play = True
                break

        while self.running:
            elapsed_time = (pygame.time.get_ticks() - start_time2) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('game_data.json', 'w') as play_data_file:
                        json.dump(self.data, play_data_file)
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.uno_rect.collidepoint(pos):  # uno 버튼이 클릭된 경우
                        if len(self.players[self.turn_num].hand.cards) == 2:
                            if self.players[0].name not in self.clicked_uno:
                                self.clicked_uno.append(self.players[0].name)
                                if len(self.clicked_uno) == 1:  # uno버튼을 첫번째로 누른 플레이어인 인간 플레이어인 경우
                                    self.clicked_uno_player = self.players[0].name
                                    self.render()

            if len(self.players[
                       self.turn_num].hand.cards) == 2:  # 현재 컴퓨터 플레이어의 카드가 2장 남았을 때 각 컴퓨터 플레이어는 랜덤하게 설정된 시간에 따라 clicked_uno에 append됨
                if can_play:
                    for idx, t in enumerate(self.random_delay):
                        if int(elapsed_time) == t and self.players[idx + 1].name not in self.clicked_uno:
                            self.clicked_uno.append(self.players[idx + 1].name)
                            if len(self.clicked_uno) == 1:  # uno버튼을 첫번째로 누른 플레이어일 경우
                                self.clicked_uno_player = self.players[idx + 1].name
                                self.render()

            if elapsed_time > 3:
                for i, element in enumerate(hand_card_list):
                    if element.can_play_on(self.top_card):  ## 일반카드 규칙 성립할 때. 모든 카드를 살펴서 제출 가능한 카드가 있으면 바로 제출하고 함수 탈출.
                        # time.sleep(1.5)
                        self.skip_flag = 0

                        self.card_clicked = element
                        if self.region == "A":  # A일 때 컴퓨터 플레이어는 콤보 사용 가능
                            if self.combo > 0:
                                self.combo -= 1
                            if element.value == "reverse":
                                for j in range(i + 1, len(hand_card_list)):
                                    if hand_card_list[j].value == "reverse":
                                        index = self.players[self.turn_num].hand.cards.index(hand_card_list[j])
                                        # reverse 2개 있을 시 맨 앞으로 오도록 하기
                                        self.players[self.turn_num].hand.cards = self.players[self.turn_num].hand.cards[
                                                                                 index:] + self.players[
                                                                                               self.turn_num].hand.cards[
                                                                                           :index]
                                        self.combo = 2
                                        self.screen.blit(self.combo_image,
                                                         (self.screen_size[0] / 2, self.screen_size[1] / 2))
                                        time.sleep(1.5)
                            player_num = len(self.players)
                            if element.value == "skip":  # 1개만 있어도 combo 가능
                                if player_num == 2:
                                    self.combo = 1
                                    self.screen.blit(self.combo_image,
                                                     (self.screen_size[0] / 2, self.screen_size[1] / 2))
                                    time.sleep(1.5)
                                elif player_num == 3 or player_num == 6:  # 3개 있어야 combo 가능
                                    for j in range(i + 1, len(hand_card_list)):
                                        if hand_card_list[j].value == "skip":
                                            for k in range(j + 1, len(hand_card_list)):
                                                if hand_card_list[k].value == "skip":
                                                    index = self.players[self.turn_num].hand.cards.index(
                                                        hand_card_list[k])
                                                    index2 = self.players[self.turn_num].hand.cards.index(
                                                        hand_card_list[j])
                                                    self.players[self.turn_num].hand.cards = self.players[
                                                                                                 self.turn_num].hand.cards[
                                                                                             index:] + self.players[
                                                                                                           self.turn_num].hand.cards[
                                                                                                       :index]
                                                    self.players[self.turn_num].hand.cards = \
                                                    self.players[self.turn_num].hand.cards[0] + self.players[
                                                                                                    self.turn_num].hand.cards[
                                                                                                index2:] + self.players[
                                                                                                               self.turn_num].hand.cards[
                                                                                                           1:index2]
                                                    self.combo = 3
                                                    self.screen.blit(self.combo_image,
                                                                     (self.screen_size[0] / 2, self.screen_size[1] / 2))
                                                    time.sleep(1.5)
                                elif player_num == 4:  # 2개 있어야 combo 가능
                                    for j in range(i + 1, len(hand_card_list)):
                                        if hand_card_list[j].value == "skip":
                                            index = self.players[self.turn_num].hand.cards.index(hand_card_list[j])
                                            self.players[self.turn_num].hand.cards = self.players[
                                                                                         self.turn_num].hand.cards[
                                                                                     index:] + self.players[
                                                                                                   self.turn_num].hand.cards[
                                                                                               :index]
                                            self.combo = 2
                                            self.screen.blit(self.combo_image,
                                                             (self.screen_size[0] / 2, self.screen_size[1] / 2))
                                            time.sleep(1.5)

                        start_time = pygame.time.get_ticks()
                        self.top_card = element
                        self.deck.append(self.top_card)
                        self.players[self.turn_num].hand.cards.remove(element)  ##카드 제출
                        if self.top_card.color == 'black':
                            colors = ['red', 'yellow', 'green', 'blue']
                            random_color = random.choice(colors)
                            self.top_card.color = random_color
                        break
                if self.card_clicked == None:
                    # time.sleep(1.5)
                    self.card_clicked = self.back_card
                    start_time = pygame.time.get_ticks()
                    self.players[self.turn_num].hand.cards.append(self.deck.pop())  ## 카드 추가

                running = True
                while running:
                    if self.card_clicked is self.back_card:
                        elapsed_time = pygame.time.get_ticks() - start_time
                        ratio = min(elapsed_time / back_to_com, 1)
                        current_pos = self.card_clicked.rect.center
                        new_pos = self.computer_pos
                        self.card_clicked.rect.center = (current_pos[0] + (new_pos[0] - current_pos[0]) * ratio,
                                                         current_pos[1] + (new_pos[1] - current_pos[1]) * ratio)
                        self.screen.blit(self.card_clicked.default_image, self.card_clicked.rect)
                        pygame.display.flip()
                        clock.tick(fps)
                        if ratio == 1:
                            return
                    else:
                        elapsed_time = pygame.time.get_ticks() - start_time
                        ratio = min(elapsed_time / com_to_deck, 1)
                        current_pos = self.computer_pos_temp
                        new_pos = self.top_card_pos
                        self.card_clicked.rect.center = (current_pos[0] + (new_pos[0] - current_pos[0]) * ratio,
                                                         current_pos[1] + (new_pos[1] - current_pos[1]) * ratio)
                        self.screen.blit(self.card_clicked.default_image, self.card_clicked.rect)
                        pygame.display.flip()
                        clock.tick(fps)
                        if ratio == 1:
                            return

    # This function is responsible for updating the game state and logic
    def update(self):
        # 색 있는 기술카드 동작 처리
        if self.top_card.value == 'skip' and self.skip_flag == 0:
            self.turn_num = self.top_card.skip_action(self.turn_num, len(self.players), self.reverse)
            self.skip = True
            self.skip_flag += 1
        elif self.top_card.value == 'reverse':
            self.reverse = self.top_card.reverse_action(self.reverse)
        elif self.top_card.value == 'draw2' or self.top_card.value == 'draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num, int(self.top_card.value[4]), self.reverse)
        elif self.top_card.value == 'wild_draw2' or self.top_card.value == 'wild_draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num, int(self.top_card.value[9]), self.reverse)

    #  is responsible for rendering the current game state to the screen, including drawing game objects
    def render(self):
        self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip,
                            self.start_time, self.clicked_uno_player)
        self.skip = False

    def set_random_delay(self):
        self.random_delay = []
        if len(self.players[self.turn_num].hand.cards) == 2:  # 현재 플레이어의 카드가 2장 남은 경우
            for _ in range(len(self.players) - 1):  # 컴퓨터 플레이어 수만큼 1~3초 사이 난수 리스트에 append
                self.random_delay.append(random.randrange(1, 4))


'''
self.back_card 는 뒷면 그려진 카드 뭉치


self.top_card 는 앞면이 보이는 카드 더미 맨 윗장
'''
