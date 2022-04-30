from typing import Union
from interactions.model import Interaction
from persons.model import dan_b, dan_e, dan_i, dan_s, dee, joy
from interactions.model import Interaction
from rooms.registry import add_room
from scenes.bathroom import BathroomScene
from scenes.dan_b_interview import DanBInterview
from scenes.dan_i_interview import DanIInterviewScene
from scenes.dan_s_interview import DanSInterviewScene
from scenes.daniel_e_interview import DanielEInterviewScene
from scenes.dee_interview import DeeInterviewScene
from scenes.engineering_table import EngineeringTableScene
from scenes.joy_interview import JoyInterviewScene
from scenes.kitchen import KitchenScene
from scenes.model import Scene


class Room:
    def __init__(self, name: str, description: str, interactions: list[Interaction]):
        self.name = name
        self.description = description
        self.interactions = interactions

        self.scene: Union[Scene, None] = None

    def get_names(self) -> list[str]:
        return [interaction.person.name for interaction in self.interactions]

    def get_scene_from_name(self, name: str) -> Scene:
        for interaction in self.interactions:
            if interaction.person.name == name:
                return interaction.scene

kitchen = add_room(Room(
    name="Kitchen",
    description="You walk into the kitchen. The sink is filled with dirty coffee cups. There's White Claw  & LaCroix cans overflowing the recycling bin. Dan I & Dan S are trying to figure out how to make coffee.",
    interactions=[
        Interaction(
            person=dan_s,
            scene=DanSInterviewScene(),
        ),
        Interaction(
            person=dan_i,
            scene=DanIInterviewScene(),
        ),
    ],
), KitchenScene)

engineering_table = add_room(Room(
    name="Engineering Table",
    description="You walk over to the Engineering Table. Dee and Joy are at the table discussing how to best implement Andrea's hopes & desires for the Candidate flow.",
    interactions=[
        Interaction(
            person=joy,
            scene=JoyInterviewScene(),
        ),
        Interaction(
            person=dee,
            scene=DeeInterviewScene(),
        ),
    ],
), EngineeringTableScene)

bathroom = add_room(Room(
    name="Bathroom",
    description="You make your way to the bathroom. In the hall you see Lauren digging for something in the closet, boxes strewn everywhere. Daniel E & Dan B are standing in line to use the bathroom. Too much coffee for everyone this morning.",
    interactions=[
        Interaction(
            person=dan_e,
            scene=DanielEInterviewScene(),
        ),
        Interaction(
            person=dan_b,
            scene=DanBInterview(),
        ),
    ],
), BathroomScene)

