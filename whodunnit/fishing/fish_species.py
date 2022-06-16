from whodunnit.engine.fishing.models import FishSpecies
from whodunnit.fishing.fish_groups import large_fish, medium_fish, omega_fish, small_fish

rainbow_smelt = FishSpecies(
    name="Rainbow Smelt",
    avg_weight=0.3,
    stdev_weight=0.1,
    fish_group=small_fish,
    population=20,
)

porgy = FishSpecies(
    name="Porgy",
    avg_weight=0.8,
    stdev_weight=0.4,
    fish_group=small_fish,
    population=20,
)

feral_goldfish = FishSpecies(
    name="Feral Goldfish",
    avg_weight=3.0,
    stdev_weight=2,
    fish_group=small_fish,
    population=20,
)

eel = FishSpecies(
    name="Eel",
    avg_weight=1,
    stdev_weight=5,
    fish_group=small_fish,
    population=20,
)

alewife_herring = FishSpecies(
    name="Alewife Herring",
    avg_weight=0.25,
    stdev_weight=0.1,
    fish_group=small_fish,
    population=20,
)

oyster_toadfish = FishSpecies(
    name="Oyster Toadfish",
    avg_weight=3,
    stdev_weight=1,
    fish_group=medium_fish,
    population=20,
)

fluke = FishSpecies(
    name="Fluke", avg_weight=4, stdev_weight=1, fish_group=medium_fish, population=20
)

blackfish = FishSpecies(
    name="Blackfish",
    avg_weight=6,
    stdev_weight=3,
    fish_group=medium_fish,
    population=20,
)

black_seabass = FishSpecies(
    name="Black Seabass",
    avg_weight=5.5,
    stdev_weight=1,
    fish_group=medium_fish,
    population=20,
)

tire = FishSpecies(
    name="Tire", avg_weight=22, stdev_weight=5, fish_group=large_fish, population=15
)

bluefish = FishSpecies(
    name="Bluefish", avg_weight=14, stdev_weight=2, fish_group=large_fish, population=15
)

striped_bass = FishSpecies(
    name="Striped Bass",
    avg_weight=25,
    stdev_weight=7,
    fish_group=large_fish,
    population=15,
)

weakfish = FishSpecies(
    name="Weakfish",
    avg_weight=14,
    stdev_weight=2,
    fish_group=large_fish,
    population=15,
)

catfish = FishSpecies(
    name="Catfish",
    avg_weight=20,
    stdev_weight=5,
    fish_group=large_fish,
    population=15,
)

bluefin_tuna = FishSpecies(
    name="Bluefin Tuna",
    avg_weight=125,
    stdev_weight=30,
    fish_group=large_fish,
    population=5,
)

big_chungus = FishSpecies(
    name="Big Chungus",
    avg_weight=325,
    stdev_weight=50,
    fish_group=omega_fish,
    population=5,
)

regular_fish = [
    rainbow_smelt,
    porgy,
    feral_goldfish,
    eel,
    alewife_herring,
    oyster_toadfish,
    fluke,
    blackfish,
    black_seabass,
    tire,
    bluefish,
    striped_bass,
    weakfish,
    catfish,
    bluefin_tuna,
]
