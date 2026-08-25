"""
Interceptor Enemy implementation (Zig-zag movement, rapid twin fire).
"""

from typing import List, Optional, Any
from enemies.enemy_base import Enemy
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_ORANGE


class InterceptorEnemy(Enemy):
    """Interceptor Class - High-speed aggressive fighter craft."""

    def __init__(self):
        super().__init__(enemy_type="INTERCEPTOR", max_health=55.0, max_speed=290.0, score_value=180, xp_value=25)
        self.collider.radius = 16.0
        self.fire_cooldown = 1.2

    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        fired = []
        dir_to_player = Vector2D.down()
        if player_target and hasattr(player_target, 'position'):
            dir_to_player = (player_target.position - self.position).normalize()

        # Twin firing pattern
        p1: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
        p1.spawn(self.position + Vector2D(-10, 10), dir_to_player * 500.0, damage=15.0)

        p2: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
        p2.spawn(self.position + Vector2D(10, 10), dir_to_player * 500.0, damage=15.0)

        fired.extend([p1, p2])
        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.circle(surface, COLOR_ORANGE, self.position.to_int_tuple(), 16)
        except Exception:
            pass
