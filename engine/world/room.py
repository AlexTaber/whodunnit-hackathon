from engine.scene import Scene
from engine.scenes.room import RoomScene


class Room:
    def __init__(self, id: str, name: str, description: str, actions: list[dict] = []):
        self.id = id
        self.name = name
        self.description = description
        self.actions = actions

        self.scene = RoomScene(self)
