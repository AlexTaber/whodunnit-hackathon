from engine.printer import print
from engine.scene import Scene


class LoseGameScene(Scene):
    def run(self):
        print("...", delay=0.5)

        print("Gunner looks over at your dying body.")
        print("You can't explain it, but you feel he possesses the power to revive you!")
        print("Then you remember, how he faithfully followed you around the office all day.")
        print("So good, and yet - you never gave him the many pets he deserved.")
        print("Gunner leaves you to die. You cannot fault him. You betrayed him. You deserve this.")
