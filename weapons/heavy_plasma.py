"""
Heavy Plasma Cannon weapon implementation.
"""

from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.player_projectile import PlayerProjectile
from projectiles.projectile_base import Projectile


class HeavyPlasma(Weapon):
    """Slow-moving high-damage explosive plasma cannon."""

    def __init__(self):
        super().__init__(name="HEAVY_PLASMA", fire_rate=2.0, damage=55.0, energy_cost=12.0)
        self.speed = 400.0

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(22.0)

        fired: List[Projectile] = []
        vel = direction.normalize() * self.speed
        
        proj: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
        proj.spawn(origin, vel, self.base_damage, weapon_type="HEAVY_PLASMA", lifetime=6.0)
        fired.append(proj)

        return fired
