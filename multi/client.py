import pygame
import socket
import json
from game_logic import GameLogic
from deck import Deck
from player import Player
import threading

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
        self.game_thread = threading.Thread(target=self.game_loop)
        self.game_thread.daemon = True
        self.listen_thread = threading.Thread(target=self.listen_to_server)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def listen_to_server(self):
        while True:
            self.update()
    def game_loop(self):
        if self.current_state is not None:
            self.current_state.run()


    def update(self):
        data = self.sock.recv(1024)
        state = self.deserialize_data(data)
        print("update")
        text_deck = state['deck']
        deck = Deck.from_list(self.screen.get_width(), self.screen.get_height(), text_deck)
        players = []
        text_player = state['players']

        for player in text_player:
            real_player = Player(self.name, self.screen, deck, False)
            real_player.from_list(self.name, self.screen, deck, 'E', 'E', player)
            players.append(real_player)

        turn_num = state['turn_num']
        reverse = state['reverse']
        self.current_state = GameLogic(self.screen.get_width(), self.screen.get_height(),
                                       deck, players, turn_num, reverse, "E")
        self.game_thread.start()


    def serialize_data(self, data):
        return json.dumps(data).encode('utf-8')

    def deserialize_data(self, data):
        return json.loads(data.decode('utf-8'))

