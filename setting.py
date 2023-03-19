## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면전환 또는 설정변경. 
import pygame
import shelve 
import main
import time

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
        font = pygame.font.SysFont("arial", screen_width//20, True, True)
        screen_sizes_font = pygame.font.SysFont("arial", screen_width//40, True, True)
        # Set the text color
        text_color = 'white'
        
        # Set the button sizes
        screen_sizes = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]



        ##게임제목
        game_title = font.render("Uno Game", True, 'white')
        game_title_rect = game_title.get_rect()
        game_title_rect.centerx = screen.get_rect().centerx
        game_title_rect.y = screen.get_size()[1] // 12
        
        
        # Create the buttons
        blind_text_surface = font.render("Color Blind Mode",True, text_color)
        blind_text_rect = blind_text_surface.get_rect()
        blind_text_rect.centerx = screen.get_rect().centerx
        blind_text_rect.y = screen.get_size()[1] // 2.4

        # Create the buttons
        default_text_surface = font.render("Default Setting",True, text_color)
        default_text_rect = default_text_surface.get_rect()
        default_text_rect.centerx = screen.get_rect().centerx
        default_text_rect.y = screen.get_size()[1] / 1.714

        # Create the buttons
        back_text_surface = font.render("Go Back",True, text_color)
        back_text_rect = back_text_surface.get_rect()
        back_text_rect.centerx = screen.get_rect().centerx
        back_text_rect.y = screen.get_size()[1] / 1.333 

        # Create the buttons
        size1_text_surface = screen_sizes_font.render("size1",True, text_color)
        size1_text_rect = size1_text_surface.get_rect()
        size1_text_rect.centerx = screen.get_rect().centerx
        size1_text_rect.x = screen.get_size()[0] / 5
        
        # Create the buttons
        size2_text_surface = screen_sizes_font.render("size2",True, text_color)
        size2_text_rect = size2_text_surface.get_rect()
        size2_text_rect.centerx = screen.get_rect().centerx
        size2_text_rect.x = screen.get_size()[0] / 2.5
        
        
        # Create the buttons
        size3_text_surface = screen_sizes_font.render("size3",True, text_color)
        size3_text_rect = size3_text_surface.get_rect()
        size3_text_rect.centerx = screen.get_rect().centerx
        size3_text_rect.x = screen.get_size()[0] / 1.6666 
        
        
        
        # Create the buttons
        size4_text_surface = screen_sizes_font.render("size4",True, text_color)
        size4_text_rect = size4_text_surface.get_rect()
        size4_text_rect.centerx = screen.get_rect().centerx
        size4_text_rect.x = screen.get_size()[0] / 1.25 
        
        
        # for i, label in enumerate(text_label):
        #     text_surface = font.render(label, True, text_color)
        #     text_rect = text_surface.get_rect()
        #     # (40 + i * 100, 50, 80, 20)
        #     text_rect.centerx = screen.get_rect().centerx
        #     text_rect.x = screen.get_size()[0] // (5-i)
        #     buttons.append((text_surface, screen_sizes[i],text_rect,text_rect.x))
            
        
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
                            main.main()
                            print("Go Back")
                        elif menu_flag == 3:
                            window_size = screen_sizes[0]
                            screen = pygame.display.set_mode(window_size)
                            print("size1")
                        elif menu_flag == 4:
                            window_size = screen_sizes[1]
                            screen = pygame.display.set_mode(window_size)
                            print("size2")
                        elif menu_flag == 5:
                            window_size = screen_sizes[2]
                            screen = pygame.display.set_mode(window_size)
                            print("size3")
                        elif menu_flag == 6:
                            window_size = screen_sizes[3]
                            screen = pygame.display.set_mode(window_size)
                            print("size4") 
                menu_flag %= 7
                


            screen.fill('black')
            # 제목 또는 버튼 출력
            screen.blit(game_title, game_title_rect)
            screen.blit(blind_text_surface, blind_text_rect)
            screen.blit(default_text_surface, default_text_rect)
            screen.blit(back_text_surface, back_text_rect)
            screen.blit(size1_text_surface,size1_text_rect)
            screen.blit(size2_text_surface,size2_text_rect)
            screen.blit(size3_text_surface,size3_text_rect)
            screen.blit(size4_text_surface,size4_text_rect)
            

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()


            # 버튼 출력과     올려놓거나 키보드 방향키 이동으로 색깔 변화. 
            
            
            
            # for i, (text_surface, _, text_rect, text_rect.x) in enumerate(buttons):
            #     screen.blit(text_surface,text_rect)
            #     if text_rect.collidepoint(mouse_pos) or menu_flag == (i+3):
            #         text_surface = font.render(text_label[i], True, "red")
            #     else: text_surface = font.render(text_label[i], True, "white")
                

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

            if size1_text_rect.collidepoint(mouse_pos) or menu_flag == 3:
                size1_text_surface = screen_sizes_font.render("size1", True, "red")
            else: size1_text_surface = screen_sizes_font.render("size1", True, "white")

            if size2_text_rect.collidepoint(mouse_pos) or menu_flag == 4:
                size2_text_surface = screen_sizes_font.render("size2", True, "red")
            else: size2_text_surface = screen_sizes_font.render("size2", True, "white")
            
            if size3_text_rect.collidepoint(mouse_pos) or menu_flag == 5:
                size3_text_surface = screen_sizes_font.render("size3", True, "red")
            else: size3_text_surface = screen_sizes_font.render("size3", True, "white")
            
            if size4_text_rect.collidepoint(mouse_pos) or menu_flag == 6:
                size4_text_surface = screen_sizes_font.render("size4", True, "red")
            else: size4_text_surface = screen_sizes_font.render("size4", True, "white")



             # 마우스 클릭 시
            if  blind_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                print("color_blind mode")
            elif default_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = (1000, 800)
                screen = pygame.display.set_mode(window_size)
                print("Default Setting")
            elif back_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                time.sleep(0.15)
                main.main()
                print("Go Back")
            elif size1_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                    window_size = screen_sizes[0]
                    screen = pygame.display.set_mode(window_size)
            elif size2_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                    window_size = screen_sizes[1]
                    screen = pygame.display.set_mode(window_size)
            elif size3_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                    window_size = screen_sizes[2]
                    screen = pygame.display.set_mode(window_size)
            elif size4_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                    window_size = screen_sizes[3]
                    screen = pygame.display.set_mode(window_size)
 
        # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit() 