import random
class Hand:
    def __init__(self, screen, deck, region):
        self.screen = screen
        self.deck = deck
        self.cards = []
        # set up the region
        if region == "A":
            random.shuffle(self.deck.cards[:40])
            random.shuffle(self.deck.cards[41:])
            for _ in range(5):
                random_number = random.uniform(0, 1)
                # skill card 맨 뒤 pop
                if random_number < 0.6:
                    card = self.deck.cards.pop()
                # 숫자 카드 맨 앞 pop
                else:
                    del self.deck.cards[0]
                    card = self.deck.cards.pop(0)
                if card:
                    self.cards.append(card)
        elif region == "D":
            for _ in range(5):      ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)
        elif region == "E":
            for _ in range(5):      ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)

    def is_empty(self):
        return len(self.cards) == 0
    