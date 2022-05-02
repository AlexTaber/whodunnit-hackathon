from engine.scene import Scene
from engine.printer import print
from state import game_state


class DanIInterviewScene(Scene):
    def run(self):
        if game_state.dan_i_interactions == 0:
            print("[secondary]What was I doing this morning?")
            print("[secondary]Umm.. stargazing?")
            print(
                "[secondary]Wait… it’s the morning. Erm.. NOT stargazing, but something else!"
            )
            print("[secondary]I don’t know, why are you bothering me?! Go away!")
        elif game_state.dan_i_interactions == 1:
            print("[secondary]Why are you looking at me so suspiciously?")
            print("[secondary]Look. I am an |[primary]ARTIST|[secondary], a docile creature incapable of such violence.")
            print("Gunner growls at Dan I.")
            print("[secondary]GET OUT OF HERE YOU STUPID DOG")
        else:
            print("Dan I stares intently at the coffee machine, ignoring you.")

        game_state.dan_i_interactions += 1
        return game_state.previous_scene
