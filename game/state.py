class GameState:
    def __init__(self):
        self.scene_history = []
        self.rooms = []

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
    def room_names(self):
        return [room.name for room in self.rooms]


game_state = GameState()
