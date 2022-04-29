from game.state import game_state
from printer import print

from scenes.model import Scene


class CoffeeScene(Scene):
    def run(self):
        print(
            "You run next door to Gotham Coffee and promptly hand over no less than $7.15 for a cup of joe."
        )
        print("Worth it.")
        return game_state.previous_scene
