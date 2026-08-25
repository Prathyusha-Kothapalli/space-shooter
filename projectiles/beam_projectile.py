"""
Beam Projectile for continuous ray / line energy cannon weapon.
"""

from projectiles.projectile_base import Projectile
from configuration.constants import CATEGORY_PLAYER_PROJECTILE, COLOR_GREEN
from utils.math_utils import Vector2D


class BeamProjectile(Projectile):
    """Instant continuous beam line energy weapon."""

    def __init__(self):
        super().__init__(category=CATEGORY_PLAYER_PROJECTILE)
        self.start_pos = Vector2D.zero()
        self.end_pos = Vector2D.zero()
        self.beam_width = 8.0

    def spawn_beam(self, start_pos: Vector2D, end_pos: Vector2D, damage: float, duration: float = 0.2) -> None:
        self.start_pos = Vector2D(start_pos.x, start_pos.y)
        self.end_pos = Vector2D(end_pos.x, end_pos.y)
        mid_pos = (start_pos + end_pos) * 0.5
        super().spawn(mid_pos, Vector2D.zero(), damage, lifetime=duration)
        self.collider.radius = (start_pos.distance_to(end_pos)) * 0.5

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.line(surface, COLOR_GREEN, self.start_pos.to_int_tuple(), self.end_pos.to_int_tuple(), int(self.beam_width))
            pygame.draw.line(surface, (255, 255, 255), self.start_pos.to_int_tuple(), self.end_pos.to_int_tuple(), int(self.beam_width * 0.4))
        except Exception:
            pass
