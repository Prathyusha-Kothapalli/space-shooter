"""
Formation Manager for generating squad flight path coordinates (V-Shape, Line, Ring).
"""

import math
from typing import List
from utils.math_utils import Vector2D


class FormationType:
    V_SHAPE = "V_SHAPE"
    LINE = "LINE"
    RING = "RING"


class FormationManager:
    """Calculates offset positions for enemy squads flying in formation."""

    @staticmethod
    def get_formation_offsets(count: int, formation_type: str = FormationType.V_SHAPE, spacing: float = 60.0) -> List[Vector2D]:
        """Generate relative offset coordinates for given squad size."""
        offsets: List[Vector2D] = []

        if formation_type == FormationType.V_SHAPE:
            for i in range(count):
                side = 1 if i % 2 == 1 else -1
                row = (i + 1) // 2
                offsets.append(Vector2D(side * row * spacing, -row * spacing * 0.75))

        elif formation_type == FormationType.LINE:
            start_x = -(count - 1) * spacing * 0.5
            for i in range(count):
                offsets.append(Vector2D(start_x + i * spacing, 0.0))

        elif formation_type == FormationType.RING:
            radius = spacing * (count / (2.0 * math.pi))
            angle_step = (2.0 * math.pi) / count if count > 0 else 0
            for i in range(count):
                angle = i * angle_step
                offsets.append(Vector2D(math.cos(angle) * radius, math.sin(angle) * radius))

        return offsets
