import pygame
import game
import main
import sys
import json

BLACK = (0, 0, 0)
SCOLOR = (228, 221, 134)
FCOLOR = (45, 43, 32)

class GameOverUI:
    def __init__(self, screen_width, screen_height, winner, color_blind_mode):

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
            "c5name" :'computer5'
            }


        self.menu_flag = 0
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
            "c5name" :'computer5'
            }

        # 화면 설정
        self.screen_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)

        # 폰트 설정
        self.main_font = pygame.font.Font("font/game2.ttf", self.screen_size[0] // 15)
        self.font = pygame.font.Font("font/game2.ttf", self.screen_size[0] // 20)

        # 색약 모드 설정
        self.color_blind_mode = color_blind_mode

        # 승리자 글자
        self.winner = self.main_font.render(f'Winner is {winner}', True, 'blue')
        self.winner_rect = self.winner.get_rect()
        self.winner_rect.centerx = self.screen.get_rect().centerx
        self.winner_rect.y = self.screen.get_size()[1] / 2.4

        # new game 버튼
        self.new_game_text = self.font.render("Back To Main", True, 'white')
        self.new_game_rect = self.new_game_text.get_rect()
        self.new_game_rect.centerx = self.screen.get_rect().centerx
        self.new_game_rect.y = self.screen.get_size()[1] / 1.714

        # exit 버튼
        self.exit_text = self.font.render("Exit", True, 'white')
        self.exit_rect = self.exit_text.get_rect()
        self.exit_rect.centerx = self.screen.get_rect().centerx
        self.exit_rect.y = self.screen.get_size()[1] / 1.4
        
        self.frame_index = 0 # gif frame index

        self.uno_game = game.Game(self.screen_size[0], self.screen_size[1], self.color_blind_mode,self.data["player_numbers"])
        
        self.achv_title = ["싱글 승리", "기술5 승리", "픽0 승리", "10턴 승리", "20턴 승리", "30턴 승리", "UNO 승리", "지역A 승리", "지역B 승리", "지역C 승리", "지역D 승리", "기술0 승리"] # 업적 타이틀
        self.achv_cnt = 0
        
        self.title_font = pygame.font.Font("font/GangwonEduPower.ttf", self.screen_size[0] // 40)
        self.radius = 10
        self.popup_width = self.screen_size[0] * 0.235
        self.popup_height = self.screen_size[1] * 0.07
        self.w_top = (self.screen_size[0] - self.popup_width) * 0.5
        self.h_top = self.screen_size[1] * 0.02
        self.achv_popup = pygame.Rect(self.w_top, self.h_top, self.popup_width, self.popup_height)
    
        self.achv_icon_size = self.screen_size[0] * 0.035
        self.inner_magrin = self.screen_size[0] * 0.01

    def display(self, comp_achv_list):
        pygame.display.set_caption("Game Over")
        self.screen.fill(BLACK)
        
        # 업적 달성 팝업 순서대로 출력
        achv_len = len(comp_achv_list)
        
        popup_time = 50
        popup_interval = 10
        
        if achv_len > 0 and popup_interval < self.achv_cnt < popup_interval + popup_time: # 첫번째 팝업
            self.shown_achv_popup(comp_achv_list[0])
        elif achv_len > 1 and popup_interval * 2 + popup_time < self.achv_cnt < popup_interval * 2 + popup_time * 2: # 두번째 팝업
            self.shown_achv_popup(comp_achv_list[1])
        elif achv_len > 2 and popup_interval * 3 + popup_time * 2 + popup_interval < self.achv_cnt < popup_interval * 3 + popup_time * 3: # 세번째 팝업
            self.shown_achv_popup(comp_achv_list[2])
        elif achv_len > 3 and popup_interval * 4 + popup_time * 3 + popup_interval < self.achv_cnt < popup_interval * 4 + popup_time * 4: # 네번째 팝업
            self.shown_achv_popup(comp_achv_list[3])
        elif achv_len > 4 and popup_interval * 5 + popup_time * 4 + popup_interval < self.achv_cnt < popup_interval * 5 + popup_time * 5: # 다섯번째 팝업
            self.shown_achv_popup(comp_achv_list[4])
        elif achv_len > 5 and popup_interval * 6 + popup_time * 5 + popup_interval < self.achv_cnt < popup_interval * 6 + popup_time * 6: # 여섯번째 팝업
            self.shown_achv_popup(comp_achv_list[5])

        self.achv_cnt += 1
        
            
        
        
        # 폭죽 이미지 출력
        if self.frame_index <= 90:
            gif_image = pygame.image.load(f"images/confetti_images/confetti_{self.frame_index}.png")
            gif_image = pygame.transform.scale(gif_image, self.screen_size) 
            self.frame_index += 1
            self.screen.blit(gif_image, gif_image.get_rect())
        
        # 글자 출력
        self.screen.blit(self.winner, self.winner_rect)
        self.screen.blit(self.new_game_text, self.new_game_rect)
        self.screen.blit(self.exit_text, self.exit_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        
        # 키보드 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.menu_flag -= 1
                elif event.key == pygame.K_DOWN:
                    self.menu_flag += 1
                elif event.key == 13:
                    if self.menu_flag == 0:
                        main.main(self.data["size"][0], self.data["size"][1],self.color_blind_mode)
                    elif self.menu_flag == 1:
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            self.menu_flag %= 2

        # 메뉴 시각화(색상 변경)
        if self.new_game_rect.collidepoint(mouse_pos) or self.menu_flag == 0:
            self.new_game_text = self.font.render("Back To Main", True, 'red')
            self.exit_text = self.font.render("Exit", True, 'white')
        else:
            self.new_game_text = self.font.render("Back To Main", True, 'white')

        if self.exit_rect.collidepoint(mouse_pos) or self.menu_flag == 1:
            self.exit_text = self.font.render("Exit", True, 'red')
            self.new_game_text = self.font.render("Back To Main", True, 'white')
        else:
            self.exit_text = self.font.render("Exit", True, 'white')
    
        # 메뉴 동작
        if self.new_game_rect.collidepoint(mouse_pos) and mouse_click:
            main.main(self.data["size"][0], self.data["size"][1],self.color_blind_mode) # 새 게임 불러오기
        elif self.exit_rect.collidepoint(mouse_pos) and mouse_click:
            sys.exit() # 종료
        pygame.display.flip()

    def shown_achv_popup(self, achv_index):
        pygame.draw.rect(self.screen, SCOLOR, self.achv_popup, border_radius=self.radius)
        achv_icon = pygame.image.load("images/acheivement/achv0.png")
        achv_icon =  pygame.transform.scale(achv_icon, (self.achv_icon_size, self.achv_icon_size))
        achv_icon_rect = achv_icon.get_rect()
        achv_icon_rect.x = self.achv_popup.x + self.inner_magrin
        achv_icon_rect.centery = self.achv_popup.centery
        self.screen.blit(achv_icon, achv_icon_rect)

        achv_title = self.title_font.render(f"{self.achv_title[achv_index]} 달성!", True, FCOLOR)
        achv_title_rect = achv_title.get_rect()
        achv_title_rect.x = self.achv_popup.x + self.inner_magrin * 2 + self.achv_icon_size
        achv_title_rect.centery = self.achv_popup.centery
        self.screen.blit(achv_title, achv_title_rect)
