import pygame
from deck import Deck
from human import Human
from computer import Computer
from gameUI import GameUI
from card import Card
class Game:
    def __init__(self, screen_width, screen_height, color_blind_mode):
        pygame.init()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        self.screen_size = (screen_width, screen_height)
        font = pygame.font.SysFont("arial", self.screen_size[0] // 42, True, True)
        self.color_blind_mode = color_blind_mode

        # Set up the game screen
        self.screen = pygame.display.set_mode(self.screen_size)
        background_image = pygame.image.load("images/green.jpg")
        background_image = pygame.transform.scale(background_image, self.screen_size)     
        self.running = True
        self.deck = Deck()
        self.deck.shuffle()
        # 임시로 앞에 넣어두기
        self.top_card = self.deck.pop()
        # Draw the Deck image on the screen(back)
        self.back_card = Card(0, "back")
        # draw five cards from the deck(front)
        self.hand = []
        for i in range(5):
            card = self.deck.draw()
            if card:
                self.hand.append(card)
        self.human = Human(self.screen, self.hand, True)
        # add computer(player 숫자 받아서 설정(추후에 변경))
        self.computer1_hand = []
        for i in range(5):
            card = self.deck.draw()
            if card:
                self.computer1_hand.append(card)
        self.computers = []
        computer1 = Computer(self.screen, self.computer1_hand)
        self.computers.append(computer1)
        self.GameUI = GameUI(self.screen.get_width(), self.screen.get_height(), True)
    def run(self):
        while self.running:
            pygame.init()
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.back_card.rect.collidepoint(pos):
                    self.hand.append(self.deck.pop())
                clicked_sprites = [s for s in self.hand if s.rect.collidepoint(pos)]
                for sprite in clicked_sprites:
                    if sprite.can_play_on(self.top_card):
                        self.deck.append(self.top_card)
                        self.top_card = sprite 
                        self.hand.remove(sprite) 
    def update(self):
        self.GameUI.gameScreen(self.hand, self.computers, self.top_card, self.back_card)
    def render(self):
        pass


    