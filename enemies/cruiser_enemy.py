"""
Cruiser Enemy implementation (Heavy armor, triple turret spread shot).
"""

from typing import List, Optional, Any
from enemies.enemy_base import Enemy
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_PURPLE


class CruiserEnemy(Enemy):
    """Cruiser Class - Heavily armored gunship with triple turrets."""

    def __init__(self):
        super().__init__(enemy_type="CRUISER", max_health=180.0, max_speed=120.0, score_value=350, xp_value=50)
        self.collider.radius = 28.0
        self.fire_cooldown = 2.4

    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        fired = []
        center_dir = Vector2D.down()
        if player_target and hasattr(player_target, 'position'):
            center_dir = (player_target.position - self.position).normalize()

        # 3-Way Spread Turret
        left_dir = center_dir.rotate(-0.35)
        right_dir = center_dir.rotate(0.35)

        for d in (left_dir, center_dir, right_dir):
            proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
            proj.spawn(self.position + Vector2D(0, 20), d * 380.0, damage=18.0)
            fired.append(proj)

        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.rect(surface, COLOR_PURPLE, (int(self.position.x - 24), int(self.position.y - 20), 48, 40))
        except Exception:
            pass
