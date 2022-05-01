from engine.world.interaction import Interaction
from engine.world.named_entity import NamedEntity
from engine.world.place import Place
from engine.world.room import Room

from prologue.coffee import CoffeeScene
from world.office.scenes.dan_b_interview import DanBInterviewScene
from world.office.scenes.dan_i_interview import DanIInterviewScene
from world.office.scenes.daniel_e_interview import DanielEInterviewScene
from world.office.scenes.dan_s_interview import DanSInterviewScene
from world.office.scenes.declare_murderer import DelcareMurdererScene
from world.office.scenes.dee_interview import DeeInterviewScene
from world.office.scenes.joy_interview import JoyInterviewScene


def _get_room_actions() -> list[dict]:
    return [
        {
            "name": "Get some coffee",
            "scene": CoffeeScene()
        },

        {
            "name": "Declare Whodunit!",
            "scene": DelcareMurdererScene()
        }
    ]


office = Place(
    id="office",
    name="The Office",
    rooms=[
        Room(
            id="kitchen",
            name="Kitchen",
            description="You walk into the kitchen. The sink is filled with dirty coffee cups. There's White Claw  & LaCroix cans overflowing the recycling bin. Dan I & Dan S are trying to figure out how to make coffee.",
            interactions=[
                Interaction(
                    entity=NamedEntity("dan_s", "Dan S"),
                    scene=DanSInterviewScene(),
                ),
                Interaction(
                    entity=NamedEntity("dan_i", "Dan I"),
                    scene=DanIInterviewScene(),
                ),
            ],
            actions=_get_room_actions()
        ),

        Room(
            id="engineering_table",
            name="Engineering Table",
            description="You walk over to the Engineering Table. Dee and Joy are at the table discussing how to best implement Andrea's hopes & desires for the Candidate flow.",
            interactions=[
                Interaction(
                    entity=NamedEntity("joy", "Joy"),
                    scene=JoyInterviewScene(),
                ),
                Interaction(
                    entity=NamedEntity("dee", "Dee"),
                    scene=DeeInterviewScene(),
                ),
            ],
            actions=_get_room_actions()
        ),

        Room(
            id="bathroom",
            name="Bathroom",
            description="You make your way to the bathroom. In the hall you see Lauren digging for something in the closet, boxes strewn everywhere. Daniel E & Dan B are standing in line to use the bathroom. Too much coffee for everyone this morning.",
            interactions=[
                Interaction(
                    entity=NamedEntity("daniel_e", "Daniel E"),
                    scene=DanielEInterviewScene(),
                ),
                Interaction(
                    entity=NamedEntity("dan_b", "Dan B"),
                    scene=DanBInterviewScene(),
                ),
            ],
            actions=_get_room_actions()
        )
    ]
)

office.default_room = office.room_map.get("engineering_table")
