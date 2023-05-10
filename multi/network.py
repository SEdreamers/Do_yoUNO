import socket
import pickle

class Network:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_server_socket(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        return server_socket

    def create_client_socket(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket

    def send_message(self, sock, message):
            data = pickle.dumps(message)
            sock.sendall(data)

    def receive_message(self, sock, buffer_size=1024):
        data = sock.recv(buffer_size)
        if data:
            return pickle.loads(data)
        return None