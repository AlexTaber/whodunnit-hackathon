from abc import ABC, abstractmethod

from battle.actions.model import Action
from battle.characters.model import Character


class Player(ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def pick_action(self, enemy: Character) -> Action:
        pass
