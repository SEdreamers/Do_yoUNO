from hand import Hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand([])

    def count_cards(self):
        return self.hand.count()