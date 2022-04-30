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
