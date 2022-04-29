from printer import print
from scenes.model import Scene
from scenes.intro import IntroScene


class CreateCharacterScene(Scene):
    def run(self) -> IntroScene:
        print("Test!")
        return IntroScene()
