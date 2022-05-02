from engine.scene import Scene
from engine.printer import print, input
from prologue.alarm import AlarmScene


class ElevatorScene(Scene):
    def run(self):
        print(
            "\nYou enter the elevator. The sixth floor button "
            "is still locked. You must be the first one at the office."
        )
        print("You try to unlock the elevator, but the key sticks.")

        value = "Not really"
        while value == "Not really":
            print("Do you want to jiggle the key?")
            value = input(["Yes", "Not really"])
            if value == "Not really":
                print("You sit and contemplate your life choices.")

        print("You jiggle the key but nothing happens.")
        print("Do you want to jiggle the key", end=" ")
        print("[primary]ten", delay=0.3, end=" ")
        print("more times?")
        input(["Yes"])
        print("Thankfully, the eighth time's the charm, and the key turns.")
        print("The elevator lurches to life and brings you to the sixth floor.")

        return AlarmScene()
