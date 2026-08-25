"""
Abstract Base Weapon class and weapon mechanics system.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Any
from utils.math_utils import Vector2D
from utils.timer import Cooldown
from projectiles.projectile_base import Projectile


class Weapon(ABC):
    """Abstract Base Class for player and enemy weapons."""

    def __init__(self, name: str, fire_rate: float, damage: float, energy_cost: float = 5.0):
        self.name = name
        self.fire_rate = float(fire_rate)
        self.base_damage = float(damage)
        self.energy_cost = float(energy_cost)
        
        self.cooldown = Cooldown(1.0 / self.fire_rate if self.fire_rate > 0 else 0.1)
        self.level = 1
        self.max_level = 5
        self.heat = 0.0
        self.max_heat = 100.0
        self.is_overheated = False
        self.overheat_cooldown_timer = 0.0

    def update(self, dt: float) -> None:
        """Update weapon cooldowns and heat dissipation."""
        self.cooldown.update(dt)

        if self.is_overheated:
            self.overheat_cooldown_timer -= dt
            if self.overheat_cooldown_timer <= 0.0:
                self.is_overheated = False
                self.heat = 0.0
        else:
            if self.heat > 0.0:
                self.heat = max(0.0, self.heat - 35.0 * dt)

    def can_fire_weapon(self) -> bool:
        """Check if weapon can fire."""
        return self.cooldown.is_ready() and not self.is_overheated

    @abstractmethod
    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        """Fire weapon and return generated projectile instances."""
        pass

    def upgrade_weapon(self) -> bool:
        """Upgrade weapon level, boosting stats."""
        if self.level < self.max_level:
            self.level += 1
            self.base_damage *= 1.2
            self.cooldown.cooldown_time *= 0.9
            return True
        return False


    def add_heat(self, amount: float) -> None:
        """Increase heat buildup."""
        self.heat += amount
        if self.heat >= self.max_heat:
            self.heat = self.max_heat
            self.is_overheated = True
            self.overheat_cooldown_timer = 2.5
