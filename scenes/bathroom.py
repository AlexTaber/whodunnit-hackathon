from rooms.model import bathroom

from scenes.model import Scene
from scenes.room import RoomScene


class BathroomScene(Scene):
    def __init__(self):
        self.room_scene = RoomScene(bathroom)

    def run(self):
        return self.room_scene.prompt_action()
