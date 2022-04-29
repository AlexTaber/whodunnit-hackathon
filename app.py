# from printer import print

# print("[secondary]apples$: Hello, $[primary]Jim$! You are looking ", end="", pause=0)

# print("[primary]FINE", end="", delay=0.2, pause=0)

# print(" today")

# print("[primary]Jim$: Thanks, $[secondary]apples$! How are you?")

# print("[green]\n\n.........................", pause=0)
# print("[green]......", end="", pause=0)
# print("[green]H A C K I N G", end="", delay=0.1, pause=0)
# print("[green]......", pause=0)
# print("[green].........................", pause=0)

from game import Game
from game.state import game_state
from rooms.model import kitchen
from rooms.registry import room_scene_registry
from scenes.title import TitleScene
from scenes.kitchen import KitchenScene

game_state.rooms.append(kitchen)

room_scene_registry["Kitchen"] = KitchenScene()

game = Game(game_state)
game.run(TitleScene())
