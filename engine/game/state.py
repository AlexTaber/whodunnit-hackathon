class GameState:
    def __init__(self):
        self.scene_history = []
        self.place_history = []
        self.dev_mode = False

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

    @property
    def current_place(self):
        try:
            return self.place_history[-1]
        except IndexError:
            return None

    @property
    def previous_place(self):
        try:
            return self.place_history[-2]
        except IndexError:
            return None

