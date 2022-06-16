from typing import Union
from whodunnit.engine.scene import Scene
from whodunnit.engine.scenes.room import RoomScene


class Room:
    def __init__(self, id: str, name: str, description: str, get_actions: callable = None):
        self.id = id
        self.name = name
        self.description = description
        self.get_actions = get_actions or (lambda: [])

        self.scene = RoomScene(self)
