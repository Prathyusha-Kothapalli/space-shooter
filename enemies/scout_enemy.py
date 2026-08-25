"""
Scout Enemy implementation (Fast, swooping movement, light laser).
"""

from typing import List, Optional, Any
from enemies.enemy_base import Enemy
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_RED


class ScoutEnemy(Enemy):
    """Scout Class - Agile light reconnaissance fighter."""

    def __init__(self):
        super().__init__(enemy_type="SCOUT", max_health=35.0, max_speed=260.0, score_value=100, xp_value=15)
        self.collider.radius = 14.0
        self.fire_cooldown = 1.8

    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        fired = []
        dir_to_player = Vector2D.down()
        if player_target and hasattr(player_target, 'position'):
            dir_to_player = (player_target.position - self.position).normalize()

        proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
        proj.spawn(self.position + Vector2D(0, 15), dir_to_player * 450.0, damage=12.0)
        fired.append(proj)
        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            p1 = (int(self.position.x), int(self.position.y + 14))
            p2 = (int(self.position.x - 12), int(self.position.y - 12))
            p3 = (int(self.position.x + 12), int(self.position.y - 12))
            pygame.draw.polygon(surface, COLOR_RED, [p1, p2, p3])
        except Exception:
            pass
