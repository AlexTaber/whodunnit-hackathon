from engine.scene import Scene
from engine.world.room import Room

class Place:
    def __init__(self, id: str, name: str, rooms: list[Room] = []):
        self.id = id
        self.name = name
        self.rooms = rooms
        self.default_room = None

        self._set_room_map()

    @property
    def room_names(self):
        return [room.name for room in self.rooms]

    @property
    def default_scene(self):
        return (self.default_room or self.rooms[0]).scene

    def _set_room_map(self):
        self.room_map = {}

        for room in self.rooms:
            self.room_map[room.id] = room
