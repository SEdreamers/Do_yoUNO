import pygame
import game
import sys

BLACK = (0, 0, 0)

class GameOverUI:
    def __init__(self, screen_width, screen_height, winner, color_blind_mode):
        self.menu_flag = 0

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
        self.new_game_text = self.font.render("New Game", True, 'white')
        self.new_game_rect = self.new_game_text.get_rect()
        self.new_game_rect.centerx = self.screen.get_rect().centerx
        self.new_game_rect.y = self.screen.get_size()[1] / 1.714

        # exit 버튼
        self.exit_text = self.font.render("Exit", True, 'white')
        self.exit_rect = self.exit_text.get_rect()
        self.exit_rect.centerx = self.screen.get_rect().centerx
        self.exit_rect.y = self.screen.get_size()[1] / 1.4
        
        self.frame_index = 0 # gif frame index

        self.uno_game = game.Game(self.screen_size[0], self.screen_size[1], self.color_blind_mode,4)

    def display(self):
        pygame.display.set_caption("Game Over")
        self.screen.fill(BLACK)
        
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
                        self.uno_game.run()
                    elif self.menu_flag == 1:
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            self.menu_flag %= 2

        # 메뉴 시각화(색상 변경)
        if self.new_game_rect.collidepoint(mouse_pos) or self.menu_flag == 0:
            self.new_game_text = self.font.render("New Game", True, 'red')
            self.exit_text = self.font.render("Exit", True, 'white')
        else:
            self.new_game_text = self.font.render("New Game", True, 'white')

        if self.exit_rect.collidepoint(mouse_pos) or self.menu_flag == 1:
            self.exit_text = self.font.render("Exit", True, 'red')
            self.new_game_text = self.font.render("New Game", True, 'white')
        else:
            self.exit_text = self.font.render("Exit", True, 'white')
    
        # 메뉴 동작
        if self.new_game_rect.collidepoint(mouse_pos) and mouse_click:
            self.uno_game.run() # 새 게임 불러오기
        elif self.exit_rect.collidepoint(mouse_pos) and mouse_click:
            sys.exit() # 종료
        pygame.display.flip()


