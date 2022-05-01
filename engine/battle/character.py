from pydantic import BaseModel

from engine.battle.job import Job


class Character(BaseModel):
    name: str
    level: int
    job: Job
    hp: int
    max_hp: int
    limit_points: int = 0
    max_limit: int = 10

    @property
    def has_limit_break(self):
        return self.limit_points >= self.max_limit

    @property
    def label(self):
        return f"$[primary]Lvl {self.level} {self.job.name} {self.name.upper()}$"
