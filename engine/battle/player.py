from abc import ABC, abstractmethod

from engine.battle.action import Action
from engine.battle.character import Character


class Player(ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def pick_action(self, enemy: Character) -> Action:
        pass
