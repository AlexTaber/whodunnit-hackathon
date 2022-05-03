from typing import Callable, Union

from engine.scene import Scene


class RoomAction:
    def __init__(self, name: str, scene: Union[Scene, Callable]):
        self.name = name
        self.scene = scene
