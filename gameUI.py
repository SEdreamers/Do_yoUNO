from turtle import color
import pygame
import colorBox
from human import Human

class GameUI:
    def __init__(self, screen_width, screen_height, color_blind_mode):
         # Color
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        self.screen_size = (screen_width, screen_height)
        font = pygame.font.SysFont("arial", self.screen_size[0] // 42, True, True)
        self.color_blind_mode = color_blind_mode
        # Set up the game screen
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background_image = pygame.image.load("images/green.jpg")
        self.background_image = pygame.transform.scale(self.background_image, self.screen_size)

        # Get the dimensions of the computer's image
        self.computer_width = self.screen_size[0] / 3.333
        self.computer_height = self.screen_size[1] / 5

        # Load the computer's image
        self.computer_image = pygame.image.load("images/gray.jpg")
        self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))

        # Load the card's image(back)
        self.card_image = pygame.image.load("images/card.png")
        self.card_image = pygame.transform.scale(self.card_image, (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))
        
        # Load the image 
        self.player_background_image = pygame.image.load("images/skyblue.jpg")
        self.player_background_image = pygame.transform.scale(self.player_background_image, (self.screen_size[0] - self.computer_width, self.screen_size[1] * 0.4))

        self.computer_background_image = pygame.image.load("images/black.jpg")
        self.computer_background_image = pygame.transform.scale(self.computer_background_image, (self.computer_width, self.screen_size[1]))
        
        # # create a deck and shuffle it
        # color_blind_mode = False
        # deck = Deck()
        # deck.shuffle()

        # set up the card dimensions and spacing
        self.card_width = self.screen_size[0] / 12.5
        self.card_height = self.screen_size[0] / 8.333
        self.card_spacing = self.screen_size[0] / 50

        # set up the deck position and spacing
        self.deck_x = self.screen_size[0] / 20
        self.deck_y = self.screen_size[0] / 2
        self.deck_spacing = self.screen_size[0] / 100

        # create a small box to display the color of the card
        self.BOX_WIDTH = self.screen_size[0] / 25
        self.BOX_HEIGHT = self.screen_size[0] / 25

        # create a UNO button
        button_width = self.screen_size[0] / 12.5
        button_height = self.screen_size[0] / 25
        self.uno_button = pygame.Surface((button_width, button_height))
        self.uno_button.fill(WHITE)
        
        # create a direction icon
        self.direction_icon = pygame.image.load("images/direction.png")
        self.direction_icon = pygame.transform.scale(self.direction_icon, (self.screen_size[0] // 25, self.screen_size[0] // 25 * 4))

        # add text to the button
        font = pygame.font.Font(None, self.screen_size[0] // 42)
        text = font.render("UNO", True, BLACK)
        text_rect = text.get_rect(center=(button_width//2, button_height//2))
        self.uno_button.blit(text, text_rect)


    def display(self, players, turn_num, top_card, back_card, reverse, skip):
        # card 위치 설정(player card)
        for i, card in enumerate(players[0].hand.cards):
            x_pos = self.deck_x + i * (self.card_width + self.deck_spacing)
            y_pos = self.deck_y
            card.set_position(x_pos, y_pos)

        # Draw the background image
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.player_background_image, (0, self.screen_size[1] * 0.6))
        self.screen.blit(self.computer_background_image, (self.screen_size[0] - self.computer_width, 0))
            
        # Draw the computer's image on the screen (computer는 0번 자리 부터 -> i - 1)
        for i in range(1, len(players)):
            players[i].draw(i - 1)
                        
        # Draw the Deck image on the screen(back)
        back_card.set_position(self.screen_size[0] * 0.2, self.screen_size[1] * 0.2)
        self.screen.blit(self.card_image, back_card.rect)

        # setting current card
        if top_card:
            top_card.set_position(self.screen_size[0] * 0.4, self.screen_size[1] * 0.2)

        # Draw the top card image on the screen(front)
        if top_card:
            if not self.color_blind_mode:
                self.screen.blit(top_card.default_image, top_card.rect)
            else:
                self.screen.blit(top_card.blind_image, top_card.rect)
            color_box = colorBox.ColorBox(top_card.color, self.BOX_WIDTH, self.BOX_HEIGHT, self.color_blind_mode)
        # Draw the card that player has
        players[0].draw()

        # Draw the box showing color of the card
        self.screen.blit(color_box.image, (self.screen_size[0] * 0.55, self.screen_size[1] * 0.2))

        #  Draw the UNO button
        self.screen.blit(self.uno_button, (self.screen_size[0] * 0.55, self.screen_size[1] * 0.27))
            
        # Draw the direction icon
        if reverse:
            direction_icon = pygame.transform.rotate(self.direction_icon, 180)
        else:
            direction_icon = self.direction_icon
        direction_rect = direction_icon.get_rect()
        direction_rect.x = self.screen_size[0] - self.screen_size[0] / 3.333 - 40
        direction_rect.centery = self.screen.get_rect().centery
        self.screen.blit(direction_icon, direction_rect)
        
        # draw the skip icon
        if skip: 
            if isinstance(players[turn_num], Human): # turn을 skip 당한 플레이어가 Human일 경우
                players[turn_num].skip_draw()
            else: # turn을 skip 당한 플레이어가 Computer일 경우
                players[turn_num].skip_draw(int(players[turn_num].name[8]))
        
        # Update the screen
        pygame.display.flip()