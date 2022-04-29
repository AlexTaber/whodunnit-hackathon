from game.state import game_state
from printer import input, print
from rooms.model import Room

from scenes.coffee import CoffeeScene
from scenes.model import Scene


class RoomScene:
    def __init__(self, room: Room):
        self.room = room

    def prompt_action(self) -> Scene:
        print(
            f"{self.room.description} In this room is {', '.join(self.room.get_names())}"
        )
        print("What do you want to do?")
        action = input(["Go To Room", "Talk", "Coffee Run"])

        if action == "Go To Room":
            print("Where do you want to go?")
            name = input(game_state.room_names)

        if action == "Talk":
            print("Who do you want to talk to?")
            name = input(self.room.get_names())
            return self.room.get_scene_from_name(name)

        if action == "Coffee Run":
            return CoffeeScene()
