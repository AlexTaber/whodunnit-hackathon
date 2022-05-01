from battle.battles import RiggedBattle
from battle.players.ai_player import AiPlayer
from battle.players.human_player import HumanPlayer
from battle_configuration.npc_characters import dan_i, gunner
from state import game_state
from engine.scene import Scene
from prologue.the_end import TheEnd


class FinalBoss(Scene):
    def run(self) -> Scene:
        player = HumanPlayer(character=game_state.player_character)  # type: ignore
        enemy = AiPlayer(character=dan_i)
        RiggedBattle(player, enemy, gunner).start()
        return TheEnd()
