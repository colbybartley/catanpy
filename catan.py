## marky - dark blue
## bear - black
## colby - green
## tyler - gold
## blade - red
## bryn - pink

from pycatan import Game
from pycatan.board import RandomBoard

import random

game = Game(RandomBoard())

p1 = game.players[0]
settlement_coords = game.board.get_valid_settlement_coords(player = p1, ensure_connected = False)
game.build_settlement(player = p1, coords = random.choice(list(settlement_coords)), cost_resources = False, ensure_connected = False)
print(game.board)