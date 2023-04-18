## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면전환 또는 설정변경. 
import pygame
import time
import json
import game
import gameUI


# Initialize Pygame
class Setting():
    def __init__(self, screen_width, screen_height, color_blind_mode,  players, turn_num, top_card, back_card, reverse, skip, start_time,move_effect):
         # Set the default size of the window
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_size = (self.screen_width, self.screen_height)
        self.color_blind_mode = color_blind_mode 
        
        self.players = players
        self.turn_num =  turn_num
        self.top_card = top_card
        self.back_card = back_card
        self.reverse = reverse
        self.skip = skip
        self.start_time = start_time
        self.move_effect = move_effect 
        
        # Create the window        
        self.screen = pygame.display.set_mode(self.window_size)
    
        self.running = True

        pygame.init()
        # Set the font for the buttons
        self.font = pygame.font.SysFont("arial", self.screen_width // 20, True)
        self.screen_sizes_font = pygame.font.SysFont("arial", self.screen_width // 40, True)
        self.vol_font = pygame.font.SysFont("arial", self.screen_width // 60, True)
        
        
        # Set the button sizes
        self.screen_sizes = [(400, 300), (600, 450), (800, 600), (1000, 750)]

        
        ## create the button code 있던 부분 -> reposition으로 옮김.
        
        try: 
            with open('setting_data.json') as game_file:
                self.data = json.load(game_file)
        except: 
            self.data ={
            "color_blind_mode": False,
            "size": (800,600),
            "Total_Volume": 0.3,
            "Background_Volume": 0.3,
            "Sideeffect_Volume": 0.3
            }
            self.save_game()

        
        # 슬라이더의 초기값과 상태 설정
        self.slider1_value = self.data["Total_Volume"]
        self.slider1_dragging = False
        # 슬라이더 색상 설정
        self.slider1_bg_color = 'red'
        self.slider1_bar_color = 'red'
        self.slider1_handle_color = (255,255,255)
        

        # 슬라이더의 초기값과 상태 설정
        self.slider2_value = self.data["Background_Volume"]
        self.slider2_dragging = False
        # 슬라이더 색상 설정
        self.slider2_bg_color = 'red'
        self.slider2_bar_color = 'red'
        self.slider2_handle_color = (255,255,255)
       

        # 슬라이더의 초기값과 상태 설정
        self.slider3_value = self.data["Sideeffect_Volume"]
        self.slider3_dragging = False
        # 슬라이더 색상 설정
        self.slider3_bg_color = 'red'
        self.slider3_bar_color = 'red'
        self.slider3_handle_color = (255,255,255)


        self.reposition(self.screen)
                
                


        
        

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
                    
                    

                ######-----------------------------------------------------------------------------------------------------------------------------------------------------------------    
                    
                ## 1) Total Volume 조절  &  2) Background Volume   & ## 3) Sideeffect Volume 
                


  
                elif event.type == pygame.MOUSEMOTION:
                    # 마우스 이동 이벤트 처리
                    if self.slider1_dragging:
                        # 슬라이더를 드래그하고 있는 경우 슬라이더 값을 업데이트
                        mouse_x, _ = event.pos
                        self.slider1_value = max(0, min(1, (mouse_x - self.slider2_x) / self.slider2_width))
                        self.slider2_value = max(0, min(1, (mouse_x - self.slider2_x) / self.slider2_width))
                        self.slider3_value = max(0, min(1, (mouse_x - self.slider3_x) / self.slider3_width))
                        pygame.mixer.music.set_volume(self.slider1_value)
                        self.data["Total_Volume"] = self.slider1_value 
                        self.save_game()


                    # 마우스 이동 이벤트 처리
                    elif self.slider2_dragging:
                        # 슬라이더를 드래그하고 있는 경우 슬라이더 값을 업데이트
                        mouse_x, _ = event.pos
                        self.slider2_value = max(0, min(1, (mouse_x - self.slider2_x) / self.slider2_width))
                        pygame.mixer.music.set_volume(self.slider2_value)
                        self.data["Background_Volume"] = self.slider2_value 
                        self.save_game()



                    # 마우스 이동 이벤트 처리
                    elif self.slider3_dragging:
                        # 슬라이더를 드래그하고 있는 경우 슬라이더 값을 업데이트
                        mouse_x, _ = event.pos
                        self.slider3_value = max(0, min(1, (mouse_x - self.slider3_x) / self.slider3_width))
                        self.move_effect.set_volume(self.slider3_value)
                        self.data["Sideeffect_Volume"] = self.slider3_value 
                        self.save_game()
                        
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 마우스 클릭 이벤트 처리
                    if event.button == 1 and self.slider1_rect.collidepoint(event.pos):
                        # 슬라이더를 클릭한 경우 슬라이더 드래그 상태로 변경
                        self.slider1_dragging = True
                    # 마우스 클릭 이벤트 처리
                    elif event.button == 1 and self.slider2_rect.collidepoint(event.pos):
                        # 슬라이더를 클릭한 경우 슬라이더 드래그 상태로 변경
                        self.slider2_dragging = True
                    # 마우스 클릭 이벤트 처리
                    elif event.button == 1 and self.slider3_rect.collidepoint(event.pos):
                        # 슬라이더를 클릭한 경우 슬라이더 드래그 상태로 변경
                        self.slider3_dragging = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    # 마우스 클릭 해제 이벤트 처리
                    if event.button == 1 and self.slider1_dragging:
                        # 슬라이더를 드래그하고 있던 경우 슬라이더 드래그 상태 해제
                        self.slider1_dragging = False
                    # 마우스 클릭 해제 이벤트 처리
                    elif event.button == 1 and self.slider2_dragging:
                        # 슬라이더를 드래그하고 있던 경우 슬라이더 드래그 상태 해제
                        self.slider2_dragging = False
                    # 마우스 클릭 해제 이벤트 처리
                    elif event.button == 1 and self.slider3_dragging:
                        # 슬라이더를 드래그하고 있던 경우 슬라이더 드래그 상태 해제
                        self.slider3_dragging = False


                ######----------------------------------------------------------------------------------------------------------------------------------------------------------------- 

                    
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
                            time.sleep(0.3)
                            play = game.Game(window_size[0], window_size[1],self.color_blind_mode,len(self.players)-1)
                            self.save_game()
                            play.run()

                            
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
                time.sleep(0.3)
                play = game.Game(window_size[0], window_size[1],self.color_blind_mode,len(self.players)-1)
                self.save_game()
                play.run()
                

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

            self.screen.blit(self.tvol, self.tvol_rect)
            self.screen.blit(self.backvol,self.backvol_rect)
            self.screen.blit(self.sidevol,self.sidevol_rect)
       
            
            
            


            
            
            
            # 슬라이더 배경 그리기
            pygame.draw.rect(self.screen, self.slider1_bg_color, self.slider1_rect)
            # # 슬라이더 바 그리기
            pygame.draw.rect(self.screen, self.slider1_bar_color, self.slider1_rect)
            # 슬라이더 핸들 그리기             
            pygame.draw.rect(self.screen, self.slider1_handle_color, pygame.Rect(self.slider1_x + self.slider1_value * self.slider1_width - 5, self.slider1_y, 10, self.slider1_height))


            # 슬라이더 배경 그리기
            pygame.draw.rect(self.screen, self.slider2_bg_color, self.slider2_rect)
            # # 슬라이더 바 그리기
            pygame.draw.rect(self.screen, self.slider2_bar_color, self.slider2_rect)
            # 슬라이더 핸들 그리기             
            pygame.draw.rect(self.screen, self.slider2_handle_color, pygame.Rect(self.slider2_x + self.slider2_value * self.slider2_width - 5, self.slider2_y, 10, self.slider2_height))



            # 슬라이더 배경 그리기
            pygame.draw.rect(self.screen, self.slider3_bg_color, self.slider3_rect)
            # # 슬라이더 바 그리기
            pygame.draw.rect(self.screen, self.slider3_bar_color, self.slider3_rect)
            # 슬라이더 핸들 그리기             
            pygame.draw.rect(self.screen, self.slider3_handle_color, pygame.Rect(self.slider3_x + self.slider3_value * self.slider3_width - 5, self.slider3_y, 10, self.slider3_height))







        # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit()
            

    def reposition(self, screen):
        self.font = pygame.font.SysFont("arial", screen.get_size()[0]//20, True)
        self.screen_sizes_font = pygame.font.SysFont("arial", screen.get_size()[0]//40, True)
        self.vol_font = pygame.font.SysFont("arial", screen.get_size()[0]//40, True)

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

        
        self.tvol = self.vol_font.render("※ Total Volume", True, 'white')
        self.tvol_rect = self.tvol.get_rect()
        self.tvol_rect.x = screen.get_size()[0]  / 20
        self.tvol_rect.y = screen.get_size()[1] / 2.2
        
        self.backvol = self.vol_font.render("※ Background Volume",True,'white')
        self.backvol_rect = self.backvol.get_rect()
        self.backvol_rect.x = screen.get_size()[0] / 20
        self.backvol_rect.y = screen.get_size()[1] / 1.6

        self.sidevol = self.vol_font.render("※ SideEffect Volume",True,'white')
        self.sidevol_rect = self.sidevol.get_rect()
        self.sidevol_rect.x = screen.get_size()[0] / 20
        self.sidevol_rect.y = screen.get_size()[1] / 1.22



       
       # 슬라이더1의 크기 설정
        self.slider1_width = self.screen.get_size()[0] / 9
        self.slider1_height = self.screen.get_size()[1] / 80
        # 슬라이더 위치
        self.slider1_x = self.screen.get_size()[0] / 20
        self.slider1_y = self.screen.get_size()[1] / 1.8
        # 슬라이더 생성
        self.slider1_rect = pygame.Rect(self.slider1_x, self.slider1_y, self.slider1_width, self.slider1_height)




        # 슬라이더2의 크기 설정
        self.slider2_width = self.screen.get_size()[0] / 9
        self.slider2_height = self.screen.get_size()[1] / 80
        # 슬라이더 위치
        self.slider2_x = self.screen.get_size()[0] / 20
        self.slider2_y = self.screen.get_size()[1] / 1.4
        # 슬라이더 생성
        self.slider2_rect = pygame.Rect(self.slider2_x, self.slider2_y, self.slider2_width, self.slider2_height)

        
    

        # 슬라이더3의 크기 설정
        self.slider3_width = self.screen.get_size()[0] / 9
        self.slider3_height = self.screen.get_size()[1] / 80
        # 슬라이더 위치
        self.slider3_x = self.screen.get_size()[0] / 20
        self.slider3_y = self.screen.get_size()[1] / 1.1
        # 슬라이더 생성
        self.slider3_rect = pygame.Rect(self.slider3_x, self.slider3_y, self.slider3_width, self.slider3_height)
        


    # def slider_value():




    # def gets(self):
    #     return self.color_blind_mode 
