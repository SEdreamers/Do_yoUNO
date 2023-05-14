import socket
import threading
import json

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
        deck = Deck(800, 600)
        deck = deck.to_list()
        players = []
        numberofPlayers = 1

        computers = []
        for i in range(numberofPlayers):
            cards = []
            for j in range(5):
                card = deck.pop()
                cards.append(card)
            computers.append(cards)
        players.extend(computers)
        # human player 만들기!
        cards = []
        for i in range(5):
            card = deck.pop()
            cards.append(card)
        players.append(cards)
        turn_num = 0
        reverse = 1
        state = {
            'deck': deck,  # Assuming your Deck class has a serialize method
            'players': players,
            'turn_num': f"{turn_num}",
            'reverse': f'{reverse}'
        }
        data = self.serialize_data(state)
        self.broadcast(data)
        print('broadcast')

    def broadcast(self, msg):
        for client in self.clients:
            client.sendall(msg)

    def handle_client(self, client):
        msg = client.recv(1024)
        self.broadcast(msg)

    def start(self):
        print("Server started...")
        while True:
            client, addr = self.sock.accept()
            print("server_working")
            self.clients.append(client)
            # self.game_logic.players.append("")
            print(client.getpeername())
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def serialize_data(self, data):
        return json.dumps(data).encode('utf-8')

    def deserialize_data(self, data):
        return json.loads(data.decode('utf-8'))
