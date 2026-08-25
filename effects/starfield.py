"""
Multi-Layered Parallax Scrolling Starfield Background with space dust.
"""

import random
from typing import List, Tuple
from utils.math_utils import Vector2D
from configuration.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LAYER_STARFIELD_FAR, LAYER_STARFIELD_NEAR


class Star:
    """Individual background star."""
    def __init__(self, x: float, y: float, speed: float, size: float, color: Tuple[int, int, int]):
        self.position = Vector2D(x, y)
        self.speed = speed
        self.size = size
        self.color = color


class Starfield:
    """3-layer parallax starfield background."""

    def __init__(self, star_count: int = 150):
        self.stars: List[Star] = []

        # Layer 1: Distant slow stars
        for _ in range(star_count // 3):
            self.stars.append(Star(
                random.uniform(0, SCREEN_WIDTH),
                random.uniform(0, SCREEN_HEIGHT),
                speed=25.0,
                size=1.0,
                color=(120, 140, 180)
            ))

        # Layer 2: Mid-distance stars
        for _ in range(star_count // 3):
            self.stars.append(Star(
                random.uniform(0, SCREEN_WIDTH),
                random.uniform(0, SCREEN_HEIGHT),
                speed=60.0,
                size=1.5,
                color=(180, 200, 240)
            ))

        # Layer 3: Foreground fast space dust
        for _ in range(star_count // 3):
            self.stars.append(Star(
                random.uniform(0, SCREEN_WIDTH),
                random.uniform(0, SCREEN_HEIGHT),
                speed=120.0,
                size=2.0,
                color=(240, 245, 255)
            ))

    def update(self, dt: float) -> None:
        """Scroll stars downward and wrap at bottom boundary."""
        for star in self.stars:
            star.position.y += star.speed * dt
            if star.position.y >= SCREEN_HEIGHT:
                star.position.y = 0.0
                star.position.x = random.uniform(0, SCREEN_WIDTH)

    def render(self, surface: any) -> None:
        try:
            import pygame
            for star in self.stars:
                pygame.draw.circle(surface, star.color, star.position.to_int_tuple(), int(star.size))
        except Exception:
            pass
