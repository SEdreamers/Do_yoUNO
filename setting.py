## 미리 정해진 4개 크기로 화면 구현 -> 비율변화 구현
import pygame
import shelve 
from gameScreen import gameScrean
# Initialize Pygame
class Setting():
    def start_setting(screen_width, screen_height):
        # Set the default size of the window
        window_size = (screen_width, screen_height)
        # Create the window
        screen = pygame.display.set_mode(window_size)
        # Set the title of the window
        pygame.display.set_caption("Resizable window")
        SAVE_DATA = shelve.open("Save Data")
    

        pygame.init()
        # Set the font for the buttons
        font = pygame.font.SysFont("arial", screen_width//40, True, True)
        # Set the text color
        text_color = 'white'
        # Set the button colors
        button_color = 'black'




        button_labels = ["size1", "size2", "size3", "size4"]
        # Set the button sizes
        button_sizes = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]



        # Create the buttons
        blind_text_surface = font.render("Color Blind Mode",True, text_color)
        blind_text_rect = blind_text_surface.get_rect()
        blind_text_rect.centerx = screen.get_rect().centerx
        blind_text_rect.y = screen.get_size()[1] // 12





        # Create the buttons
        default_text_surface = font.render("Default Setting",True, text_color)
        default_text_rect = default_text_surface.get_rect()
        default_text_rect.centerx = screen.get_rect().centerx
        default_text_rect.y = screen.get_size()[1] // 4


        # Create the buttons
        back_text_surface = font.render("Go Back",True, text_color)
        back_text_rect = back_text_surface.get_rect()
        back_text_rect.centerx = screen.get_rect().centerx
        back_text_rect.y = screen.get_size()[1] // 1.1


        # Create the buttons
        buttons = []
        for i, label in enumerate(button_labels):
            text_surface = font.render(label, True, text_color)
            text_rect = text_surface.get_rect()
            button_rect = pygame.Rect(40 + i * 100, 50, 80, 20)
            text_rect.center = button_rect.center
            buttons.append((button_rect, text_surface, button_sizes[i]))


        #메뉴 상수
        menu_flag = 0


        # Game loop
        running = True
        while running:


            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_flag -= 1
                    elif event.key == pygame.K_DOWN:
                        menu_flag += 1
                    elif event.key == 13:
                        if menu_flag == 0:
                            print("Color blind mode")
                        elif menu_flag == 1:
                            print("Default mode")
                        elif menu_flag == 2:
                            print("Go Back")
                menu_flag %= 3
                


            
            screen.fill('black')
            # Draw the buttons
            screen.blit(blind_text_surface, blind_text_rect)
            screen.blit(default_text_surface, default_text_rect)
            screen.blit(back_text_surface, back_text_rect)

            # Draw the buttons
            for i, (button_rect, text_surface, _) in enumerate(buttons):
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, "red", button_rect)
                else:
                    pygame.draw.rect(screen, button_color, button_rect)
                screen.blit(text_surface, button_rect)


            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()


            ## 올려놓거나 키보드 방향키 이동으로 색깔 변화. 
            if blind_text_rect.collidepoint(mouse_pos) or menu_flag == 0:
                blind_text_surface = font.render("Color Blind Mode", True, "red")
            else: blind_text_surface = font.render("Color Blind Mode", True, "white")



            if default_text_rect.collidepoint(mouse_pos) or menu_flag == 1:
                default_text_surface = font.render("Default Setting", True, "red")
            else: default_text_surface = font.render("Default Setting", True, "white")



            if back_text_rect.collidepoint(mouse_pos) or menu_flag == 2:
                back_text_surface = font.render("Go Back", True, "red")
            else: back_text_surface = font.render("Go Back", True, "white")


            for i, (button_rect, _, size) in enumerate(buttons):
                if button_rect.collidepoint(mouse_pos):
                    window_size = size
                    screen = pygame.display.set_mode(window_size)

             # 마우스 클릭 시
            if  blind_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                print("color_blind mode")
            elif default_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = (1000, 800)
                screen = pygame.display.set_mode(window_size)
                print("Default Setting")
            elif back_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                print("Go Back")

            # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit() 

