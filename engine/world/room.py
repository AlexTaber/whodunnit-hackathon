from engine.world.interaction import Interaction
from engine.world.interaction import Interaction
from engine.scene import Scene
from engine.scenes.room import RoomScene


class Room:
    def __init__(self, id: str, name: str, description: str, interactions: list[Interaction] = [], actions: list[dict] = []):
        self.id = id
        self.name = name
        self.description = description
        self.interactions = interactions
        self.actions = actions

        self.scene = RoomScene(self)

    def get_names(self) -> list[str]:
        return [interaction.entity.name for interaction in self.interactions]

    def get_scene_from_name(self, name: str) -> Scene:
        for interaction in self.interactions:
            if interaction.entity.name == name:
                return interaction.scene
