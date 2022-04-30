from game import Game
from game.state import game_state
from places.model import init
from scenes.title import TitleScene

print("\033[H\033[J", end="")

init()
game = Game(game_state)
game.run(TitleScene())
