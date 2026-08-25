"""
Achievement system tracking milestone unlocks and player progress.
"""

from typing import Dict, List, Any


class Achievement:
    """Represents a game achievement milestone."""
    def __init__(self, id_name: str, title: str, description: str, secret: bool = False):
        self.id_name = id_name
        self.title = title
        self.description = description
        self.secret = secret
        self.unlocked = False


class AchievementManager:
    """Manages tracking and unlocking of achievements."""

    def __init__(self):
        self.achievements: Dict[str, Achievement] = {
            "FIRST_BLOOD": Achievement("FIRST_BLOOD", "First Blood", "Destroy your first enemy ship."),
            "SCOUT_HUNTER": Achievement("SCOUT_HUNTER", "Scout Hunter", "Destroy 50 Scout ships."),
            "DREADNOUGHT_SLAYER": Achievement("DREADNOUGHT_SLAYER", "Dreadnought Slayer", "Defeat the Void Dreadnought boss."),
            "CARRIER_DOWN": Achievement("CARRIER_DOWN", "Carrier Down", "Defeat the Starlight Carrier mothership."),
            "HIGH_SCORE_100K": Achievement("HIGH_SCORE_100K", "Ace Pilot", "Reach a score of 100,000 points."),
            "SURVIVOR": Achievement("SURVIVOR", "Veteran Survivor", "Survive 10 waves without dying."),
        }

    def check_achievements(self, stats: Dict[str, Any]) -> List[Achievement]:
        """Check for unlocked achievements based on session statistics."""
        newly_unlocked = []

        kills = stats.get("total_kills", 0)
        score = stats.get("high_score", 0)
        bosses = stats.get("bosses_defeated", 0)

        if kills >= 1 and self._try_unlock("FIRST_BLOOD"):
            newly_unlocked.append(self.achievements["FIRST_BLOOD"])
        if kills >= 50 and self._try_unlock("SCOUT_HUNTER"):
            newly_unlocked.append(self.achievements["SCOUT_HUNTER"])
        if bosses >= 1 and self._try_unlock("DREADNOUGHT_SLAYER"):
            newly_unlocked.append(self.achievements["DREADNOUGHT_SLAYER"])
        if bosses >= 2 and self._try_unlock("CARRIER_DOWN"):
            newly_unlocked.append(self.achievements["CARRIER_DOWN"])
        if score >= 100000 and self._try_unlock("HIGH_SCORE_100K"):
            newly_unlocked.append(self.achievements["HIGH_SCORE_100K"])

        return newly_unlocked

    def _try_unlock(self, id_name: str) -> bool:
        ach = self.achievements.get(id_name)
        if ach and not ach.unlocked:
            ach.unlocked = True
            return True
        return False
