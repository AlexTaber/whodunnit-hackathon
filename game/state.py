class GameState:
    def __init__(self):
        self.scene_history = []
        self.current_place = None
        self.player_name = "Michael"

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
    def qa_mode(self):
        return self.player_name.lower() == "qa"


game_state = GameState()
