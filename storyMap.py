import pygame
import sys
import game
import regionB
import regionC
import regionD
import json

class StoryMap:
    def __init__(self, screen_width, screen_height):
        self.K_UP = pygame.K_w
        self.K_DOWN = pygame.K_s
        self.K_LEFT = pygame.K_a
        self.K_RIGHT = pygame.K_d
        
        self.menu_flag = 0
        # 화면 크기 설정
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        # 폰트
        self.title_font = pygame.font.Font("font/GangwonEduPower.ttf", self.screen_width // 20)
        self.desc_font = pygame.font.Font("font/GangwonEduPower.ttf", self.screen_width // 30)
        
        # 마우스 클릭 여부 설정
        self.mouse_click = False
        
        # 메뉴 선택 여부 설정
        self.selected = False
        
        # 맵 배경 이미지
        self.background_image =  pygame.image.load("images/map/map.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # 지역
        self.current_region = 0 # 현재 마우스나 키보드로 선택한 지역
        try:
            with open('story_mode_data.json') as story_mode_data_file:
                data = json.load(story_mode_data_file)
                unlocked_regions = data['unlocked_regions'] # 저장된 값 불러오기
                self.unlocked_regions = unlocked_regions # 잠금해제 지역 리스트
        except: 
            data = {
                "unlocked_regions": ["regionA"]
            }
            with open('story_mode_data.json','w') as story_mode_data_file: 
                json.dump(data, story_mode_data_file)
    
        ## 지역 이미지
        self.regionA_image = pygame.image.load("images/map/regionA.png")
        self.regionA_image = pygame.transform.scale(self.regionA_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.bw_regionA_image =  pygame.image.load("images/map/bw_regionA.png")
        self.bw_regionA_image = pygame.transform.scale(self.bw_regionA_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.regionA_rect = self.regionA_image.get_rect()
        self.bw_regionA_rect = self.regionA_image.get_rect()

        self.regionB_image =  pygame.image.load("images/map/regionB.png")
        self.regionB_image = pygame.transform.scale(self.regionB_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.bw_regionB_image =  pygame.image.load("images/map/bw_regionB.png")
        self.bw_regionB_image = pygame.transform.scale(self.bw_regionB_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.regionB_rect = self.regionB_image.get_rect()
        self.bw_regionB_rect = self.regionB_image.get_rect()
        
        self.regionC_image =  pygame.image.load("images/map/regionC.png")
        self.regionC_image = pygame.transform.scale(self.regionC_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.bw_regionC_image = pygame.image.load("images/map/bw_regionC.png")
        self.bw_regionC_image = pygame.transform.scale(self.bw_regionC_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.regionC_rect = self.regionC_image.get_rect()
        self.bw_regionC_rect = self.regionC_image.get_rect()
        
        self.regionD_image = pygame.image.load("images/map/regionD.png")
        self.regionD_image = pygame.transform.scale(self.regionD_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.bw_regionD_image =  pygame.image.load("images/map/bw_regionD.png")
        self.bw_regionD_image = pygame.transform.scale(self.bw_regionD_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.regionD_rect = self.regionD_image.get_rect()
        self.bw_regionD_rect = self.regionD_image.get_rect()

        # 캐릭터 이미지
        self.dear_image = pygame.image.load("images/map/deer.png")
        self.dear_image = pygame.transform.scale(self.dear_image, (self.screen_width/8, self.screen_width/8))
        
        self.lion_image = pygame.image.load("images/map/lion.png")
        self.lion_image = pygame.transform.scale(self.lion_image, (self.screen_width/7, self.screen_width/7))
        
        self.snake_image = pygame.image.load("images/map/snake.png")
        self.snake_image = pygame.transform.scale(self.snake_image, (self.screen_width/7, self.screen_width/7))
        
        self.dragon_image = pygame.image.load("images/map/dragon.png")
        self.dragon_image = pygame.transform.scale(self.dragon_image, (self.screen_width/6, self.screen_width/6))
     
        # 자물쇠 이미지
        self.lock_icon = pygame.image.load("images/map/lock.png")
        self.lock_icon = pygame.transform.scale(self.lock_icon, (self.screen_width/12, self.screen_width/12))
        self.lock_rect = self.lock_icon.get_rect()
        
        # 검정색 반투명 이미지
        self.black_surface = pygame.Surface((self.screen_width, self.screen_height))
        self.black_surface.fill((0, 0, 0))
        self.black_surface.set_alpha(170)
        
        # start window 이미지, 버튼 이미지
        self.start_window_image = pygame.image.load("images/map/start_window.png")
        self.start_window_image = pygame.transform.scale(self.start_window_image, (self.screen_width/1.5256, self.screen_height/1.5))
        self.start_window_rect = self.start_window_image.get_rect()
        
        self.start_btn1 = pygame.image.load("images/map/start_btn1.png")
        self.start_btn1 = pygame.transform.scale(self.start_btn1, (self.screen_width/4.1929, self.screen_height/9.8684))
        self.start_btn1_rect = self.start_btn1.get_rect()
        
        self.back_btn1 = pygame.image.load("images/map/back_btn1.png")
        self.back_btn1 = pygame.transform.scale(self.back_btn1, (self.screen_width/4.1929, self.screen_height/9.8684))
        self.back_btn1_rect = self.back_btn1.get_rect()
        
        self.start_btn2 = pygame.image.load("images/map/start_btn2.png")
        self.start_btn2 = pygame.transform.scale(self.start_btn2, (self.screen_width/4.1929, self.screen_height/9.8684))
        self.start_btn2_rect = self.start_btn2.get_rect()
        
        self.back_btn2 = pygame.image.load("images/map/back_btn2.png")
        self.back_btn2 = pygame.transform.scale(self.back_btn2, (self.screen_width/4.1929, self.screen_height/9.8684))
        self.back_btn2_rect = self.back_btn2.get_rect()
        
        self.start_btn1_rect.x = self.screen_width/4.15
        self.start_btn1_rect.y = self.screen_height/1.46
        self.back_btn1_rect.x = self.screen_width/1.95
        self.back_btn1_rect.y = self.screen_height/1.46
        

        
    def start_window(self):
        # 지역 마우스 선택 불가능하게 설정
        self.regionA_rect.x = -2000
        self.regionA_rect.y = -2000
        self.regionB_rect.x = -2000
        self.regionB_rect.y = -2000
        self.regionC_rect.x = -2000
        self.regionC_rect.y = -2000
        self.regionD_rect.x = -2000
        self.regionD_rect.y = -2000
        
        # 설명 및 시작창
        self.start_window_rect.centerx = self.screen_width / 2
        self.start_window_rect.centery = self.screen_height / 2
        self.screen.blit(self.black_surface, (0, 0))
        self.screen.blit(self.start_window_image, self.start_window_rect)
        self.screen.blit(self.start_btn1, (self.screen_width/4.15, self.screen_height/1.46))
        self.screen.blit(self.back_btn1, (self.screen_width/1.95, self.screen_height/1.46))
        
        # 선택 region, region description 출력
        if self.current_region == 0:
            title_text = self.title_font.render("지역 A", True, (13, 0, 12))
            desc_text = "첫 분배시 컴퓨터 플레이어에게\n기술 카드가 50% 더 높은 확률로 분배됩니다.\n컴퓨터 플레이어가 2~3장 이상의 카드를\n한 번에 낼 수 있는 콤보 사용합니다."
        elif self.current_region == 1:
            title_text = self.title_font.render("지역 B", True, (13, 0, 12))
            desc_text = "3명의 플레이어와 대전합니다.\n첫 카드를 제외한 모든 카드가 같은 수만큼\n 플레이어들에게 분배됩니다."
        elif self.current_region == 2:
            title_text = self.title_font.render("지역 C", True, (13, 0, 12))
            desc_text = "2명의 플레이어와 대전합니다.\n매 5턴마다 낼 수 있는 카드의 색상이\n 무작위로 변경됩니다."
        elif self.current_region == 3:
            title_text = self.title_font.render("지역 D", True, (13, 0, 12))
            desc_text = "1명의 플레이어와 대전합니다.\n카드는 플레이어 당 8장씩 주어집니다."
            
        lines = desc_text.split('\n')
        for i, line in enumerate(lines):
            # 글자 렌더링
            desc_text = self.desc_font.render(line, True, (13, 0, 12))
            # 글자 위치 설정
            desc_rect = desc_text.get_rect()
            desc_rect.centerx = self.screen_width / 2
            desc_rect.centery = self.screen_height / 2.5 + (i*self.screen_height*0.05)
            # 화면에 글자 출력
            self.screen.blit(desc_text, desc_rect)
        
        title_rect = title_text.get_rect()
        title_rect.centerx = self.screen_width / 2
        title_rect.centery = self.screen_height / 3.9
        self.screen.blit(title_text, title_rect)
        
        # start, back 마우스 오버, 키보드 선택
        mouse_pos = pygame.mouse.get_pos()
        ## start
        if self.start_btn1_rect.collidepoint(mouse_pos) or self.menu_flag == 0:
            self.menu_flag = 0
            self.screen.blit(self.start_btn2, (self.screen_width/4.15, self.screen_height/1.46))
        else:
            self.screen.blit(self.start_btn1, (self.screen_width/4.15, self.screen_height/1.46))
        ## back
        if self.back_btn1_rect.collidepoint(mouse_pos) or self.menu_flag == 1:
            self.menu_flag = 1
            self.screen.blit(self.back_btn2, (self.screen_width/1.95, self.screen_height/1.46))
        else:
            self.screen.blit(self.back_btn1, (self.screen_width/1.95, self.screen_height/1.46))
            
        # 마우스 클릭
        if self.start_btn1_rect.collidepoint(mouse_pos) and self.mouse_click:
            if self.current_region == 0:
                gameA = game.Game(self.size[0], self.size[1], self.color, 1, "A")
                gameA.run()
            elif self.current_region == 1:
                gameB = regionB.Game(self.size[0], self.size[1], self.color, 3, "B")
                gameB.run()
            elif self.current_region == 2:
                gameC = regionC.Game(self.size[0], self.size[1], self.color, 2, "C")
                gameC.run()
            elif self.current_region == 3:
                gameD = regionD.Game(self.size[0], self.size[1], self.color, 3, "D")
                gameD.run()
            self.mouse_click = False ## 임시 // 추후 게임 로드 추가 시 삭제해도됨
        elif self.back_btn1_rect.collidepoint(mouse_pos) and self.mouse_click:
            self.selected = False
            self.mouse_click = False
            
        self.mouse_click = False
        
        
    def handle_events(self):
        # 키보드 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.selected: # 지역 선택
                    if event.key == self.K_UP:
                        self.current_region -= 1
                    elif event.key == self.K_DOWN:
                        self.current_region += 1
                    elif event.key == 13: # enter
                        self.selected = True
                else: # start, back 선택
                    if event.key == self.K_LEFT:
                        self.menu_flag -= 1
                    elif event.key == self.K_RIGHT:
                        self.menu_flag += 1
                    elif event.key == 13: # enter
                        if self.menu_flag == 0: # start
                            if self.current_region == 0:
                                print('regionA')
                                gameA = game.Game(self.size[0], self.size[1], self.color, 1,"A")
                                gameA.run()
                            elif self.current_region == 1:
                                print('regionB')
                                gameB = regionB.Game(self.size[0], self.size[1], self.color, 3, "B")
                                gameB.run()
                            elif self.current_region == 2:
                                print('regionC')
                                gameC = regionC.Game(self.size[0], self.size[1], self.color, 2, "C")
                                gameC.run()
                            elif self.current_region == 3:
                                print('regionD')
                                gameD = regionD.Game(self.size[0], self.size[1], self.color, 4, "D")
                                gameD.run()
                        elif self.menu_flag == 1: # back
                            self.selected = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True
                
            self.current_region %= len(self.unlocked_regions) # 잠금해제 지역만 선택 가능
            self.menu_flag %= 2


    def display(self):
        pygame.display.set_caption("Story mode")
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.background_image, (0, 0))
        
        if not self.selected:
            self.regionA_rect.x = self.screen_width/3.1847
            self.regionA_rect.y = self.screen_height/6.6372
            self.regionB_rect.x = self.screen_width/6.8027
            self.regionB_rect.y = self.screen_height/2.5685
            self.regionC_rect.x = self.screen_width/3.5714
            self.regionC_rect.y = self.screen_height/1.656
            self.regionD_rect.x = self.screen_width/1.67
            self.regionD_rect.y = self.screen_height/31.9149

        ## region 마우스 오버, 키보드 선택
         ## regionA
        if self.regionA_rect.collidepoint(mouse_pos) or self.current_region == 0:
            self.current_region = 0
            self.screen.blit(self.regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
            self.screen.blit(self.bw_regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
            self.screen.blit(self.bw_regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
            self.screen.blit(self.bw_regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
            
         ## regionB
        if self.regionB_rect.collidepoint(mouse_pos) or self.current_region == 1:
            if len(self.unlocked_regions) > 1: # 잠금해제 지역만 선택 가능
                self.current_region = 1
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
         ## regionC
        if self.regionC_rect.collidepoint(mouse_pos) or self.current_region == 2:
            if len(self.unlocked_regions) > 2: # 잠금해제 지역만 선택 가능
                self.current_region = 2
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
         ## regionD
        if self.regionD_rect.collidepoint(mouse_pos) or self.current_region == 3:
            if len(self.unlocked_regions) > 3: # 잠금해제 지역만 선택 가능
                self.current_region = 3
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
                
        # 캐릭터 이미지 출력
        self.screen.blit(self.dear_image, (self.screen_width/2.3256, self.screen_height/4.1667))
        self.screen.blit(self.lion_image, (self.screen_width/11.8343, self.screen_height/1.5213))
        self.screen.blit(self.snake_image, (self.screen_width/2, self.screen_height/1.2285))
        self.screen.blit(self.dragon_image, (self.screen_width/1.2423, self.screen_height/2.1))
        
        # 잠겨있는 맵 자물쇠 출력
        if 'regionB' not in self.unlocked_regions:
            self.screen.blit(self.lock_icon, (self.screen_width/4.89, self.screen_height/1.7647))
        if 'regionC' not in self.unlocked_regions:
            self.screen.blit(self.lock_icon, (self.screen_width/2.3557, self.screen_height/1.2712))
        if 'regionD' not in self.unlocked_regions:
            self.screen.blit(self.lock_icon, (self.screen_width/1.32, self.screen_height/2.8937))
        
        if self.selected:
            self.start_window()

        with open('setting_data.json') as game_file:
            data = json.load(game_file)
            self.color = data['color_blind_mode']     ## 저장된 값 불러오기. 
            self.size = data["size"]
            
            if data["AWDS"] == True:
                self.K_UP = pygame.K_w
                self.K_DOWN = pygame.K_s
                self.K_LEFT = pygame.K_a
                self.K_RIGHT = pygame.K_d
            else: 
                self.K_UP = pygame.K_UP
                self.K_DOWN = pygame.K_DOWN
                self.K_LEFT = pygame.K_LEFT
                self.K_RIGHT = pygame.K_RIGHT

        ## region 클릭
        if self.mouse_click:
            if self.regionA_rect.collidepoint(mouse_pos) and len(self.unlocked_regions):
                self.selected = True
                self.mouse_click = False

            if self.regionB_rect.collidepoint(mouse_pos) and len(self.unlocked_regions) > 1:
                self.selected = True
                self.mouse_click = False

            if self.regionC_rect.collidepoint(mouse_pos) and len(self.unlocked_regions) > 2:
                self.selected = True
                self.mouse_click = False
            if self.regionD_rect.collidepoint(mouse_pos) and len(self.unlocked_regions) > 3:
                self.selected = True
                self.mouse_click = False
        self.mouse_click = False
        pygame.display.flip()

    def run(self):
        while True:
            self.display()
            self.handle_events()
