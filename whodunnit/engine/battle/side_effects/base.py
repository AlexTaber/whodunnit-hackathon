from typing import TYPE_CHECKING

from whodunnit.engine.battle.side_effects.interface import SideEffect

if TYPE_CHECKING:
    from whodunnit.engine.battle.character import Character


class ResetLimitBreak(SideEffect):
    def apply(self, caster: "Character", target: "Character"):
        caster.limit_points = 0

    @property
    def description(self):
        return None
