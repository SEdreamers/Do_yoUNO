import pygame

class Card(pygame.sprite.Sprite): 
    def __init__(self, value, color, screen):
        super().__init__()
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.screen_size = (screen.get_width(), screen.get_height())
        self.value = value
        self.color = color
        self.image = pygame.transform.smoothscale(pygame.image.load(f"cards/default_mode/{color}_{value}.png"), (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))
        self.blind_image = pygame.transform.smoothscale(pygame.image.load(f"cards/color_blind_mode/{color}_{value}.png"), (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def control(self, x, y):
        self.movex += x
        self.movey += y
    
    def can_play_on(self, other_card):
        # Check if the colors match
        if self.color == other_card.color:
            return True

        # Check if the numbers match
        if self.value == other_card.value:
            return True
        
        # Otherwise, the card can't be played
        return False

    def skip_action(self, turn_num, players_num, reverse):
        if not reverse:
            turn_num += 1
            if turn_num >= players_num:
                return 0
        else:
            turn_num -= 1
            if turn_num < 0:
                return players_num - 1
        return turn_num
        
    def reverse_action(self, reverse):
        return not reverse
    
    def draw_action(self, deck, players, turn_num, value, reverse):
        for _ in range(value):
                if not reverse:
                    players[turn_num+1].hand.cards.append(deck.pop())
                else:
                    players[turn_num-1].hand.cards.append(deck.pop())
    
    def __repr__(self):
        return self.color + ' ' + self.value
    
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
