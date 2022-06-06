from abc import ABC, abstractmethod
from typing import Optional


class Scene(ABC):
    @abstractmethod
    def run(self) -> Optional["Scene"]:
        """Commands that eventually pass off to another scene"""
        pass
