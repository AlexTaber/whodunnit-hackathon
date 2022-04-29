from persons.model import Person
from scenes.model import Scene


class Interaction:
    def __init__(self, person: Person, scene: Scene):
        self.person = person
        self.scene = scene
