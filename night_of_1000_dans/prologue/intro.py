from engine.scene import Scene
from engine.printer import print, input
from night_of_1000_dans.prologue.door import DoorScene
from night_of_1000_dans.world.coffee.scenes.coffee import CoffeeScene


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
