import pygame
from player import Player
import computer 


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
        ## Draw the computer's image on the screen (computer는 0번 자리 부터 -> i - 1)
        
        
        # for i in range(1, len(players)):
        #     players[i].draw(i - 1)

        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


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

    