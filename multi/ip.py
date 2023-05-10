from server import Server
from client import Client
import socket

def get_local_ip_address():
    hostname = socket.gethostname()
    local_ip_address = socket.gethostbyname(hostname)
    return local_ip_address

host = get_local_ip_address()
print(f"Local IP address: {host}")

server = Server(host, 5555)
server.start()

# client = Client("192.168.1.122", 5555)
# client.connect()
# client.send_message("hello")