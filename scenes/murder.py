import random

from printer import print, input

from scenes.model import Scene
from scenes.coffee import CoffeeScene
from scenes.slack import SlackScene


class MurderScene(Scene):
    def run(self):
        print("\n\nYou turn to head towards your desk. Suddenly...")
        print("\n[secondary]...is ", pause=0.5, delay=0, end="")
        print("[secondary]that ", pause=0.5, delay=0, end="")
        print("[secondary]a ", pause=0.5, delay=0, end="")
        print("[danger]BODY!?", pause=1, delay=0)
        print(
            "\nYou recognize them -- it's the venture capitalist from yesterday's team meeting!"
        )
        print("\nThe were going to fund our Series B!", end=" ")
        print("[muted](This doesn't bode well for our stock options)")
        print(
            "\nThey sit slouched against the wall of the ROOM-brand phone booth (available at hushoffice.com)"
        )
        print(
            "You scream at the grusome sight. You're not sure if they're dead or alive."
        )

        value = "Hell no"
        while value == "Hell no":
            print("Do you want to help them?")
            value = input(["Yes", "Hell no", "Coffee run"])
            if value == "Coffee run":
                return CoffeeScene()
            if value == "Hell no":
                print("You're not in the right headspace to help them right now.")
                browsing_options = [
                    "You read some hot takes on Twitter...",
                    "You browse Pinterest for baking inspiration...",
                    "You watch cat videos on Tiktok...",
                ]
                print(random.choice(browsing_options))
                print("\n...", delay=0.3)
                print("\nYou hear a moan coming from the phone booth.")
                print("You should probably help them.")

        print(
            "\nYou hear them breathe. You run to the VC honcho.  As the life drains from their lips, they say..."
        )
        print("[primary]\n...Dan did it...", delay=0.5)

        return SlackScene()
