import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.load_cards()
    
    def load_cards(self):
        values = [str(i) for i in range(0, 10)] + ["skip", "reverse", "draw"]
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            for value in values:
                card = Card(value, color)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
            
    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None