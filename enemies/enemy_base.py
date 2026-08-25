"""
Abstract Base Enemy Class defining health, movement AI, weapon firing,
and collision attributes.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Any
from utils.math_utils import Vector2D, clamp
from combat.health_system import HealthComponent
from collision.collider import Collider
from ai.ai_controller import AIController
from configuration.constants import CATEGORY_ENEMY, LAYER_ENEMIES, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(ABC):
    """Abstract Base Class for all enemy space crafts."""

    def __init__(self, enemy_type: str, max_health: float, max_speed: float, score_value: int, xp_value: int):
        self.enemy_type = enemy_type
        self.position = Vector2D.zero()
        self.velocity = Vector2D.zero()
        self.direction = Vector2D.down()
        
        self.max_speed = float(max_speed)
        self.score_value = int(score_value)
        self.xp_value = int(xp_value)
        
        self.layer = LAYER_ENEMIES
        self.is_active = False
        
        self.health = HealthComponent(max_health=max_health, on_death_callback=self._on_death)
        self.collider = Collider(self, category=CATEGORY_ENEMY, radius=18.0)
        self.ai = AIController(self)
        
        self.fire_cooldown = 2.0
        self.fire_timer = 0.0

    def spawn(self, position: Vector2D) -> None:
        """Spawn enemy at designated position."""
        self.position = Vector2D(position.x, position.y)
        self.velocity = Vector2D(0, self.max_speed * 0.5)
        self.health.current_health = self.health.max_health
        self.health.is_dead = False
        self.is_active = True
        self.collider.is_active = True
        self.fire_timer = 0.0

    def update(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        """Update AI steering, movement, and firing."""
        if not self.is_active or self.health.is_dead:
            return []

        # Update Health
        self.health.update(dt)

        # Compute AI steering vector
        steering_force = self.ai.update(dt, player_target)
        self.velocity = (self.velocity + steering_force * dt).clamp_magnitude(self.max_speed)
        self.position += self.velocity * dt

        # Wrap / Clamp bounds
        self.position.x = clamp(self.position.x, 15.0, SCREEN_WIDTH - 15.0)

        # Handle Firing logic
        self.fire_timer += dt
        fired = []
        if self.fire_timer >= self.fire_cooldown:
            self.fire_timer = 0.0
            fired = self.fire_weapons(projectile_pool, player_target)

        return fired

    @abstractmethod
    def fire_weapons(self, projectile_pool: Any, player_target: Optional[Any]) -> List[Any]:
        """Fire enemy weapons and return spawned projectiles."""
        pass

    def _on_death(self) -> None:
        """Callback on entity death."""
        self.is_active = False
        self.collider.is_active = False

    def render(self, surface: any) -> None:
        """Render enemy visuals."""
        pass
