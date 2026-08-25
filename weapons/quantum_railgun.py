"""
Quantum Railgun weapon implementation.
"""

from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.player_projectile import PlayerProjectile
from projectiles.projectile_base import Projectile


class QuantumRailgun(Weapon):
    """High-velocity energy beam railgun."""

    def __init__(self):
        super().__init__(name="QUANTUM_RAILGUN", fire_rate=1.5, damage=85.0, energy_cost=15.0)
        self.speed = 1800.0

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(30.0)

        fired: List[Projectile] = []
        vel = direction.normalize() * self.speed
        
        proj: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
        proj.spawn(origin, vel, self.base_damage, weapon_type="QUANTUM_RAILGUN", lifetime=3.0)
        fired.append(proj)

        return fired
