from printer import print

from scenes.create_character import CreateCharacterScene
from scenes.model import Scene


class TitleScene(Scene):
    def run(self) -> CreateCharacterScene:
        print("Test!")
        return CreateCharacterScene()
