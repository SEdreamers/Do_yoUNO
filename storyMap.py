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
        self.cleared_locations = ['location0', 'location1'] # 클리어한 장소 리스트
        
        ## 장소 이미지
        self.location0_image =  pygame.image.load("images/map/location0.png")
        self.location0_image = pygame.transform.scale(self.location0_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.bw_location0_image =  pygame.image.load("images/map/bw_location0.png")
        self.bw_location0_image = pygame.transform.scale(self.bw_location0_image, (self.screen_width/4.4944, self.screen_height/4.0107))
        self.location0_rect = self.location0_image.get_rect()
        self.bw_location0_rect = self.location0_image.get_rect()

        self.location1_image =  pygame.image.load("images/map/location1.png")
        self.location1_image = pygame.transform.scale(self.location1_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.bw_location1_image =  pygame.image.load("images/map/bw_location1.png")
        self.bw_location1_image = pygame.transform.scale(self.bw_location1_image, (self.screen_width/5.2083, self.screen_height/2.6643))
        self.location1_rect = self.location1_image.get_rect()
        self.bw_location1_rect = self.location1_image.get_rect()
        
        self.location2_image =  pygame.image.load("images/map/location2.png")
        self.location2_image = pygame.transform.scale(self.location2_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.bw_location2_image = pygame.image.load("images/map/bw_location2.png")
        self.bw_location2_image = pygame.transform.scale(self.bw_location2_image, (self.screen_width/2.9412, self.screen_height/2.6224))
        self.location2_rect = self.location2_image.get_rect()
        self.bw_location2_rect = self.location2_image.get_rect()
        
        self.location3_image = pygame.image.load("images/map/location3.png")
        self.location3_image = pygame.transform.scale(self.location3_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.bw_location3_image =  pygame.image.load("images/map/bw_location3.png")
        self.bw_location3_image = pygame.transform.scale(self.bw_location3_image, (self.screen_width/2.5478, self.screen_height/1.5511))
        self.location3_rect = self.location3_image.get_rect()
        self.bw_location3_rect = self.location3_image.get_rect()
        
        self.location0_rect.x = self.screen_width/3.1847
        self.location0_rect.y = self.screen_height/6.6372
        self.location1_rect.x = self.screen_width/6.8027
        self.location1_rect.y = self.screen_height/2.5685
        self.location2_rect.x = self.screen_width/3.5714
        self.location2_rect.y = self.screen_height/1.656
        self.location3_rect.x = self.screen_width/1.67
        self.location3_rect.y = self.screen_height/31.9149
        self.bw_location0_rect.x = self.screen_width/3.1847
        self.bw_location0_rect.y = self.screen_height/6.6372
        self.bw_location1_rect.x = self.screen_width/6.8027
        self.bw_location1_rect.y = self.screen_height/2.5685
        self.bw_location2_rect.x = self.screen_width/3.5714
        self.bw_location2_rect.y = self.screen_height/1.656
        self.bw_location3_rect.x = self.screen_width/1.67
        self.bw_location3_rect.y = self.screen_height/31.9149
        
        
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True
            self.current_location %= len(self.cleared_locations) # 클리어하거나 도전 중인 맵만 선택 가능


    def display(self):
        pygame.display.set_caption("Story mode")
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.background_image, (0, 0))
        
        # location0 선택 시
        if self.location0_rect.collidepoint(mouse_pos) or self.current_location == 0:
            self.current_location = 0
            self.screen.blit(self.location0_image, (self.screen_width/3.1847, self.screen_height/6.6372))
            self.screen.blit(self.bw_location1_image, (self.screen_width/6.8027, self.screen_height/2.5685))
            self.screen.blit(self.bw_location2_image, (self.screen_width/3.5714, self.screen_height/1.656))
            self.screen.blit(self.bw_location3_image, (self.screen_width/1.67, self.screen_height/31.9149))
            
        # location1 선택 시
        if self.location1_rect.collidepoint(mouse_pos) or self.current_location == 1:
            if len(self.cleared_locations) > 1: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 1
                self.screen.blit(self.bw_location0_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.location1_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_location2_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_location3_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
        # location2 선택 시
        if self.location2_rect.collidepoint(mouse_pos) or self.current_location == 2:
            if len(self.cleared_locations) > 2: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 2
                self.screen.blit(self.bw_location0_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_location1_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.location2_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.bw_location3_image, (self.screen_width/1.67, self.screen_height/31.9149))
        
        # location3 선택 시
        if self.location3_rect.collidepoint(mouse_pos) or self.current_location == 3:
            if len(self.cleared_locations) > 3: # 클리어하거나 도전 중인 맵만 선택 가능
                self.current_location = 3
                self.screen.blit(self.bw_location0_image, (self.screen_width/3.1847, self.screen_height/6.6372))
                self.screen.blit(self.bw_location1_image, (self.screen_width/6.8027, self.screen_height/2.5685))
                self.screen.blit(self.bw_location2_image, (self.screen_width/3.5714, self.screen_height/1.656))
                self.screen.blit(self.location3_image, (self.screen_width/1.67, self.screen_height/31.9149))

        
        # 캐릭터 이미지 출력
        self.screen.blit(self.dear_image, (self.screen_width/2.3256, self.screen_height/4.1667))
        self.screen.blit(self.lion_image, (self.screen_width/11.8343, self.screen_height/1.5213))
        self.screen.blit(self.snake_image, (self.screen_width/2, self.screen_height/1.2285))
        self.screen.blit(self.dragon_image, (self.screen_width/1.2423, self.screen_height/2.1))
        
        # 클리어하지 않았거나 클리어 진행 중이지 않은 맵 자물쇠 출력
        if 'location1' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.location1_rect.centerx * 0.83, self.location1_rect.centery * 0.95))
        if 'location2' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.location2_rect.centerx * 0.97, self.location2_rect.centery * 0.97))
        if 'location3' not in self.cleared_locations:
            self.screen.blit(self.lock_icon, (self.location3_rect.centerx * 0.95, self.location3_rect.centery))
        pygame.display.flip()

    def run(self):
        while True:
            self.display()
            self.handle_events()