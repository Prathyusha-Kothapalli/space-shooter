"""
Test 5: Wave generator composition and boss wave milestone assertions.
"""

import unittest
from waves.wave_generator import WaveGenerator
from waves.wave_manager import WaveManager


class TestWaves(unittest.TestCase):
    def test_wave_progression(self):
        """Verify regular waves spawn scaling enemy counts and wave 5 triggers boss fight."""
        # 1. Standard wave composition scaling
        wave1 = WaveGenerator.generate_wave(1)
        self.assertFalse(wave1.is_boss_wave)
        self.assertTrue(len(wave1.enemies_to_spawn) > 0)

        wave2 = WaveGenerator.generate_wave(2)
        self.assertTrue(len(wave2.enemies_to_spawn) > len(wave1.enemies_to_spawn))

        # 2. Boss Wave 5
        wave5 = WaveGenerator.generate_wave(5)
        self.assertTrue(wave5.is_boss_wave)
        self.assertEqual(wave5.boss_type, "VOID_DREADNOUGHT")

        # 3. Wave Manager execution
        wm = WaveManager()
        wm.start_wave(1)
        self.assertTrue(len(wm.active_enemies) > 0)


if __name__ == "__main__":
    unittest.main()

