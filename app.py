from prologue.title import TitleScene
from state import game_state
from engine.game import game

print("\033[H\033[J", end="")

game.run(game_state, TitleScene())
