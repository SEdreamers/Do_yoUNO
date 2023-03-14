import pygame

# 게임 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색상 상수 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def main():
    pygame.init()

    # 화면 생성
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Uno Game")

    # 폰트 생성
    font = pygame.font.SysFont("arial", SCREEN_WIDTH // 16, True, True)

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
    single_player_rect.y = 250

    settings_rect = settings_text.get_rect()
    settings_rect.centerx = screen.get_rect().centerx
    settings_rect.y = 350

    exit_rect = exit_text.get_rect()
    exit_rect.centerx = screen.get_rect().centerx
    exit_rect.y = 450

    # 게임 루프
    play = True
    while play:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 play = False

        # 화면 그리기
        screen.fill(BLACK)
        screen.blit(game_title, game_title_rect)
        screen.blit(single_player_text, single_player_rect)
        screen.blit(settings_text, settings_rect)
        screen.blit(exit_text, exit_rect)

        # 마우스 이벤트 처리
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        mouse_focused = pygame.mouse.get_focused()

        # 키보드 이벤트 처리
        menu_flag = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu_flag += 1
            elif event.type == pygame.KEYUP:
                menu_flag -= 1
            if menu_flag < 0:
                menu_flag = 2
            elif menu_flag > 2:
                menu_flag = 0
        
        # 싱글 플레이어 게임 선택
        if single_player_rect.collidepoint(mouse_pos) and mouse_click[0]:
            print("Single Player")
        if single_player_rect.collidepoint(mouse_pos) and mouse_focused:
            single_player_text = font.render("Single Player", True, RED)
        else:
            single_player_text = font.render("Single Player", True, WHITE)

        # 설정 선택
        if settings_rect.collidepoint(mouse_pos) and mouse_click[0]:
            print("Settings")
        if settings_rect.collidepoint(mouse_pos) and mouse_focused:
            settings_text = font.render("Settings", True, RED)
        else:
            settings_text = font.render("Settings", True, WHITE)

        # 종료 선택
        if exit_rect.collidepoint(mouse_pos) and mouse_click[0]:
            play = False
        if exit_rect.collidepoint(mouse_pos) and mouse_focused:
            exit_text = font.render("Exit", True, RED)
        else:
            exit_text = font.render("Exit", True, WHITE)

        pygame.display.flip()

    # Pygame 종료
    pygame.quit()

if __name__=='__main__':
    main()