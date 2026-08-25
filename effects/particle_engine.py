"""
High-performance Particle Engine for thruster plumes, explosions, debris, and sparks.
"""

import random
from typing import List, Tuple
from utils.math_utils import Vector2D, lerp
from utils.color_utils import lerp_color
from configuration.constants import LAYER_EFFECTS, LAYER_EXPLOSIONS


class Particle:
    """Individual particle instance."""

    def __init__(self):
        self.position = Vector2D.zero()
        self.velocity = Vector2D.zero()
        self.start_color = (255, 255, 255)
        self.end_color = (0, 0, 0)
        self.size = 3.0
        self.end_size = 0.0
        self.lifetime = 1.0
        self.age = 0.0
        self.is_active = False

    def spawn(
        self,
        position: Vector2D,
        velocity: Vector2D,
        start_color: Tuple[int, int, int],
        end_color: Tuple[int, int, int],
        size: float,
        lifetime: float
    ) -> None:
        self.position = Vector2D(position.x, position.y)
        self.velocity = Vector2D(velocity.x, velocity.y)
        self.start_color = start_color
        self.end_color = end_color
        self.size = float(size)
        self.lifetime = float(lifetime)
        self.age = 0.0
        self.is_active = True

    def update(self, dt: float) -> None:
        if not self.is_active:
            return

        self.position += self.velocity * dt
        self.velocity *= 0.96  # Drag dampening
        self.age += dt

        if self.age >= self.lifetime:
            self.is_active = False

    def get_current_color(self) -> Tuple[int, int, int]:
        progress = self.age / self.lifetime if self.lifetime > 0 else 1.0
        return lerp_color(self.start_color, self.end_color, progress)

    def get_current_size(self) -> float:
        progress = self.age / self.lifetime if self.lifetime > 0 else 1.0
        return lerp(self.size, 0.0, progress)


class ParticleEngine:
    """Manages particle emitters and pool rendering."""

    def __init__(self, max_particles: int = 500):
        self.pool: List[Particle] = [Particle() for _ in range(max_particles)]

    def emit_explosion(self, position: Vector2D, count: int = 30, color: Tuple[int, int, int] = (255, 140, 0)) -> None:
        """Create radial explosion particle burst."""
        for _ in range(count):
            angle = random.uniform(0, 6.28318)
            speed = random.uniform(100.0, 450.0)
            vel = Vector2D(1, 0).rotate(angle) * speed
            p = self._get_free_particle()
            if p:
                p.spawn(position, vel, color, (50, 10, 10), random.uniform(3.0, 8.0), random.uniform(0.3, 0.9))

    def emit_thruster(self, position: Vector2D, color: Tuple[int, int, int] = (0, 230, 255)) -> None:
        """Emit rocket exhaust thruster particle."""
        vel = Vector2D(random.uniform(-20, 20), random.uniform(180, 260))
        p = self._get_free_particle()
        if p:
            p.spawn(position, vel, color, (20, 40, 80), random.uniform(2.0, 5.0), random.uniform(0.15, 0.4))

    def update(self, dt: float) -> None:
        for p in self.pool:
            if p.is_active:
                p.update(dt)

    def _get_free_particle(self) -> Optional[Particle]:
        for p in self.pool:
            if not p.is_active:
                return p
        return None

    def render(self, surface: any) -> None:
        try:
            import pygame
            for p in self.pool:
                if p.is_active:
                    col = p.get_current_color()
                    sz = int(max(1, p.get_current_size()))
                    pygame.draw.circle(surface, col, p.position.to_int_tuple(), sz)
        except Exception:
            pass
