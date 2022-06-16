from whodunnit.engine.printer import print
from whodunnit.engine.scene import Scene


class WinGameScene(Scene):
    def run(self):
        print("...", delay=0.5)

        print("Way to go detective! You solved the case!")
