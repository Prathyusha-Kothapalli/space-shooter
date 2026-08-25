"""
Procedural Nebula Cloud Gas Generator for space background aesthetics.
"""

import random
from typing import List, Tuple
from utils.math_utils import Vector2D
from configuration.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class NebulaCloud:
    """Represents a procedural space nebula gas cloud."""

    def __init__(self, position: Vector2D, radius: float, color: Tuple[int, int, int]):
        self.position = position
        self.radius = radius
        self.color = color


class NebulaGenerator:
    """Generates procedural nebula background layers."""

    def __init__(self, cloud_count: int = 5):
        self.clouds: List[NebulaCloud] = []

        colors = [
            (80, 20, 120),   # Purple Nebula
            (10, 60, 140),   # Deep Blue Nebula
            (120, 30, 80),   # Magenta Gas
            (20, 80, 100),   # Cyan Dust
        ]

        for _ in range(cloud_count):
            pos = Vector2D(random.uniform(100, SCREEN_WIDTH - 100), random.uniform(100, SCREEN_HEIGHT - 100))
            rad = random.uniform(150.0, 350.0)
            col = random.choice(colors)
            self.clouds.append(NebulaCloud(pos, rad, col))

    def render(self, surface: any) -> None:
        try:
            import pygame
            for cloud in self.clouds:
                s = pygame.Surface((int(cloud.radius * 2), int(cloud.radius * 2)), pygame.SRCALPHA)
                pygame.draw.circle(s, (*cloud.color, 40), (int(cloud.radius), int(cloud.radius)), int(cloud.radius))
                surface.blit(s, (int(cloud.position.x - cloud.radius), int(cloud.position.y - cloud.radius)))
        except Exception:
            pass
