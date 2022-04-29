from rooms.model import engineering_table

from scenes.model import Scene
from scenes.room import RoomScene


class EngineeringTableScene(Scene):
    def __init__(self):
        self.room_scene = RoomScene(engineering_table)

    def run(self):
        return self.room_scene.prompt_action()
