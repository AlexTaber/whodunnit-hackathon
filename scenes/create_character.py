from printer import print
from scenes.model import Scene
from scenes.intro import IntroScene
from printer import input


class CreateCharacterScene(Scene):
    def run(self) -> IntroScene:
        print("Select character class:")

        print("\nEngineer")
        print("Special ability: Crippling anxiety")

        print("\nProduct Manager")
        print("Special ability: Jira Mastery")

        print("\nSales")
        print("Special ability: Smooth talkin'")

        print("\nNew Hire")
        print("Special ability: On-site onboarding per diem")

        result = input(["Engineer", "Product Manager", "Sales", "New Hire"])

        if result == "Engineer":
            print("You're an engineer, master of code")
            print("Stats:")
            print("Inteligence: 5", delay=0, pause=0.1)
            print("Charisma: null", delay=0, pause=0.1)
            print("Stamina: 4", delay=0, pause=0.1)
            print("People skills: 1", delay=0, pause=0.1)
        elif result == "Product Manager":
            print("You're a product manager, master of product")
            print("Inteligence: 3", delay=0, pause=0.1)
            print("Charisma: 1", delay=0, pause=0.1)
            print("Stamina: 5", delay=0, pause=0.1)
            print("People skills: 3", delay=0, pause=0.1)
        elif result == "Sales":
            print("You're a sales, master of the close")
            print("Inteligence: 2")
            print("Charisma: 5")
            print("Stamina: 3")
            print("People skills: 4")
        elif result == "New Hire":
            print("You're a new hire, master of none")
            print("Inteligence: null")
            print("Charisma: null")
            print("Stamina: null")
            print("People skills: null")

        # TODO - save class to game state

        return IntroScene()
