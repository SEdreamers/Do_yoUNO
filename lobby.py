import pygame
from player import Player
import computer 
import json
import game

class Lobby():
    def __init__(self, screen_width, screen_height, color_blind_mode):

        # Set up the game screen
        self.screen_size = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.color_blind_mode = color_blind_mode 
         

        # Get the dimensions of the computer's image  사이즈
        self.computer_width = self.screen_size[0] / 3.333
        self.computer_height = self.screen_size[1] / 5

        # Load the computer's image   
        self.computer_image = pygame.image.load("images/gray.jpg")
        self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))

        # Load the image 
        self.computer_background_image = pygame.image.load("images/black.jpg")
        self.computer_background_image = pygame.transform.scale(self.computer_background_image, (self.computer_width, self.screen_size[1]))
    
        self.running = True
        



    def displayPlayer(self, players):
        ## Draw the background image
        self.screen.blit(self.computer_background_image, (self.screen_size[0] - self.computer_width, 0))
        
        

        ##?? 이거 되나? 
        ## Draw the computer's image on the screen (computer는 0번 자리 부터 -> i - 1)
        computer_x = self.screen_size[0] - self.computer_width
        computer_y = 0
        self.screen.blit(self.computer_image, (computer_x, computer_y + 5 * self.computer_height))


        
        # for i in range(1, len(players)):
        #     players[i].draw(i - 1)
        

        with open('setting_data.json') as game_file:
            data = json.load(game_file)
            color = data['color_blind_mode']     ## 저장된 값 불러오기. 
            size = data["size"]



        ## Player 수 입력받기
        font = pygame.font.SysFont("arial", size[0] // 40, True) 
        player_numbers = ""
        
        c1name = ""
        c2name = ""
        c3name = ""
        c4name = ""
        c5name = ""

        input_active = True     # 사용자 이름 입력 상태 여부
        blink_timer = 0         # 깜빡이는 커서 타이머
        cursor_visible = True   # 커서 가시성 상태


        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if input_active:  # 사용자 이름 입력 상태일 때만 입력 받기
                        if event.key == pygame.K_BACKSPACE:
                            player_numbers = player_numbers[:-1]  # 백스페이스 키 입력 처리
                        elif event.key == pygame.K_RETURN:
                            input_active = False  # 엔터 키 입력 처리 후 사용자 이름 입력 상태 해제
                        else: player_numbers += event.unicode  # 다른 키 입력 처리
                        



            # 깜빡이는 커서 타이머 업데이트
            blink_timer += pygame.time.get_ticks() / 2 
            if blink_timer >= 500:  # 0.5초마다 커서 가시성 상태 변경
                cursor_visible = not cursor_visible
                blink_timer = 0

            # 화면에 이름과 커서 출력
            self.screen.fill((0,0,0))    ##검은색 바탕
            if input_active:
                text_surface = font.render("Enter Player Numbers(1~5): " + player_numbers, True, (255,255,255))
                self.screen.blit(text_surface, (100, 100))  # 화면에 텍스트 출력
                if cursor_visible:  # 커서 가시성에 따라 커서 출력
                    pygame.draw.rect(self.screen, (255, 0, 0), (100 + text_surface.get_width(), 100, 2, text_surface.get_height()))
            else:
                text_surface = font.render("Wrong! Choose Again!" + player_numbers, True, (255,255,255))
                self.screen.blit(text_surface, (100, 100))  # 화면에 텍스트 출력

                # computer_name = computer.Computer()


                uno_game = game.Game(size[0],size[1], color,int(player_numbers))  
                uno_game.run()

        # Update the display
            pygame.display.update()
        # Quit Pygame
        pygame.quit()




# class Computer(Player):
#     def __init__(self, screen, deck, i, region):
#         super().__init__("Computer" + str(i), screen, deck, region)
#         self.screen = screen
#         self.screen_size = (screen.get_width(), screen.get_height())
#         # Get the dimensions of the computer's image
#         self.computer_width = self.screen_size[0] / 3.333
#         self.computer_height = self.screen_size[1] / 5
#         # Load the computer's image
#         self.computer_image = pygame.image.load("images/gray.jpg")
#         self.computer_image = pygame.transform.scale(self.computer_image, (self.computer_width, self.computer_height))
#         self.backcard_image = pygame.image.load("images/card.png")
#         self.backcard_image = pygame.transform.scale(self.backcard_image, (self.screen_size[0] / 12.5, self.screen_size[0] / 8.333))


#         font = pygame.font.SysFont("arial", self.screen_size[0]//40, True)
#         # create computer name 
#         self.c1name = font.render("computer1",True,'GREEN')      ## 이름 받는 부분
#         self.c1name_rect = self.c1name.get_rect()
#         self.c2name = font.render("computer2",True,'GREEN')      ## 이름 받는 부분
#         self.c2name_rect = self.c2name.get_rect()
#         self.c3name = font.render("computer3",True,'GREEN')      ## 이름 받는 부분
#         self.c3name_rect = self.c3name.get_rect()


#     def draw(self, i):      ## 컴퓨터 플레이어 수만큼 호출
#         # Set the position of the computer's image on the right side of the screen
#         computer_x = self.screen_size[0] - self.computer_width
#         computer_y = 0
#         self.screen.blit(self.computer_image, (computer_x, computer_y + i * self.computer_height))

#         N = Player.count_cards(self)
#         for x in range(N):
#             self.screen.blit(self.backcard_image,(computer_x+ x*self.computer_height*0.1, computer_y + i * self.computer_height))

#         # 컴퓨터 이름 화면에 띄우는 부분. 
#         if i == 0: 
#             self.c1name_rect.x, self.c1name_rect.y = computer_x, i * self.computer_height
#             self.screen.blit(self.c1name,self.c1name_rect)
#         elif i == 1: 
#             self.c2name_rect.x, self.c2name_rect.y = computer_x, i * self.computer_height
#             self.screen.blit(self.c2name,self.c2name_rect)
#         elif i == 2: 
#             self.c3name_rect.x, self.c3name_rect.y = computer_x, i * self.computer_height
#             self.screen.blit(self.c3name,self.c3name_rect)

    