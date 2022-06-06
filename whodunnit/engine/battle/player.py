from abc import ABC, abstractmethod

from whodunnit.engine.battle.action import Action
from whodunnit.engine.battle.character import Character


class Player(ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def pick_action(self, enemy: Character) -> Action:
        pass
