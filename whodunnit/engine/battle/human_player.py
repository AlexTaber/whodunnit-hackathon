from whodunnit.engine.battle.action import Action
from whodunnit.engine.battle.character import Character
from whodunnit.engine.battle.player import Player
from whodunnit.engine.printer import input


class HumanPlayer(Player):
    LIMIT_BREAK_LABEL = "LIMIT BREAK ✨✨✨"

    def pick_action(self, enemy: Character) -> Action:
        valid_moves = self.character.job.moves
        move_names = [move.name for move in valid_moves]
        if self.character.has_limit_break:
            move_names.append(self.LIMIT_BREAK_LABEL)

        move_name = input(move_names)

        if move_name == self.LIMIT_BREAK_LABEL:
            move = self.character.job.limit_break
        else:
            move = valid_moves[move_names.index(move_name)]

        # Eventually would want to support manual targetting
        target = self.character if move.default_to_target_self else enemy

        return Action(move=move, caster=self.character, target=target)
