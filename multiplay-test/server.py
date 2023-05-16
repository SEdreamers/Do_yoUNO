import asyncio
import json
import pickle
import game_logic
from deck import Deck
from computer import Computer
from human import Human

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def broadcast(self, msg):
        for client in self.clients:
            await client.write(msg.encode())

    async def handle_client(self, reader, writer):
        while True:
            msg = await reader.read(100)
            if msg:
                print(f'Received {msg.decode()}')
                await self.broadcast(msg.decode())

    async def send_game_state(self):
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
            await self.broadcast(f)

    async def start_server(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port)

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server = Server('localhost', 8888)
    asyncio.run(server.start_server())
