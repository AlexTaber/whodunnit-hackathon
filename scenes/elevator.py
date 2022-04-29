from printer import print

from scenes.model import Scene
from scenes.alarm import AlarmScene


class ElevatorScene(Scene):
    def run(self):
        print(
            "\nYou enter the elevator. The sixth floor button "
            "is still locked. You must be the first one at the office."
        )
        print("You try to unlock the elevator, but the key sticks.")
        print("Do you want to jiggle the key?")
        input(["Yes", "Not really"])
        print("You jiggle the key but nothing happens.")
        print("Do you want to jiggle the key ten more times?")
        input(["Yes"])
        print("Thankfully, the eight time's the charm, and the key turns")
        print("The elevator lurches to life and brings you to the sixth floor.")

        return AlarmScene()
