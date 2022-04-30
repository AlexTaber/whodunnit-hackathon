from scenes.model import Scene
from scenes.room import RoomScene


class KitchenScene(Scene):
    def __init__(self, room):
        self.room_scene = RoomScene(room)

    def run(self):
        return self.room_scene.prompt_action()
