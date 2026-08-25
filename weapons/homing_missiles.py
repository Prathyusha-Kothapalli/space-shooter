"""
Homing Missile Pod weapon implementation.
"""

from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.homing_projectile import HomingProjectile
from projectiles.projectile_base import Projectile


class HomingMissilePod(Weapon):
    """Fires self-guided tracking missiles towards active enemies."""

    def __init__(self):
        super().__init__(name="HOMING_MISSILES", fire_rate=2.5, damage=32.0, energy_cost=8.0)

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(15.0)

        fired: List[Projectile] = []
        dir_norm = direction.normalize()

        num_missiles = 2 if self.level < 3 else 4
        for i in range(num_missiles):
            angle = -0.3 + (i * 0.6 / max(1, num_missiles - 1))
            init_dir = dir_norm.rotate(angle)
            
            proj: HomingProjectile = projectile_pool.acquire(HomingProjectile)
            proj.spawn_homing(origin, init_dir, target, self.base_damage)
            fired.append(proj)

        return fired
