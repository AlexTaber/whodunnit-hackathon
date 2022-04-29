from printer import print

from scenes.model import Scene
from scenes.kitchen import KitchenScene


class IntroScene(Scene):
    def run(self):
        print(
            "\nIt's a warmer day than expected in New York.  You're overdressed "
            "for the day and are hot and sweaty from your train ride in from Brooklyn"
        )
        print("You arrive at the RippleMatch office bright and early.")

        print("What do you want to do?")

        return KitchenScene()
        # action = input(["Enter", "Coffee run"])

        # if action == "Enter":
        #     return Door
