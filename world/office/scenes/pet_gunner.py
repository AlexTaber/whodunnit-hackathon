from engine.scene import Scene
from engine.printer import print
from state import game_state


class PetGunnerScene(Scene):
    def run(self):
        game_state.pet_gunner = True
        print("You give Gunner the many pets he deserves.")
        print("He is such a good pupper!")
        return game_state.previous_scene
