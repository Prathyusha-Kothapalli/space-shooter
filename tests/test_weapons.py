"""
Test 2: Weapon firing, heat buildup, and cooldown assertions.
"""

import unittest
from weapons.pulse_cannon import PulseCannon
from projectiles.projectile_pool import ProjectilePool
from utils.math_utils import Vector2D


class TestWeapons(unittest.TestCase):
    def test_weapon_firing_and_cooldown(self):
        """Verify weapon fire triggers cooldowns, generates projectiles, and accumulates heat."""
        weapon = PulseCannon()
        pool = ProjectilePool()

        origin = Vector2D(100, 100)
        direction = Vector2D.up()

        # 1. Fire weapon successfully
        fired = weapon.fire(origin, direction, pool)
        self.assertTrue(len(fired) > 0)
        self.assertTrue(weapon.heat > 0.0)
        self.assertFalse(weapon.cooldown.is_ready())

        # 2. Immediate second fire fails due to cooldown
        fired_second = weapon.fire(origin, direction, pool)
        self.assertEqual(len(fired_second), 0)

        # 3. Update cooldown timer and fire again
        weapon.update(0.2)
        self.assertTrue(weapon.cooldown.is_ready())
        fired_third = weapon.fire(origin, direction, pool)
        self.assertTrue(len(fired_third) > 0)


if __name__ == "__main__":
    unittest.main()

