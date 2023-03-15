import pygame
from deck import Deck
from card import Card


def gameScrean(screen_width, screen_height):
    # Color
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    screen_size = (screen_width, screen_height)

    # Initialize Pygame
    pygame.init()
    font = pygame.font.SysFont("arial", screen_size[0] // 42, True, True)

    # Set up the game screen
    screen = pygame.display.set_mode(screen_size)
    background_image = pygame.image.load("images/background.jpg")
    background_image = pygame.transform.scale(background_image, screen_size)

    # Get the dimensions of the computer's image
    computer_width = screen_size[0] / 3.333
    computer_height = screen_size[1] / 5

    # Load the computer's image
    computer_image = pygame.image.load("images/computer.png")
    computer_image = pygame.transform.scale(computer_image, (computer_width, computer_height))

    # Set the position of the computer's image on the right side of the screen
    computer_x = screen_size[0] - computer_width
    computer_y = 0

    # add computer(player 숫자 받아서 설정(추후에 변경))
    computers = []
    computers.append(1)
    computers.append(2)

    # Load the card's image(back)
    card_image = pygame.image.load("images/card.png")
    card_image = pygame.transform.scale(card_image, (screen_size[0] / 12.5, screen_size[0] / 8.333))

    # create a deck and shuffle it
    color_blind_mode = True
    deck = Deck(color_blind_mode)
    deck.shuffle()

    # draw five cards from the deck(front)
    hand = []
    for i in range(5):
        card = deck.draw()
        if card:
            hand.append(card)

    # set up the card dimensions and spacing
    card_width = screen_size[0] / 12.5
    card_height = screen_size[0] / 8.333
    card_spacing = screen_size[0] / 50

    # set up the deck position and spacing
    deck_x = screen_size[0] / 20
    deck_y = screen_size[0] / 2
    deck_spacing = screen_size[0] / 100

    # setting player's deck position 
    for i, card in enumerate(hand):
        x_pos = deck_x + i * (card_width + deck_spacing)
        y_pos = deck_y
        card.set_position(x_pos, y_pos)
        
    # setting current card(peek)
    top_card = deck.peek()
    if top_card:
        top_card = Card(top_card.value, top_card.color, color_blind_mode)
        top_card.set_position(screen_size[0] * 0.4, screen_size[1] * 0.2)

    # create a small box to display the color of the card
    BOX_WIDTH = screen_size[0] / 25
    BOX_HEIGHT = screen_size[0] / 25
    color_box = pygame.Surface((BOX_WIDTH, BOX_HEIGHT))

    # create a UNO button
    button_width = screen_size[0] / 12.5
    button_height = screen_size[0] / 25
    uno_button = pygame.Surface((button_width, button_height))
    uno_button.fill(WHITE)

    # add text to the button
    font = pygame.font.Font(None, screen_size[0] // 42)
    text = font.render("UNO", True, BLACK)
    text_rect = text.get_rect(center=(button_width//2, button_height//2))
    uno_button.blit(text, text_rect)

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
        if top_card:
            screen.blit(top_card.image, top_card.rect)
            if top_card.color == "yellow":
                color_box.fill(YELLOW)
            elif top_card.color == "blue":
                color_box.fill(BLUE)
            elif top_card.color == "green":
                color_box.fill(GREEN)
            elif top_card.color == "red":
                color_box.fill(RED)

        # draw the cards(player)(front)
        for card in hand:
            screen.blit(card.image, card.rect)

        # Draw the box showing color of the card
        screen.blit(color_box, (screen_size[0] * 0.55, screen_size[1] * 0.2))

        #  Draw the UNO button
        screen.blit(uno_button, (screen_size[0] * 0.55, screen_size[1] * 0.27))

        # Update the screen
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()