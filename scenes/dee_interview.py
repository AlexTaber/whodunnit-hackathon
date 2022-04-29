from game.state import game_state
from printer import print

from scenes.model import Scene


class DeeInterviewScene(Scene):
    def run(self):
        print(
            "[secondary]So tragic to hear what happened. And now everyone is suspecting it’s me because he said it was a Dan! But… no one even calls me that?"
        )
        print(
            "[secondary]Also, I was having a race with Daniel E to determine the preeminent 2-wheeled vehicle! Obviously, motorcycles are best."
        )
        print("[secondary]Who won? Oh umm… I mean, ", end="")
        print("[primary]D E F I N I T E L Y", delay=0.1, end="")
        print("[secondary] me")
        return game_state.previous_scene
