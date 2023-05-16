import socket
import threading
import json
import game_logic
import json
import pickle 
from deck import Deck
from computer import Computer
from human import Human

class Server:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, int(port)))
        self.sock.listen(1)
        # make game
        self.clients = []

    def send_game_state(self):
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
        uno_game = game_logic.Game(lst["size"][0], lst["size"][1], lst["color_blind_mode"],
                                               lst["player_numbers"])
        with open('game_data.pickle', 'wb') as f:
            send_deck = uno_game.deck.to_list()
            send_players = []
            for player in uno_game.players:
                send_player = player.to_list()
                send_players.append(send_player)
            data = (send_deck, send_players, uno_game.turn_num, uno_game.reverse, uno_game.skip, uno_game.start_time)
            pickle.dump(data, f)
            self.broadcast(f)

    def broadcast(self, msg):
        for client in self.clients:
            client.sendall(msg)

    def handle_client(self):
        messages = []
        for client in self.clients:
            msg = client.recv(1024)
            messages.append(msg)
        self.broadcast(messages[0])

    def start(self):
        print("Server started...")
        while True:
            client, addr = self.sock.accept()
            print("server_working")
            self.clients.append(client)
            # self.game_logic.players.append("")
            print(client.getpeername())
            threading.Thread(target=self.handle_client, args=(client,)).start()

    