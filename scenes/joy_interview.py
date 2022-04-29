from game.state import game_state
from printer import print

from scenes.model import Scene


class JoyInterviewScene(Scene):
    def run(self):
        print("[secondary]Hey! I… need to talk to you about something.")
        print(
            "[secondary]Did you know that all of the Daniels were buying out equity in RippleMatch?"
        )
        print(
            "[secondary]We should have seen this coming. Why else would they have hired all these Daniels?!"
        )
        print("[secondary]It’s a coup!")
        print(
            "[secondary]Do you think they all killed the VC together? Wouldn’t surprise me."
        )
        return game_state.previous_scene
