import pygame
from deck import Deck
from human import Human
from computer import Computer
from gameUI import GameUI
from card import Card   
import innersetting 
import time 
import json
import math

class Game:
    def __init__(self, screen_width, screen_height, color_blind_mode):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        # font = pygame.font.SysFont("arial", self.screen_size[0] // 42, True, True)
        self.color_blind_mode = color_blind_mode


        ##innersetting.py의 Setting class
        self.set = innersetting.Setting(self.screen_width, self.screen_height)

        # Set up the game screen
        self.screen = pygame.display.set_mode(self.screen_size)
        background_image = pygame.image.load("images/green.jpg")
        background_image = pygame.transform.scale(background_image, self.screen_size)     
        self.running = True

        # Set up the Deck
        self.deck = Deck(self.screen_size[0], self.screen_size[1])
        self.deck.shuffle()

        # Draw the Deck image on the screen(back)
        self.back_card = Card(0, "back", self.screen_width, self.screen_height)
        
        # players 저장
        self.players = []
        # human player 만들기!
        human = Human(self.screen, self.deck, self.color_blind_mode)
        self.players.append(human)
        # add computers(player 숫자 받아서 설정)

        computers = []
        for i in range(1):
            computers.append(Computer(self.screen, self.deck, i))
        self.players.extend(computers)

        # turn, reverse, skip 세팅
        self.turn_num = 0
        self.reverse = False
        self.skip = False


        self.firstDeck = Deck(self.screen_size[0], self.screen_size[1]) 
        self.lst = self.firstDeck.showlist()
        not_first_top_list = [x for x in self.lst if "reverse" or "draw2" or "draw4" or "wild" or "wild_draw4" or "wild_swap" in x]
        # print(not_first_top_list)
        self.top_card = self.deck.pop()  


        # 시작 카드(top_card) 동작 처리
        if self.top_card.value == 'skip':
            self.turn_num = self.top_card.skip_action(self.turn_num, len(self.players), self.reverse)
            self.skip = True
        elif self.top_card.value == 'reverse':
            self.reverse = self.top_card.reverse_action(self.reverse)
        elif self.top_card.value == 'draw2' or self.top_card.value == 'draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num-1, int(self.top_card.value[4]), self.reverse)
        else: ## 추후 나머지 기술 카드 동작 처리 추가 
            pass 

        # Game 너비, 높이 기본 배경 설정
        self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), self.color_blind_mode)
        



        # 실행중이던 게임을 딕셔너리 형태로 저장
        self.data = {
            "hi":1
        }
        
        self.back_card_pos = [self.screen_size[0] * 0.2, self.screen_size[1] * 0.2]
        self.top_card_pos = [self.screen_size[0] * 0.4, self.screen_size[1] * 0.2]


    def run(self):
        pygame.init()

        if self.skip: # 시작 카드가 skip 카드인 경우
            self.GameUI.display(self.players, self.turn_num-1, self.top_card, self.back_card, self.reverse, self.skip)
            self.skip = False
        else:
            self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip)
        
        try: 
            with open('play_data.txt','w') as play_data_file: 
                json.dump(self.data, play_data_file)
        except: 
            print("No file created yet!")     ## 처음으로 게임 시작하게 될 경우, 하다가 나가버리면 자동으로 play_data.txt 가 생성되고 후에 불러올 수 있음. 



        while self.running:
            # Human turn인지 Computer turn인지 구분
            if isinstance(self.players[self.turn_num], Human): # Human turn
                print('Human turn:' + str(self.turn_num))
                is_draw = self.handle_events()
                if not is_draw: # 카드를 낸 경우만
                    self.update()
            else: # Computer turn
                print('Computer turn:' + str(self.turn_num))
                self.auto_handling()   ## 자동으로 카드 가져가거나 내도록
                self.update()
                
            
            '''
            # 카드 개수와 종류 출력하는 test
            for i in range(len(self.players)):
                print(str(i) + '(' + str(len(self.players[i].hand.cards)), end='): ') # 플레이어 번호(가지고 있는 카드 장수):
                print(self.players[i].hand.cards)
            '''
            


            self.render()

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
        game_paused = False
        # for animation
        move_speed = 10
        self.card_clicked = None
        deck_x = self.screen_size[0] / 20
        deck_y = self.screen_size[0] / 2
        temp = self.screen_size[0] / 50 + self.screen_size[0] / 12.5
        
        # set position
        self.hand_card_pos_temp = [deck_x + (len(self.players[0].hand.cards) - 1) * temp, deck_y]
        self.hand_card_pos = [temp + self.hand_card_pos_temp[0], self.hand_card_pos_temp[1]]
       
        # set rect
        self.back_card.set_position(self.screen_size[0] * 0.2, self.screen_size[1] * 0.2)
        self.players[0].hand.cards[len(self.players[0].hand.cards) - 1].set_position(self.hand_card_pos_temp[0], self.hand_card_pos_temp[1])
        self.back_rect = self.back_card.rect
        self.hand_rect = self.players[0].hand.cards[len(self.players[0].hand.cards) - 1].rect
        # set distance
        back_to_hand = math.dist(self.back_card_pos, self.hand_card_pos) / move_speed
        hand_to_deck = math.dist(self.hand_card_pos_temp, self.top_card_pos) / move_speed
        start_time = None
        clock = pygame.time.Clock()
        fps = 500
        while self.running:
            if game_paused == True: pass
            # Calculate the interpolation ratio 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    with open('play_data.txt','w') as play_data_file: 
                        json.dump(self.data, play_data_file)
                    self.running = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: 
                        print("Pause!")
                        game_paused = True
                        self.set.run(self.screen_width, self.screen_height)          
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.back_card.rect.collidepoint(pos):
                        self.card_clicked = self.back_card
                        start_time = pygame.time.get_ticks()
                        self.players[self.turn_num].hand.cards.append(self.deck.pop())
                        print('-' + str(self.reverse))     ## reverse 여부. 
                        
                        
                    clicked_sprites = [s for s in self.players[self.turn_num].hand.cards if s.rect.collidepoint(pos)]
                    for sprite in clicked_sprites:
                        if sprite.can_play_on(self.top_card):
                            self.card_clicked = sprite
                            start_time = pygame.time.get_ticks()
                            
                            self.top_card = sprite 
                            self.deck.append(self.top_card)
                            self.players[self.turn_num].hand.cards.remove(sprite)
                            
                            
            if self.card_clicked is not None:
                running = True
                while running:
                    if self.card_clicked == self.back_card:
                        elapsed_time = pygame.time.get_ticks() - start_time
                        ratio = min(elapsed_time / back_to_hand, 1)
                        current_pos = self.card_clicked.rect.center
                        new_pos = self.hand_card_pos
                        self.card_clicked.rect.center = (current_pos[0] + (new_pos[0] - current_pos[0]) * ratio,
                                                    current_pos[1] + (new_pos[1] - current_pos[1]) * ratio)
                        self.screen.blit(self.card_clicked.default_image, self.card_clicked.rect)
                        pygame.display.flip()
                        if ratio == 1:
                            self.card_clicked = None
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
                        if ratio == 1:
                            print(self.card_clicked.rect.center)
                            print(self.top_card_pos)
                            self.card_clicked = None 
                            return False
                    clock.tick(fps)


            


    def auto_handling(self):     ## 자동으로 카드 가져가거나 내도록
        while self.running:
            hand_card_list = [s for s in self.players[self.turn_num].hand.cards]
            for element in hand_card_list:  
                if  element.can_play_on(self.top_card):    ## 일반카드 규칙 성립할 때. 모든 카드를 살펴서 제출 가능한 카드가 있으면 바로 제출하고 함수 탈출. 
                    time.sleep(1.5)
                    self.top_card = element
                    self.deck.append(self.top_card)
                    self.players[self.turn_num].hand.cards.remove(element)  ##카드 제출
                    return
            else:   
                time.sleep(1.5)
                self.players[self.turn_num].hand.cards.append(self.deck.pop())  ## 카드 추가
                return 
            
                          
    # This function is responsible for updating the game state and logic
    def update(self):
        # 색 있는 기술카드 동작 처리
        if self.top_card.value == 'skip':
            self.turn_num = self.top_card.skip_action(self.turn_num, len(self.players), self.reverse)
            self.skip = True
        elif self.top_card.value == 'reverse':
            self.reverse = self.top_card.reverse_action(self.reverse)
        elif self.top_card.value == 'draw2' or self.top_card.value == 'draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num, int(self.top_card.value[4]), self.reverse)
        # 색 없는 기술카드 동작
        elif self.top_card.value == 'wild_draw4':
            pass
        elif self.top_card.value == 'wild_swap':
            pass
        elif self.top_card.value == 'wild':
            pass

    #  is responsible for rendering the current game state to the screen, including drawing game objects
    def render(self):
        self.GameUI.display(self.players, self.turn_num, self.top_card, self.back_card, self.reverse, self.skip)
        self.skip = False











'''
self.back_card 는 뒷면 그려진 카드 뭉치


self.top_card 는 앞면이 보이는 카드 더미 맨 윗장
'''