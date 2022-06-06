from pydantic import BaseModel


class FishGroup(BaseModel):
    hint: str  # e.g., "This feels like a big one!"
    min_reel_power: int  # Inclusive
    max_reel_power: int  # Inclusive


class FishSpecies(BaseModel):
    name: str
    avg_weight: float
    stdev_weight: float
    fish_group: FishGroup
    population: int


class Fish(BaseModel):
    species: FishSpecies
    weight: float
