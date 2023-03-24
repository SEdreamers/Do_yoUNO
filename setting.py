## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면전환 또는 설정변경. 
import pygame
import time
import main
import json

# Initialize Pygame
class Setting():
    def __init__(self, screen_width, screen_height):
         # Set the default size of the window
        self.window_size = (screen_width, screen_height)
        # Create the window
        self.screen = pygame.display.set_mode(self.window_size)
        # Set the title of the window
    
        self.running = True
        self.color_blind_mode = False 

        pygame.init()
        # Set the font for the buttons
        self.font = pygame.font.SysFont("arial", screen_width // 20, True)
        self.screen_sizes_font = pygame.font.SysFont("arial", screen_width // 40, True)
        
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


        # 실행중이던 세팅 설정을 딕셔너리 형태로 저장
        self.data ={

        }

    def run(self, screen_width, screen_height):
        window_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(window_size)
        

        try: 
            with open('setting_data.txt','w') as setting_data_file: 
                json.dump(self.data, setting_data_file)
        except: 
            print("No file created yet!")     ## 처음으로 게임 시작하게 될 경우, 하다가 나가버리면 자동으로 play_data.txt 가 생성되고 후에 불러올 수 있음. 


        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('setting_data.txt','w') as setting_data_file: 
                        json.dump(self.data, setting_data_file)
                    self.running = False
                    
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
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            ## 색깔 변화. 
            if self.blind_text_rect.collidepoint(mouse_pos):
                self.blind_text_surface = self.font.render("Color Blind Mode", True, "red")
            else: self.blind_text_surface = self.font.render("Color Blind Mode", True, "white")

            if self.default_text_rect.collidepoint(mouse_pos):
                self.default_text_surface = self.font.render("Default Setting", True, "red")
            else: self.default_text_surface = self.font.render("Default Setting", True, "white")

            if self.back_text_rect.collidepoint(mouse_pos):
                self.back_text_surface = self.font.render("Go Back", True, "red")
            else: self.back_text_surface = self.font.render("Go Back", True, "white")

            if self.exit_text_rect.collidepoint(mouse_pos):
                self.exit_text_surface = self.font.render("Exit", True, "red")
            else: self.exit_text_surface = self.font.render("Exit", True, "white")




            if self.size1_text_rect.collidepoint(mouse_pos):
                self.size1_text_surface = self.screen_sizes_font.render("size1", True, "red")
            else: self.size1_text_surface = self.screen_sizes_font.render("size1", True, "white")

            if self.size2_text_rect.collidepoint(mouse_pos):
                self.size2_text_surface = self.screen_sizes_font.render("size2", True, "red")
            else: self.size2_text_surface = self.screen_sizes_font.render("size2", True, "white")
            
            if self.size3_text_rect.collidepoint(mouse_pos):
                self.size3_text_surface = self.screen_sizes_font.render("size3", True, "red")
            else: self.size3_text_surface = self.screen_sizes_font.render("size3", True, "white")
            
            if self.size4_text_rect.collidepoint(mouse_pos):
                self.size4_text_surface = self.screen_sizes_font.render("size4", True, "red")
            else: self.size4_text_surface = self.screen_sizes_font.render("size4", True, "white")

            
             # 마우스 클릭 시
            if  self.blind_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                # print("color_blind mode")
                self.color_blind_mode = True
                # self.gets() 

            elif self.default_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = (800, 600)
                screen = pygame.display.set_mode(window_size)

                self.color_blind_mode = False 
                # self.gets()
                self.reposition(screen)
                
            elif self.back_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                time.sleep(0.3)
                main.main(window_size[0], window_size[1],self.color_blind_mode)
                

            elif self.exit_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                self.running = False


            elif self.size1_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[0]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
            elif self.size2_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[1]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
            elif self.size3_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[2]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
            elif self.size4_text_rect.collidepoint(mouse_pos) and mouse_click[0]:
                window_size = self.screen_sizes[3]
                screen = pygame.display.set_mode(window_size)
                self.reposition(screen)
 
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
