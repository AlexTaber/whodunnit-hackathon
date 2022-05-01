from engine.scene import Scene
from engine.printer import print
from state import game_state


class DeeInterviewScene(Scene):
    def run(self):
        print("[secondary]So tragic to hear what happened. I can't believe one of the Dans would do something like that.")
        print("[secondary]Wait, am I under investigation too? No one ever calls me Dan!")
        print(
            "[secondary]Also, I was having a race with Daniel E to determine the preeminent 2-wheeled vehicle! Obviously, motorcycles are best."
        )
        print("[secondary]Who won? Oh umm… I mean, ", end="")
        print("[primary]DEFINITELY", delay=0.1, end="")
        print("[secondary] me.")
        return game_state.previous_scene
