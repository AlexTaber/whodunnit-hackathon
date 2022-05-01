from engine.scene import Scene
from engine.game import game
from engine.printer import input, print

class RoomScene(Scene):
    def __init__(self, room):
        self.room = room

    def run(self) -> Scene:
        print(f"{self.room.description}")
        print("What do you want to do?")
        input_value = input(self._get_input_options())

        if input_value == "Go To Room":
            print("Where do you want to go?")
            name = input(game.state.current_place.room_names)
            room = next(r for r in game.state.current_place.rooms if r.name == name)
            return room.scene

        selected_action = next((a for a in self.room.actions if a.name == input_value), None)
        if selected_action:
            return selected_action.scene() if callable(selected_action.scene) else selected_action.scene

    def _get_input_options(self) -> list[str]:
        options = []

        if len(game.state.current_place.rooms) > 1:
            options.append("Go To Room")

        return options + [action.name for action in self.room.actions]
