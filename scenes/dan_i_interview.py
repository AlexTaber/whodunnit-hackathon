from game.state import game_state
from printer import print

from scenes.model import Scene


class DanIInterviewScene(Scene):
    def run(self):
        print("[secondary]What was I doing this morning?")
        print("[secondary] Umm.. stargazing?")
        print(
            "[secondary] Wait… it’s the morning. Erm.. NOT stargazing, but something else!"
        )
        print("[secondary] I don’t know, why are you bothering me?! Go away!")
        return game_state.previous_scene
