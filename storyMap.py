import pygame
import sys

class StoryMap:
    def __init__(self, screen_width, screen_height):
        # 화면 크기 설정
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        # 마우스 클릭 설정
        self.mouse_click = False
        
        # 맵 배경 이미지
        self.background_image =  pygame.image.load("images/map/map.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # 장소
        self.current_region = 0 # 현재 마우스나 키보드로 선택한 장소
        self.cleared_regions = ['regionA', 'regionB', 'regionC'] # 클리어한 장소 리스트
        
        ## 장소 이미지
        self.regionA_image =  pygame.image.load("images/map/regionA.png")
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
        
        self.regionA_rect.x = self.screen_width/3.1847
        self.regionA_rect.y = self.screen_height/6.6372
        self.regionB_rect.x = self.screen_width/6.8027
        self.regionB_rect.y = self.screen_height/2.5685
        self.regionC_rect.x = self.screen_width/3.5714
        self.regionC_rect.y = self.screen_height/1.656
        self.regionD_rect.x = self.screen_width/1.67
        self.regionD_rect.y = self.screen_height/31.9149
        self.bw_regionA_rect.x = self.screen_width/3.1847
        self.bw_regionA_rect.y = self.screen_height/6.6372
        self.bw_regionB_rect.x = self.screen_width/6.8027
        self.bw_regionB_rect.y = self.screen_height/2.5685
        self.bw_regionC_rect.x = self.screen_width/3.5714
        self.bw_regionC_rect.y = self.screen_height/1.656
        self.bw_regionD_rect.x = self.screen_width/1.67
        self.bw_regionD_rect.y = self.screen_height/31.9149
        
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
 
    
    def handle_events(self):
        # 키보드 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_region -= 1
                elif event.key == pygame.K_DOWN:
                    self.current_region += 1
                elif event.key == 13: # enter key
                    if self.current_region == 0:
                        print('regionA')
                        pass # 지역A 게임 로드
                    elif self.current_region == 1:
                        print('regionB')
                        pass # 지역B 게임 로드
                    elif self.current_region == 2:
                        print('regionC')
                        pass # 지역C 게임 로드
                    elif self.current_region == 3:
                        print('regionD')
                        pass # 지역D 게임 로드 
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True
                
            self.current_region %= len(self.cleared_regions) # 클리어하거나 도전 중인 맵만 선택 가능


    def display(self):
        pygame.display.set_caption("Story mode")
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.background_image, (0, 0))
        
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
            if len(self.cleared_regions) > 1: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_region = 1
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
         ## regionC
        if self.regionC_rect.collidepoint(mouse_pos) or self.current_region == 2:
            if len(self.cleared_regions) > 2: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_region = 2
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
         ## regionD
        if self.regionD_rect.collidepoint(mouse_pos) or self.current_region == 3:
            if len(self.cleared_regions) > 3: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_region = 3
                self.screen.blit(self.bw_regionA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_regionB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_regionC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.regionD_image, (self.screen_width/1.67, self.screen_height/31.9149))
                
        ## region 클릭
        if self.regionA_rect.collidepoint(mouse_pos) and self.mouse_click:
            print('regionA')
            pass # 지역A 게임 로드
        elif self.regionB_rect.collidepoint(mouse_pos) and self.mouse_click:
            print('regionB')
            pass # 지역B 게임 로드
        elif self.regionC_rect.collidepoint(mouse_pos) and self.mouse_click:
            print('regionC')
            pass # 지역C 게임 로드
        elif self.regionD_rect.collidepoint(mouse_pos) and self.mouse_click:
            print('regionD')
            pass # 지역D 게임 로드
        
        # 캐릭터 이미지 출력
        self.screen.blit(self.dear_image, (self.screen_width/2.3256, self.screen_height/4.1667))
        self.screen.blit(self.lion_image, (self.screen_width/11.8343, self.screen_height/1.5213))
        self.screen.blit(self.snake_image, (self.screen_width/2, self.screen_height/1.2285))
        self.screen.blit(self.dragon_image, (self.screen_width/1.2423, self.screen_height/2.1))
        
        # 클리어하지 않았거나 클리어 진행 중이지 않은 맵 자물쇠 출력
        if 'regionB' not in self.cleared_regions:
            self.screen.blit(self.lock_icon, (self.regionB_rect.centerx * 0.83, self.regionB_rect.centery * 0.95))
        if 'regionC' not in self.cleared_regions:
            self.screen.blit(self.lock_icon, (self.regionC_rect.centerx * 0.97, self.regionC_rect.centery * 0.97))
        if 'regionD' not in self.cleared_regions:
            self.screen.blit(self.lock_icon, (self.regionD_rect.centerx * 0.95, self.regionD_rect.centery))
        pygame.display.flip()

    def run(self):
        while True:
            self.display()
            self.handle_events()