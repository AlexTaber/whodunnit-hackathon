from interactions.model import Interaction
from game.state import game_state
from rooms.model import Room
from persons.model import dan_b, dan_e, dan_i, dan_s, dee, joy
from scenes.dan_b_interview import DanBInterview
from scenes.dan_i_interview import DanIInterviewScene
from scenes.dan_s_interview import DanSInterviewScene
from scenes.daniel_e_interview import DanielEInterviewScene
from scenes.dee_interview import DeeInterviewScene
from scenes.joy_interview import JoyInterviewScene

class Place:
    def __init__(self, id: str, name: str, rooms: list[Room] = []):
        self.id = id
        self.name = name
        self.rooms = rooms

        self._set_room_map()

    @property
    def room_names(self):
        return [room.name for room in self.rooms]

    def _set_room_map(self):
        self.room_map = {}

        for room in self.rooms:
            self.room_map[room.id] = room


def init():
    game_state.current_place = Place(
        id="office",
        name="The Office",
        rooms=[
            Room(
                id="kitchen",
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
            ),

            Room(
                id="engineering_table",
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
            ),

            Room(
                id="bathroom",
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
            )
        ]
    )
