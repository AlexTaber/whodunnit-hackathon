from engine.printer import print
from engine.scene import Scene


class TheEnd(Scene):
    def run(self):
        print("...", delay=0.5)

        print("Way to go detective! You solved the case!")
