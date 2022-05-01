from pydantic import BaseModel

from battle.moves.model import Move


class Job(BaseModel):
    name: str
    motto: str
    moves: list[Move]
    limit_break: Move
    base_intelligence: int
    base_charisma: int
    base_stamina: int
    base_people_skills: int
