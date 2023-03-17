import pygame
from hand import Hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand([])

    def draw(self, x, y):
        font = pygame.font.SysFont(None, 30)
        # name_text = font.render(self.name, True, WHITE)
        # screen.blit(name_text, (x, y))
        # self.hand.draw(x + 10, y + 30)

    def add_card(self, card):
        self.hand.add_card(card)

    def remove_card(self, card):
        self.hand.remove_card(card)

    def get_card_index(self, card):
        return self.hand.get_card_index(card)

    def get_card_by_index(self, index):
        return self.hand.get_card_by_index(index)

    def has_color(self, color):
        return self.hand.has_color(color)

    def has_number(self, number):
        return self.hand.has_number(number)
    
    def get_playable_cards(self, top_card_color, top_card_value):
        playable_cards = []
        for card in self.hand.cards:
            if card.color == top_card_color or card.number == top_card_value:
                playable_cards.append(card)
        return playable_cards

    def count_cards(self):
        return self.hand.count()