class Hand:
    def __init__(self, screen, cards):
        self.screen = screen
        self.cards = cards
        
    def count(self):
        return len(self.cards)

    def is_empty(self):
        return len(self.cards) == 0