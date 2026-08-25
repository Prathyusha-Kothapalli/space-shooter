"""
Tech Tree Node Upgrade Definitions and dependency graph.
"""

from typing import Dict, List, Any


class UpgradeNode:
    """Represents a node in the tech tree."""
    def __init__(self, id_name: str, display_name: str, description: str, cost: int, stat_key: str, stat_bonus: float):
        self.id_name = id_name
        self.display_name = display_name
        self.description = description
        self.cost = cost
        self.stat_key = stat_key
        self.stat_bonus = stat_bonus
        self.is_unlocked = False


class TechUpgradeTree:
    """Tech Tree manager for spending skill points on ship upgrades."""

    def __init__(self):
        self.nodes: Dict[str, UpgradeNode] = {
            "OVERLOAD_DAMAGE": UpgradeNode("OVERLOAD_DAMAGE", "Plasma Overload", "+15% All Damage", 1, "damage", 0.15),
            "SHIELD_MATRIX": UpgradeNode("SHIELD_MATRIX", "Shield Capacity Matrix", "+20% Max Shield", 1, "shield", 0.20),
            "HYPER_DRIVE": UpgradeNode("HYPER_DRIVE", "Hyperdrive Thrusters", "+10% Movement Speed", 1, "speed", 0.10),
            "RAPID_FEED": UpgradeNode("RAPID_FEED", "Rapid Fire Feeder", "+10% Fire Rate", 1, "fire_rate", 0.10),
        }

    def unlock_upgrade(self, node_id: str, stats: Any) -> bool:
        """Unlock tech node if skill points available."""
        node = self.nodes.get(node_id)
        if node and not node.is_unlocked and stats.skill_points >= node.cost:
            node.is_unlocked = True
            stats.upgrade_stat(node.stat_key)
            return True
        return False
