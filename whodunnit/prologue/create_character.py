import inflect

from whodunnit.engine.scene import Scene
from whodunnit.engine.printer import print, input
from whodunnit.prologue.intro import IntroScene
from whodunnit.state import game_state
import whodunnit.battle.jobs as jobs
from whodunnit.engine.battle.character import Character


p = inflect.engine()


class CreateCharacterScene(Scene):
    def run(self) -> Scene:
        print("[info]What is your name?")
        player_name = input()

        if player_name.lower() == "qa":
            game_state.dev_mode = True

        print("Select character class:")

        valid_jobs = [
            jobs.engineer,
            jobs.product_manager,
            jobs.salesperson,
            jobs.new_hire,
        ]
        for job in valid_jobs:
            self._print_class(job.name, job.limit_break.name)

        selected_job_name = input([job.name for job in valid_jobs])
        selected_job = [job for job in valid_jobs if job.name == selected_job_name][0]

        game_state.player_character = Character(
            name=player_name,
            job=selected_job,
            level=5,
            hp=20,
            max_hp=20,
        )

        self._print_selected_class(
            f"You're |[primary]{p.a(selected_job.name)}|, {selected_job.motto}",
            {
                "Intelligence": selected_job.base_intelligence,
                "Charisma": selected_job.base_charisma,
                "Stamina": selected_job.base_stamina,
                "People Skills": selected_job.base_people_skills,
            },
        )

        return IntroScene()

    def _print_class(self, name: str, ability: str):
        print(f"[primary]\n{name}", delay=0)
        print(f"Special Ability: |[secondary]{ability}", delay=0)

    def _print_selected_class(self, desc: str, stats: dict):
        print(desc)

        for key in list(stats.keys()):
            print(f"[primary]{key}: |[secondary]{stats.get(key)}", delay=0)
