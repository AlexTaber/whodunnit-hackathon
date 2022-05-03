import random
from typing import Optional

from engine.fishing.models import Fish, FishSpecies


class Fishing:
    def __init__(self, species: list[FishSpecies]):
        self.species = species
        self.species_weights = [species.population for species in self.species]
        self.on_hook = None

    def cast(self) -> FishSpecies:
        """Cast a line and return the species of fish on the hook."""
        self.on_hook = random.choices(self.species, self.species_weights)[0]
        return self.on_hook

    def reel(self, reel_power: float) -> Optional[Fish]:
        """Reel the fish in the line and return it if successful."""
        success = (
            self.on_hook
            and self.on_hook.fish_group.min_reel_power
            <= reel_power
            <= self.on_hook.fish_group.max_reel_power
        )
        return (
            Fish(
                species=self.on_hook,
                weight=max(
                    0.05,
                    random.gauss(self.on_hook.avg_weight, self.on_hook.stdev_weight),
                ),
            )
            if self.on_hook and success
            else None
        )
