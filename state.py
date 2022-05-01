from typing import Optional
from engine.game.state import GameState
from battle.characters.model import Character

class NOTDGameState(GameState):
    def __init__(self):
        super().__init__()
        self.player_character: Optional[Character] = None

    @property
    def qa_mode(self):
        return self.player_name.lower() == "qa"

game_state = NOTDGameState()
