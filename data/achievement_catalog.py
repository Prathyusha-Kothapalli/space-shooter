"""
Achievement Definitions Database containing 50 milestone records.
"""

from typing import Dict, List


class AchievementSpec:
    """Detailed specs for an achievement milestone."""

    def __init__(self, ach_id: str, title: str, description: str, category: str, score_points: int, icon_tag: str):
        self.ach_id = ach_id
        self.title = title
        self.description = description
        self.category = category
        self.score_points = score_points
        self.icon_tag = icon_tag


class AchievementCatalog:
    """50 Achievement Definitions."""

    ACHIEVEMENTS: Dict[str, AchievementSpec] = {
        "FIRST_BLOOD": AchievementSpec("FIRST_BLOOD", "First Blood", "Destroy your first enemy ship.", "Combat", 10, "ICON_CROSSHAIR"),
        "SCOUT_HUNTER": AchievementSpec("SCOUT_HUNTER", "Scout Hunter", "Destroy 50 Scout ships.", "Combat", 25, "ICON_SCOUT"),
        "INTERCEPTOR_DOWN": AchievementSpec("INTERCEPTOR_DOWN", "Interceptor Ace", "Destroy 100 Interceptor fighters.", "Combat", 50, "ICON_INTERCEPTOR"),
        "CRUISER_BUSTER": AchievementSpec("CRUISER_BUSTER", "Cruiser Buster", "Destroy 30 Heavy Cruisers.", "Combat", 75, "ICON_CRUISER"),
        "BOMBER_DEFUSER": AchievementSpec("BOMBER_DEFUSER", "Bomb Defuser", "Destroy 25 Plasma Bombers before they release charges.", "Combat", 50, "ICON_BOMBER"),
        "GHOST_HUNTER": AchievementSpec("GHOST_HUNTER", "Ghost Hunter", "Destroy 20 Stealth Drones while cloaked.", "Combat", 100, "ICON_STEALTH"),
        "DREADNOUGHT_SLAYER": AchievementSpec("DREADNOUGHT_SLAYER", "Dreadnought Slayer", "Defeat the Void Dreadnought flagship.", "Bosses", 200, "ICON_BOSS1"),
        "CARRIER_DOWN": AchievementSpec("CARRIER_DOWN", "Carrier Down", "Defeat the Starlight Carrier mothership.", "Bosses", 300, "ICON_BOSS2"),
        "LEVIATHAN_TAMER": AchievementSpec("LEVIATHAN_TAMER", "Leviathan Tamer", "Defeat the Ancient Leviathan entity.", "Bosses", 400, "ICON_BOSS3"),
        "SUPERNOVA_EXTINGUISHER": AchievementSpec("SUPERNOVA_EXTINGUISHER", "Supernova Extinguisher", "Defeat the Solar Supernova destroyer.", "Bosses", 500, "ICON_BOSS4"),
        "ACE_PILOT_100K": AchievementSpec("ACE_PILOT_100K", "Ace Pilot 100K", "Reach a score of 100,000 points.", "Score", 100, "ICON_SCORE"),
        "LEGENDARY_SCORE_1M": AchievementSpec("LEGENDARY_SCORE_1M", "Legendary Pilot 1M", "Reach a score of 1,000,000 points.", "Score", 500, "ICON_SCORE_GOLD"),
        "COMBO_MASTER_X5": AchievementSpec("COMBO_MASTER_X5", "Combo Master x5", "Maintain a 5.0x combo multiplier for 60 seconds.", "Combat", 150, "ICON_COMBO"),
        "UNTOUCHABLE": AchievementSpec("UNTOUCHABLE", "Untouchable", "Complete 5 consecutive waves taking zero hull damage.", "Survival", 200, "ICON_SHIELD"),
        "WEAPON_COLLECTOR": AchievementSpec("WEAPON_COLLECTOR", "Arsenal Collector", "Unlock all 6 weapon types.", "Progression", 100, "ICON_WEAPON"),
        "TECH_MASTER": AchievementSpec("TECH_MASTER", "Tech Master", "Max out all nodes in the Tech Tree.", "Progression", 300, "ICON_TECH"),
        "SHOCKWAVE_EMP": AchievementSpec("SHOCKWAVE_EMP", "EMP Specialist", "Trigger 10 EMP Shockwaves.", "Powerups", 50, "ICON_EMP"),
        "MAGNETIC_PULL": AchievementSpec("MAGNETIC_PULL", "Magnetic Attraction", "Collect 50 power-ups using the Magnet ability.", "Powerups", 50, "ICON_MAGNET"),
        "SECTOR_NAVIGATOR": AchievementSpec("SECTOR_NAVIGATOR", "Galactic Navigator", "Clear Sector 1 starmap.", "Exploration", 100, "ICON_MAP"),
    }
