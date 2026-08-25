"""
Power-Up entity floating items (Health, Shield, Rapid-Fire, Double-Damage, Speed-Boost, EMP, Magnet).
"""

from utils.math_utils import Vector2D
from collision.collider import Collider
from configuration.constants import CATEGORY_POWERUP, LAYER_POWERUPS, POWERUP_DURATION_DEFAULT


class PowerUp:
    """Floating powerup pickup item entity."""

    def __init__(self, powerup_type: str, position: Vector2D):
        self.powerup_type = powerup_type
        self.position = Vector2D(position.x, position.y)
        self.velocity = Vector2D(0.0, 60.0)  # Gentle downward drift
        self.duration = POWERUP_DURATION_DEFAULT
        self.lifetime = 12.0
        self.age = 0.0
        self.is_active = True
        
        self.layer = LAYER_POWERUPS
        self.collider = Collider(self, category=CATEGORY_POWERUP, radius=14.0)

    def update(self, dt: float) -> None:
        """Update floating position and expiry."""
        if not self.is_active:
            return

        self.position += self.velocity * dt
        self.age += dt
        if self.age >= self.lifetime:
            self.deactivate()

    def deactivate(self) -> None:
        self.is_active = False
        self.collider.is_active = False

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            color_map = {
                "HEALTH": (50, 255, 50),
                "SHIELD": (0, 230, 255),
                "RAPID_FIRE": (255, 215, 0),
                "DOUBLE_DAMAGE": (255, 50, 50),
                "SPEED_BOOST": (155, 89, 182),
                "EMP_SHOCKWAVE": (255, 0, 128),
                "MAGNET": (255, 140, 0),
            }
            color = color_map.get(self.powerup_type, (255, 255, 255))
            pygame.draw.circle(surface, color, self.position.to_int_tuple(), 14)
            pygame.draw.circle(surface, (255, 255, 255), self.position.to_int_tuple(), 14, 2)
        except Exception:
            pass
