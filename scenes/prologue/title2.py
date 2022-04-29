from app import game
from printer import print
from scenes.model import Scene


class TitleScene2(Scene):
    def run(self):
        print("Test 2!")
        return game.previous_scene
