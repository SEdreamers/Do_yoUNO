import pygame
import socket
import pickle
import json
import game_logic
import computer as Computer
import human as hm
from deck import Deck
from player import Player
import threading
import queue

class Client:
    def __init__(self, host, port, screen, name):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = int(port)
        self.sock.connect((self.host, self.port))
        self.name = name
        print(f"Client started on {self.host}:{self.port}")
        self.running = False
        # Initialize pygame and the game display here...
        self.screen = screen
        self.current_state = None
        self.listen_thread = threading.Thread(target=self.listen_to_server)
        self.listen_thread.daemon = True
        self.listen_thread.start()
        self.queue = queue.Queue()
        try:
            with open('setting_data.json') as game_file:
                self.lst = json.load(game_file)
        except:
            self.lst = {
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

    def listen_to_server(self):
        while True:
            data = self.sock.recv(1024)
            print("listen_to_server")
            self.queue.put(data)

    def game_loop(self):
        if not self.queue.empty():
            self.update(self.queue.get())
            print("updated")
        if self.current_state is not None:
            print("start")
            self.current_state.run()
        pygame.time.delay(33)  # to limit the frame rate to 30 fps

    def update(self, data):
        with open('game_data.pickle', 'rb') as f:
            data = pickle.load(f)
            deck, players, turn_num, reverse, skip, start_time = data
            deck = Deck.from_list(self.lst["size"][0], self.lst["size"][1], deck)
        print(f"{data}")
        real_players = [] 
        for idx, player in enumerate(players):
            if idx == 0:
                real_player = hm.Human.from_list(self.screen, deck, False, 'Z', player)
            else:
                real_player = Computer.from_list(self.screen, deck, idx, 'Z', player)
        real_players.append(real_player)
        uno_game = game_logic.Game(self.lst["size"][0], self.lst["size"][1], self.lst["color_blind_mode"],
                                               self.lst["player_numbers"])
        uno_game.run(deck, real_players, turn_num, reverse, skip, start_time)
        

    def serialize_data(self, data):
        return pickle.dumps(data)

    def deserialize_data(self, data):
        return pickle.loads(data)
