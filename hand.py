class Hand:
    def __init__(self, screen, cards):
        self.screen = screen
        self.cards = cards

    def draw(self, x, y):
        for i, card in enumerate(self.cards):
            card.draw(x + i * 110, y)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def get_card_index(self, card):
        return self.cards.index(card)

    def get_card_by_index(self, index):
        return self.cards[index]

    def has_color(self, color):
        for card in self.cards:
            if card.color == color:
                return True
        return False

    def has_number(self, number):
        for card in self.cards:
            if card.number == number:
                return True
        return False
    def show(self):
        for card in self.cards:
            self.screen.blit(card.image, card.rect)
    def count(self):
        return len(self.cards)

    def is_empty(self):
        return len(self.cards) == 0