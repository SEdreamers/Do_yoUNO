import pygame
from deck import Deck
from card import Card

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
font = pygame.font.SysFont('Arial', 24)

# Set up the game screen
screen_size = (1000, 800)
screen = pygame.display.set_mode(screen_size)
background_image = pygame.image.load("images/background.jpg")
background_image = pygame.transform.scale(background_image, screen_size)

# Get the dimensions of the computer's image
computer_width = 300
computer_height = 200

# Load the computer's image
computer_image = pygame.image.load("images/computer.png")
computer_image = pygame.transform.scale(computer_image, (computer_width, computer_height))

# Load the card's image
card_image = pygame.image.load("images/card.png")
card_image = pygame.transform.scale(card_image, (90, 120))

# Set the position of the computer's image on the right side of the screen
computer_x = screen_size[0] - computer_width
computer_y = 0

computers = []
computers.append(1)
computers.append(2)

# create a small box to display the color of the card
BOX_WIDTH = 40
BOX_HEIGHT = 40
color_box = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))
color_box.fill(RED)  # change this to whatever color you want to display

# create a UNO button
button_width = 80
button_height = 40
uno_button = pygame.Surface((button_width, button_height))
uno_button.fill(WHITE)

# add text to the button
font = pygame.font.Font(None, 30)
text = font.render("UNO", True, BLACK)
text_rect = text.get_rect(center=(button_width//2, button_height//2))
uno_button.blit(text, text_rect)

# create a deck and shuffle it
deck = Deck()
deck.shuffle()

# draw five cards from the deck
hand = []
for i in range(5):
    card = deck.draw()
    if card:
        hand.append(card)

# set up the card dimensions and spacing
card_width = 90
card_height = 120
card_spacing = 20

# set up the deck position and spacing
deck_x = 50
deck_y = 500
deck_spacing = 10

# setting player's deck position 
for i, card in enumerate(hand):
    x_pos = deck_x + i * (card_width + deck_spacing)
    y_pos = deck_y
    card.set_position(x_pos, y_pos)

top_card = deck.peek()
if top_card:
    top_card = Card(top_card.value, top_card.color)
    top_card.set_position(screen_size[0] * 0.4, screen_size[1] * 0.2)

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the computer's image on the screen
    for i in range(len(computers)):
        screen.blit(computer_image, (computer_x, computer_y + i * computer_height))
    
    # Draw the Deck image on the screen(back)
    screen.blit(card_image, (screen_size[0] * 0.2, screen_size[1] * 0.2))

    # Draw the Card image on the screen(front)
    # screen.blit(card_image, (screen_size[0] * 0.4, screen_size[1] * 0.2))
    if top_card:
        screen.blit(top_card.image, top_card.rect)

    # Draw the box showing color of the card
    screen.blit(color_box, (screen_size[0] * 0.55, screen_size[1] * 0.2))

    #  Draw the UNO button
    screen.blit(uno_button, (screen_size[0] * 0.55, screen_size[1] * 0.27))
    
    # draw the cards(player)
    for card in hand:
        screen.blit(card.image, card.rect)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()