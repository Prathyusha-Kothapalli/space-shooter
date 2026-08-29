class AchievementTracker:
    def __init__(self):
        self.unlocked = set()
        self.stats = {'kills': 0, 'bosses': 0, 'score': 0}

    def update_stat(self, stat_name, value):
        self.stats[stat_name] = self.stats.get(stat_name, 0) + value
        self.check_achievements()

    def check_achievements(self):
        if self.stats['kills'] >= 100 and 'sharpshooter' not in self.unlocked:
            self.unlocked.add('sharpshooter')
        if self.stats['bosses'] >= 1 and 'boss_slayer' not in self.unlocked:
            self.unlocked.add('boss_slayer')