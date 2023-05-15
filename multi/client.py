import pygame
import socket
import json
from game_logic import GameLogic
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

    def listen_to_server(self):
        while True:
            data = self.sock.recv(1024)
            print("listen_to_server")
            self.queue.put(data)

    def game_loop(self):
        if not self.queue.empty():
            self.update(self.queue.get())
            print("updated")
        print("game_loop")
        if self.current_state is not None:
            print("start")
            self.current_state.run()
        pygame.display.flip()
        pygame.time.delay(33)  # to limit the frame rate to 30 fps

    def update(self, data):
        state = self.deserialize_data(data)
        print(f"{state}")
        text_deck = state['deck']
        deck = Deck.from_list(self.screen.get_width(), self.screen.get_height(), text_deck)
        players = []
        text_player = state['players']

        for player in text_player:
            real_player = Player(self.name, self.screen, deck, 'E', False)
            print(player)
            real_player.from_list(self.name, self.screen, deck, 'E', False, player)
            players.append(real_player)

        turn_num = int(state['turn_num'])
        reverse = int(state['reverse'])
        try:
            self.current_state = GameLogic(self.screen.get_width(), self.screen.get_height(), False, 0, deck,
                                           players, turn_num, reverse, False, "E")

            print(self.client)
            print(self.current_state)
        except Exception as e:
            print("Error creating GameLogic:", str(e))

    def serialize_data(self, data):
        return json.dumps(data).encode('utf-8')

    def deserialize_data(self, data):
        return json.loads(data.decode('utf-8'))
