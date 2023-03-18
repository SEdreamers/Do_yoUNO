from player import Player
class Human(Player):
    def __init__(self, screen, deck, color_blind_mode):
        super().__init__("name", screen, deck)
        self.screen = screen
        self.screen_size = (self.screen.get_width(), self.screen.get_height())
        self.color_blind_mode = color_blind_mode
    
    def draw(self):
    # draw the cards(player)(front)
        for card in self.hand.cards:
            if not self.color_blind_mode:                
                self.screen.blit(card.default_image, card.rect)
            else:              
                self.screen.blit(card.blind_image, card.rect)