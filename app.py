from game import Game
from game.state import game_state
# from scenes.title import TitleScene
from rooms.model import init_rooms

init_rooms()
game = Game(game_state)
game.run(game_state.rooms[0].scene)
