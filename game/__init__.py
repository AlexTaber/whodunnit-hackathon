from scenes.model import Scene


class Game:
    def __init__(self):
        self.scene_history = []

    @property
    def current_scene(self):
        try:
            return self.scene_history[-1]
        except IndexError:
            return None

    @property
    def previous_scene(self):
        try:
            return self.scene_history[-2]
        except IndexError:
            return None

    def run(self, scene: Scene):
        self.add_scene(scene)

    def add_scene(self, scene: Scene):
        self.scene_history.append(scene)
        next_scene = scene.run()

        if next_scene:
            self.add_scene(next_scene)


game = Game()
