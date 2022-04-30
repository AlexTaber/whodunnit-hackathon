from game.state import game_state
from printer import input, print

from scenes.coffee import CoffeeScene
from scenes.declare_murderer import DelcareMurdererScene
from scenes.model import Scene


class RoomScene(Scene):
    def __init__(self, room):
        self.room = room

    def run(self) -> Scene:
        print(f"{self.room.description}")
        print("What do you want to do?")
        action = input(["Go To Room", "Talk", "Coffee Run", "Declare Murderer"])

        if action == "Go To Room":
            print("Where do you want to go?")
            name = input(game_state.current_place.room_names)
            room = next(r for r in game_state.current_place.rooms if r.name == name)
            return room.scene

        if action == "Talk":
            print("Who do you want to talk to?")
            name = input(self.room.get_names())
            return self.room.get_scene_from_name(name)

        if action == "Coffee Run":
            return CoffeeScene()

        if action == "Declare Murderer":
            return DelcareMurdererScene()
