import random
from typing import Optional

from engine.fishing.fishing import Fishing
from engine.fishing.models import Fish, FishSpecies
from engine.printer import input, print
from engine.printer.oscilating_input import get_input_from_oscilating_meter
from engine.scene import Scene
from fishing.fish_species import big_chungus, regular_fish
from state import FishingState, game_state
from world.office.scenes.fishing_bad_ending import FishingBadEnding
from world.office.scenes.fishing_good_ending import FishingGoodEnding


class FishingScene(Scene):

    streak_dialogue = {
        1: "Nice! You're getting the hang of this.",
        2: "2 in a row! You're doing great!",
        3: "3 in a row! Terrific!",
        4: "That's 4 in a row! You're doing awesome!",
        5: "5 in a row! Sick skills!!",
        6: "6 in a row! Smokin' sexy style!!",
    }
    min_streak_for_big_chungus = 7

    def run(self):
        print("You arrive at the East River.")
        print("You see fish lurking under the surface.")
        self._print_records(game_state.fishing)

        elect_to_fish = True
        while elect_to_fish:
            print("You cast your line.")

            session = Fishing(self._get_available_fish(game_state.fishing))
            on_hook = session.cast()

            wait = random.randrange(1, 6)
            print(f"{'.' * wait}", delay=1)
            print("Something's biting!", pause=0.5, delay=0)
            print(on_hook.fish_group.hint)

            reel_power = self._get_reel_power(30 if on_hook == big_chungus else 10)
            caught = session.reel(reel_power)

            self._handle_catch(caught, game_state.fishing)
            if on_hook == big_chungus:
                if caught:
                    return FishingGoodEnding()
                else:
                    return FishingBadEnding()
            print("[info]Do you want to fish again?", delay=0)
            elect_to_fish = input(["Yes", "No"]) == "Yes"

        game_state.fishing.current_streak = 0
        print("That's enough for now. You decide to pack it up.")
        return game_state.previous_scene

    def _get_reel_power(self, max_power: int = 10) -> int:
        """Get the reel strength from the user."""
        print("[info]Press ENTER to reel in the fish!", delay=0)
        return get_input_from_oscilating_meter("Reel power", max_power)

    def _handle_catch(self, caught: Optional[Fish], fishing_state: FishingState):
        if caught is None:
            print("Looks like it got away.")
            fishing_state.current_streak = 0
        else:
            print(f"You caught a {caught.species.name}!")
            print(f"It weighs {caught.weight:.2f} lbs.")
            if caught.weight > fishing_state.record_weight:
                fishing_state.record_weight = caught.weight
                print("That's a new weight record!")
            fishing_state.current_streak += 1
            if fishing_state.current_streak > fishing_state.record_streak:
                fishing_state.record_streak = fishing_state.current_streak
            if fishing_state.current_streak:
                default = (
                    f"{fishing_state.current_streak} in a row! You feel like you might "
                    "be able to catch a very special fish..."
                )
                print(self.streak_dialogue.get(fishing_state.current_streak, default))

    def _print_records(self, fishing_state: FishingState):
        if fishing_state.record_weight:
            print(f"[info]Weight record: {fishing_state.record_weight:.2f} lbs.")
        if fishing_state.record_streak:
            print(f"[info]Streak record: {fishing_state.record_streak} fish in a row")

    def _get_available_fish(self, fishing_state: FishingState) -> list[FishSpecies]:
        available_fish = regular_fish
        if fishing_state.current_streak >= self.min_streak_for_big_chungus:
            available_fish.append(big_chungus)
        return available_fish
