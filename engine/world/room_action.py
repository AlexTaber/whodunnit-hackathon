from typing import Union
from engine.scene import Scene


class RoomAction:
    def __init__(self, name: str, scene: Union[Scene, callable]):
        self.name = name
        self.scene = scene
