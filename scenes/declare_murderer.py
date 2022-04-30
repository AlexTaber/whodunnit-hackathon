from printer import print, input
from game.state import game_state

from scenes.model import Scene
from scenes.dan_i_admission import DanIAdmissionScene


class DelcareMurdererScene(Scene):
    def run(self):
      print("Are you ready to declare the murderer?")
      value = input(["Yes", "No"])

      if value == "Yes":
        print("Who do you think it was?")
        value = input(["Dan B", "Dan I", "Dan S", "Daniel E", "Dee"])

        if value == "Dan I":
          return DanIAdmissionScene()
        else:
          print(f"You really think ${value} did it? That's quite the accusation. But if you're sure... we trust you!")
          print(f"{value} is promptly fired for breach of contract, specifically Article A section C 'Do not murder any prospective investors in the company'.")
          print("Way to go detective. Hope you're sure about your choice.")
      else:
        return game_state.previous_scene
