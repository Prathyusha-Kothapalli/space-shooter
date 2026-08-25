"""
Collider primitives (Circle, AABB) attached to game entities.
"""

from enum import Enum
from utils.math_utils import Vector2D, circle_intersects_circle, aabb_intersects_aabb


class ColliderType(Enum):
    CIRCLE = "CIRCLE"
    AABB = "AABB"


class Collider:
    """Collider component class."""
    def __init__(self, owner: any, category: int, radius: float = 16.0, box_size: Vector2D = None):
        self.owner = owner
        self.category = category
        self.collider_type = ColliderType.CIRCLE if box_size is None else ColliderType.AABB
        self.radius = float(radius)
        self.box_size = box_size if box_size is not None else Vector2D(radius * 2, radius * 2)
        self.is_active = True

    def get_position(self) -> Vector2D:
        """Get position from owner entity."""
        if hasattr(self.owner, 'position'):
            return self.owner.position
        return Vector2D.zero()

    def intersects(self, other: 'Collider') -> bool:
        """Check intersection with another collider component."""
        if not self.is_active or not other.is_active:
            return False

        pos1 = self.get_position()
        pos2 = other.get_position()

        if self.collider_type == ColliderType.CIRCLE and other.collider_type == ColliderType.CIRCLE:
            return circle_intersects_circle(pos1, self.radius, pos2, other.radius)
        elif self.collider_type == ColliderType.AABB and other.collider_type == ColliderType.AABB:
            return aabb_intersects_aabb(pos1, self.box_size, pos2, other.box_size)
        else:
            # Circle vs AABB fallback
            r = self.radius if self.collider_type == ColliderType.CIRCLE else other.radius
            box_pos = pos2 if self.collider_type == ColliderType.CIRCLE else pos1
            box_size = other.box_size if self.collider_type == ColliderType.CIRCLE else self.box_size
            circle_pos = pos1 if self.collider_type == ColliderType.CIRCLE else pos2

            closest_x = max(box_pos.x, min(circle_pos.x, box_pos.x + box_size.x))
            closest_y = max(box_pos.y, min(circle_pos.y, box_pos.y + box_size.y))
            closest_pt = Vector2D(closest_x, closest_y)

            return circle_pos.distance_squared_to(closest_pt) <= (r * r)
