from player import Player
class Human(Player):
    def __init__(self, screen, cards, color_blind_mode):
        self.screen = screen
        self.cards = cards
        self.screen_size = (screen.get_width(), screen.get_height())
        self.color_blind_mode = color_blind_mode
    
    def draw(self):
    # draw the cards(player)(front)
        for card in self.cards:
            if not self.color_blind_mode:                
                self.screen.blit(card.default_image, card.rect)
            else:              
                self.screen.blit(card.blind_image, card.rect)