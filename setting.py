## 미리 정해진 4개 크기로 화면 구현 -> 비율변화 구현
import pygame
import shelve 


# Initialize Pygame
class Setting():
    def start_setting():
        # Set the default size of the window
        window_size = (1000, 800)
        # Create the window
        screen = pygame.display.set_mode(window_size)
        # Set the title of the window
        pygame.display.set_caption("Resizable_window")
        SAVE_DATA = shelve.open("Save Data")


        pygame.init()
        # Set the font for the buttons
        set_font = pygame.font.SysFont("Minecraft", 40)
        # Set the text color
        text_color = 'black'
        # Set the button colors
        button_color = 'yellow'
        button_highlight_color = 'gray'
        # Set the button labels
        blind_label = "Color Blind Mode"
        default_label = "  Default Setting"
        button_labels = ["size1", "size2", "size3", "size4"]
        button_labels_2 = ["+", "-", "<", ">"]
        # Set the button sizes
        button_sizes = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]





        # Create the buttons
        blind_text_surface = set_font.render(blind_label,True, text_color)
        blind_text_rect = blind_text_surface.get_rect()
        color_blind = pygame.Rect(600,380,240,30)
        blind_text_rect.center = color_blind.center


        # Create the buttons
        default_text_surface = set_font.render(default_label,True, text_color)
        default_text_rect = default_text_surface.get_rect()
        default = pygame.Rect(600,500,240,30)
        default_text_rect.center = default.center




        buttons = []
        for i, label in enumerate(button_labels):
            text_surface = set_font.render(label, True, text_color)
            text_rect = text_surface.get_rect()
            button_rect = pygame.Rect(40 + i * 100, 50, 80, 20)
            text_rect.center = button_rect.center
            buttons.append((button_rect, text_surface, button_sizes[i]))

        buttons2 = []
        for i, label in enumerate(button_labels_2):
            text_surface_2 = set_font.render(label, True, text_color)
            text_rect_2 = text_surface_2.get_rect()
            button_rect_2 = pygame.Rect(40 + (i+4) * 100, 50, 10, 20)
            text_rect_2.center = button_rect_2.center
            buttons2.append((button_rect_2, text_surface_2))

        # Game loop
        running = True
        while running:
            # Handle events
            ## ["size1", "size2", "size3", "size4"]
            # Clear the screen
            screen.fill('yellow')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a button was clicked
                    
                    if color_blind.collidepoint(event.pos):
                        print("color_blind mode")


                    if default.collidepoint(event.pos):
                        window_size = (1440, 744)
                        screen = pygame.display.set_mode(window_size)
                        print("Default Setting")


                    for i, (button_rect, _, size) in enumerate(buttons):
                        if button_rect.collidepoint(event.pos):
                            window_size = size
                            screen = pygame.display.set_mode(window_size)

                    for i, (button_rect_2, _) in enumerate(buttons2):
                        if button_rect_2.collidepoint(event.pos):
                            if i == 0:
                                window_size = (window_size[0] + 100, window_size[1] + 100)
                                screen = pygame.display.set_mode(window_size)
                            elif i == 1:
                                window_size = (window_size[0] - 100, window_size[1] - 100)
                                screen = pygame.display.set_mode(window_size)
                            elif i == 2:
                                window_size = (window_size[0] - 100, window_size[1])
                                screen = pygame.display.set_mode(window_size)
                            elif i == 3:
                                window_size = (window_size[0] + 100, window_size[1])
                                screen = pygame.display.set_mode(window_size)
            


            

            # Draw the buttons
            if color_blind.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, button_highlight_color, color_blind)
            else:
                pygame.draw.rect(screen, button_color, color_blind)
            screen.blit(blind_text_surface, color_blind)



        # Draw the buttons
            if default.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, button_highlight_color, default)
            else:
                pygame.draw.rect(screen, button_color,default)
            screen.blit(default_text_surface, default)


            # Draw the buttons
            for i, (button_rect, text_surface, _) in enumerate(buttons):
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, button_highlight_color, button_rect)
                else:
                    pygame.draw.rect(screen, button_color, button_rect)
                screen.blit(text_surface, button_rect)


            # Draw the buttons
            for i, (button_rect_2, text_surface_2) in enumerate(buttons2):
                if button_rect_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, button_highlight_color, button_rect_2)
                else:
                    pygame.draw.rect(screen, button_color, button_rect_2)
                screen.blit(text_surface_2, button_rect_2)



            # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit()
