from pydantic import BaseModel
from scenes.model import Scene


class Game(BaseModel):
    current_scene: Scene
