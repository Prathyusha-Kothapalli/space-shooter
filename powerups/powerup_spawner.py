"""
Power-Up Spawner manager. Evaluates drop chance on enemy kill and spawns items.
"""

import random
from typing import List, Optional
from utils.math_utils import Vector2D
from powerups.powerup_base import PowerUp
from configuration.constants import (
    POWERUP_HEALTH, POWERUP_SHIELD, POWERUP_RAPID_FIRE,
    POWERUP_DOUBLE_DAMAGE, POWERUP_SPEED_BOOST, POWERUP_EMP_SHOCKWAVE, POWERUP_MAGNET
)


class PowerUpSpawner:
    """Manages spawning of power-ups upon enemy destruction."""

    def __init__(self, drop_chance: float = 0.25):
        self.drop_chance = drop_chance
        self.active_powerups: List[PowerUp] = []

    def try_spawn_powerup(self, position: Vector2D) -> Optional[PowerUp]:
        """Roll random chance and spawn a powerup at position."""
        if random.random() <= self.drop_chance:
            types = [
                POWERUP_HEALTH, POWERUP_SHIELD, POWERUP_RAPID_FIRE,
                POWERUP_DOUBLE_DAMAGE, POWERUP_SPEED_BOOST, POWERUP_EMP_SHOCKWAVE, POWERUP_MAGNET
            ]
            chosen_type = random.choice(types)
            powerup = PowerUp(chosen_type, position)
            self.active_powerups.append(powerup)
            return powerup
        return None

    def update(self, dt: float) -> None:
        """Update active powerups."""
        for p in list(self.active_powerups):
            if p.is_active:
                p.update(dt)
            else:
                self.active_powerups.remove(p)
