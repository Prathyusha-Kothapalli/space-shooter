"""
Bomber Enemy implementation (Drops explosive heavy plasma charges).
"""

from typing import List, Optional, Any
from enemies.enemy_base import Enemy
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_LIME


class BomberEnemy(Enemy):
    """Bomber Class - Heavy assault ship deploying area-of-effect plasma charges."""

    def __init__(self):
        super().__init__(enemy_type="BOMBER", max_health=140.0, max_speed=150.0, score_value=280, xp_value=40)
        self.collider.radius = 22.0
        self.fire_cooldown = 2.8

    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        fired = []
        proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
        proj.spawn(self.position + Vector2D(0, 15), Vector2D.down() * 250.0, damage=35.0)
        proj.collider.radius = 12.0  # Large explosive plasma radius
        fired.append(proj)
        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.circle(surface, COLOR_LIME, self.position.to_int_tuple(), 22)
        except Exception:
            pass
