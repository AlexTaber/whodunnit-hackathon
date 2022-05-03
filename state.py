from typing import Optional

from pydantic import BaseModel

from engine.battle.character import Character
from engine.game.state import GameState


class FishingState(BaseModel):
    current_streak: int = 0
    record_streak: int = 0
    record_weight: float = 0.0


class NOTDGameState(GameState):
    def __init__(self):
        super().__init__()
        self.player_character: Optional[Character] = None
        self.pet_gunner = False
        self.dan_i_interactions = 0
        self.fishing: FishingState = FishingState()


game_state = NOTDGameState()
