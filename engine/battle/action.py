from engine.battle.character import Character
from engine.battle.move import LimitBreak, Move
from engine.printer import print


class Action:
    def __init__(self, move: Move, caster: Character, target: Character):
        self.move = move
        self.caster = caster
        self.target = target

    def execute(self) -> None:
        # This is slapdash. Later, we'd want to account for character level,
        # accuracy, status effects, etc.  Kept simple for now.
        #
        # We'll also want to decouple state update logic and
        # presentational logic
        self._print_spell(self.move)
        if isinstance(self.move, LimitBreak):
            print(f"{self.caster.label} is transcending their limits!! ✨✨✨")

        if self.move.description:
            print(
                self.move.description.format(
                    TARGET=self.target.label,
                    CASTER=self.caster.label,
                )
            )
        if self.move.base_dmg:
            self.target.hp = max(0, self.target.hp - self.move.base_dmg)
            self.target.limit_points += self.move.base_dmg // 2
            print(f"{self.target.name} took {self.move.base_dmg} damage!")
            if self.target.hp == 0:
                print(f"{self.target.name} fainted!")
        if self.move.base_heal:
            self.target.hp = min(
                self.target.max_hp, self.target.hp + self.move.base_heal
            )
            print(f"{self.target.name} regained {self.move.base_heal} HP!")

        for side_effect in self.move.side_effects:
            side_effect.apply(self.caster, self.target)
            if side_effect.description:
                print(side_effect.description)

    def _print_spell(self, move):
        print(
            f"{self.caster.label} casts $[secondary]'{move.name.upper()}'$ on "
            f"{self.target.label}!"
        )
