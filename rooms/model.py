from interactions.model import Interaction
from persons.model import joy
from scenes.joy_interview import JoyInterviewScene
from scenes.model import Scene


class Room:
    def __init__(self, name: str, descrription: str, interactions: list[Interaction]):
        self.name = name
        self.description = descrription
        self.interactions = interactions

    def get_names(self) -> list[str]:
        return [interaction.person.name for interaction in self.interactions]

    def get_scene_from_name(self, name: str) -> Scene:
        for interaction in self.interactions:
            if interaction.person.name == name:
                return interaction.scene


kitchen = Room(
    name="Kitchen",
    descrription="You suddenly feel a wave of hunger as you enter the kitchen.",
    interactions=[
        Interaction(
            person=joy,
            scene=JoyInterviewScene(),
        )
    ],
)
