from whodunnit.engine.scene import Scene
from whodunnit.engine.printer import print, input
from whodunnit.prologue.arrival import ArrivalScene
from whodunnit.state import game_state


class SlackScene(Scene):
    def run(self):
        print("\nYou grab your phone to message #coreteam to get help.")
        print("[info]Enter your cry for help:")
        value = input()

        self._print_slack(game_state.player_character.name, value)  # type: ignore
        self._print_slack("Jacks", "😱😱😱 OMG 😱😱😱")
        self._print_slack("Shannon", "Do not touch anything!")
        self._print_slack("Lauren", "I'm not cleaning that up")
        self._print_slack("Dan B", "Big yikes")
        self._print_slack("Eric", "Sorry can't help, with other VCs")
        self._print_slack("Andrew", "Please keep Gunner away from the body")

        return ArrivalScene()

    def _print_slack(self, sender: str, message: str):
        print(f"[secondary] 8:21 AM - #coreteam: |[primary]@{sender}| - {message}")
