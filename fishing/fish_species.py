from engine.fishing.models import FishSpecies
from fishing.fish_groups import large_fish, omega_fish, small_fish

rainbow_smelt = FishSpecies(
    name="Rainbow Smelt",
    avg_weight=0.3,
    stdev_weight=0.1,
    fish_group=small_fish,
    population=20,
)

fluke = FishSpecies(
    name="Fluke", avg_weight=4, stdev_weight=1, fish_group=large_fish, population=20
)

porgy = FishSpecies(
    name="Porgy",
    avg_weight=0.8,
    stdev_weight=0.4,
    fish_group=large_fish,
    population=20,
)

oyster_toadfish = FishSpecies(
    name="Oyster Toadfish",
    avg_weight=3,
    stdev_weight=1,
    fish_group=large_fish,
    population=20,
)

big_chungus = FishSpecies(
    name="Big Chungus",
    avg_weight=325,
    stdev_weight=50,
    fish_group=omega_fish,
    population=4,
)

regular_fish = [rainbow_smelt, fluke, porgy, oyster_toadfish]
