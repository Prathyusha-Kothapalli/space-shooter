"""
Wave Manager handling wave state transitions, spawning timers, and victory triggers.
"""

from typing import List, Optional, Any
from waves.wave_generator import WaveGenerator, WaveData
from enemies.enemy_factory import EnemyFactory
from bosses.void_dreadnought import VoidDreadnought
from bosses.starlight_carrier import StarlightCarrier
from utils.logger import log_info


class WaveManager:
    """Manages active wave spawning cycle."""

    def __init__(self):
        self.current_wave_number = 1
        self.active_wave_data: Optional[WaveData] = None
        self.active_enemies: List[Any] = []
        self.active_boss: Optional[Any] = None
        self.wave_completed = False
        self.rest_timer = 0.0

    def start_wave(self, wave_number: int) -> None:
        """Initialize and start wave."""
        self.current_wave_number = wave_number
        self.active_wave_data = WaveGenerator.generate_wave(wave_number)
        self.active_enemies.clear()
        self.active_boss = None
        self.wave_completed = False
        self.rest_timer = 3.0

        log_info("WaveManager", f"Starting Wave #{wave_number} (Boss Wave: {self.active_wave_data.is_boss_wave})")

        if self.active_wave_data.is_boss_wave:
            if self.active_wave_data.boss_type == "STARLIGHT_CARRIER":
                self.active_boss = StarlightCarrier()
            else:
                self.active_boss = VoidDreadnought()
            self.active_boss.spawn()
        else:
            # Spawn regular enemies
            for enemy_info in self.active_wave_data.enemies_to_spawn:
                enemy = EnemyFactory.create_enemy(enemy_info["type"])
                enemy.spawn(enemy_info["position"])
                self.active_enemies.append(enemy)

    def update(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        """Update active wave enemies and boss."""
        fired_projectiles = []

        if self.active_boss and self.active_boss.is_active:
            fired_projectiles.extend(self.active_boss.update(dt, player_target, projectile_pool))

        for enemy in list(self.active_enemies):
            if enemy.is_active:
                fired_projectiles.extend(enemy.update(dt, player_target, projectile_pool))
            else:
                self.active_enemies.remove(enemy)

        # Check wave completion condition
        if not self.wave_completed:
            if self.active_wave_data and self.active_wave_data.is_boss_wave:
                if self.active_boss and not self.active_boss.is_active:
                    self.wave_completed = True
            else:
                if len(self.active_enemies) == 0:
                    self.wave_completed = True

        return fired_projectiles
