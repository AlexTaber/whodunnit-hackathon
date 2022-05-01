from engine.battle.battles import RiggedBattle, Battle
from engine.battle.ai_player import AiPlayer
from engine.battle.human_player import HumanPlayer
from battle.npc_characters import dan_i, gunner
from state import game_state
from engine.scene import Scene
from world.office.scenes.lose_game import LoseGameScene
from world.office.scenes.win_game import WinGameScene


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
