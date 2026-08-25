"""
Enemy Projectile implementations.
"""

from projectiles.projectile_base import Projectile
from configuration.constants import CATEGORY_ENEMY_PROJECTILE, COLOR_CRIMSON, LAYER_PROJECTILES_ENEMY
from utils.math_utils import Vector2D


class EnemyProjectile(Projectile):
    """Energy bolt or plasma sphere fired by enemies."""

    def __init__(self):
        super().__init__(category=CATEGORY_ENEMY_PROJECTILE)
        self.layer = LAYER_PROJECTILES_ENEMY
        self.color = COLOR_CRIMSON

    def spawn(self, position: Vector2D, velocity: Vector2D, damage: float, lifetime: float = 6.0) -> None:
        super().spawn(position, velocity, damage, lifetime)
        self.collider.radius = 7.0

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.circle(surface, self.color, self.position.to_int_tuple(), int(self.collider.radius))
            pygame.draw.circle(surface, (255, 200, 200), self.position.to_int_tuple(), int(self.collider.radius * 0.4))
        except Exception:
            pass
