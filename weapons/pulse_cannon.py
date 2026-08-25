"""
Pulse Cannon Weapon Implementation.
"""

from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.player_projectile import PlayerProjectile
from projectiles.projectile_base import Projectile


class PulseCannon(Weapon):
    """Primary rapid-fire single/twin pulse cannon weapon."""

    def __init__(self):
        super().__init__(name="PULSE_CANNON", fire_rate=8.0, damage=18.0, energy_cost=2.0)
        self.speed = 850.0

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(4.0)

        fired: List[Projectile] = []
        dir_norm = direction.normalize()
        vel = dir_norm * self.speed

        if self.level == 1:
            proj: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
            proj.spawn(origin, vel, self.base_damage, weapon_type="PULSE_CANNON")
            fired.append(proj)
        else:
            # Twin fire for level 2+
            offset = dir_norm.rotate(1.5708) * 10.0
            p1: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
            p1.spawn(origin + offset, vel, self.base_damage, weapon_type="PULSE_CANNON")
            
            p2: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
            p2.spawn(origin - offset, vel, self.base_damage, weapon_type="PULSE_CANNON")
            fired.extend([p1, p2])

        return fired
