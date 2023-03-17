import pygame
from deck import Deck
from hand import Hand
class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.cards = []
        self.selected_card = None

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()

    # def handle_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    #             pos = pygame.mouse.get_pos()
    #     clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
    #     for sprite in clicked_sprites:
    #         sprite.on_click()


    