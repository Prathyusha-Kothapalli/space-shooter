"""
Homing Missile projectile implementation.
"""

import math
from typing import Optional, Any
from projectiles.projectile_base import Projectile
from configuration.constants import CATEGORY_PLAYER_PROJECTILE, COLOR_ORANGE
from utils.math_utils import Vector2D, clamp


class HomingProjectile(Projectile):
    """Guided homing missile that steers towards target entity."""

    def __init__(self):
        super().__init__(category=CATEGORY_PLAYER_PROJECTILE)
        self.target: Optional[Any] = None
        self.turn_rate = math.radians(280.0)  # rad/sec
        self.speed = 450.0
        self.color = COLOR_ORANGE
        self.collider.radius = 8.0

    def spawn_homing(self, position: Vector2D, initial_dir: Vector2D, target: Optional[Any], damage: float, speed: float = 450.0) -> None:
        velocity = initial_dir.normalize() * speed
        super().spawn(position, velocity, damage, lifetime=5.0)
        self.target = target
        self.speed = speed

    def update(self, dt: float) -> None:
        if not self.is_active:
            return

        # Check if target is valid and active
        if self.target and hasattr(self.target, 'is_active') and self.target.is_active and hasattr(self.target, 'position'):
            target_pos = self.target.position
            desired_dir = (target_pos - self.position).normalize()
            current_dir = self.velocity.normalize()

            # Steer vector towards desired direction
            angle_diff = current_dir.cross(desired_dir)
            rotation = clamp(angle_diff, -self.turn_rate * dt, self.turn_rate * dt)
            
            new_dir = current_dir.rotate(rotation).normalize()
            self.velocity = new_dir * self.speed

        super().update(dt)

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            pygame.draw.circle(surface, self.color, self.position.to_int_tuple(), int(self.collider.radius))
            # Exhaust line
            tail = self.position - self.velocity.normalize() * 12.0
            pygame.draw.line(surface, (255, 255, 200), self.position.to_int_tuple(), tail.to_int_tuple(), 2)
        except Exception:
            pass
