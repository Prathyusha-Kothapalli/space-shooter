"""
Player Projectile implementations.
"""

from projectiles.projectile_base import Projectile
from configuration.constants import CATEGORY_PLAYER_PROJECTILE, COLOR_CYAN, COLOR_YELLOW, COLOR_MAGENTA
from utils.math_utils import Vector2D


class PlayerProjectile(Projectile):
    """Standard laser or energy shot fired by player."""

    def __init__(self, weapon_type: str = "PULSE_CANNON"):
        super().__init__(category=CATEGORY_PLAYER_PROJECTILE)
        self.weapon_type = weapon_type
        self.color = COLOR_CYAN
        self.trail_history = []

    def spawn(self, position: Vector2D, velocity: Vector2D, damage: float, weapon_type: str = "PULSE_CANNON", lifetime: float = 4.0) -> None:
        super().spawn(position, velocity, damage, lifetime)
        self.weapon_type = weapon_type
        self.trail_history.clear()

        if weapon_type == "PULSE_CANNON":
            self.color = COLOR_CYAN
            self.collider.radius = 6.0
        elif weapon_type == "SPREAD_SHOT":
            self.color = COLOR_YELLOW
            self.collider.radius = 5.0
        elif weapon_type == "HEAVY_PLASMA":
            self.color = COLOR_MAGENTA
            self.collider.radius = 12.0

    def update(self, dt: float) -> None:
        if not self.is_active:
            return
        
        # Save trail point
        self.trail_history.append(Vector2D(self.position.x, self.position.y))
        if len(self.trail_history) > 6:
            self.trail_history.pop(0)

        super().update(dt)

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            # Draw glow circle
            pygame.draw.circle(surface, self.color, self.position.to_int_tuple(), int(self.collider.radius))
            pygame.draw.circle(surface, (255, 255, 255), self.position.to_int_tuple(), int(self.collider.radius * 0.5))
        except Exception:
            pass
