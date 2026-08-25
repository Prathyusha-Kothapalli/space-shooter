"""
Test 3: Enemy damage reception, health depletion, and death callback assertions.
"""

import unittest
from enemies.scout_enemy import ScoutEnemy
from utils.math_utils import Vector2D


class TestEnemy(unittest.TestCase):
    def test_enemy_damage_and_death(self):
        """Verify enemy health reduction and active flag deactivation on death."""
        enemy = ScoutEnemy()
        enemy.spawn(Vector2D(200, 200))

        self.assertTrue(enemy.is_active)
        self.assertEqual(enemy.health.current_health, 35.0)

        # Non-lethal damage
        enemy.health.take_damage(20.0)
        self.assertEqual(enemy.health.current_health, 15.0)
        self.assertTrue(enemy.is_active)

        # Lethal damage
        enemy.health.take_damage(20.0)
        self.assertEqual(enemy.health.current_health, 0.0)
        self.assertFalse(enemy.is_active)


if __name__ == "__main__":
    unittest.main()

