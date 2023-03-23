import pygame
from deck import Deck
from human import Human
from computer import Computer
from gameUI import GameUI
from card import Card
import time 

class Game:
    def __init__(self, screen_width, screen_height, color_blind_mode):
        pygame.init()
        self.screen_size = (screen_width, screen_height)
        # font = pygame.font.SysFont("arial", self.screen_size[0] // 42, True, True)
        self.color_blind_mode = color_blind_mode

        # Set up the game screen
        self.screen = pygame.display.set_mode(self.screen_size)
        background_image = pygame.image.load("images/green.jpg")
        background_image = pygame.transform.scale(background_image, self.screen_size)     
        self.running = True

        # Set up the Deck
        self.deck = Deck(self.screen_size[0], self.screen_size[1])
        self.deck.shuffle()

        # Draw the Deck image on the screen(back)
        self.back_card = Card(0, "back", screen_width, screen_height)

        # players 저장
        self.players = []
        # human player 만들기!
        human = Human(self.screen, self.deck, self.color_blind_mode)
        self.players.append(human)
        # add computers(player 숫자 받아서 설정)

        computers = []
        for _ in range(1):
            computers.append(Computer(self.screen, self.deck))
        self.players.extend(computers)

        # turn과 방향 세팅
        self.turn_num = 0
        self.reverse = False

        # top_card deck에서 하나 뽑아서 설정
        self.top_card = self.deck.pop()  

        # 시작 카드(top_card) 동작 처리
        if self.top_card.value == 'skip':
            self.turn_num = self.top_card.skip_action(self.turn_num, len(self.players), self.reverse)
        elif self.top_card.value == 'reverse':
            self.reverse = self.top_card.reverse_action(self.reverse)
        elif self.top_card.value == 'draw2' or self.top_card.value == 'draw4':
            self.top_card.draw_action(self.deck, self.players, self.turn_num-1, int(self.top_card.value[4]), self.reverse)
        else: ## 추후 나머지 기술 카드 동작 처리 추가 
            pass 

        # Game 너비, 높이 기본 배경 설정
        self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), True)

    def run(self):
        pygame.init()
        self.GameUI.display(self.players, self.top_card, self.back_card, self.reverse)

        while self.running:
            # Human turn인지 Computer turn인지 구분
            if isinstance(self.players[self.turn_num], Human): # Human turn
                is_draw = self.handle_events()
                if not is_draw: # 카드를 낸 경우만
                    self.update()
                print('Human turn:' + str(self.turn_num))
            else: # Computer turn
                self.auto_handling()   ## 자동으로 카드 가져가거나 내도록
                self.update()
                print('Computer turn:' + str(self.turn_num))
                

            # 카드 개수와 종류 출력하는 test
            for i in range(len(self.players)):
                print(str(i) + '(' + str(len(self.players[i].hand.cards)), end='): ') # 플레이어 번호(가지고 있는 카드 장수):
                print(self.players[i].hand.cards)
            


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
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.back_card.rect.collidepoint(pos):
                        self.players[self.turn_num].hand.cards.append(self.deck.pop())
                        print('-' + str(self.reverse))
                        return True
                    clicked_sprites = [s for s in self.players[self.turn_num].hand.cards if s.rect.collidepoint(pos)]
                    for sprite in clicked_sprites:
                        if sprite.can_play_on(self.top_card):
                            self.top_card = sprite 
                            self.deck.append(self.top_card)
                            self.players[self.turn_num].hand.cards.remove(sprite)
                            return False
    

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
        self.GameUI.display(self.players, self.top_card, self.back_card, self.reverse)












'''
self.back_card 는 뒷면 그려진 카드 뭉치


self.top_card 는 앞면이 보이는 카드 더미 맨 윗장
'''