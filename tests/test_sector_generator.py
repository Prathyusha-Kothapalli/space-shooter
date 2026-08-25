"""
Test 6: Sector Starmap Procedural Graph Generation and Navigation assertions.
"""

import unittest
from sector_map.sector_generator import SectorGenerator, SectorGraph, SectorNodeType
from sector_map.sector_manager import SectorManager


class TestSectorGenerator(unittest.TestCase):
    def test_sector_graph_generation(self):
        """Verify starmap graph contains start node, boss node, and valid connections."""
        graph = SectorGenerator.generate_sector(sector_id=1, total_columns=8)

        self.assertIsNotNone(graph)
        self.assertTrue(len(graph.nodes) >= 8)

        # Verify Start Node (Column 0)
        start_node = graph.columns[0][0]
        self.assertEqual(start_node.node_type, SectorNodeType.COMBAT)
        self.assertTrue(start_node.available)

        # Verify Boss Node (Column 7)
        boss_node = graph.columns[7][0]
        self.assertEqual(boss_node.node_type, SectorNodeType.BOSS)

    def test_sector_manager_traversal(self):
        """Verify traveling to nodes unlocks connected future starmap nodes."""
        manager = SectorManager(current_sector_id=1)
        start_node_id = manager.graph.columns[0][0].node_id

        # Travel to start node
        node = manager.travel_to_node(start_node_id)
        self.assertIsNotNone(node)
        self.assertTrue(node.visited)

        # Verify at least 1 connected next column node becomes available
        available_nodes = [n for n in manager.graph.nodes.values() if n.available]
        self.assertTrue(len(available_nodes) > 0)


if __name__ == "__main__":
    unittest.main()
