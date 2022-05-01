from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from battle.characters.model import Character


class SideEffect(ABC):
    @abstractmethod
    def apply(self, caster: "Character", target: "Character") -> None:
        pass

    @property
    @abstractmethod
    def description(self) -> Optional[str]:
        pass
