from hand import Hand
from card import Card

class Player:
    def __init__(self, name, screen, deck, region):
        self.name = name
        self.deck = deck
        self.screen = screen

        if region == 'Z':
            self.hand = None
        else:
            self.hand = Hand(screen, deck, region, True)
            
    def get_hand(self):
        return self.hand
    def count_cards(self):
        return len(self.hand.cards)

    def to_list(self):
        return [card.__str__() for card in self.hand.cards]

    @classmethod
    def from_list(cls, name, screen, deck, region, data):
        player = cls(name, screen, deck, region)
        print(player)
        player.hand = Hand(screen, deck, region, False)
        player.hand.cards = [Card.from_str(screen.get_width(), screen.get_height(), card) for card in data]
        return player
