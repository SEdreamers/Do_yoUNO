import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import socket
import threading
from network import Network
from deck import Deck
import pickle 
from player import Player
import pygame



class Server:
    def __init__(self, host, port, max_clients=4):
        self.deck = Deck(800,600)
        self.screen = pygame.display.set_mode((800,600))
        self.players = Player("name",self.screen,self.deck,'E')
        self.turn_num = 1
        
        self.network = Network(host, port)
        self.server_socket = self.network.create_server_socket()
        self.max_clients = max_clients  
        self.clients = []
        

        self.data = {
        "deck": self.deck,
        "players": self.players,
        "turn_num": self.turn_num
        }
        f = open("test.pkl","wb")
        pickle.dumps(self.data,f)
        f.close() 
        
        
        
    def update(self):
        self.start() 
        
        
        
        
    def start(self):
        self.server_socket.listen(self.max_clients)
        print(f"Server started on {self.network.host}:{self.network.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Client connected from {client_address}")
            self.clients.append(client_socket)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = self.network.receive_message(client_socket)
                
                self.deck = message['deck']
                self.players = message['players']
                self.turn_num = message['turn_num']
                
                self.data = {
                "deck": self.deck,
                "players": self.players,
                "turn_num": self.turn_num
                }
                self.network.send_message(client_socket,self.data)
                
                
                if message:
                    print(f"Received message: {message}")
                    # Process the message, update the game state, and broadcast updates to all clients
                    self.broadcast_message(message)
                else:
                    break
            except socket.error:
                break


        print("Client disconnected")
        client_socket.close()
        self.clients.remove(client_socket)
        
    def broadcast_message(self, message):
        for client_socket in self.clients:
            self.network.send_message(client_socket, message)