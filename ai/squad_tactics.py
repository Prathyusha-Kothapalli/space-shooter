"""
Squad Tactical Coordination System for multi-ship enemy squad maneuvers.
"""

from typing import List, Any
from utils.math_utils import Vector2D


class SquadTactics:
    """Computes tactical squad movement vectors."""

    @staticmethod
    def calculate_pincher_vectors(squad_members: List[Any], target_pos: Vector2D) -> List[Vector2D]:
        """Compute pincher attack trajectory vectors flanking target from both sides."""
        vectors = []
        for i, member in enumerate(squad_members):
            side = -1.0 if i % 2 == 0 else 1.0
            flank_offset = Vector2D(side * 220.0, -50.0)
            desired_pos = target_pos + flank_offset
            vec = (desired_pos - member.position).normalize() * member.max_speed
            vectors.append(vec)
        return vectors
