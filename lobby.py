import pygame
from player import Player
import time
import json
import game
import sys


class Lobby():
    def __init__(self, screen_width, screen_height, color_blind_mode):

        # Set up the game screen
        self.screen_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.color_blind_mode = color_blind_mode 
        self.unclicked_lst = []


        try:
            with open('setting_data.json') as game_file:
                self.data = json.load(game_file)
        except: 
            self.data ={
            "color_blind_mode": False,
            "size": (800,600),
            "Total_Volume": 0.3,
            "Background_Volume": 0.3,
            "Sideeffect_Volume": 0.3,
            "player_numbers":3,
            "me": 'player',
            "c1name" :'computer1',
            "c2name" :'computer2',
            "c3name" :'computer3',
            "c4name" :'computer4',
            "c5name" :'computer5',
            "unclicked_list": []
            }
            self.save_game()

    
      
    def save_game(self):
    # 실행중이던 세팅 설정을 딕셔너리 형태로 저장 
        with open('setting_data.json','w') as setting_data_file: 
            json.dump(self.data, setting_data_file)


    def draw_text(self,num,text,font,text_col,x,y):           ##화면에 nameInput(지역변수 text) 출력하기 위한 함수.
        if num ==0: img = font.render("My name: " +text, True, text_col)
        elif num ==1: img = font.render("Computer1 name: " +text, True, text_col)
        elif num ==2: img = font.render("Computer2 name: " +text, True, text_col)
        elif num ==3: img = font.render("Computer3 name: " +text, True, text_col)
        elif num ==4: img = font.render("Computer4 name: " +text, True, text_col)
        elif num ==5: img = font.render("Computer5 name: " +text, True, text_col)
        self.screen.blit(img, (x*0.3, y*0.5))  


    def displayPlayer(self):
        with open('setting_data.json') as game_file:
            self.data = json.load(game_file)
            color = self.data['color_blind_mode']     ## 저장된 값 불러오기. 
            size = self.data["size"]

      
    

        screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        font = pygame.font.SysFont("arial", size[0] // 40, True)
        
        title = font.render("Lobby", True, 'white')
        title_rect = title.get_rect()
        title_rect.centerx = screen.get_rect().centerx
        title_rect.y = screen.get_size()[1] // 12


        play_text = font.render("Play", True, 'white')
        play_rect = play_text.get_rect()
        play_rect.centerx = screen.get_rect().centerx
        play_rect.y = screen.get_size()[1] * 0.81

        #메뉴 상수
        menu_flag = 0




        # 버튼 크기 및 간격 설정
        button_width = 150
        button_height = 50
        button_spacing = 10

        # 버튼 색상 설정
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255,0,0)

        # 버튼 초기 상태 설정
        button_states = [False, False, False, False, False]

        # 버튼 좌표 계산
        button_x = (self.screen_size[0] - button_width) // 2
        button_y = (self.screen_size[1] - (button_height + button_spacing) * 5) // 2



        nameInput = [""]

        
        
        # pygame 초기화
        pygame.init()
        # 게임 루프
        while True:
            # 배경 색상 설정
            screen.fill(BLACK)  
            


            #####################################
            ##display typed input
            for i, line in enumerate(nameInput): 
                if i <= 5: 
                    self.draw_text(i, line,font,RED,self.screen_size[0] /2 , 200+(i*size[0] // 20))
                    if  i ==0:   
                        if line == "":  self.data["me"] = "me"
                        else: self.data["me"] = line
                    elif i == 1: 
                        if line == "": self.data["c1name"] = "c1"
                        else: self.data["c1name"] = line 
                    elif i == 2: 
                        if line == "": self.data["c2name"] = "c2"
                        else: self.data["c2name"] = line
                    elif i == 3: 
                        if line == "": self.data["c3name"] = "c3"
                        else: self.data["c3name"] = line
                    elif i == 4: 
                        if line == "": self.data["c4name"] = "c4"
                        else: self.data["c4name"] = line
                    elif i == 5: 
                        if line == "": self.data["c5name"] = "c5"
                        else: self.data["c5name"] = line

            #####################################

                        


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_game()
                    pygame.quit()
                    sys.exit()


                #####################################
                elif event.type == pygame.TEXTINPUT:
                    nameInput[-1] += event.text
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nameInput[-1] = nameInput[-1][:-1]
                        if len(nameInput[-1]) == 0:
                            if len(nameInput) > 1:
                                nameInput = nameInput[:-1]
                    elif event.key == pygame.K_RETURN:
                        nameInput.append("")
                #####################################

                

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 마우스 클릭 시 버튼 상태 변경
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(5):
                        button_rect = pygame.Rect(button_x, button_y + i * (button_height + button_spacing), button_width, button_height)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            button_states[i] = not button_states[i]

                        


                



            # 버튼 그리기
            for i in range(5):
                if button_states[i]:
                    pygame.draw.rect(screen, BLACK, (button_x, button_y + i * (button_height + button_spacing), button_width, button_height))
                    text = pygame.font.SysFont(None, 24).render("", True, WHITE)
                    screen.blit(text, (button_x + button_width // 2 - text.get_width() // 2, button_y + i * (button_height + button_spacing) + button_height // 2 - text.get_height() // 2))
                else:
                    pygame.draw.rect(screen, WHITE, (button_x, button_y + i * (button_height + button_spacing), button_width, button_height))
                    if i == 0: text = pygame.font.SysFont(None, 24).render(self.data["c1name"], True, BLACK)
                    elif i == 1: text = pygame.font.SysFont(None, 24).render(self.data["c2name"], True, BLACK)
                    elif i == 2: text = pygame.font.SysFont(None, 24).render(self.data["c3name"], True, BLACK)
                    elif i == 3: text = pygame.font.SysFont(None, 24).render(self.data["c4name"], True, BLACK)
                    elif i == 4: text = pygame.font.SysFont(None, 24).render(self.data["c5name"], True, BLACK)
                    
                    screen.blit(text, (button_x + button_width // 2 - text.get_width() // 2, button_y + i * (button_height + button_spacing) + button_height // 2 - text.get_height() // 2))
                    


            # 마우스 이벤트 처리
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if play_rect.collidepoint(mouse_pos) or menu_flag == 0:
                play_text = font.render("Play", True, 'white')
            # 마우스 클릭 시
            if play_rect.collidepoint(mouse_pos) and mouse_click[0]:
                
                ## 최종적으로 클릭되지 않은, 살아 있는 컴퓨터들을 리스트에 포함시킴.       
                for i in range(5):
                    if not button_states[i]:
                        self.unclicked_lst.append(i)
                self.unclicked_lst = list(set(self.unclicked_lst))
                self.data["unclicked_list"] = self.unclicked_lst

                Player_number = 5 - button_states.count(True)
                self.data["player_numbers"] = Player_number
                self.save_game()
                uno_game = game.Game(self.screen_size[0], self.screen_size[1], color, self.data["player_numbers"]) 
                uno_game.run()


            screen.blit(title, title_rect)
            screen.blit(play_text, play_rect)
            pygame.display.flip()
            