"""
Sector Navigation Manager controlling active starmap graph traversal, fog of war,
and node selection.
"""

from typing import Optional, Dict, Any, List
from sector_map.sector_generator import SectorGenerator, SectorGraph, SectorNode


class SectorManager:
    """Manages active sector starmap state and pathing."""

    def __init__(self, current_sector_id: int = 1):
        self.current_sector_id = current_sector_id
        self.graph: SectorGraph = SectorGenerator.generate_sector(current_sector_id)
        self.visited_history: List[str] = []

    def travel_to_node(self, node_id: str) -> Optional[SectorNode]:
        """Travel player fleet to target starmap node."""
        target_node = self.graph.nodes.get(node_id)
        if not target_node or not target_node.available:
            return None

        # Mark previous node visited
        if self.graph.current_node_id:
            curr = self.graph.nodes.get(self.graph.current_node_id)
            if curr:
                curr.visited = True

        # Set new current node
        self.graph.current_node_id = node_id
        target_node.visited = True
        target_node.available = False
        self.visited_history.append(node_id)

        # Update availability of connected future nodes
        self._update_node_availabilities(target_node)

        return target_node

    def _update_node_availabilities(self, active_node: SectorNode) -> None:
        """Lock unavailable nodes and unlock direct outgoing connections."""
        for n in self.graph.nodes.values():
            n.available = False

        for next_id in active_node.connected_node_ids:
            next_node = self.graph.nodes.get(next_id)
            if next_node and not next_node.visited:
                next_node.available = True
