import pygame
import sys

class StoryMapUI:
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
        self.current_location = 0 # 현재 마우스나 키보드로 선택한 장소
        self.cleared_locations = ['locationA', 'locationB'] # 클리어한 장소 리스트
        
        ## 장소 이미지
        self.locationA_image =  pygame.image.load("images/map/locationA.png")
        self.locationA_image = pygame.transform.scale(self.locationA_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.bw_locationA_image =  pygame.image.load("images/map/bw_locationA.png")
        self.bw_locationA_image = pygame.transform.scale(self.bw_locationA_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.locationA_rect = self.locationA_image.get_rect()
        self.bw_locationA_rect = self.locationA_image.get_rect()

        self.locationB_image =  pygame.image.load("images/map/locationB.png")
        self.locationB_image = pygame.transform.scale(self.locationB_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.bw_locationB_image =  pygame.image.load("images/map/bw_locationB.png")
        self.bw_locationB_image = pygame.transform.scale(self.bw_locationB_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.locationB_rect = self.locationB_image.get_rect()
        self.bw_locationB_rect = self.locationB_image.get_rect()
        
        self.locationC_image =  pygame.image.load("images/map/locationC.png")
        self.locationC_image = pygame.transform.scale(self.locationC_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.bw_locationC_image = pygame.image.load("images/map/bw_locationC.png")
        self.bw_locationC_image = pygame.transform.scale(self.bw_locationC_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.locationC_rect = self.locationC_image.get_rect()
        self.bw_locationC_rect = self.locationC_image.get_rect()
        
        self.locationD_image = pygame.image.load("images/map/locationD.png")
        self.locationD_image = pygame.transform.scale(self.locationD_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.bw_locationD_image =  pygame.image.load("images/map/bw_locationD.png")
        self.bw_locationD_image = pygame.transform.scale(self.bw_locationD_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.locationD_rect = self.locationD_image.get_rect()
        self.bw_locationD_rect = self.locationD_image.get_rect()
        
        self.locationA_rect.x = self.screen_width/3.1847
        self.locationA_rect.y = self.screen_height/6.6372
        self.locationB_rect.x = self.screen_width/6.8027
        self.locationB_rect.y = self.screen_height/2.5685
        self.locationC_rect.x = self.screen_width/3.5714
        self.locationC_rect.y = self.screen_height/1.656
        self.locationD_rect.x = self.screen_width/1.67
        self.locationD_rect.y = self.screen_height/31.9149
        self.bw_locationA_rect.x = self.screen_width/3.1847
        self.bw_locationA_rect.y = self.screen_height/6.6372
        self.bw_locationB_rect.x = self.screen_width/6.8027
        self.bw_locationB_rect.y = self.screen_height/2.5685
        self.bw_locationC_rect.x = self.screen_width/3.5714
        self.bw_locationC_rect.y = self.screen_height/1.656
        self.bw_locationD_rect.x = self.screen_width/1.67
        self.bw_locationD_rect.y = self.screen_height/31.9149
        
        
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
                    self.current_location -= 1
                elif event.key == pygame.K_DOWN:
                    self.current_location += 1
                elif event.key == 13: # enter key
                    if self.current_location == 0:
                        pass
                    elif self.current_location == 1:
                        pass
                    elif self.current_location == 2:
                        pass
                    elif self.current_location == 3:
                        pass    
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True
            self.current_location %= len(self.cleared_locations) # 클리어하거나 도전 중인 맵만 선택 가능


    def display(self):
        pygame.display.set_caption("Story mode")
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.background_image, (0, 0))
        
        # locationA 선택 시
        if self.locationA_rect.collidepoint(mouse_pos) or self.current_location == 0:
            self.current_location = 0
            self.screen.blit(self.locationA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
            self.screen.blit(self.bw_locationB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
            self.screen.blit(self.bw_locationC_image, (self.screen_width/3.5714, self.screen_height/1.656))
            self.screen.blit(self.bw_locationD_image, (self.screen_width/1.67, self.screen_height/31.9149))
            
        # locationB 선택 시
        if self.locationB_rect.collidepoint(mouse_pos) or self.current_location == 1:
            if len(self.cleared_locations) > 1: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 1
                self.screen.blit(self.bw_locationA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.locationB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_locationC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_locationD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
        # locationC 선택 시
        if self.locationC_rect.collidepoint(mouse_pos) or self.current_location == 2:
            if len(self.cleared_locations) > 2: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 2
                self.screen.blit(self.bw_locationA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_locationB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.locationC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_locationD_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
        # locationD 선택 시
        if self.locationD_rect.collidepoint(mouse_pos) or self.current_location == 3:
            if len(self.cleared_locations) > 3: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 3
                self.screen.blit(self.bw_locationA_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_locationB_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_locationC_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.locationD_image, (self.screen_width/1.67, self.screen_height/31.9149))

        
        # 캐릭터 이미지 출력
        self.screen.blit(self.dear_image, (self.screen_width/2.3256, self.screen_height/4.1667))
        self.screen.blit(self.lion_image, (self.screen_width/11.8343, self.screen_height/1.5213))
        self.screen.blit(self.snake_image, (self.screen_width/2, self.screen_height/1.2285))
        self.screen.blit(self.dragon_image, (self.screen_width/1.2423, self.screen_height/2.1))
        
        # 클리어하지 않았거나 클리어 진행 중이지 않은 맵 자물쇠 출력
        if 'locationB' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.locationB_rect.centerx * 0.83, self.locationB_rect.centery * 0.95))
        if 'locationC' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.locationC_rect.centerx * 0.97, self.locationC_rect.centery * 0.97))
        if 'locationD' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.locationD_rect.centerx * 0.95, self.locationD_rect.centery))
        pygame.display.flip()

    def run(self):
        while True:
            self.display()
            self.handle_events()