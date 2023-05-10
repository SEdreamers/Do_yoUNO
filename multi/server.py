import socket
import threading
import json
from network import Network

class Server:
    def __init__(self, host, port, max_clients=4):
        self.network = Network(host, port)
        self.server_socket = self.network.create_server_socket()
        self.max_clients = max_clients
        self.clients = []

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