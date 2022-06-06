import whodunnit.battle.jobs as jobs
from whodunnit.engine.battle.character import Character
from whodunnit.state import game_state
from whodunnit.world.office.scenes.final_boss import FinalBoss
from whodunnit.engine.scene import Scene


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
