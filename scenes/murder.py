from printer import print


from scenes.model import Scene
from scenes.coffee import CoffeeScene
from scenes.slack import SlackScene


class MurderScene(Scene):
    def run(self):
        print("\n\nYou turn around heading towards a desk. Suddenly, you see a body...")
        print(
            "\nYou recognize them -- it's the venture capitalist from yesterday's LFGA!"
        )
        print(
            "\nThe body hangs lifeless out of the ROOM-brand phone booth (available at hushoffice.com)."
        )
        print("You scream at the sight of seeing a body laying on the floor")
        print("Do you want to help them?")
        value = input(["Yes", "Hell no", "Coffee run"])
        if value == "Coffee run":
            return CoffeeScene()
        if value == "Hell no":
            print("You should REALLY help them...")

        print(
            "\nYou hear him breathe. You run to the VC honcho.  As the life drains from their lips, they say..."
        )
        print("[primary]\nDan did it...\n")

        return SlackScene()
