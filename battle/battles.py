from battle.actions.model import Action
from battle.characters.model import Character
from battle.players.model import Player
from engine.printer import print


class RiggedBattle:
    """A battle in which the player is guaranteed to win.

    The savior character will revive the player if the player faints.
    """

    def __init__(self, player: Player, enemy: Player, savior: Character):
        self.player = player
        self.enemy = enemy
        self.savior = savior

    def start(self):
        print(
            f"\n{self.enemy.character.label} challenges {self.player.character.label}"
            " to a battle!"
        )
        while self.enemy.character.hp > 0:
            if self.player.character.hp <= 0:
                self._revive_player()
            print("\n---------------------", delay=0, pause=0.2)
            self._print_status(self.player)
            self._print_status(self.enemy)
            print("---------------------", delay=0, pause=0.2)
            print("Your turn!")
            self.player.pick_action(self.enemy.character).execute()
            if self.enemy.character.hp > 0:
                print(f"{self.enemy.character.name}'s turn")
                self.enemy.pick_action(self.player.character).execute()

        print(f"{self.enemy.character.label} has been defeated!\n")

    def _revive_player(self):
        print(f"{self.savior.label} arrives at your side!")
        for move in self.savior.job.moves:
            action = Action(move=move, caster=self.savior, target=self.player.character)
            action.execute()

    def _print_status(self, player):
        player_hp = f"HP: {player.character.hp}/{player.character.max_hp}"
        player_limit_so_far = min(
            player.character.limit_points, player.character.max_limit
        )
        player_limit_remaining = player.character.max_limit - player_limit_so_far
        player_limit_diagram = (
            f'Limit: ({"▮" * player_limit_so_far}{" " * player_limit_remaining})'
        )
        print(
            f"{player.character.label} | {player_hp} | {player_limit_diagram}",
            delay=0,
            pause=0.2,
        )
