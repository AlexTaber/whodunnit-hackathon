from game import Game
from game.state import game_state
from rooms.model import init_rooms
from scenes.title import TitleScene

print("\033[H\033[J", end="")

init_rooms()
game = Game(game_state)
game.run(TitleScene())
