"""
Test 9: Spatial Hash Grid partitioning assertions.
"""

import unittest
from physics.spatial_hash import SpatialHashGrid
from utils.math_utils import Vector2D


class DummyEntity:
    def __init__(self, x: float, y: float):
        self.position = Vector2D(x, y)


class TestSpatialHash(unittest.TestCase):
    def test_grid_queries(self):
        """Verify spatial hash grid inserts entities and queries nearby radius items."""
        grid = SpatialHashGrid(cell_size=64.0)

        e1 = DummyEntity(100, 100)
        e2 = DummyEntity(110, 110)
        e3 = DummyEntity(900, 900)

        grid.insert(e1)
        grid.insert(e2)
        grid.insert(e3)

        # Query nearby point (105, 105)
        found = grid.query_radius(Vector2D(105, 105), radius=50.0)

        self.assertIn(e1, found)
        self.assertIn(e2, found)
        self.assertNotIn(e3, found)


if __name__ == "__main__":
    unittest.main()
