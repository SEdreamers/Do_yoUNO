import random
from card import Card

class Deck:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.cards = []
        self.list = [] 
        self.load_cards()
    
    def load_cards(self):
        values = [str(i) for i in range(0, 10)]
        # skil card가 뒤쪽에 오도록 추가
        skill_values = ["skip", "reverse", "draw2", "draw4"]
        colorless_values = ["wild", "wild_draw2", "wild_draw4"]
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            for value in values:
                card = Card(value, color, self.screen_size[0], self.screen_size[1])
                self.cards.append(card)
                
        for color in colors:
            for value in skill_values:
                card = Card(value, color, self.screen_size[0], self.screen_size[1])
                self.cards.append(card)

        for value in colorless_values:
            for _ in range(3):
                card = Card(value, "black", self.screen_size[0], self.screen_size[1])
                self.cards.append(card)
        self.list = self.cards.copy()
                
    def shuffle(self):
        random.shuffle(self.cards)
    
            
    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    def append(self, card):
        self.cards.append(card)
    
    def pop(self):
        return self.cards.pop(0)
    
    def showlist(self):
        return self.list 
    

    def to_list(self):
        return [card.__str__() for card in self.cards]

    @classmethod
    def from_list(cls, screen_width, screen_height, data):
        deck = cls(screen_width, screen_height)
        print(data)
        for card_data in data:
            deck.cards = [Card.from_str(screen_width, screen_height, card_data)]
        return deck