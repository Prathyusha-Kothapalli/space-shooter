"""
Game Statistics Tracker recording match metrics and lifetime stats.
"""

from typing import Dict, Any


class StatsTracker:
    """Records gameplay session metrics."""

    def __init__(self):
        self.shots_fired = 0
        self.shots_hit = 0
        self.total_kills = 0
        self.bosses_defeated = 0
        self.damage_dealt = 0.0
        self.damage_taken = 0.0
        self.powerups_collected = 0
        self.time_played_seconds = 0.0

    def record_shot_fired(self) -> None:
        self.shots_fired += 1

    def record_shot_hit(self) -> None:
        self.shots_hit += 1

    def record_kill(self) -> None:
        self.total_kills += 1

    def record_boss_kill(self) -> None:
        self.bosses_defeated += 1

    def record_damage_dealt(self, amount: float) -> None:
        self.damage_dealt += amount

    def record_damage_taken(self, amount: float) -> None:
        self.damage_taken += amount

    def record_powerup(self) -> None:
        self.powerups_collected += 1

    def update_time(self, dt: float) -> None:
        self.time_played_seconds += dt

    def get_accuracy_percentage(self) -> float:
        if self.shots_fired == 0:
            return 0.0
        return (self.shots_hit / self.shots_fired) * 100.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "shots_fired": self.shots_fired,
            "shots_hit": self.shots_hit,
            "accuracy_percent": round(self.get_accuracy_percentage(), 1),
            "total_kills": self.total_kills,
            "bosses_defeated": self.bosses_defeated,
            "damage_dealt": round(self.damage_dealt, 1),
            "damage_taken": round(self.damage_taken, 1),
            "powerups_collected": self.powerups_collected,
            "time_played_seconds": round(self.time_played_seconds, 1),
        }
