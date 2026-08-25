"""
Procedural Sector Starmap Generator creating multi-column branching navigation graphs.
"""

import random
from typing import List, Dict, Optional, Set, Any
from utils.math_utils import Vector2D



class SectorNodeType:
    COMBAT = "COMBAT"
    ELITE_COMBAT = "ELITE_COMBAT"
    BOSS = "BOSS"
    SHOP = "SHOP"
    EVENT = "EVENT"
    REPAIR = "REPAIR"
    BLACK_MARKET = "BLACK_MARKET"


class SectorNode:
    """Represents a node in the sector starmap graph."""

    def __init__(self, node_id: str, column: int, row: int, node_type: str, position: Vector2D):
        self.node_id = node_id
        self.column = column
        self.row = row
        self.node_type = node_type
        self.position = position
        self.connected_node_ids: List[str] = []
        self.visited = False
        self.available = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "column": self.column,
            "row": self.row,
            "node_type": self.node_type,
            "position": (self.position.x, self.position.y),
            "connected_node_ids": self.connected_node_ids,
            "visited": self.visited,
            "available": self.available,
        }


class SectorGraph:
    """Contains sector starmap nodes and connection topology."""

    def __init__(self, sector_id: int):
        self.sector_id = sector_id
        self.nodes: Dict[str, SectorNode] = {}
        self.columns: Dict[int, List[SectorNode]] = {}
        self.current_node_id: Optional[str] = None

    def add_node(self, node: SectorNode) -> None:
        self.nodes[node.node_id] = node
        if node.column not in self.columns:
            self.columns[node.column] = []
        self.columns[node.column].append(node)


class SectorGenerator:
    """Generates procedural branching starmap graphs for galactic sectors."""

    @staticmethod
    def generate_sector(sector_id: int, total_columns: int = 8, rows_per_column: int = 4) -> SectorGraph:
        """Generate a procedural multi-branch sector starmap graph."""
        graph = SectorGraph(sector_id)

        # 1. Generate Start Node (Column 0)
        start_node = SectorNode("node_0_0", 0, 0, SectorNodeType.COMBAT, Vector2D(50.0, 360.0))
        start_node.available = True
        graph.add_node(start_node)

        # 2. Generate Intermediate Columns (Columns 1 to total_columns - 2)
        node_counter = 1
        for col in range(1, total_columns - 1):
            num_nodes = random.randint(2, rows_per_column)
            x_pos = 50.0 + (col / (total_columns - 1)) * 1180.0
            
            for row in range(num_nodes):
                y_pos = 100.0 + (row / max(1, num_nodes - 1)) * 520.0
                
                # Determine Node Type weighted by depth
                if col == total_columns - 2:
                    n_type = SectorNodeType.REPAIR
                else:
                    roll = random.random()
                    if roll < 0.45:
                        n_type = SectorNodeType.COMBAT
                    elif roll < 0.65:
                        n_type = SectorNodeType.EVENT
                    elif roll < 0.80:
                        n_type = SectorNodeType.SHOP
                    elif roll < 0.92:
                        n_type = SectorNodeType.ELITE_COMBAT
                    else:
                        n_type = SectorNodeType.BLACK_MARKET

                node_id = f"node_{col}_{row}"
                node = SectorNode(node_id, col, row, n_type, Vector2D(x_pos, y_pos))
                graph.add_node(node)

        # 3. Generate Final Boss Node (Column total_columns - 1)
        boss_node = SectorNode(
            f"node_{total_columns - 1}_0",
            total_columns - 1,
            0,
            SectorNodeType.BOSS,
            Vector2D(1230.0, 360.0)
        )
        graph.add_node(boss_node)

        # 4. Connect Adjacent Columns with Graph Edges
        for col in range(total_columns - 1):
            curr_col_nodes = graph.columns.get(col, [])
            next_col_nodes = graph.columns.get(col + 1, [])

            for node in curr_col_nodes:
                # Ensure each node connects to at least 1 next node
                target = random.choice(next_col_nodes)
                if target.node_id not in node.connected_node_ids:
                    node.connected_node_ids.append(target.node_id)

                # Optional secondary branch connection
                if len(next_col_nodes) > 1 and random.random() < 0.4:
                    sec_target = random.choice(next_col_nodes)
                    if sec_target.node_id not in node.connected_node_ids:
                        node.connected_node_ids.append(sec_target.node_id)

        return graph
