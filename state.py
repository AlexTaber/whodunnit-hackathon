from typing import Optional
from engine.game.state import GameState
from engine.battle.character import Character

class NOTDGameState(GameState):
    def __init__(self):
        super().__init__()
        self.player_character: Optional[Character] = None
        self.pet_gunner = False
        self.dan_i_interactions = 0

    @property
    def qa_mode(self):
        return self.player_name.lower() == "qa"

game_state = NOTDGameState()
