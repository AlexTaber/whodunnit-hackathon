from engine.fishing.models import FishGroup

small_fish = FishGroup(
    hint=(
        "It's a small one. You'll need to use a light "
        "touch so you don't scare it. Can you?"
    ),
    min_reel_power=0,
    max_reel_power=2,
)

medium_fish = FishGroup(
    hint=(
        "It feels like a fair-size fish. You'll need to reel in with "
        "just the right touch -- not too powerful, not too light. "
        "Can you?"
    ),
    min_reel_power=4,
    max_reel_power=6,
)

large_fish = FishGroup(
    hint="It feels big! You'll need some elbow grease to reel it in. Can you?",
    min_reel_power=9,
    max_reel_power=10,
)

omega_fish = FishGroup(
    hint=(
        "It's... |[primary]ENORMOUS|! Could it be?! Yes! You're sure of "
        "it...\nIt's the legendary |[primary]BIG CHUNGUS|!\nYou're gonna need to "
        "muster up extra-human strength to reel in this bad boy."
    ),
    min_reel_power=28,
    max_reel_power=99,
)
