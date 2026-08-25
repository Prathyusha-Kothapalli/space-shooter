"""
Player Stats and Experience Level Progression tracking data structure.
"""

class PlayerStats:
    """Tracks XP, Levels, Skill Points, and Stat Multipliers."""

    def __init__(self):
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        self.skill_points = 0

        # Upgrade Stat Multipliers
        self.speed_multiplier = 1.0
        self.damage_multiplier = 1.0
        self.shield_multiplier = 1.0
        self.fire_rate_multiplier = 1.0

    def add_xp(self, amount: int) -> bool:
        """Add XP and handle level ups. Returns True if leveled up."""
        self.xp += amount
        leveled_up = False

        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.skill_points += 1
            self.xp_to_next_level = int(self.xp_to_next_level * 1.35)
            leveled_up = True

        return leveled_up

    def upgrade_stat(self, stat_name: str) -> bool:
        """Spend skill point to boost stat."""
        if self.skill_points <= 0:
            return False

        if stat_name == "speed":
            self.speed_multiplier += 0.1
        elif stat_name == "damage":
            self.damage_multiplier += 0.15
        elif stat_name == "shield":
            self.shield_multiplier += 0.2
        elif stat_name == "fire_rate":
            self.fire_rate_multiplier += 0.1
        else:
            return False

        self.skill_points -= 1
        return True
