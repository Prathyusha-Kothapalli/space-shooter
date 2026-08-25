"""
Abstract Base Boss Class featuring multi-phase state machine and enraged state.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Any
from utils.math_utils import Vector2D, clamp
from combat.health_system import HealthComponent
from collision.collider import Collider
from configuration.constants import CATEGORY_BOSS, LAYER_BOSS, SCREEN_WIDTH, SCREEN_HEIGHT


class Boss(ABC):
    """Abstract Base Class for multi-phase flagship bosses."""

    def __init__(self, boss_name: str, max_health: float, score_value: int = 5000, xp_value: int = 1000):
        self.boss_name = boss_name
        self.position = Vector2D(SCREEN_WIDTH * 0.5, 120.0)
        self.velocity = Vector2D.zero()
        
        self.current_phase = 1
        self.total_phases = 3
        self.is_enraged = False
        
        self.score_value = score_value
        self.xp_value = xp_value
        self.layer = LAYER_BOSS
        self.is_active = False

        self.health = HealthComponent(max_health=max_health, on_death_callback=self._on_death)
        self.collider = Collider(self, category=CATEGORY_BOSS, radius=60.0)
        
        self.phase_timer = 0.0

    def spawn(self) -> None:
        """Spawn boss in upper screen arena."""
        self.position = Vector2D(SCREEN_WIDTH * 0.5, 120.0)
        self.velocity = Vector2D(100.0, 0.0)
        self.current_phase = 1
        self.is_enraged = False
        self.health.current_health = self.health.max_health
        self.health.is_dead = False
        self.is_active = True
        self.collider.is_active = True
        self.phase_timer = 0.0

    def update(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        """Update phase state, arena movement, and phase attack patterns."""
        if not self.is_active or self.health.is_dead:
            return []

        self.health.update(dt)
        self.phase_timer += dt

        # Evaluate Phase Transition based on health milestones
        hp_ratio = self.health.health_percentage()
        if hp_ratio <= 0.33 and self.current_phase < 3:
            self.current_phase = 3
            self.is_enraged = True
            self._on_phase_change(3)
        elif hp_ratio <= 0.66 and self.current_phase < 2:
            self.current_phase = 2
            self._on_phase_change(2)

        # Smooth horizontal arena movement
        self.position += self.velocity * dt
        if self.position.x <= 150.0 or self.position.x >= SCREEN_WIDTH - 150.0:
            self.velocity.x = -self.velocity.x

        return self.execute_phase_attacks(dt, player_target, projectile_pool)

    @abstractmethod
    def execute_phase_attacks(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        """Execute phase specific attack algorithms."""
        pass

    @abstractmethod
    def _on_phase_change(self, new_phase: int) -> None:
        """Handle phase transition effects and stat adjustments."""
        pass

    def _on_death(self) -> None:
        self.is_active = False
        self.collider.is_active = False

    def render(self, surface: any) -> None:
        """Render boss graphics."""
        pass
