import random
from card import Card

class Deck:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.cards = []
        self.load_cards()
    
    def load_cards(self):
        values = [str(i) for i in range(0, 10)] + ["skip", "reverse", "draw2", "draw4"]
        colorless_values = ["wild", "wild_draw4", "wild_swap"]
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            for value in values:
                card = Card(value, color, self.screen_size[0], self.screen_size[1])
                self.cards.append(card)
        for value in colorless_values:
            for _ in range(4):
                card = Card(value, "black", self.screen_size[0], self.screen_size[1])
                self.cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.cards)
    
    def pop(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
            
    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    def append(self, card):
        self.cards.append(card)
    
    def pop(self):
        return self.cards.pop(0)
