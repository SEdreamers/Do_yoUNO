import pygame
from deck import Deck
from human import Human
from computer import Computer
from gameUI import GameUI
from card import Card
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
        self.deck = Deck()
        self.deck.shuffle()

        # top_card deck에서 하나 뽑아서 설정
        self.top_card = self.deck.pop()

        # Draw the Deck image on the screen(back)
        self.back_card = Card(0, "back")

        # players 저장
        self.players = []
        # human player 만들기!
        human = Human(self.screen, self.deck, True)
        self.players.append(human)
        # add computers(player 숫자 받아서 설정)
        computers = []
        for _ in range(1):
            computers.append(Computer(self.screen, self.deck))
        self.players.extend(computers)

        # Game 너비, 높이 기본 배경 설정
        self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), True)

    def run(self):
        while self.running:
            pygame.init()
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()

    # function is responsible for handling user input and events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.back_card.rect.collidepoint(pos):
                    self.players[0].hand.cards.append(self.deck.pop())
                clicked_sprites = [s for s in self.players[0].hand.cards if s.rect.collidepoint(pos)]
                for sprite in clicked_sprites:
                    if sprite.can_play_on(self.top_card):
                        self.deck.append(self.top_card)
                        self.top_card = sprite 
                        self.players[0].hand.cards.remove(sprite) 

    # This function is responsible for updating the game state and logic
    def update(self):
        pass

    #  is responsible for rendering the current game state to the screen, including drawing game objects
    def render(self):
        self.GameUI.display(self.players, self.top_card, self.back_card)


    