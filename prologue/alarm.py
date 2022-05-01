import hashlib
from engine.scene import Scene
from engine.printer import print, input
from prologue.murder import MurderScene


class AlarmScene(Scene):
    def run(self):
        print("\nThe alarm pad is beeping ominously.  Its screen reads ", end="")
        print("[primary]ARMED", delay=0.2)
        print("You know the alarm code, right?  Enter the code:")
        value = input(None)
        code_hash = hashlib.sha256(value.encode("utf-8")).hexdigest()
        if (
            code_hash
            == "7ac25d5d84cae3dcc037c52a93dfe320fe83b2a6abe787451b4fc15aeba2c9e7"
        ):
            print("The alarm goes ", end="")
            print("[primary]DISARMED - READY TO ARM", delay=0.1)
        else:
            print(f"\nYou enter {value}. That's not the code.")
            print("The alarm begins emitting a high-pitched screech.")
            print("Meh, it's probably fine.")

        return MurderScene()
