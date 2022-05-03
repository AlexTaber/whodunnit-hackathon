import datetime
import sys
import threading
import time


class OscillatingMeterPrompt(threading.Thread):
    """Display a meter that rises and falls every 2 seconds."""

    def __init__(self, label: str, num_increments: int):
        super().__init__()
        self.label = label
        self.num_increments = num_increments
        self.increment_length = 1000000 / self.num_increments  # In microseconds
        self.should_run = True

    @property
    def meter_value(self):
        now = datetime.datetime.now()
        ascending = now.second % 2 == 0
        microseconds = now.microsecond

        base_value = int(microseconds // self.increment_length)
        return base_value + 1 if ascending else self.num_increments - base_value

    def run(self):
        current_thread = threading.currentThread()
        while self.should_run:
            # while getattr(current_thread, "should_run", True):
            time.sleep(self.increment_length / 1000000)

            if getattr(current_thread, "should_run", True):
                # Now overwrite what was there in the prompt
                sys.stdout.write("\r" + self.get_prompt())
                sys.stdout.flush()

    def get_prompt(self):
        increments_remaining = self.num_increments - self.meter_value
        return f'{self.label}: [{"▮" * self.meter_value}{" " * increments_remaining}]'

    def set_prompt(self, new_prompt):
        self.prompt = new_prompt


def get_input_from_oscilating_meter(label: str, num_increments: int):
    """Get the reel strength from the user."""
    # Create and start thread to continously overwrite input prompt
    reel_input = OscillatingMeterPrompt(label, num_increments)
    reel_input.start()

    # Get value of meter when user presses "Enter" -- we ignore the actual input
    # value, since we're only interested in the value of the meter
    input(reel_input.get_prompt())
    reel_input.should_run = False
    return reel_input.meter_value


if __name__ == "__main__":
    print("Press ENTER to test your might")
    print(get_input_from_oscilating_meter("POWER", 20))
