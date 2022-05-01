from pydantic import BaseModel

from engine.battle.move import Move


class Job(BaseModel):
    name: str
    motto: str
    moves: list[Move]
    limit_break: Move
    base_intelligence: int
    base_charisma: int
    base_stamina: int
    base_people_skills: int
