import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import socket
from _thread import *
import pickle
from game_logic import Game

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()     
print("Waiting for a connection, Server Started")




connected = set()
games = {}                 # dictionary
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:break
        except:break

    print("Lost connection")
    
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    
    idCount -= 1
    conn.close()








while True:                         #여기서 서버 연결 시작. 
    conn, addr = s.accept()
    print("Connected to:", addr)    # addr가 ('127.0.0.1',52980)같은 식으로 print됨

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2       # 2명씩 짝지운 것. 
    if idCount % 2 == 1:            # 홀수번째 player  --> 여기서는 player 0 (즉, p = 0)만 출력. 
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1                       # 짝수번째 player  --> 여기서는 player 1 (즉, p = 1)만 출력. 
    start_new_thread(threaded_client, (conn, p, gameId))   # client connection