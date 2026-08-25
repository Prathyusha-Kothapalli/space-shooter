"""
XP and Level progression manager.
"""

from typing import Dict, Any
from player.player_stats import PlayerStats


class XPManager:
    """Manages level up calculations and XP rewards."""

    def __init__(self, stats: PlayerStats):
        self.stats = stats

    def award_xp(self, amount: int) -> Dict[str, Any]:
        """Award XP and return status of level advancement."""
        old_level = self.stats.level
        leveled_up = self.stats.add_xp(amount)
        return {
            "amount": amount,
            "old_level": old_level,
            "new_level": self.stats.level,
            "leveled_up": leveled_up,
            "skill_points_earned": self.stats.level - old_level
        }
