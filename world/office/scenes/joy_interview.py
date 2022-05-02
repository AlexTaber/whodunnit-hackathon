from engine.scene import Scene
from engine.printer import print
from state import game_state


class JoyInterviewScene(Scene):
    def run(self):
        print(
            "[secondary]Did you know that the Dans were buying out equity in RippleMatch?"
        )
        print(
            "[secondary]We should have seen this coming. Why else would they have hired all these Dans?!"
        )
        print("[secondary]It's a coup!")
        print(
            "[secondary]Do you think they all killed the VC together? Wouldn't surprise me."
        )
        return game_state.previous_scene
