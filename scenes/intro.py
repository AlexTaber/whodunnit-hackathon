from printer import input, print

from scenes.coffee import CoffeeScene
from scenes.door import DoorScene
from scenes.model import Scene


class IntroScene(Scene):
    def run(self):
        print(
            "\nIt's a warmer day than expected in New York.  You're overdressed "
            "for the day and are hot and sweaty from your train ride in from Brooklyn"
        )
        print("You arrive at the RippleMatch office bright and early.")

        print("What do you want to do?")
        action = input(["Enter", "Coffee run"])

        if action == "Coffee run":
            return CoffeeScene()
        elif action == "Enter":
            return DoorScene()
