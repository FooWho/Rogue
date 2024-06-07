from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        attack_power_bonus: int = 0,
        attack_precision_bonus: int = 0,
        defense_mitigation_bonus: int = 0,
        defense_avoidance_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.attack_power_bonus = attack_power_bonus
        self.attack_precision_bonus = attack_precision_bonus
        self.defense_mitigation_bonus = defense_mitigation_bonus
        self.defense_avoidance_bonus = defense_avoidance_bonus


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, attack_power_bonus=2)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, attack_power_bonus=4)

class GreatSword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, attack_power_bonus=6)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_mitigation_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_mitigation_bonus=3)

class PlateMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_mitigation_bonus=5)

