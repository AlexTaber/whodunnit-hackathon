from whodunnit.prologue.title import TitleScene
from whodunnit.state import game_state
from whodunnit.engine.game import game

def run():
	print("\033[H\033[J", end="")
	game.run(game_state, TitleScene())
