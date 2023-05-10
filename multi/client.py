import socket
import threading
from network import Network

class Client:
    def __init__(self, host, port):
        self.network = Network(host, port)
        self.client_socket = self.network.create_client_socket()

    def connect(self):
        try:
            self.client_socket.connect((self.network.host, self.network.port))
            print(f"Connected to the server {self.network.host}:{self.network.port}")

            listen_thread = threading.Thread(target=self.listen_for_messages)
            listen_thread.start()

            # Connect to the game, initialize the GameUI, and run the game loop

        except socket.error as e:
            print(f"Connection error: {e}")

    def listen_for_messages(self):
        while True:
            try:
                message = self.network.receive_message(self.client_socket)
                if message:
                    print(f"Received message: {message}")
                    # Update the game state based on the received message
                else:
                    break
            except socket.error:
                break

        print("Disconnected from the server")
        self.client_socket.close()

    def send_message(self, message):
        self.network.send_message(self.client_socket, message)
        print(f"Sent message: {message}")
