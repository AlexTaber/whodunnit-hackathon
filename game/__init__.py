from scenes.model import Scene

from game.state import GameState


class Game:
    def __init__(self, state: GameState):
        self.state = state

    def run(self, scene: Scene):
        self.add_scene(scene)

    def add_scene(self, scene: Scene):
        self.state.scene_history.append(scene)
        next_scene = scene.run()

        if next_scene:
            self.add_scene(next_scene)
