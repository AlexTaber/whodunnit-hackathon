from whodunnit.engine.battle.battles import RiggedBattle, Battle
from whodunnit.engine.battle.ai_player import AiPlayer
from whodunnit.engine.battle.human_player import HumanPlayer
from whodunnit.battle.npc_characters import dan_i, gunner
from whodunnit.state import game_state
from whodunnit.engine.scene import Scene
from whodunnit.world.office.scenes.lose_game import LoseGameScene
from whodunnit.world.office.scenes.win_game import WinGameScene


class FinalBoss(Scene):
    def run(self) -> Scene:
        player = HumanPlayer(character=game_state.player_character)  # type: ignore
        enemy = AiPlayer(character=dan_i)

        if game_state.pet_gunner:
            RiggedBattle(player, enemy, gunner).start()
            return WinGameScene()

        else:
            winner = Battle(player, enemy).start()
            if winner == player:
                return WinGameScene()
            else:
                return LoseGameScene()
