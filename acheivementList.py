import pygame
import game
import main
import sys
import innersetting
import json

BGCOLOR = (221, 195, 81)
SCOLOR = (228, 221, 134)
FCOLOR = (45, 43, 32)
BCOLOR = (40, 62, 255)


class AcheivementList:
    def __init__(self, screen_width, screen_height, color_blind_mode):
        self.achv_info = ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"]
        self.achv_title = ["싱글 승리", "싱글 기술5", "싱글 기술7", "10턴 승리", "픽0 승리", "30턴 승리", "UNO 승리", "지역A 승리", "지역B 승리", "지역C 승리", "지역D 승리", "기술0 승리"]
        
        self.color_blind_mode = color_blind_mode
        
        # 화면 설정
        self.screen_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        
        # 폰트
        self.title_font = pygame.font.Font("font/GangwonEduPower.ttf", self.screen_size[0] // 40)
        self.desc_font = pygame.font.Font("font/GangwonEduPower.ttf", self.screen_size[1] // 43)

        self.radius = 10
        self.box_width = self.screen_size[0] * 0.27778
        self.box_height = self.screen_size[1] * 0.1845
        self.w_top = self.screen_size[0] * 0.055556
        self.h_top = self.screen_size[1] * 0.074
        self.w_margin = self.screen_size[0] * 0.0278
        self.h_margin = self.screen_size[1] * 0.037
        
        self.box0 = pygame.Rect(self.w_top, self.h_top, self.box_width, self.box_height)
        self.box1 = pygame.Rect(self.w_top + self.box_width + self.w_margin, self.h_top, self.box_width, self.box_height)
        self.box2 = pygame.Rect(self.w_top + self.box_width * 2 + self.w_margin * 2, self.h_top, self.box_width, self.box_height)
        self.box3 = pygame.Rect(self.w_top, self.h_top + self.h_margin + self.box_height, self.box_width, self.box_height)
        self.box4 = pygame.Rect(self.w_top + self.box_width + self.w_margin, self.h_top + self.h_margin + self.box_height, self.box_width, self.box_height)
        self.box5 = pygame.Rect(self.w_top + self.box_width * 2 + self.w_margin * 2, self.h_top + self.h_margin + self.box_height, self.box_width, self.box_height)
        self.box6 = pygame.Rect(self.w_top, self.h_top + self.h_margin * 2 + self.box_height * 2, self.box_width, self.box_height)
        self.box7 = pygame.Rect(self.w_top + self.box_width + self.w_margin, self.h_top + self.h_margin * 2 + self.box_height * 2, self.box_width, self.box_height)
        self.box8 = pygame.Rect(self.w_top + self.box_width * 2 + self.w_margin * 2, self.h_top + self.h_margin * 2 + self.box_height * 2, self.box_width, self.box_height)
        self.box9 = pygame.Rect(self.w_top, self.h_top + self.h_margin * 3 + self.box_height * 3, self.box_width, self.box_height)
        self.box10 = pygame.Rect(self.w_top + self.box_width + self.w_margin, self.h_top + self.h_margin * 3 + self.box_height * 3, self.box_width, self.box_height)    
        self.box11 = pygame.Rect(self.w_top + self.box_width * 2 + self.w_margin * 2, self.h_top + self.h_margin * 3 + self.box_height * 3, self.box_width, self.box_height)
        
        self.achv_icon_size = self.screen_size[0] * 0.08333
        self.inner_magrin = self.screen_size[0] * 0.01944
        
        self.achv0_icon = pygame.image.load("images/acheivement/achv0.png")
        self.achv0_icon =  pygame.transform.scale(self.achv0_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv0_icon = pygame.image.load("images/acheivement/bw_achv0.png")
        self.bw_achv0_icon =  pygame.transform.scale(self.bw_achv0_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv0_title = self.title_font.render(self.achv_title[0], True, FCOLOR)
        self.achv0_desc1 = self.desc_font.render("싱글 플레이어", True, FCOLOR)
        self.achv0_desc2 = self.desc_font.render("게임에서 승리하기", True, FCOLOR)
        
        self.achv1_icon = pygame.image.load("images/acheivement/achv1.png")
        self.achv1_icon =  pygame.transform.smoothscale(self.achv1_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv1_icon = pygame.image.load("images/acheivement/bw_achv1.png")
        self.bw_achv1_icon = pygame.transform.scale(self.bw_achv1_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv1_title = self.title_font.render(self.achv_title[1], True, FCOLOR)
        self.achv1_desc1 = self.desc_font.render("싱글 플레이어", True, FCOLOR)
        self.achv1_desc2 = self.desc_font.render("게임에서 기술카드", True, FCOLOR)
        self.achv1_desc3 = self.desc_font.render("5장 사용하기", True, FCOLOR)
        
        self.achv2_icon = pygame.image.load("images/acheivement/achv2.png")
        self.achv2_icon =  pygame.transform.smoothscale(self.achv2_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv2_icon = pygame.image.load("images/acheivement/bw_achv2.png")
        self.bw_achv2_icon = pygame.transform.scale(self.bw_achv2_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv2_title = self.title_font.render(self.achv_title[2], True, FCOLOR)
        self.achv2_desc1 = self.desc_font.render("싱글 플레이어", True, FCOLOR)
        self.achv2_desc2 = self.desc_font.render("게임에서 기술카드", True, FCOLOR)
        self.achv2_desc3 = self.desc_font.render("7장 사용하기", True, FCOLOR)
        
        
        self.achv3_icon = pygame.image.load("images/acheivement/achv3.png")
        self.achv3_icon =  pygame.transform.scale(self.achv3_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv3_icon = pygame.image.load("images/acheivement/bw_achv3.png")
        self.bw_achv3_icon =  pygame.transform.scale(self.bw_achv3_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv3_title = self.title_font.render(self.achv_title[3], True, FCOLOR)
        self.achv3_desc1 = self.desc_font.render("싱글 플레이어", True, FCOLOR)
        self.achv3_desc2 = self.desc_font.render("게임에서 10턴 안에", True, FCOLOR)
        self.achv3_desc3 = self.desc_font.render("승리하기", True, FCOLOR)
        
        self.achv4_icon = pygame.image.load("images/acheivement/achv4.png")
        self.achv4_icon =  pygame.transform.scale(self.achv4_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv4_icon = pygame.image.load("images/acheivement/bw_achv4.png")
        self.bw_achv4_icon =  pygame.transform.scale(self.bw_achv4_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv4_title = self.title_font.render(self.achv_title[4], True, FCOLOR)
        self.achv4_desc1 = self.desc_font.render("싱글 플레이어", True, FCOLOR)
        self.achv4_desc2 = self.desc_font.render("게임에서 20턴", True, FCOLOR)
        self.achv4_desc3 = self.desc_font.render("안에 승리하기", True, FCOLOR)       
        
        self.achv5_icon = pygame.image.load("images/acheivement/achv5.png")
        self.achv5_icon =  pygame.transform.scale(self.achv5_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv5_icon = pygame.image.load("images/acheivement/bw_achv5.png")
        self.bw_achv5_icon =  pygame.transform.scale(self.bw_achv5_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv5_title = self.title_font.render(self.achv_title[5], True, FCOLOR)
        self.achv5_desc1 = self.desc_font.render("카드를 1장도", True, FCOLOR)
        self.achv5_desc2 = self.desc_font.render("뽑지않고 승리하기", True, FCOLOR)
        
        self.achv6_icon = pygame.image.load("images/acheivement/achv6.png")
        self.achv6_icon =  pygame.transform.scale(self.achv6_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv6_icon = pygame.image.load("images/acheivement/bw_achv6.png")
        self.bw_achv6_icon =  pygame.transform.scale(self.bw_achv6_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv6_title = self.title_font.render(self.achv_title[6], True, FCOLOR)
        self.achv6_desc1 = self.desc_font.render("다른 플레이어가", True, FCOLOR)
        self.achv6_desc2 = self.desc_font.render("UNO를 선언한 뒤", True, FCOLOR)
        self.achv6_desc3 = self.desc_font.render("승리하기", True, FCOLOR)
                
        self.achv7_icon = pygame.image.load("images/acheivement/achv7.png")
        self.achv7_icon =  pygame.transform.scale(self.achv7_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv7_icon = pygame.image.load("images/acheivement/bw_achv7.png")
        self.bw_achv7_icon =  pygame.transform.scale(self.bw_achv7_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv7_title = self.title_font.render(self.achv_title[7], True, FCOLOR)
        self.achv7_desc1 = self.desc_font.render("스토리 모드", True, FCOLOR)
        self.achv7_desc2 = self.desc_font.render("지역A 승리하기", True, FCOLOR)
        
        self.achv8_icon = pygame.image.load("images/acheivement/achv8.png")
        self.achv8_icon =  pygame.transform.scale(self.achv8_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv8_icon = pygame.image.load("images/acheivement/bw_achv8.png")
        self.bw_achv8_icon =  pygame.transform.scale(self.bw_achv8_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv8_title = self.title_font.render(self.achv_title[8], True, FCOLOR)
        self.achv8_desc1 = self.desc_font.render("스토리 모드", True, FCOLOR)
        self.achv8_desc2 = self.desc_font.render("지역B 승리하기", True, FCOLOR)
        
        self.achv9_icon = pygame.image.load("images/acheivement/achv9.png")
        self.achv9_icon =  pygame.transform.scale(self.achv9_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv9_icon = pygame.image.load("images/acheivement/bw_achv9.png")
        self.bw_achv9_icon =  pygame.transform.scale(self.bw_achv9_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv9_title = self.title_font.render(self.achv_title[9], True, FCOLOR)
        self.achv9_desc1 = self.desc_font.render("스토리 모드", True, FCOLOR)
        self.achv9_desc2 = self.desc_font.render("지역C 승리하기", True, FCOLOR)
        
        self.achv10_icon = pygame.image.load("images/acheivement/achv10.png")
        self.achv10_icon =  pygame.transform.scale(self.achv10_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv10_icon = pygame.image.load("images/acheivement/bw_achv10.png")
        self.bw_achv10_icon =  pygame.transform.scale(self.bw_achv10_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv10_title = self.title_font.render(self.achv_title[10], True, FCOLOR)
        self.achv10_desc1 = self.desc_font.render("스토리 모드", True, FCOLOR)
        self.achv10_desc2 = self.desc_font.render("지역D 승리하기", True, FCOLOR)
        
        self.achv11_icon = pygame.image.load("images/acheivement/achv11.png")
        self.achv11_icon =  pygame.transform.scale(self.achv11_icon, (self.achv_icon_size, self.achv_icon_size))
        self.bw_achv11_icon = pygame.image.load("images/acheivement/bw_achv11.png")
        self.bw_achv11_icon =  pygame.transform.scale(self.bw_achv11_icon, (self.achv_icon_size, self.achv_icon_size))
        self.achv11_title = self.title_font.render(self.achv_title[11], True, FCOLOR)
        self.achv11_desc1 = self.desc_font.render("기술 카드를", True, FCOLOR)
        self.achv11_desc2 = self.desc_font.render("단 한 번도 사용", True, FCOLOR)
        self.achv11_desc3 = self.desc_font.render("하지 않고 승리하기", True, FCOLOR)
        
        self.lock_icon_size = self.screen_size[0] * 0.04
        self.lock_icon = pygame.image.load("images/acheivement/lock.png")
        
        self.lock0_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock0_rect = self.lock0_icon.get_rect()
        
        self.lock1_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock1_rect = self.lock1_icon.get_rect()
        
        self.lock2_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock2_rect = self.lock2_icon.get_rect()
        
        self.lock3_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock3_rect = self.lock3_icon.get_rect()
        
        self.lock4_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock4_rect = self.lock4_icon.get_rect()
        
        self.lock5_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock5_rect = self.lock5_icon.get_rect()
        
        self.lock6_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock6_rect = self.lock6_icon.get_rect()
        
        self.lock7_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock7_rect = self.lock7_icon.get_rect()
        
        self.lock7_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock7_rect = self.lock7_icon.get_rect()
        
        self.lock8_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock8_rect = self.lock8_icon.get_rect()
        
        self.lock9_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock9_rect = self.lock9_icon.get_rect()
        
        self.lock10_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock10_rect = self.lock10_icon.get_rect()
        
        self.lock11_icon = pygame.transform.scale(self.lock_icon, (self.lock_icon_size, self.lock_icon_size))
        self.lock11_rect = self.lock11_icon.get_rect()
        
        # 뒤로가기
        self.back_icon = pygame.image.load("images/acheivement/back.png")
        self.back_icon = pygame.transform.scale(self.back_icon, (self.screen_size[0] // 23, self.screen_size[0] // 23))
        self.back_rect = self.back_icon.get_rect()

        


    def display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
        try:
            with open('acheivement_data.json') as acheivement_data_file:
                data = json.load(acheivement_data_file)
                achv_info = data['achv_info'] # 저장된 값 불러오기
                self.achv_info = achv_info # 달성한 업적 리스트
        except: 
            data = {
                "achv_info": ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"]
            }
            self.achv_info = data['achv_info']
            with open('acheivement_data.json','w') as acheivement_data_file: 
                json.dump(data, acheivement_data_file)
                
            
        pygame.display.set_caption("Acheivement List")
        self.screen.fill(BGCOLOR)
        
        
        pygame.draw.rect(self.screen, SCOLOR, self.box0, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box1, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box2, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box3, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box4, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box5, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box6, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box7, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box8, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box9, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box10, border_radius=self.radius)
        pygame.draw.rect(self.screen, SCOLOR, self.box11, border_radius=self.radius)
        
        
        # 업적0 정보 출력
        if self.achv_info[0] == "None":
            achv0_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv0_icon, (self.box0.x + self.inner_magrin, self.box0.y + self.inner_magrin))
            self.lock0_rect.x = self.box0.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock0_rect.y = self.box0.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock0_icon, self.lock0_rect)
        else:
            achv0_date = self.desc_font.render(f"{self.achv_info[0]}", True, BCOLOR)
            self.screen.blit(self.achv0_icon, (self.box0.x + self.inner_magrin, self.box0.y + self.inner_magrin))
            
        self.screen.blit(self.achv0_title, (self.box0.x + self.inner_magrin * 2 + self.achv_icon_size, self.box0.y + self.inner_magrin))
        self.screen.blit(self.achv0_desc1, (self.box0.x + self.inner_magrin * 2 + self.achv_icon_size, self.box0.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv0_desc2, (self.box0.x + self.inner_magrin * 2 + self.achv_icon_size, self.box0.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv0_date, (self.box0.x + self.inner_magrin * 2 + self.achv_icon_size, self.box0.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적1 정보 출력
        if self.achv_info[1] == "None":
            achv1_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv1_icon, (self.box1.x + self.inner_magrin, self.box1.y + self.inner_magrin))
            self.lock1_rect.x = self.box1.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock1_rect.y = self.box1.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock1_icon, self.lock1_rect)
        else:
            achv1_date = self.desc_font.render(f"{self.achv_info[1]}", True, BCOLOR)
            self.screen.blit(self.achv1_icon, (self.box1.x + self.inner_magrin, self.box1.y + self.inner_magrin))
            
        self.screen.blit(self.achv1_title, (self.box1.x + self.inner_magrin * 2 + self.achv_icon_size, self.box1.y + self.inner_magrin))
        self.screen.blit(self.achv1_desc1, (self.box1.x + self.inner_magrin * 2 + self.achv_icon_size, self.box1.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv1_desc2, (self.box1.x + self.inner_magrin * 2 + self.achv_icon_size, self.box1.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv1_desc3, (self.box1.x + self.inner_magrin * 2 + self.achv_icon_size, self.box1.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv1_date, (self.box1.x + self.inner_magrin * 2 + self.achv_icon_size, self.box1.y + self.inner_magrin + self.screen_size[1] * 0.118))
        
        # 업적2 정보 출력
        if self.achv_info[2] == "None":
            achv2_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv2_icon, (self.box2.x + self.inner_magrin, self.box2.y + self.inner_magrin))
            self.lock2_rect.x = self.box2.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock2_rect.y = self.box2.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock2_icon, self.lock2_rect)
        else:
            achv2_date = self.desc_font.render(f"{self.achv_info[2]}", True, BCOLOR)
            self.screen.blit(self.achv2_icon, (self.box2.x + self.inner_magrin, self.box2.y + self.inner_magrin))
            
        self.screen.blit(self.achv2_title, (self.box2.x + self.inner_magrin * 2 + self.achv_icon_size, self.box2.y + self.inner_magrin))
        self.screen.blit(self.achv2_desc1, (self.box2.x + self.inner_magrin * 2 + self.achv_icon_size, self.box2.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv2_desc2, (self.box2.x + self.inner_magrin * 2 + self.achv_icon_size, self.box2.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv2_desc3, (self.box2.x + self.inner_magrin * 2 + self.achv_icon_size, self.box2.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv2_date, (self.box2.x + self.inner_magrin * 2 + self.achv_icon_size, self.box2.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적3 정보 출력
        if self.achv_info[3] == "None":
            achv3_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv3_icon, (self.box3.x + self.inner_magrin, self.box3.y + self.inner_magrin))
            self.lock3_rect.x = self.box3.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock3_rect.y = self.box3.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock3_icon, self.lock3_rect)
        else:
            achv3_date = self.desc_font.render(f"{self.achv_info[3]}", True, BCOLOR)
            self.screen.blit(self.achv3_icon, (self.box3.x + self.inner_magrin, self.box3.y + self.inner_magrin))
            
        self.screen.blit(self.achv3_title, (self.box3.x + self.inner_magrin * 2 + self.achv_icon_size, self.box3.y + self.inner_magrin))
        self.screen.blit(self.achv3_desc1, (self.box3.x + self.inner_magrin * 2 + self.achv_icon_size, self.box3.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv3_desc2, (self.box3.x + self.inner_magrin * 2 + self.achv_icon_size, self.box3.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv3_desc3, (self.box3.x + self.inner_magrin * 2 + self.achv_icon_size, self.box3.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv3_date, (self.box3.x + self.inner_magrin * 2 + self.achv_icon_size, self.box3.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        
        # 업적4 정보 출력
        if self.achv_info[4] == "None":
            achv4_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv4_icon, (self.box4.x + self.inner_magrin, self.box4.y + self.inner_magrin))
            self.lock4_rect.x = self.box4.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock4_rect.y = self.box4.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock4_icon, self.lock4_rect)
        else:
            achv4_date = self.desc_font.render(f"{self.achv_info[4]}", True, BCOLOR)
            self.screen.blit(self.achv4_icon, (self.box4.x + self.inner_magrin, self.box4.y + self.inner_magrin))
            
        self.screen.blit(self.achv4_title, (self.box4.x + self.inner_magrin * 2 + self.achv_icon_size, self.box4.y + self.inner_magrin))
        self.screen.blit(self.achv4_desc1, (self.box4.x + self.inner_magrin * 2 + self.achv_icon_size, self.box4.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv4_desc2, (self.box4.x + self.inner_magrin * 2 + self.achv_icon_size, self.box4.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv4_desc3, (self.box4.x + self.inner_magrin * 2 + self.achv_icon_size, self.box4.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv4_date, (self.box4.x + self.inner_magrin * 2 + self.achv_icon_size, self.box4.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적5 정보 출력
        if self.achv_info[5] == "None":
            achv5_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv5_icon, (self.box5.x + self.inner_magrin, self.box5.y + self.inner_magrin))
            self.lock5_rect.x = self.box5.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock5_rect.y = self.box5.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock5_icon, self.lock5_rect)
        else:
            achv5_date = self.desc_font.render(f"{self.achv_info[5]}", True, BCOLOR)
            self.screen.blit(self.achv5_icon, (self.box4.x + self.inner_magrin, self.box4.y + self.inner_magrin))
        self.screen.blit(self.achv5_title, (self.box5.x + self.inner_magrin * 2 + self.achv_icon_size, self.box5.y + self.inner_magrin))
        self.screen.blit(self.achv5_desc1, (self.box5.x + self.inner_magrin * 2 + self.achv_icon_size, self.box5.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv5_desc2, (self.box5.x + self.inner_magrin * 2 + self.achv_icon_size, self.box5.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv5_date, (self.box5.x + self.inner_magrin * 2 + self.achv_icon_size, self.box5.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적6 정보 출력
        if self.achv_info[6] == "None":
            achv6_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv6_icon, (self.box6.x + self.inner_magrin, self.box6.y + self.inner_magrin))
            self.lock6_rect.x = self.box6.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock6_rect.y = self.box6.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock6_icon, self.lock6_rect)
        else:
            achv6_date = self.desc_font.render(f"{self.achv_info[6]}", True, BCOLOR)
            self.screen.blit(self.achv6_icon, (self.box6.x + self.inner_magrin, self.box6.y + self.inner_magrin))
            
        self.screen.blit(self.achv6_title, (self.box6.x + self.inner_magrin * 2 + self.achv_icon_size, self.box6.y + self.inner_magrin))
        self.screen.blit(self.achv6_desc1, (self.box6.x + self.inner_magrin * 2 + self.achv_icon_size, self.box6.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv6_desc2, (self.box6.x + self.inner_magrin * 2 + self.achv_icon_size, self.box6.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv6_desc3, (self.box6.x + self.inner_magrin * 2 + self.achv_icon_size, self.box6.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv6_date, (self.box6.x + self.inner_magrin * 2 + self.achv_icon_size, self.box6.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적7 정보 출력
        if self.achv_info[7] == "None":
            achv7_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv7_icon, (self.box7.x + self.inner_magrin, self.box7.y + self.inner_magrin))
            self.lock7_rect.x = self.box7.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock7_rect.y = self.box7.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock7_icon, self.lock7_rect)
        else:
            achv7_date = self.desc_font.render(f"{self.achv_info[7]}", True, BCOLOR)
            self.screen.blit(self.achv7_icon, (self.box7.x + self.inner_magrin, self.box7.y + self.inner_magrin))
            
        self.screen.blit(self.achv7_title, (self.box7.x + self.inner_magrin * 2 + self.achv_icon_size, self.box7.y + self.inner_magrin))
        self.screen.blit(self.achv7_desc1, (self.box7.x + self.inner_magrin * 2 + self.achv_icon_size, self.box7.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv7_desc2, (self.box7.x + self.inner_magrin * 2 + self.achv_icon_size, self.box7.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv7_date, (self.box7.x + self.inner_magrin * 2 + self.achv_icon_size, self.box7.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적8 정보 출력
        if self.achv_info[8] == "None":
            achv8_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv8_icon, (self.box8.x + self.inner_magrin, self.box8.y + self.inner_magrin))
            self.lock8_rect.x = self.box8.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock8_rect.y = self.box8.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock8_icon, self.lock8_rect)
        else:
            achv8_date = self.desc_font.render(f"{self.achv_info[8]}", True, BCOLOR)
            self.screen.blit(self.achv8_icon, (self.box8.x + self.inner_magrin, self.box8.y + self.inner_magrin))
            
        self.screen.blit(self.achv8_title, (self.box8.x + self.inner_magrin * 2 + self.achv_icon_size, self.box8.y + self.inner_magrin))
        self.screen.blit(self.achv8_desc1, (self.box8.x + self.inner_magrin * 2 + self.achv_icon_size, self.box8.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv8_desc2, (self.box8.x + self.inner_magrin * 2 + self.achv_icon_size, self.box8.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv8_date, (self.box8.x + self.inner_magrin * 2 + self.achv_icon_size, self.box8.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적9 정보 출력
        if self.achv_info[9] == "None":
            achv9_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv9_icon, (self.box9.x + self.inner_magrin, self.box9.y + self.inner_magrin))
            self.lock9_rect.x = self.box9.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock9_rect.y = self.box9.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock9_icon, self.lock9_rect)
        else:
            achv9_date = self.desc_font.render(f"{self.achv_info[9]}", True, BCOLOR)
            self.screen.blit(self.achv9_icon, (self.box9.x + self.inner_magrin, self.box9.y + self.inner_magrin))
            
        self.screen.blit(self.achv9_title, (self.box9.x + self.inner_magrin * 2 + self.achv_icon_size, self.box9.y + self.inner_magrin))
        self.screen.blit(self.achv9_desc1, (self.box9.x + self.inner_magrin * 2 + self.achv_icon_size, self.box9.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv9_desc2, (self.box9.x + self.inner_magrin * 2 + self.achv_icon_size, self.box9.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv9_date, (self.box9.x + self.inner_magrin * 2 + self.achv_icon_size, self.box9.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적10 정보 출력
        if self.achv_info[10] == "None":
            achv10_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv10_icon, (self.box10.x + self.inner_magrin, self.box10.y + self.inner_magrin))
            self.lock10_rect.x = self.box10.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock10_rect.y = self.box10.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock10_icon, self.lock10_rect)
        else:
            achv10_date = self.desc_font.render(f"{self.achv_info[10]}", True, BCOLOR)
            self.screen.blit(self.achv10_icon, (self.box10.x + self.inner_magrin, self.box10.y + self.inner_magrin))
            
        self.screen.blit(self.achv10_title, (self.box10.x + self.inner_magrin * 2 + self.achv_icon_size, self.box10.y + self.inner_magrin))
        self.screen.blit(self.achv10_desc1, (self.box10.x + self.inner_magrin * 2 + self.achv_icon_size, self.box10.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv10_desc2, (self.box10.x + self.inner_magrin * 2 + self.achv_icon_size, self.box10.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(achv10_date, (self.box10.x + self.inner_magrin * 2 + self.achv_icon_size, self.box10.y + self.inner_magrin + self.screen_size[1] * 0.117))
        
        # 업적11 정보 출력
        if self.achv_info[11] == "None":
            achv11_date = self.desc_font.render("미달성", True, BCOLOR)
            self.screen.blit(self.bw_achv11_icon, (self.box11.x + self.inner_magrin, self.box11.y + self.inner_magrin))
            self.lock11_rect.x = self.box11.x + self.inner_magrin + self.screen_size[0] * 0.021665
            self.lock11_rect.y = self.box11.y + self.inner_magrin + self.screen_size[0] * 0.021665
            self.screen.blit(self.lock11_icon, self.lock11_rect)
        else:
            achv11_date = self.desc_font.render(f"{self.achv_info[11]}", True, BCOLOR)
            self.screen.blit(self.achv11_icon, (self.box11.x + self.inner_magrin, self.box11.y + self.inner_magrin))
            
        self.screen.blit(self.achv11_title, (self.box11.x + self.inner_magrin * 2 + self.achv_icon_size, self.box11.y + self.inner_magrin))
        self.screen.blit(self.achv11_desc1, (self.box11.x + self.inner_magrin * 2 + self.achv_icon_size, self.box11.y + self.inner_magrin + self.screen_size[1] * 0.04))
        self.screen.blit(self.achv11_desc2, (self.box11.x + self.inner_magrin * 2 + self.achv_icon_size, self.box11.y + self.inner_magrin + self.screen_size[1] * 0.065))
        self.screen.blit(self.achv11_desc3, (self.box11.x + self.inner_magrin * 2 + self.achv_icon_size, self.box11.y + self.inner_magrin + self.screen_size[1] * 0.09))
        self.screen.blit(achv11_date, (self.box11.x + self.inner_magrin * 2 + self.achv_icon_size, self.box11.y + self.inner_magrin + self.screen_size[1] * 0.117))

        # 뒤로가기 아이콘 출력
        self.screen.blit(self.back_icon, (self.screen_size[0] // 100, self.screen_size[0] // 100))     
        pygame.display.flip()
        
        
    def run(self):
        running = True
        while running:
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # ESC키
                        running = False
                        main.main(self.screen_size[0], self.screen_size[1], self.color_blind_mode)    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.back_rect.collidepoint(pos):
                        running = False
                        main.main(self.screen_size[0], self.screen_size[1], self.color_blind_mode)        
            

