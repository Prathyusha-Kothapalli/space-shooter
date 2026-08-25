"""
Spatial Quadtree Data Structure for efficient $O(N \\log N)$ 2D collision detection queries.
"""

from typing import List, Tuple, Optional, Any
from utils.math_utils import Vector2D, aabb_intersects_aabb, circle_intersects_circle


class QuadtreeRect:
    """Bounding box rect helper for Quadtree nodes."""
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)

    def contains_point(self, point: Vector2D) -> bool:
        return (
            point.x >= self.x and
            point.x <= self.x + self.width and
            point.y >= self.y and
            point.y <= self.y + self.height
        )

    def intersects(self, other: 'QuadtreeRect') -> bool:
        return not (
            other.x > self.x + self.width or
            other.x + other.width < self.x or
            other.y > self.y + self.height or
            other.y + other.height < self.y
        )


class QuadtreeItem:
    """Encapsulates a game object inside the Quadtree with bounding info."""
    def __init__(self, obj: Any, position: Vector2D, radius: float):
        self.obj = obj
        self.position = position
        self.radius = radius
        self.rect = QuadtreeRect(
            position.x - radius,
            position.y - radius,
            radius * 2.0,
            radius * 2.0
        )


class Quadtree:
    """Spatial partitioning Quadtree node."""

    def __init__(self, bounds: QuadtreeRect, max_objects: int = 10, max_levels: int = 5, level: int = 0):
        self.bounds = bounds
        self.max_objects = max_objects
        self.max_levels = max_levels
        self.level = level
        self.objects: List[QuadtreeItem] = []
        self.nodes: List[Optional['Quadtree']] = [None, None, None, None]

    def clear(self) -> None:
        """Clear quadtree node and sub-nodes."""
        self.objects.clear()
        for i in range(4):
            if self.nodes[i] is not None:
                self.nodes[i].clear()
                self.nodes[i] = None

    def _subdivide(self) -> None:
        """Subdivide node into 4 quadrant children."""
        half_w = self.bounds.width / 2.0
        half_h = self.bounds.height / 2.0
        x = self.bounds.x
        y = self.bounds.y

        self.nodes[0] = Quadtree(QuadtreeRect(x + half_w, y, half_w, half_h), self.max_objects, self.max_levels, self.level + 1)
        self.nodes[1] = Quadtree(QuadtreeRect(x, y, half_w, half_h), self.max_objects, self.max_levels, self.level + 1)
        self.nodes[2] = Quadtree(QuadtreeRect(x, y + half_h, half_w, half_h), self.max_objects, self.max_levels, self.level + 1)
        self.nodes[3] = Quadtree(QuadtreeRect(x + half_w, y + half_h, half_w, half_h), self.max_objects, self.max_levels, self.level + 1)

    def insert(self, item: QuadtreeItem) -> bool:
        """Insert object into Quadtree."""
        if not self.bounds.intersects(item.rect):
            return False

        if len(self.objects) < self.max_objects or self.level >= self.max_levels:
            self.objects.append(item)
            return True

        if self.nodes[0] is None:
            self._subdivide()

        inserted = False
        for node in self.nodes:
            if node and node.insert(item):
                inserted = True
                break

        if not inserted:
            self.objects.append(item)
            
        return True

    def query(self, search_rect: QuadtreeRect, found: Optional[List[QuadtreeItem]] = None) -> List[QuadtreeItem]:
        """Return all items inside or intersecting search bounding rect."""
        if found is None:
            found = []

        if not self.bounds.intersects(search_rect):
            return found

        for item in self.objects:
            if search_rect.intersects(item.rect):
                found.append(item)

        if self.nodes[0] is not None:
            for node in self.nodes:
                if node:
                    node.query(search_rect, found)

        return found
