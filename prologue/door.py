from engine.scene import Scene
from engine.printer import print, input
from prologue.elevator import ElevatorScene


class DoorScene(Scene):
    def run(self):
        print(
            "\nYou're in front of the heavy building door.  Both of your keys looks basically the same."
        )
        print(
            "Do you want to use the silverish gold key with a nub or the gold silverish key with two nubs?"
        )
        input(["Use gold key", "Use silver key"])
        print(
            "I always pick the wrong damn key. I should really add tape to the door key."
        )
        print("You unlock the door with the other key and enter the lobby.")

        return ElevatorScene()
