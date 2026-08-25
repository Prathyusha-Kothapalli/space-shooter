"""
Continuous Beam Cannon weapon implementation.
"""

from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.beam_projectile import BeamProjectile
from projectiles.projectile_base import Projectile


class BeamCannon(Weapon):
    """Continuous line-of-sight laser beam weapon."""

    def __init__(self):
        super().__init__(name="BEAM_CANNON", fire_rate=5.0, damage=12.0, energy_cost=4.0)

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(8.0)

        fired: List[Projectile] = []
        end_pos = origin + direction.normalize() * 900.0

        proj: BeamProjectile = projectile_pool.acquire(BeamProjectile)
        proj.spawn_beam(origin, end_pos, self.base_damage, duration=0.15)
        fired.append(proj)

        return fired
