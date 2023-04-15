## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면전환 또는 설정변경. 
import pygame
import time
import main
import json


# Initialize Pygame
class Setting():
    def __init__(self, screen_width, screen_height):
         # Set the default size of the window
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_size = (self.screen_width, self.screen_height)
        # Create the window        
        self.screen = pygame.display.set_mode(self.window_size)
        # Set the title of the window
    
        self.running = True
        self.color_blind_mode = False 

        pygame.init()
        # Set the font for the buttons
        self.font = pygame.font.SysFont("arial", self.screen_width // 20, True)
        self.screen_sizes_font = pygame.font.SysFont("arial", self.screen_width // 40, True)
        
        # Set the button sizes
        self.screen_sizes = [(400, 300), (600, 450), (800, 600), (1000, 750)]

        ##게임제목
        self.game_title = self.font.render("Settings", True, 'white')
        self.game_title_rect = self.game_title.get_rect()
    
        # Create the buttons
        self.blind_text_surface = self.font.render("Color Blind Mode",True, 'white')
        self.blind_text_rect = self.blind_text_surface.get_rect()
    
        # Create the buttons
        self.default_text_surface = self.font.render("Default Setting",True, 'white')
        self.default_text_rect = self.default_text_surface.get_rect()
        
        # Create the buttons
        self.back_text_surface = self.font.render("Go Back",True, 'white')
        self.back_text_rect = self.back_text_surface.get_rect()
        
        # Create the Exit buttons
        self.exit_text_surface = self.font.render("Exit",True, 'white')
        self.exit_text_rect = self.exit_text_surface.get_rect()

        # Create the buttons
        self.size1_text_surface = self.screen_sizes_font.render("size1",True, 'white')
        self.size1_text_rect = self.size1_text_surface.get_rect()       
        
        # Create the buttons
        self.size2_text_surface = self.screen_sizes_font.render("size2",True, 'white')
        self.size2_text_rect = self.size2_text_surface.get_rect()       
        
        # Create the buttons
        self.size3_text_surface = self.screen_sizes_font.render("size3",True, 'white')
        self.size3_text_rect = self.size3_text_surface.get_rect()        
        
        # Create the buttons
        self.size4_text_surface = self.screen_sizes_font.render("size4",True, 'white')
        self.size4_text_rect = self.size4_text_surface.get_rect()

        self.reposition(self.screen)
        
        try:
            with open('setting_data.json') as game_file:
                self.data = json.load(game_file)
        except: 
            self.data ={
            "color_blind_mode": False,
            "size": (800,600) 
            }
            self.save_game()

    def save_game(self):
        # 실행중이던 세팅 설정을 딕셔너리 형태로 저장 
        with open('setting_data.json','w') as setting_data_file: 
            json.dump(self.data, setting_data_file)
 

    def run(self, screen_width, screen_height):
        window_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(window_size)
                
        #메뉴 상수
        menu_flag = 0
        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game() 
                    self.running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_flag -= 1
                    elif event.key == pygame.K_DOWN:
                        menu_flag += 1
                    elif event.key == 13:
                        if menu_flag == 0:
                            print("Color blind mode")
                            self.color_blind_mode = True
                            self.data['color_blind_mode'] = self.color_blind_mode
                            
                        elif menu_flag == 1:
                            print("Default mode")
                            window_size = (800, 600)
                            screen = pygame.display.set_mode(window_size)
                            self.color_blind_mode = False 
                            self.data['color_blind_mode'] = self.color_blind_mode
                            self.reposition(screen)
                            

                        elif menu_flag == 2:
                            self.save_game()
                            time.sleep(0.3)
                            main.main(self.data["size"][0], self.data["size"][1], self.color_blind_mode)
                            
                        elif menu_flag == 3: 
                            self.save_game()
                            self.running = False
                            
                        elif menu_flag == 4:
                            window_size = self.screen_sizes[0]
                            screen = pygame.display.set_mode(window_size)
                            self.reposition(screen)
                            print("size1")
                            self.data["size"] = window_size
                        elif menu_flag == 5:
                            window_size = self.screen_sizes[1]
                            screen = pygame.display.set_mode(window_size)
                            self.reposition(screen)
                            print("size2")
                            self.data["size"] = window_size

                        elif menu_flag == 6:
                            window_size = self.screen_sizes[2]
                            screen = pygame.display.set_mode(window_size)
                            self.reposition(screen)
                            print("size3")
                            self.data["size"] = window_size

                        elif menu_flag == 7:
                            window_size = self.screen_sizes[3]
                            screen = pygame.display.set_mode(window_size)
                            self.reposition(screen)
                            print("size4") 
                            self.data["size"] = window_size
                menu_flag %= 8        
                    
                    
                    
                    
                    
            
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            ## 색깔 변화. 
            if self.blind_text_rect.collidepoint(mouse_pos) or menu_flag == 0:
                self.blind_text_surface = self.font.render("Color Blind Mode", True, "red")
            else: self.blind_text_surface = self.font.render("Color Blind Mode", True, "white")

            if self.default_text_rect.collidepoint(mouse_pos) or menu_flag == 1:
                self.default_text_surface = self.font.render("Default Setting", True, "red")
            else: self.default_text_surface = self.font.render("Default Setting", True, "white")

            if self.back_text_rect.collidepoint(mouse_pos) or menu_flag == 2:
                self.back_text_surface = self.font.render("Go Back", True, "red")
            else: self.back_text_surface = self.font.render("Go Back", True, "white")

            if self.exit_text_rect.collidepoint(mouse_pos) or menu_flag == 3:
                self.exit_text_surface = self.font.render("Exit", True, "red")
            else: self.exit_text_surface = self.font.render("Exit", True, "white")




            if self.size1_text_rect.collidepoint(mouse_pos) or menu_flag == 4:
                self.size1_text_surface = self.screen_sizes_font.render("size1", True, "red")
            else: self.size1_text_surface = self.screen_sizes_font.render("size1", True, "white")

            if self.size2_text_rect.collidepoint(mouse_pos) or menu_flag == 5:
                self.size2_text_surface = self.screen_sizes_font.render("size2", True, "red")
            else: self.size2_text_surface = self.screen_sizes_font.render("size2", True, "white")
            
            if self.size3_text_rect.collidepoint(mouse_pos) or menu_flag == 6:
                self.size3_text_surface = self.screen_sizes_font.render("size3", True, "red")
            else: self.size3_text_surface = self.screen_sizes_font.render("size3", True, "white")
            
            if self.size4_text_rect.collidepoint(mouse_pos) or menu_flag == 7:
                self.size4_text_surface = self.screen_sizes_font.render("size4", True, "red")
            else: self.size4_text_surface = self.screen_sizes_font.render("size4", True, "white")

            
             # 마우스 클릭 시
            if  self.blind_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                self.color_blind_mode = True
                self.data['color_blind_mode'] = self.color_blind_mode
                

            elif self.default_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = (800, 600)
                screen = pygame.display.set_mode(window_size)
                self.color_blind_mode = False 
                self.data['color_blind_mode'] = self.color_blind_mode 
                self.reposition(screen)
                
                
            elif self.back_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                self.save_game()
                time.sleep(0.3)
                main.main(self.data["size"][0], self.data["size"][1],self.color_blind_mode)
                

            elif self.exit_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                self.save_game()
                self.running = False


            elif self.size1_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[0]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
                self.data["size"] = window_size

            elif self.size2_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[1]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
                self.data["size"] = window_size

            elif self.size3_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[2]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
                self.data["size"] = window_size

            elif self.size4_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[3]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
                self.data["size"] = window_size



            self.screen.fill('black')
            # 제목 또는 버튼 출력
            self.screen.blit(self.game_title, self.game_title_rect)
            self.screen.blit(self.blind_text_surface, self.blind_text_rect)
            self.screen.blit(self.default_text_surface, self.default_text_rect)
            self.screen.blit(self.back_text_surface, self.back_text_rect)
            self.screen.blit(self.exit_text_surface, self.exit_text_rect)

            self.screen.blit(self.size1_text_surface,self.size1_text_rect)
            self.screen.blit(self.size2_text_surface,self.size2_text_rect)
            self.screen.blit(self.size3_text_surface,self.size3_text_rect)
            self.screen.blit(self.size4_text_surface,self.size4_text_rect)


        # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit()
            

    def reposition(self, screen):
        self.font = pygame.font.SysFont("arial", screen.get_size()[0]//20, True)
        self.screen_sizes_font = pygame.font.SysFont("arial", screen.get_size()[0]//40, True)

        self.game_title = self.font.render("Settings", True, 'white')
        self.game_title_rect = self.game_title.get_rect()
        self.game_title_rect.centerx = screen.get_rect().centerx
        self.game_title_rect.y = screen.get_size()[1] / 12

        self.blind_text_surface = self.font.render("Color Blind Mode",True, 'white')
        self.blind_text_rect = self.blind_text_surface.get_rect()
        self.blind_text_rect.centerx = screen.get_rect().centerx
        self.blind_text_rect.y = screen.get_size()[1] / 2.4

        self.default_text_surface = self.font.render("Default Setting",True, 'white')
        self.default_text_rect = self.default_text_surface.get_rect()
        self.default_text_rect.centerx = screen.get_rect().centerx
        self.default_text_rect.y = screen.get_size()[1] / 1.714

        self.back_text_surface = self.font.render("Go Back",True, 'white')
        self.back_text_rect = self.back_text_surface.get_rect()
        self.back_text_rect.centerx = screen.get_rect().centerx
        self.back_text_rect.y = screen.get_size()[1] / 1.333

        self.exit_text_surface = self.font.render("Exit",True, 'white')
        self.exit_text_rect = self.back_text_surface.get_rect()
        self.exit_text_rect.centerx = screen.get_rect().centerx
        self.exit_text_rect.x = screen.get_size()[0] / 2.222
        self.exit_text_rect.y = screen.get_size()[1] / 1.111



        self.size1_text_surface = self.screen_sizes_font.render("size1",True, 'white')
        self.size1_text_rect = self.size1_text_surface.get_rect() 
        self.size1_text_rect.centerx = screen.get_rect().centerx
        self.size1_text_rect.x = screen.get_size()[0] / 5
        self.size1_text_rect.y = screen.get_size()[1] / 4

        self.size2_text_surface = self.screen_sizes_font.render("size2",True, 'white')
        self.size2_text_rect = self.size2_text_surface.get_rect() 
        self.size2_text_rect.centerx = screen.get_rect().centerx
        self.size2_text_rect.x = screen.get_size()[0] / 2.5
        self.size2_text_rect.y = screen.get_size()[1] / 4

        self.size3_text_surface = self.screen_sizes_font.render("size3",True, 'white')
        self.size3_text_rect = self.size3_text_surface.get_rect()  
        self.size3_text_rect.centerx = screen.get_rect().centerx
        self.size3_text_rect.x = screen.get_size()[0] / 1.6666
        self.size3_text_rect.y = screen.get_size()[1] / 4

        self.size4_text_surface = self.screen_sizes_font.render("size4",True, 'white')
        self.size4_text_rect = self.size4_text_surface.get_rect()
        self.size4_text_rect.centerx = screen.get_rect().centerx
        self.size4_text_rect.x = screen.get_size()[0] / 1.25
        self.size4_text_rect.y = screen.get_size()[1] / 4




    # def gets(self):
    #     return self.color_blind_mode 
