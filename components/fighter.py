from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor

class Fighter(BaseComponent):
    def __init__(self, hp: int, defense: int, power: int) -> None:
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

        @property
        def hp(self) -> int:
            return self.hp
        
        @hp.setter
        def hp(self, value: int) -> None:
            self._hp = max(0, min(value, self.max_hp))

