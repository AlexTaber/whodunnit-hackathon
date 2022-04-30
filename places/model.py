from rooms.model import Room

class Place:
    def __init__(self, name: str, rooms: list[Room] = []):
        self.name = name
        self.rooms = rooms

        self.room_map = self._get_room_map()

    def _get_room_map(self):
        pass
