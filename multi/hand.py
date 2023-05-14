import random


class Hand:
    def __init__(self, screen, deck, region, character):
        self.screen = screen
        self.deck = deck
        self.region = region
        self.character = character
        self.cards = []

    def give_cards(self):
        # set up the region
        if self.region == "A" or self.character == True:
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
        elif self.region == "B":
            for _ in range(16):  ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)
        elif self.region == "C":
            for _ in range(5):  ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)
        elif self.region == "D":
            for _ in range(5):  ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)
        elif self.region == "E":
            for _ in range(5):  ## 처음 주어지는 카드 수
                card = self.deck.pop()
                if card:
                    self.cards.append(card)

    def is_empty(self):
        return len(self.cards) == 0
