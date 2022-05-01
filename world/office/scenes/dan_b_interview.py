from engine.scene import Scene
from engine.printer import print
from state import game_state


class DanBInterviewScene(Scene):
    def run(self):
        print("[secondary]Terrible news about the dead guy.")
        print(
            "[secondary]Do you want to hear my latest recording I finished this morning?"
        )
        print("[secondary]I’ve been awake for 37 hours straight recording it.")
        print("[secondary]What? No I don’t need coffee. I ", end="")
        print("[primary]AM", delay=0.3, end="")
        print("[secondary] the coffee.")
        return game_state.previous_scene
