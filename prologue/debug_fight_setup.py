import battle_configuration.jobs as jobs
from battle.characters.model import Character
from state import game_state
from prologue.final_boss import FinalBoss
from engine.scene import Scene


class DebugFightSetup(Scene):
    def run(self) -> Scene:

        game_state.player_character = Character(
            name="QA",
            job=jobs.engineer,
            level=5,
            hp=20,
            max_hp=20,
        )

        return FinalBoss()
