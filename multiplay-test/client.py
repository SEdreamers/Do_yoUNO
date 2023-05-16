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

class Client:
    def __init__(self, screen):
        self.screen = screen
        
    def menu_screen(self):
        pygame.font.init()

        width = 700
        height = 700
        win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Client")
        run = True
        clock = pygame.time.Clock()   # 시간 동기화

        try:
            with open('setting_data.json') as game_file:
                lst = json.load(game_file)
        except:
            lst = {
                "color_blind_mode": False,
                "size": (800, 600),
                "Total_Volume": 0.3,
                "Background_Volume": 0.3,
                "Sideeffect_Volume": 0.3,
                "player_numbers": 3,
                "me": 'player',
                "c1name": 'computer1',
                "c2name": 'computer2',
                "c3name": 'computer3',
                "c4name": 'computer4',
                "c5name": 'computer5',
                "unclicked_list": [],
                "characters": []
            }

        while run:
            clock.tick(60)                          # 프레임 속도 제한
            font = pygame.font.SysFont("arial", 60, True)
            text = font.render("Click to Play!", 1, (255,0,0))
            win.blit(text, (200,200))
            pygame.display.update()
        

            for event in pygame.event.get():                           #  게임 종료 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    print(lst)
                    uno_game = game_logic.Game(lst["size"][0], lst["size"][1], lst["color_blind_mode"],
                                               lst["player_numbers"])
                    with open('game_data.pickle', 'wb') as f:
                        send_deck = uno_game.deck.to_list()
                        send_players = []
                        for player in uno_game.players:
                            send_player = player.to_list()
                            send_players.append(send_player)
                        print(send_players)
                        data = (send_deck, send_players, uno_game.turn_num, uno_game.reverse, uno_game.skip, uno_game.start_time)
                        pickle.dump(data, f)
                    

                    
                    while True:
                        with open('game_data.pickle', 'rb') as f:
                            data = pickle.load(f)
                            deck, players, turn_num, reverse, skip, start_time = data
                            deck = Deck.from_list(lst["size"][0], lst["size"][1], deck)

                        real_players = [] 
                        for idx, player in enumerate(players):
                            if idx == 0:
                                real_player = hm.Human.from_list(self.screen, deck, False, 'Z', player)
                            else:
                                real_player = Computer.from_list(self.screen, deck, idx, 'Z', player)
                            real_players.append(real_player)
                        uno_game.run(deck, real_players, turn_num, reverse, skip, start_time)

    4
if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))  # 시작
    client = Client(screen)
    client.menu_screen()
