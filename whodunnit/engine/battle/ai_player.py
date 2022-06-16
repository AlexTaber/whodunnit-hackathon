import random

from whodunnit.engine.battle.action import Action
from whodunnit.engine.battle.character import Character
from whodunnit.engine.battle.player import Player


class AiPlayer(Player):
    def pick_action(self, enemy: Character) -> Action:
        if self.character.has_limit_break:
            move = self.character.job.limit_break
        else:
            move = random.choice(self.character.job.moves)

        return Action(
            move=move,
            caster=self.character,
            target=self.character if move.default_to_target_self else enemy,
        )
