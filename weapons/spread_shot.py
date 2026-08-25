"""
Spread Shot Weapon Implementation.
"""

import math
from typing import List, Optional, Any
from weapons.weapon_base import Weapon
from utils.math_utils import Vector2D
from projectiles.player_projectile import PlayerProjectile
from projectiles.projectile_base import Projectile


class SpreadShot(Weapon):
    """Multi-projectile cone spread shot weapon."""

    def __init__(self):
        super().__init__(name="SPREAD_SHOT", fire_rate=4.0, damage=14.0, energy_cost=6.0)
        self.speed = 750.0

    def fire(self, origin: Vector2D, direction: Vector2D, projectile_pool: Any, target: Optional[Any] = None) -> List[Projectile]:
        if not self.can_fire_weapon():
            return []

        self.cooldown.trigger()
        self.add_heat(10.0)

        fired: List[Projectile] = []
        dir_norm = direction.normalize()

        num_projectiles = 3 if self.level < 3 else 5
        spread_angle = math.radians(30.0)
        start_angle = -spread_angle / 2.0
        angle_step = spread_angle / (num_projectiles - 1)

        for i in range(num_projectiles):
            angle = start_angle + i * angle_step
            p_dir = dir_norm.rotate(angle)
            vel = p_dir * self.speed
            
            proj: PlayerProjectile = projectile_pool.acquire(PlayerProjectile)
            proj.spawn(origin, vel, self.base_damage, weapon_type="SPREAD_SHOT")
            fired.append(proj)

        return fired
