from engine.battle.action import Action
from engine.battle.character import Character
from engine.battle.player import Player
from engine.printer import print


class BaseBattle:
    """A battle that simply returns a winner.

    This class may be wrapped with additional functionality ie the RiggedBattle
    """

    def __init__(self, player: Player, enemy: Player):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(
            f"\n{self.enemy.character.label} challenges {self.player.character.label}"
            " to a battle!"
        )
        return self._battle()

    def _battle(self) -> Character:
        while self.enemy.character.hp > 0:
            if self.player.character.hp <= 0:
                return self.enemy.character
            print("\n---------------------", delay=0, pause=0.2)
            self._print_status(self.player)
            self._print_status(self.enemy)
            print("---------------------", delay=0, pause=0.2)
            print("Your turn!")
            self.player.pick_action(self.enemy.character).execute()
            if self.enemy.character.hp > 0:
                print(f"{self.enemy.character.name}'s turn")
                self.enemy.pick_action(self.player.character).execute()

        return self.player.character

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

class Battle(BaseBattle):
    """A battle that prints the outcome.

    This is the default battle class for fair encounters
    """

    def __init__(self, player: Player, enemy: Player):
        super().__init__(player, enemy)

    def start(self) -> Character:
        winner = super().start()

        if winner == self.player:
            print(f"{self.enemy.character.label} has been defeated!\n")
        else:
            print(f"{self.player.character.label} has been defeated!\n")

        return winner

    def _revive_player(self):
        print(f"{self.savior.label} arrives at your side!")
        for move in self.savior.job.moves:
            action = Action(move=move, caster=self.savior, target=self.player.character)
            action.execute()

class RiggedBattle(BaseBattle):
    """A battle in which the player is guaranteed to win.

    The savior character will revive the player if the player faints.
    """

    def __init__(self, player: Player, enemy: Player, savior: Character):
        super().__init__(player, enemy)
        self.savior = savior

    def start(self):
        winner = super().start()

        if winner == self.player:
            print(f"{self.enemy.character.label} has been defeated!\n")
        else:
            self._revive_player()

    def _revive_player(self):
        print(f"{self.savior.label} arrives at your side!")
        for move in self.savior.job.moves:
            action = Action(move=move, caster=self.savior, target=self.player.character)
            action.execute()
            self._battle()
