"""
Test 1: Player damage, health reduction, shield absorption, and life loss assertions.
"""

import unittest
from player.player_ship import PlayerShip
from utils.math_utils import Vector2D


class TestPlayer(unittest.TestCase):
    def test_player_health_and_damage(self):
        """Verify player shield absorbs damage first, followed by health and death callbacks."""
        player = PlayerShip(Vector2D(400, 500))

        initial_hp = player.health.current_health
        initial_shield = player.health.current_shield

        self.assertEqual(initial_hp, 100.0)
        self.assertEqual(initial_shield, 100.0)

        # 1. Shield absorbs damage first
        player.health.take_damage(40.0)
        self.assertEqual(player.health.current_shield, 60.0)
        self.assertEqual(player.health.current_health, 100.0)

        # 2. Shield break & direct health damage
        player.health.take_damage(80.0)
        self.assertEqual(player.health.current_shield, 0.0)
        self.assertEqual(player.health.current_health, 80.0)

        # 3. Lethal damage triggers life deduction
        initial_lives = player.lives
        player.health.take_damage(100.0)
        self.assertEqual(player.lives, initial_lives - 1)
        self.assertEqual(player.health.current_health, 100.0)  # Respawned health


if __name__ == "__main__":
    unittest.main()

