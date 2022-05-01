from typing import Optional
from battle.characters.model import Character


class GameState:
    def __init__(self):
        self.scene_history = []
        self.current_place = None
        self.rooms = []
        self.player_character: Optional[Character] = None

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
        return self.player_character and self.player_character.name.lower() == "qa"


game_state = GameState()
