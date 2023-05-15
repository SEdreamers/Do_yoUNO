from hand import Hand
from card import Card

class Player:
    def __init__(self, name, screen, deck, region):
        self.name = name
        self.deck = deck
        self.screen = screen
        self.hand = Hand(screen, deck, region)
    def get_hand(self):
        return self.hand
    def count_cards(self):
        return len(self.hand.cards)
    

    @classmethod
    def from_list(cls, name, screen, deck, region, character, data):
        player = cls(name, screen, deck, region, character)
        player.hand = Hand(screen, deck, region, character)
        player.hand.cards = [Card.from_str(screen.get_width(), screen.get_height(), card) for card in data]