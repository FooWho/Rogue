from __future__ import annotations

from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    parent: Actor

    def __init__(self, hp: int, base_defense_mitigation: int, base_defense_avoidance: int, base_attack_power: int, base_attack_precision: int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense_mitigation = base_defense_mitigation
        self.base_defense_avoidance = base_defense_avoidance
        self.base_attack_power = base_attack_power
        self.base_attack_precision = base_attack_precision

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    @property
    def defense_mitigation(self) -> int:
        return self.base_defense_mitigation + self.defense_mitigation_bonus
    
    @property
    def defense_avoidance(self) -> int:
        return self.base_defense_avoidance + self.defense_avoidance_bonus

    @property
    def attack_power(self) -> int:
        return self.base_attack_power + self.attack_power_bonus

    @property
    def attack_precision(self) -> int:
        return self.base_attack_precision + self.attack_precision_bonus

    @property
    def defense_mitigation_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.defense_mitigation_bonus
        else:
            return 0
        
    @property
    def defense_avoidance_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.defense_avoidance_bonus
        else:
            return 0

    @property
    def attack_power_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.attack_power_bonus
        else:
            return 0
        
    @property
    def attack_precision_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.attack_precision_bonus
        else:
            return 0

    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = color.player_die
        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_color = color.enemy_die

        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_color)

        self.engine.player.level.add_xp(self.parent.level.xp_given)

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount