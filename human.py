from player import Player
import pygame

class Human(Player):
    def __init__(self, screen, deck, color_blind_mode):
        super().__init__("Human", screen, deck)
        self.screen = screen
        self.screen_size = (self.screen.get_width(), self.screen.get_height())
        self.color_blind_mode = color_blind_mode
        
        # create a skip icon
        self.skip_icon = pygame.image.load("images/skip.png")
        self.skip_icon = pygame.transform.scale(self.skip_icon, (self.screen_size[0] / 10, self.screen_size[0] / 10))
        self.skip_rect = self.skip_icon.get_rect()

    
    def draw(self):
    # draw the cards(player)(front)
        for card in self.hand.cards:
            if not self.color_blind_mode:                
                self.screen.blit(card.default_image, card.rect)
            else:              
                self.screen.blit(card.blind_image, card.rect)

    def draw_one(self, cur_card):
        if not self.color_blind_mode:                
            self.screen.blit(self.hand.cards[cur_card].default_image, self.hand.cards[cur_card].rect)
        else:              
            self.screen.blit(self.hand.cards[cur_card].blind_image, self.hand.cards[cur_card].rect)
                
    def skip_draw(self): # draw the skip icon
        skip_x = (self.screen_size[0] - self.screen_size[0] / 3.333) / 2
        skip_y = self.screen_size[1] * 0.8
        self.skip_rect.centerx = skip_x
        self.skip_rect.centery = skip_y
        self.screen.blit(self.skip_icon, self.skip_rect)