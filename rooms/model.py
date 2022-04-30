from interactions.model import Interaction
from interactions.model import Interaction
from scenes.model import Scene
from scenes.room import RoomScene


class Room:
    def __init__(self, id: str, name: str, description: str, interactions: list[Interaction]):
        self.id = id
        self.name = name
        self.description = description
        self.interactions = interactions

        self.scene = RoomScene(self)

    def get_names(self) -> list[str]:
        return [interaction.person.name for interaction in self.interactions]

    def get_scene_from_name(self, name: str) -> Scene:
        for interaction in self.interactions:
            if interaction.person.name == name:
                return interaction.scene
