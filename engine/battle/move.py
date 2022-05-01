from typing import Optional

from pydantic import BaseModel

from engine.battle.side_effects.base import ResetLimitBreak
from engine.battle.side_effects.interface import SideEffect


class Move(BaseModel):
    name: str
    base_dmg: int = 0
    base_heal: int = 0
    description: str = ""  # e.g., "{CASTER} throws an egg at {TARGET}"
    illustration: Optional[str] = None
    default_to_target_self: bool = False
    side_effects: list[SideEffect] = []

    class Config:
        arbitrary_types_allowed = True


class LimitBreak(Move):
    side_effects: list[SideEffect] = [ResetLimitBreak()]
