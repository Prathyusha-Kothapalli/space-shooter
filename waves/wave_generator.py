"""
Procedural Wave Generator calculating wave enemy compositions and boss milestones.
"""

import random
from typing import Dict, List, Any, Optional
from utils.math_utils import Vector2D
from configuration.constants import (
    ENEMY_SCOUT, ENEMY_INTERCEPTOR, ENEMY_CRUISER,
    ENEMY_BOMBER, ENEMY_STEALTH, BOSS_VOID_DREADNOUGHT, BOSS_STARLIGHT_CARRIER,
    SCREEN_WIDTH
)


class WaveData:
    """Encapsulates composition of a wave."""
    def __init__(self, wave_number: int, enemies_to_spawn: List[Dict[str, Any]], is_boss_wave: bool = False, boss_type: Optional[str] = None):
        self.wave_number = wave_number
        self.enemies_to_spawn = enemies_to_spawn
        self.is_boss_wave = is_boss_wave
        self.boss_type = boss_type


class WaveGenerator:
    """Generates scaling wave compositions based on wave number."""

    @staticmethod
    def generate_wave(wave_number: int) -> WaveData:
        """Construct wave definition."""
        # Boss Waves every 5th wave
        if wave_number % 10 == 0:
            return WaveData(wave_number, [], is_boss_wave=True, boss_type=BOSS_STARLIGHT_CARRIER)
        elif wave_number % 5 == 0:
            return WaveData(wave_number, [], is_boss_wave=True, boss_type=BOSS_VOID_DREADNOUGHT)

        # Standard Procedural Waves
        total_enemy_count = 5 + int(wave_number * 2.5)
        enemies_list: List[Dict[str, Any]] = []

        available_types = [ENEMY_SCOUT]
        if wave_number >= 2:
            available_types.append(ENEMY_INTERCEPTOR)
        if wave_number >= 3:
            available_types.append(ENEMY_CRUISER)
        if wave_number >= 4:
            available_types.append(ENEMY_BOMBER)
        if wave_number >= 6:
            available_types.append(ENEMY_STEALTH)

        for i in range(total_enemy_count):
            e_type = random.choice(available_types)
            spawn_x = random.uniform(50.0, SCREEN_WIDTH - 50.0)
            spawn_y = -random.uniform(50.0, 400.0)
            enemies_list.append({
                "type": e_type,
                "position": Vector2D(spawn_x, spawn_y)
            })

        return WaveData(wave_number, enemies_list)
