"""
Spatial Hash Grid Broadphase Partitioning for high-performance 2D spatial queries.
"""

import math
from typing import Dict, List, Set, Tuple, Any
from utils.math_utils import Vector2D


class SpatialHashGrid:
    """Fast spatial hashing grid for entity queries."""

    def __init__(self, cell_size: float = 64.0):
        self.cell_size = float(cell_size)
        self.grid: Dict[Tuple[int, int], List[Any]] = {}

    def _get_cell_coords(self, pos: Vector2D) -> Tuple[int, int]:
        return (int(math.floor(pos.x / self.cell_size)), int(math.floor(pos.y / self.cell_size)))

    def clear(self) -> None:
        self.grid.clear()

    def insert(self, entity: Any) -> None:
        """Insert entity into spatial grid cell."""
        if not hasattr(entity, 'position'):
            return
        cell = self._get_cell_coords(entity.position)
        if cell not in self.grid:
            self.grid[cell] = []
        self.grid[cell].append(entity)

    def query_radius(self, center: Vector2D, radius: float) -> List[Any]:
        """Return entities in cell buckets surrounding center point within radius."""
        min_cell = self._get_cell_coords(Vector2D(center.x - radius, center.y - radius))
        max_cell = self._get_cell_coords(Vector2D(center.x + radius, center.y + radius))

        found: Set[Any] = set()

        for cx in range(min_cell[0], max_cell[0] + 1):
            for cy in range(min_cell[1], max_cell[1] + 1):
                cell_entities = self.grid.get((cx, cy), [])
                for e in cell_entities:
                    if hasattr(e, 'position') and center.distance_squared_to(e.position) <= radius * radius:
                        found.add(e)

        return list(found)
