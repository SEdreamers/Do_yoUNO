## # 이벤트 처리, # 마우스 클릭 시 에 추가해야 화면 전환. 
import pygame
import game
import setting 
import json


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
    except: pass 
    
    # 화면 생성
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Uno Game")

    # 폰트 생성
    font = pygame.font.SysFont("arial", screen_width // 20, True)

    # 메뉴 텍스트 생성
    game_title = font.render("Uno Game", True, WHITE)
    single_player_text = font.render("Single Player", True, RED)
    settings_text = font.render("Settings", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)

    # 메뉴 위치 설정
    game_title_rect = game_title.get_rect()
    game_title_rect.centerx = screen.get_rect().centerx
    game_title_rect.y = screen.get_size()[1] // 12

    single_player_rect = single_player_text.get_rect()
    single_player_rect.centerx = screen.get_rect().centerx
    single_player_rect.y = screen.get_size()[1] / 2.4

    settings_rect = settings_text.get_rect()
    settings_rect.centerx = screen.get_rect().centerx
    settings_rect.y = screen.get_size()[1] / 1.714

    exit_rect = exit_text.get_rect()
    exit_rect.centerx = screen.get_rect().centerx
    exit_rect.y = screen.get_size()[1] / 1.333

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
                if event.key == pygame.K_UP:
                    menu_flag -= 1
                elif event.key == pygame.K_DOWN:
                    menu_flag += 1
                elif event.key == 13:
                    if menu_flag == 0:
                        uno_game = game.Game(screen_width, screen_height, color_blind_mode)
                        uno_game.run()
                    elif menu_flag == 1:
                        set = setting.Setting(screen_width, screen_height)
                        set.run(screen_width, screen_height)
                    elif menu_flag == 2:                        
                        play = False
            menu_flag %= 3


        # 화면 그리기
        screen.fill(BLACK)
        screen.blit(game_title, game_title_rect)
        screen.blit(single_player_text, single_player_rect)
        screen.blit(settings_text, settings_rect)
        screen.blit(exit_text, exit_rect)

        # 마우스 이벤트 처리
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        # mouse_focused = pygame.mouse.get_focused()
        
        # 메뉴 시각화
        if single_player_rect.collidepoint(mouse_pos) or menu_flag == 0:
            single_player_text = font.render("Single Player", True, RED)
        else:
            single_player_text = font.render("Single Player", True, WHITE)
        if settings_rect.collidepoint(mouse_pos) or menu_flag == 1:
            settings_text = font.render("Settings", True, RED)
        else:
            settings_text = font.render("Settings", True, WHITE)
        if exit_rect.collidepoint(mouse_pos) or menu_flag == 2:
            exit_text = font.render("Exit", True, RED)
        else:
            exit_text = font.render("Exit", True, WHITE)



        # 마우스 클릭 시
        if single_player_rect.collidepoint(mouse_pos) and mouse_click[0]:
            uno_game = game.Game(screen_width, screen_height, color_blind_mode)
            uno_game.run()
        elif settings_rect.collidepoint(mouse_pos) and mouse_click[0]:
            set = setting.Setting(screen_width, screen_height)
            set.run(screen_width, screen_height)
        elif exit_rect.collidepoint(mouse_pos) and mouse_click[0]:
            play = False

        pygame.display.update()
    pygame.quit()
if __name__=='__main__':
    main()





