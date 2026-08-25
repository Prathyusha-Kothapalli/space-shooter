"""
Stealth Drone Enemy implementation (Cloaking mechanism, surprise ambush).
"""

from typing import List, Optional, Any
from enemies.enemy_base import Enemy
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_DARK_GRAY, COLOR_CYAN


class StealthDroneEnemy(Enemy):
    """Stealth Drone - Cloaked unit that uncloaks to fire ambush bursts."""

    def __init__(self):
        super().__init__(enemy_type="STEALTH", max_health=70.0, max_speed=320.0, score_value=250, xp_value=35)
        self.collider.radius = 15.0
        self.fire_cooldown = 2.0
        self.is_cloaked = True
        self.cloak_timer = 0.0

    def update(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        self.cloak_timer += dt
        if self.cloak_timer >= 3.0:
            self.cloak_timer = 0.0
            self.is_cloaked = not self.is_cloaked

        return super().update(dt, player_target, projectile_pool)

    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        fired = []
        if self.is_cloaked:
            return fired  # Cannot fire while cloaked

        dir_to_player = Vector2D.down()
        if player_target and hasattr(player_target, 'position'):
            dir_to_player = (player_target.position - self.position).normalize()

        proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
        proj.spawn(self.position, dir_to_player * 550.0, damage=20.0)
        fired.append(proj)
        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            color = COLOR_DARK_GRAY if self.is_cloaked else COLOR_CYAN
            pygame.draw.circle(surface, color, self.position.to_int_tuple(), 15, 2 if self.is_cloaked else 0)
        except Exception:
            pass
