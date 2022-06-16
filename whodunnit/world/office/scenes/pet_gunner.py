from whodunnit.engine.scene import Scene
from whodunnit.engine.printer import print
from whodunnit.state import game_state


class PetGunnerScene(Scene):
    def run(self):
        game_state.pet_gunner = True
        print("Gunner eyes you cautiously, as if trying to determine what kind of person you are.")
        print("You want to show him you're a good person!")
        print("You give Gunner the many pets he deserves.")
        print("Gunner accepts your pets and leaves, seemingly satisfied by your impeccable character.")
        print("What a good pupper!")
        return game_state.previous_scene
