class Hand:
    def __init__(self, screen, deck):
        self.screen = screen
        self.deck = deck
        self.cards = []
        for _ in range(5):      ## 처음 주어지는 카드 수
            card = self.deck.pop()
            if card:
                self.cards.append(card)

    def is_empty(self):
        return len(self.cards) == 0
    
