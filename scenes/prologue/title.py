from printer import print
from scenes.model import Scene
from scenes.prologue.title2 import TitleScene2


class TitleScene(Scene):
    def run(self) -> TitleScene2:
        print("Test!")
        return TitleScene2()
