"""
Base Projectile class representing active projectiles in the game world.
"""

from utils.math_utils import Vector2D
from collision.collider import Collider
from configuration.constants import LAYER_PROJECTILES_PLAYER


class Projectile:
    """Base class for all energy shots, plasma blasts, and missiles."""

    def __init__(self, category: int):
        self.position = Vector2D.zero()
        self.velocity = Vector2D.zero()
        self.damage = 10.0
        self.lifetime = 5.0
        self.age = 0.0
        self.is_active = False
        self.layer = LAYER_PROJECTILES_PLAYER
        self.collider = Collider(self, category=category, radius=6.0)

    def spawn(self, position: Vector2D, velocity: Vector2D, damage: float, lifetime: float = 5.0) -> None:
        """Spawn or re-activate projectile from object pool."""
        self.position = Vector2D(position.x, position.y)
        self.velocity = Vector2D(velocity.x, velocity.y)
        self.damage = float(damage)
        self.lifetime = float(lifetime)
        self.age = 0.0
        self.is_active = True
        self.collider.is_active = True

    def update(self, dt: float) -> None:
        """Update projectile position and age."""
        if not self.is_active:
            return

        self.position += self.velocity * dt
        self.age += dt

        if self.age >= self.lifetime:
            self.deactivate()

    def deactivate(self) -> None:
        """Deactivate projectile for recycling."""
        self.is_active = False
        self.collider.is_active = False

    def render(self, surface: any) -> None:
        """Render projectile sprite or vector shape."""
        pass
