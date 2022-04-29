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
from rooms.model import bathroom, engineering_table, kitchen
from rooms.registry import room_scene_registry
from scenes.bathroom import BathroomScene
from scenes.engineering_table import EngineeringTableScene
from scenes.kitchen import KitchenScene
from scenes.title import TitleScene

game_state.rooms.append(kitchen)
game_state.rooms.append(engineering_table)
game_state.rooms.append(bathroom)

room_scene_registry["Kitchen"] = KitchenScene()
room_scene_registry["Engineering Table"] = EngineeringTableScene()
room_scene_registry["Bathroom"] = BathroomScene()

game = Game(game_state)
game.run(TitleScene())
