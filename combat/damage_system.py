"""
Damage calculation system incorporating damage types, critical hits,
difficulty scalers, and armor penetration.
"""

import random
from typing import Dict, Any


class DamageType:
    PHYSICAL = "PHYSICAL"
    ENERGY = "ENERGY"
    PLASMA = "PLASMA"
    EXPLOSIVE = "EXPLOSIVE"


class DamagePayload:
    """Calculates final damage values based on attacker stats and target attributes."""

    def __init__(
        self,
        base_damage: float,
        damage_type: str = DamageType.ENERGY,
        crit_chance: float = 0.05,
        crit_multiplier: float = 1.5,
        armor_pen: float = 0.0
    ):
        self.base_damage = float(base_damage)
        self.damage_type = damage_type
        self.crit_chance = float(crit_chance)
        self.crit_multiplier = float(crit_multiplier)
        self.armor_pen = float(armor_pen)

    def calculate_final_damage(self, difficulty_mult: float = 1.0, damage_boost: float = 1.0) -> Dict[str, Any]:
        """Compute final damage value and critical hit determination."""
        is_crit = random.random() < self.crit_chance
        mult = (self.crit_multiplier if is_crit else 1.0) * difficulty_mult * damage_boost
        final_dmg = self.base_damage * mult

        return {
            "amount": final_dmg,
            "is_crit": is_crit,
            "damage_type": self.damage_type,
        }
