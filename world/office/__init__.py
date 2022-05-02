from engine.world.room_action import RoomAction
from engine.world.place import Place
from engine.world.room import Room

from prologue.coffee import CoffeeScene
from state import game_state
from world.office.scenes.dan_b_interview import DanBInterviewScene
from world.office.scenes.dan_i_interview import DanIInterviewScene
from world.office.scenes.daniel_e_interview import DanielEInterviewScene
from world.office.scenes.dan_s_interview import DanSInterviewScene
from world.office.scenes.declare_murderer import DelcareMurdererScene
from world.office.scenes.dee_interview import DeeInterviewScene
from world.office.scenes.joy_interview import JoyInterviewScene
from world.office.scenes.pet_gunner import PetGunnerScene


def _get_room_actions(actions: list[RoomAction]) -> list[RoomAction]:
    def get_base_actions():
        base_actions = [
            RoomAction(name="Coffee run", scene=CoffeeScene()),
            RoomAction(name="Declare Whodunit!", scene=DelcareMurdererScene())
        ]

        if not game_state.pet_gunner:
            base_actions.append(RoomAction(name="Give Gunner Pets", scene=PetGunnerScene()))

        return base_actions

    return lambda: actions + get_base_actions()


office = Place(
    id="office",
    name="The Office",
    rooms=[
        Room(
            id="kitchen",
            name="Kitchen",
            description="You walk into the kitchen. The sink is filled with dirty coffee cups. There's White Claw & LaCroix cans overflowing the recycling bin. Dan I & Dan S are trying to figure out how to make coffee.",
            get_actions=_get_room_actions([
                RoomAction(
                    name="Talk to Dan S",
                    scene=DanSInterviewScene(),
                ),
                RoomAction(
                    name="Talk to Dan I",
                    scene=DanIInterviewScene(),
                ),
            ])
        ),

        Room(
            id="engineering_table",
            name="Engineering Table",
            description="You walk over to the Engineering Table. Dee and Joy are at the table discussing how to best implement Andrea's hopes & desires for the Candidate flow.",
            get_actions=_get_room_actions([
                RoomAction(
                    name="Talk to Joy",
                    scene=JoyInterviewScene(),
                ),
                RoomAction(
                    name="Talk to Dee",
                    scene=DeeInterviewScene(),
                ),
            ])
        ),

        Room(
            id="bathroom",
            name="Bathroom",
            description="You make your way to the bathroom. In the hall you see Lauren digging for something in the closet, boxes strewn everywhere. Daniel E & Dan B are standing in line to use the bathroom. Too much coffee for everyone this morning.",
            get_actions=_get_room_actions([
                RoomAction(
                    name="Talk to Daniel E",
                    scene=DanielEInterviewScene(),
                ),
                RoomAction(
                    name="Talk to Dan B",
                    scene=DanBInterviewScene(),
                ),
            ])
        )
    ]
)

office.default_room = office.room_map.get("engineering_table")
