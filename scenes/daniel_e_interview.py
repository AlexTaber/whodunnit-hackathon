from game.state import game_state
from printer import print

from scenes.model import Scene


class DanielEInterviewScene(Scene):
    def run(self):
        print(
            "[secondary] Let me tell you about my morning.  I met up with Dee to determine which is faster way to get to work, my mountain bike or his motorcycle."
        )
        print(
            "[secondary] It was a very close race but without a doubt my bike is faster and more efficient."
        )
        print("[secondary] Or maybe it’s just me who is faster.")
        return game_state.previous_scene
