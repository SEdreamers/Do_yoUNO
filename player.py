from hand import Hand
class Player:
    def __init__(self, name, screen, deck, region, character):
        self.name = name
        self.deck = deck
        self.screen = screen
        self.hand = Hand(screen, deck, region, character)
    def get_hand(self):
        return self.hand
    def count_cards(self):
        return len(self.hand.cards)