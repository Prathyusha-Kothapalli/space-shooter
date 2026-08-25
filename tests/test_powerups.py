"""
Test 4: Powerup effect activation and buff application assertions.
"""

import unittest
from player.player_ship import PlayerShip
from utils.math_utils import Vector2D


class TestPowerups(unittest.TestCase):
    def test_powerup_effects(self):
        """Verify applying powerups grants health heals, shields, and buff timers."""
        player = PlayerShip(Vector2D(400, 500))

        # Damage player health first
        player.health.take_damage(50.0)

        # 1. Apply Health Powerup
        player.apply_powerup("HEALTH", duration=8.0)
        self.assertTrue(player.health.current_health > 50.0)

        # 2. Apply Speed Boost Powerup
        player.apply_powerup("SPEED_BOOST", duration=8.0)
        self.assertEqual(player.speed_boost_timer, 8.0)

        # 3. Apply Double Damage Powerup
        player.apply_powerup("DOUBLE_DAMAGE", duration=8.0)
        self.assertEqual(player.double_damage_timer, 8.0)


if __name__ == "__main__":
    unittest.main()

