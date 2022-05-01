from engine.scene import Scene
from engine.printer import print, input
from night_of_1000_dans.prologue.intro import IntroScene
from night_of_1000_dans.state import game_state


class CreateCharacterScene(Scene):
    def run(self) -> IntroScene:
        print("What is your name?")
        game_state.player_name = input()

        print("Select character class:")

        self._print_class("Engineer", "Crippling Anxiety")
        self._print_class("Product Manager", "Jira Mastery")
        self._print_class("Salesperson", "Smooth Talkin'")
        self._print_class("New Hire", "On-Site Onboarding Per Diem")

        result = input(["Engineer", "Product Manager", "Salesperson", "New Hire"])

        if result == "Engineer":
            self._print_selected_class("You're an $[primary]Engineer$, master of code", {
                "Intelligence": 5,
                "Charisma": "null",
                "Stamina": 4,
                "People Skills": 1
            })
        elif result == "Product Manager":
            self._print_selected_class("You're a $[primary]Product Manager$, master of product", {
                "Intelligence": 3,
                "Charisma": 1,
                "Stamina": 5,
                "People Skills": 3
            })
        elif result == "Salesperson":
            self._print_selected_class("You're a $[primary]Salesperson$, master of the close", {
                "Intelligence": 2,
                "Charisma": 5,
                "Stamina": 3,
                "People Skills": 4
            })
        elif result == "New Hire":
            self._print_selected_class("You're a $[primary]New Hire$, master of none", {
                "Intelligence": "null",
                "Charisma": "null",
                "Stamina": "null",
                "People Skills": "null"
            })

        # TODO - save class to game state

        return IntroScene()

    def _print_class(self, name: str, ability: str):
        print(f"[primary]\n{name}", delay=0)
        print(f"Special Ability: $[secondary]{ability}", delay=0)

    def _print_selected_class(self, desc: str, stats: dict):
        print(desc)

        for key in list(stats.keys()):
            print(f"[primary]{key}: $[secondary]{stats.get(key)}", delay=0)
