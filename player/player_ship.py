"""
Player Spaceship entity containing physics movement, health/shield systems,
weapons loadout, and status effects.
"""

from typing import List, Optional, Any
from utils.math_utils import Vector2D, clamp
from combat.health_system import HealthComponent
from collision.collider import Collider
from player.player_stats import PlayerStats
from weapons.weapon_base import Weapon
from weapons.weapon_factory import WeaponFactory
from configuration.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, LAYER_PLAYER,
    CATEGORY_PLAYER, PLAYER_DEFAULT_SPEED,
    PLAYER_MAX_HEALTH, PLAYER_MAX_SHIELD,
    WEAPON_PULSE_CANNON, WEAPON_SPREAD_SHOT, WEAPON_HEAVY_PLASMA,
    WEAPON_HOMING_MISSILES, WEAPON_QUANTUM_RAILGUN, WEAPON_BEAM_CANNON
)


class PlayerShip:
    """Player spaceship entity class."""

    def __init__(self, position: Optional[Vector2D] = None):
        self.position = position if position is not None else Vector2D(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.85)
        self.velocity = Vector2D.zero()
        self.direction = Vector2D.up()
        
        self.base_speed = PLAYER_DEFAULT_SPEED
        self.lives = 3
        self.layer = LAYER_PLAYER
        self.is_active = True

        self.stats = PlayerStats()
        self.health = HealthComponent(
            max_health=PLAYER_MAX_HEALTH,
            max_shield=PLAYER_MAX_SHIELD,
            shield_regen_rate=15.0,
            shield_regen_delay=2.5,
            on_death_callback=self._handle_death
        )

        self.collider = Collider(self, category=CATEGORY_PLAYER, radius=20.0)

        # Weapons Inventory & Active Slot
        self.weapons: List[Weapon] = [
            WeaponFactory.create_weapon(WEAPON_PULSE_CANNON),
            WeaponFactory.create_weapon(WEAPON_SPREAD_SHOT),
            WeaponFactory.create_weapon(WEAPON_HEAVY_PLASMA),
            WeaponFactory.create_weapon(WEAPON_HOMING_MISSILES),
            WeaponFactory.create_weapon(WEAPON_QUANTUM_RAILGUN),
            WeaponFactory.create_weapon(WEAPON_BEAM_CANNON),
        ]
        self.active_weapon_index = 0

        # Powerup Status Buffs
        self.rapid_fire_timer = 0.0
        self.double_damage_timer = 0.0
        self.speed_boost_timer = 0.0

    @property
    def active_weapon(self) -> Weapon:
        return self.weapons[self.active_weapon_index]

    def switch_weapon(self, index: int) -> None:
        """Switch active weapon slot."""
        if 0 <= index < len(self.weapons):
            self.active_weapon_index = index

    def next_weapon(self) -> None:
        """Cycle to next weapon."""
        self.active_weapon_index = (self.active_weapon_index + 1) % len(self.weapons)

    def previous_weapon(self) -> None:
        """Cycle to previous weapon."""
        self.active_weapon_index = (self.active_weapon_index - 1) % len(self.weapons)

    def handle_input(self, input_manager: Any) -> None:
        """Process movement and weapon firing inputs."""
        if not self.is_active or self.health.is_dead:
            return

        move_dir = Vector2D.zero()

        if input_manager.is_action_pressed("MOVE_UP"):
            move_dir.y -= 1.0
        if input_manager.is_action_pressed("MOVE_DOWN"):
            move_dir.y += 1.0
        if input_manager.is_action_pressed("MOVE_LEFT"):
            move_dir.x -= 1.0
        if input_manager.is_action_pressed("MOVE_RIGHT"):
            move_dir.x += 1.0

        if move_dir.length_squared() > 0:
            move_dir = move_dir.normalize()

        speed_multiplier = self.stats.speed_multiplier
        if self.speed_boost_timer > 0.0:
            speed_multiplier *= 1.5

        target_velocity = move_dir * (self.base_speed * speed_multiplier)
        self.velocity = self.velocity.lerp(target_velocity, 0.2)

    def update(self, dt: float) -> None:
        """Update player ship position, health timers, weapons, and status buffs."""
        if not self.is_active:
            return

        # Update position with screen boundary clamping
        self.position += self.velocity * dt
        self.position.x = clamp(self.position.x, 24.0, SCREEN_WIDTH - 24.0)
        self.position.y = clamp(self.position.y, 24.0, SCREEN_HEIGHT - 24.0)

        # Update Health Component
        self.health.update(dt)

        # Update Weapons Cooldowns
        for weapon in self.weapons:
            weapon.update(dt)

        # Update Active Powerup Buff Timers
        if self.rapid_fire_timer > 0.0:
            self.rapid_fire_timer -= dt
        if self.double_damage_timer > 0.0:
            self.double_damage_timer -= dt
        if self.speed_boost_timer > 0.0:
            self.speed_boost_timer -= dt

    def fire_weapon(self, projectile_pool: Any, target: Optional[Any] = None) -> List[Any]:
        """Fire active weapon."""
        if not self.is_active or self.health.is_dead:
            return []

        fire_origin = self.position + Vector2D(0, -20)
        fired_projectiles = self.active_weapon.fire(fire_origin, self.direction, projectile_pool, target)
        
        # Apply Double Damage powerup if active
        if self.double_damage_timer > 0.0:
            for p in fired_projectiles:
                p.damage *= 2.0

        return fired_projectiles

    def apply_powerup(self, powerup_type: str, duration: float = 8.0) -> None:
        """Apply powerup buff effect."""
        if powerup_type == "HEALTH":
            self.health.heal(50.0)
        elif powerup_type == "SHIELD":
            self.health.restore_shield(50.0)
        elif powerup_type == "RAPID_FIRE":
            self.rapid_fire_timer = duration
        elif powerup_type == "DOUBLE_DAMAGE":
            self.double_damage_timer = duration
        elif powerup_type == "SPEED_BOOST":
            self.speed_boost_timer = duration

    def _handle_death(self) -> None:
        """Handle ship destruction and life deduction."""
        self.lives -= 1
        if self.lives > 0:
            # Respawn
            self.position = Vector2D(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.85)
            self.health.current_health = self.health.max_health
            self.health.current_shield = self.health.max_shield
            self.health.is_dead = False
            self.health.set_invulnerable(3.0)
        else:
            self.is_active = False

    def render(self, surface: any) -> None:
        """Render player ship visuals."""
        if not self.is_active:
            return
        try:
            import pygame
            # Render ship triangle
            top = (int(self.position.x), int(self.position.y - 20))
            left = (int(self.position.x - 18), int(self.position.y + 15))
            right = (int(self.position.x + 18), int(self.position.y + 15))
            
            # Invulnerability flashing
            if self.health.is_invulnerable:
                ship_color = (0, 255, 255)
            else:
                ship_color = (30, 144, 255)

            pygame.draw.polygon(surface, ship_color, [top, left, right])
            pygame.draw.polygon(surface, (240, 245, 255), [top, left, right], 2)

            # Draw Shield Ring if active
            if self.health.current_shield > 0:
                pygame.draw.circle(surface, (0, 230, 255, 120), self.position.to_int_tuple(), 28, 2)
        except Exception:
            pass
