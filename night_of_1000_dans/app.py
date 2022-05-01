from night_of_1000_dans.prologue.title import TitleScene
from night_of_1000_dans.state import game_state
from engine.game import game

print("\033[H\033[J", end="")

game.run(game_state, TitleScene())
