from rooms.model import kitchen

from scenes.model import Scene
from scenes.room import RoomScene


class KitchenScene(Scene):
    def __init__(self):
        self.room_scene = RoomScene(kitchen)

    def run(self):
        return self.room_scene.prompt_action()
