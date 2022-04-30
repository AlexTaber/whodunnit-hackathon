from printer import input, print

from scenes.arrival import ArrivalScene
from scenes.model import Scene
from game.state import game_state


class SlackScene(Scene):
    def run(self):
        print("\nYou grab your phone to message #coreteam to get help.")
        print("Enter your cry for help:")
        value = input()

        self._print_slack(game_state.player_name, value)
        self._print_slack("Jacks", "😱😱😱 OMG 😱😱😱")
        self._print_slack("Shannon", "Do not touch anything!")
        self._print_slack("Lauren", "I'm not cleaning that up")
        self._print_slack("Dan B", "Big yikes")
        self._print_slack("Eric", "Sorry can't help, with other VCs")
        self._print_slack("Andrew", "Please keep Gunner away from the body")

        return ArrivalScene()

    def _print_slack(self, sender: str, message: str):
        print(f"[secondary] 8:21 AM - #coreteam: $[primary]@{sender}$ - {message}")
