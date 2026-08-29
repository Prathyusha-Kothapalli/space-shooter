from achievements.tracker import AchievementTracker
from bosses.enrage_system import BossEnrageSystem

def test_achievement_unlock():
    tracker = AchievementTracker()
    tracker.update_stat('kills', 100)
    assert 'sharpshooter' in tracker.unlocked

def test_boss_enrage():
    assert BossEnrageSystem.is_enraged(25, 100) is True
    assert BossEnrageSystem.is_enraged(50, 100) is False