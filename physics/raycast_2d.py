"""
2D Raycasting Engine for line-of-sight perception and beam weapon ray intersection.
"""

from typing import Optional, List, Tuple, Any
from utils.math_utils import Vector2D


class RaycastHit2D:
    """Raycast intersection hit result."""

    def __init__(self, hit_entity: Any, point: Vector2D, normal: Vector2D, distance: float):
        self.hit_entity = hit_entity
        self.point = point
        self.normal = normal
        self.distance = distance


class Raycast2D:
    """2D Raycast intersection calculator."""

    @staticmethod
    def cast_ray(origin: Vector2D, direction: Vector2D, max_distance: float, targets: List[Any]) -> Optional[RaycastHit2D]:
        """Cast ray from origin in direction and return closest intersection hit."""
        dir_norm = direction.normalize()
        closest_hit: Optional[RaycastHit2D] = None
        min_dist = max_distance

        for target in targets:
            if not hasattr(target, 'position') or not hasattr(target, 'collider'):
                continue

            target_pos = target.position
            r = getattr(target.collider, 'radius', 15.0)

            # Ray vs Circle intersection
            origin_to_center = target_pos - origin
            projection = origin_to_center.dot(dir_norm)

            if projection < 0 or projection > max_distance:
                continue

            perp_dist_sq = origin_to_center.length_squared() - (projection * projection)

            if perp_dist_sq <= r * r:
                hit_dist = projection - (r * r - perp_dist_sq) ** 0.5
                if hit_dist < min_dist:
                    min_dist = hit_dist
                    hit_pt = origin + dir_norm * hit_dist
                    normal = (hit_pt - target_pos).normalize()
                    closest_hit = RaycastHit2D(target, hit_pt, normal, hit_dist)

        return closest_hit
