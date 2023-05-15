import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pygame
from network import Network
import gamedisplay
import game_logic
import json
import pickle 
from card import Card  
from player import Player
from computer import Computer
import human as hm 
from deck import Deck


pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


try:
    with open('setting_data.json') as game_file:
        lst = json.load(game_file)
except: 
    lst ={
    "color_blind_mode": False,
    "size": (800,600),
    "Total_Volume": 0.3,
    "Background_Volume": 0.3,
    "Sideeffect_Volume": 0.3,
    "player_numbers":3,
    "me": 'player',
    "c1name" :'computer1',
    "c2name" :'computer2',
    "c3name" :'computer3',
    "c4name" :'computer4',
    "c5name" :'computer5',
    "unclicked_list": [],
    "characters" : []
    }

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):            # 버튼 출력 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):           # 클릭 여부
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, p):      ## 화면 출력 
    win.fill((128,128,128))

    if not(game.connected()):
        print(1)
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        
        
        
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 255,255))
        win.blit(text, (80, 200))

        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]






## 여기가 존나게 반복되고 있음. 
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255,0,0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)
class Client:
    def __init__(self, screen):
        self.screen = screen
    def menu_screen(self):
        run = True
        clock = pygame.time.Clock()                 # 시간 동기화

        while run:
            clock.tick(60)                          # 프레임 속도 제한



            uno_game = game_logic.Game(lst["size"][0],lst["size"][1], lst["color_blind_mode"], lst["player_numbers"]) 
            with open('game_data.pickle', 'wb') as f:
                send_deck = uno_game.deck.to_list()
                send_players = []
                for player in uno_game.players:
                    send_player = player.to_list()
                    send_players.append(send_player)
                print(send_players)
                # send_turn_num = uno_game.turn_num.to_list()
                data = (send_deck, send_players, uno_game.turn_num, uno_game.reverse, uno_game.skip, uno_game.start_time)
                pickle.dump(data, f)
            

            with open('game_data.pickle', 'rb') as f:
                data = pickle.load(f)
                deck, players, turn_num, reverse, skip, start_time = data
                deck = Deck.from_list(lst["size"][0],lst["size"][1], deck)
                real_players = [] 
                
                for idx, player in enumerate(players):
                    if idx == 0:
                        real_player = hm.Human.from_list(self.screen, deck, False, 'Z', player)
                    else:
                        real_player = Computer.from_list(self.screen, deck, idx, 'Z', player)
                    real_players.append(real_player)

                # print(deck)
                # print(players)
            uno_game.run(deck, real_players, turn_num, reverse, skip, start_time)



            # win.fill((128, 128, 128)) 
            # font = pygame.font.SysFont("comicsans", 60)
            # text = font.render("Click to Play!", 1, (255,0,0))
            # win.blit(text, (100,200))
            # pygame.display.update()

            for event in pygame.event.get():                           #  게임 종료 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False

        main()
    screen = pygame.display.set_mode((800, 600))
    while True:               # 시작 
        menu_screen(screen)
