from engine.scene import Scene
from engine.printer import print, input
from prologue.create_character import CreateCharacterScene


class TitleScene(Scene):
    def run(self) -> CreateCharacterScene:
        print(
            """
 ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓    ▒█████    █████▒    ▄▄▄
 ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒   ▒██▒  ██▒▓██   ▒    ▒████▄
▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░   ▒██░  ██▒▒████ ░    ▒██  ▀█▄
▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░    ▒██   ██░░▓█▒  ░    ░██▄▄▄▄██
▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░    ░ ████▓▒░░▒█░        ▓█   ▓██▒
░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░      ░ ▒░▒░▒░  ▒ ░        ▒▒   ▓▒█░
░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░         ░ ▒ ▒░  ░           ▒   ▒▒ ░
   ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░         ░ ░ ░ ▒   ░ ░         ░   ▒
         ░  ░        ░  ░  ░  ░                ░ ░                   ░  ░

▄▄▄█████▓ ██░ ██  ▒█████   █    ██   ██████  ▄▄▄       ███▄    █ ▓█████▄
▓  ██▒ ▓▒▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒██░  ██▒▓██  ▒██░░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒██   ██░▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░ ████▓▒░▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓
  ▒ ░░    ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒
    ░     ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒
  ░       ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░    ░   ▒      ░   ░ ░  ░ ░  ░
          ░  ░  ░    ░ ░     ░           ░        ░  ░         ░    ░
                                                                  ░
▓█████▄  ▄▄▄       ███▄    █   ██████
▒██▀ ██▌▒████▄     ██ ▀█   █ ▒██    ▒
░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄
░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒
░▒████▓  ▓█   ▓██▒▒██░   ▓██░▒██████▒▒
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░
 ░ ░  ░   ░   ▒      ░   ░ ░ ░  ░  ░
   ░          ░  ░         ░       ░
 ░
        """,
            delay=0.001,
        )
        print("Off-By-One Entertainment.  All Rights Reserved.\n")
        print("Press enter to continue...")
        input(None)
        return CreateCharacterScene()