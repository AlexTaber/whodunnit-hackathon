from whodunnit.engine.game.state import GameState
from whodunnit.engine.scene import Scene


class Game:
    def __init__(self):
        self.state = None

    def run(self, state: GameState, scene: Scene):
        self.state = state
        self.add_scene(scene)

    def add_place(self, place) -> Scene:
        self.state.place_history.append(place)
        scene = place.default_scene
        self.state.scene_history.append(scene)
        return scene.run()

    def add_scene(self, scene: Scene):
        self.state.scene_history.append(scene)
        next_scene = scene.run()

        if next_scene:
            self.add_scene(next_scene)

game = Game()
