from printer import print

from scenes.model import Scene
from scenes.engineering_table import EngineeringTableScene


class ArrivalScene(Scene):
    def run(self):
        print("\n\n[primary] ...a short while later...\n\n")

        print(
            "Folks have begun to trickle into the office. The body is getting stinky."
        )

        print("\nJacks and Lauren arrive. Joy arrives too.")
        print(
            "\nAlso, it looks like the Dans are all here... Dan B., Dan S., Dan 'Dee' Ansong, Dan E, Dan I..."
        )
        return EngineeringTableScene()
