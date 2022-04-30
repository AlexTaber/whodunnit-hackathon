from game import Game
from game.state import game_state
from rooms.model import bathroom, engineering_table, kitchen
# from scenes.title import TitleScene

game_state.rooms.append(kitchen)
game_state.rooms.append(engineering_table)
game_state.rooms.append(bathroom)

game = Game(game_state)
game.run(game_state.rooms[0].scene)
