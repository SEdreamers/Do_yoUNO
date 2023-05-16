import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import socket
from _thread import *
import pickle
from game_logic import Game
import json

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
games = {}
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
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()





try:
    with open('setting_data.json') as game_file:
        lst = json.load(game_file)
except: 
    lst ={
    "color_blind_mode": False,
    "size": (800,600),
    "Total_Volume": 0.3,
    "Background_Volume": 0.3,
    "Sideeffect_Volume": 0.3,
    "player_numbers":3,
    "me": 'player',
    "c1name" :'computer1',
    "c2name" :'computer2',
    "c3name" :'computer3',
    "c4name" :'computer4',
    "c5name" :'computer5',
    "unclicked_list": [],
    "characters" : []
    }


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(lst["size"][0],lst["size"][1],lst["color_blind_mode"],lst["player_numbers"],lst["characters"],gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))