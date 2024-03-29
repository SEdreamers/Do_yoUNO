## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면 전환. 
import pygame
import setting 
import json
import time
import storyMap
import lobby
import acheivementList
from pygame.locals import *

# 색상 상수 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def main(screen_width = 800, screen_height = 600, color_blind_mode = False):
    pygame.init()
    try:
        with open('setting_data.json') as game_file:
            data = json.load(game_file)
            color = data['color_blind_mode']     ## 저장된 값 불러오기. 
            size = data["size"]
        screen = pygame.display.set_mode((size[0],size[1]))
        screen_width = size[0]
        screen_height = size[1]
        font = pygame.font.SysFont("arial", size[0] // 20, True)
        if data["AWDS"] == True:
            key_up = pygame.K_w
            key_down = pygame.K_s
        else:
            key_up = pygame.K_UP
            key_down = pygame.K_DOWN
        
    except: 
        print("No file created yet!")
        set = setting.Setting(screen_width,screen_height)
        set.save_game()
        screen = pygame.display.set_mode((screen_width, screen_height))
        font = pygame.font.SysFont("arial", screen_width // 20, True)

    # 화면 생성
    pygame.display.set_caption("Uno Game")

    # 메뉴 텍스트 생성
    game_title = font.render("Uno Game", True, WHITE)
    single_player_text = font.render("Play Mode", True, RED)
    story_mode_text = font.render("Story Mode", True, WHITE)
    settings_text = font.render("Settings", True, WHITE)
    achv_text = font.render("Acheivments", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)

    # 메뉴 위치 설정
    game_title_rect = game_title.get_rect()
    game_title_rect.centerx = screen.get_rect().centerx
    game_title_rect.y = screen.get_size()[1] // 12
    
    start_y = 0.25 # 메뉴 출력 시작 y값
    interval = 0.14 # 메뉴 간격

    single_player_rect = single_player_text.get_rect()
    single_player_rect.centerx = screen.get_rect().centerx
    single_player_rect.y = screen.get_size()[1] * start_y
    
    story_mode_rect = story_mode_text.get_rect()
    story_mode_rect.centerx = screen.get_rect().centerx
    story_mode_rect.y = screen.get_size()[1] * (start_y + interval)

    settings_rect = settings_text.get_rect()
    settings_rect.centerx = screen.get_rect().centerx
    settings_rect.y = screen.get_size()[1] * (start_y + interval * 2)
    
    achv_rect = achv_text.get_rect()
    achv_rect.centerx = screen.get_rect().centerx
    achv_rect.y = screen.get_size()[1] * (start_y + interval * 3)

    exit_rect = exit_text.get_rect()
    exit_rect.centerx = screen.get_rect().centerx
    exit_rect.y = screen.get_size()[1] * (start_y + interval * 4)

    #메뉴 상수
    menu_flag = 0

    # 게임 루프
    play = True
    
    while play: 
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 play = False
            if event.type == pygame.KEYDOWN:
                if event.key == key_up:
                    menu_flag -= 1
                elif event.key == key_down:
                    menu_flag += 1
                elif event.key == 13:
                    if menu_flag == 0:
                        lobbystate = lobby.Lobby(size[0], size[1], color)
                        lobbystate.displayPlayer()
                    elif menu_flag == 1:
                        story_mode = storyMap.StoryMap(size[0], size[1])
                        story_mode.run()
                    elif menu_flag == 2:
                        set = setting.Setting(size[0], size[1])
                        set.run(size[0], size[1])
                    elif menu_flag == 3:
                        achv_screen = acheivementList.AcheivementList(size[0], size[1], color_blind_mode)
                        achv_screen.run()
                    elif menu_flag == 4:
                        play = False

            menu_flag %= 5
        
        # 마우스 이벤트 처리
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # mouse_focused = pygame.mouse.get_focused()
        
        # 메뉴 시각화
        if single_player_rect.collidepoint(mouse_pos) or menu_flag == 0:
            single_player_text = font.render("Play Game", True, RED)
        else:
            single_player_text = font.render("Play Game", True, WHITE)
            
        if story_mode_rect.collidepoint(mouse_pos) or menu_flag == 1:
            story_mode_text = font.render("Story Mode", True, RED)
            single_player_text = font.render("Play Game", True, WHITE)
        else:
            story_mode_text = font.render("Story Mode", True, WHITE)
            
            
        if settings_rect.collidepoint(mouse_pos) or menu_flag == 2:
            settings_text = font.render("Settings", True, RED)
            single_player_text = font.render("Play Game", True, WHITE)
        else:
            settings_text = font.render("Settings", True, WHITE)
        if achv_rect.collidepoint(mouse_pos) or menu_flag == 3:
            achv_text = font.render("Acheivements", True, RED)
            single_player_text = font.render("Play Game", True, WHITE)
        else:
            achv_text = font.render("Acheivements", True, WHITE)
        if exit_rect.collidepoint(mouse_pos) or menu_flag == 4:
            exit_text = font.render("Exit", True, RED)
            single_player_text = font.render("Play Game", True, WHITE)
        else:
            exit_text = font.render("Exit", True, WHITE)
            

            
        # 마우스 클릭 시
        if single_player_rect.collidepoint(mouse_pos) and mouse_click[0]:

            
            lobbystate = lobby.Lobby(size[0],size[1], color)
            lobbystate.displayPlayer() 
        elif story_mode_rect.collidepoint(mouse_pos) and mouse_click[0]:
            story_mode = storyMap.StoryMap(size[0], size[1])
            story_mode.run()
        elif settings_rect.collidepoint(mouse_pos) and mouse_click[0]:
            time.sleep(0.5)
            set = setting.Setting(size[0],size[1])
            set.run(size[0], size[1])
        elif achv_rect.collidepoint(mouse_pos) and mouse_click[0]:
            achv_screen = acheivementList.AcheivementList(size[0], size[1], color_blind_mode)
            while True:
                achv_screen.run()
        elif exit_rect.collidepoint(mouse_pos) and mouse_click[0]:
            play = False


        # 화면 그리기
        screen.fill(BLACK)
        screen.blit(game_title, game_title_rect)
        screen.blit(single_player_text, single_player_rect)
        screen.blit(story_mode_text, story_mode_rect)
        screen.blit(settings_text, settings_rect)
        screen.blit(exit_text, exit_rect)
        screen.blit(achv_text, achv_rect)

        pygame.display.update()
    pygame.quit()
if __name__=='__main__':
    main()

