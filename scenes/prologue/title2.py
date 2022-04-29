from game.state import game_state
from printer import input, print
from scenes.model import Scene


class TitleScene2(Scene):
    def run(self):
        print("Test 2!")
        name = input(["Alex", "Michael"])
        return game_state.previous_scene
