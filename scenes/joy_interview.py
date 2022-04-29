from game.state import game_state
from printer import print

from scenes.model import Scene


class JoyInterviewScene(Scene):
    def run(self):
        print("Test!")
        return game_state.previous_scene
