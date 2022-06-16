from whodunnit.engine.printer.oscilating_input import get_input_from_oscilating_meter


def get_reel_power(max_power: int = 10) -> int:
    """Get the reel strength from the user."""
    print("Press ENTER to reel in the fish!")
    return get_input_from_oscilating_meter("Reel power", max_power)
