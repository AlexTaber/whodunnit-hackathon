from engine.scene import Scene
from engine.world.named_entity import NamedEntity


class Interaction:
    def __init__(self, entity: NamedEntity, scene: Scene):
        self.entity = entity
        self.scene = scene
