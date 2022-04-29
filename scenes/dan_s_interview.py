from game.state import game_state
from printer import print

from scenes.model import Scene


class DanSInterviewScene(Scene):
    def run(self):
        print(
            "[secondary]I cannot believe the VC is dead! I came into town to have dinner with him last night!"
        )
        print("[secondary]Wait. That sounds suspisicious.")
        print("[secondary]Well it’s ", end="")
        print("[primary]NOT", delay=0.2, end="")
        print(
            "[secondary] suspicious! I definitely didn’t kill him! I was spending this morning recovering from jet lag after barely making it through a late night!"
        )
        return game_state.previous_scene
