from printer import print, input

from scenes.model import Scene
from scenes.murder import MurderScene


class AlarmScene(Scene):
    def run(self):
        print(
            "\nAlarm Pad is beeping begging for you to smash its buttons with the correct code"
        )
        print(
            "You start to sweat more worried you'll enter the wrong code.  Enter the code:"
        )
        value = input(None)
        print(f"\nYou enter {value} and it happens to be wrong")
        print(
            "You open your phone to look at our Notion doc to get the correct passcode while the alarm beeping gets faster"
        )
        print("You finally enter the correct code")

        return MurderScene()
