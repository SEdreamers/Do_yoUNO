import random
from card import Card

class Deck:
    def __init__(self, color_blind_mode):
        self.cards = []
        self.load_cards(color_blind_mode)
    
    def load_cards(self, color_blind_mode):
        values = [str(i) for i in range(0, 10)] + ["skip", "reverse", "draw2", "draw4"]
        colorless_values = ["wild", "wild_draw4", "wild_swap"]
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            for value in values:
                card = Card(value, color, color_blind_mode)
                self.cards.append(card)
        for value in colorless_values:
            for _ in range(4):
                card = Card(value, "black", color_blind_mode)
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