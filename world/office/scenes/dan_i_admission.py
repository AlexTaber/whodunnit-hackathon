from engine.scene import Scene
from engine.printer import print
from prologue.final_boss import FinalBoss


class DanIAdmissionScene(Scene):
    def run(self):
        print("[secondary] OK FINE. YOU GOT ME.")
        print("[secondary] I DID IT! AND YOU KNOW WHY?")
        print(
            "[secondary] THAT PUNK STOLE MY ART ASSETS FOR SOME GAME COMPANY THAT HE OWNS!"
        )
        print("[secondary] Why does this keep happening to me?!")
        print("[secondary] I regret nothing, he deserved it.\n\n")

        return FinalBoss()
