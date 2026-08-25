"""
Health and Shield system component. Handles health reduction, shield absorption,
shield regeneration, invulnerability frames, and death states.
"""

from typing import Optional, Callable


class HealthComponent:
    """Manages hit points, shields, armor, and invulnerability."""

    def __init__(
        self,
        max_health: float = 100.0,
        max_shield: float = 0.0,
        shield_regen_rate: float = 0.0,
        shield_regen_delay: float = 3.0,
        on_death_callback: Optional[Callable[[], None]] = None
    ):
        self.max_health = float(max_health)
        self.current_health = float(max_health)
        
        self.max_shield = float(max_shield)
        self.current_shield = float(max_shield)
        self.shield_regen_rate = float(shield_regen_rate)
        self.shield_regen_delay = float(shield_regen_delay)
        self.shield_regen_timer = 0.0

        self.invulnerable_timer = 0.0
        self.is_invulnerable = False

        self.on_death_callback = on_death_callback
        self.is_dead = False

    def update(self, dt: float) -> None:
        """Update shield regeneration and invulnerability timers."""
        if self.is_dead:
            return

        # Update invulnerability timer
        if self.invulnerable_timer > 0.0:
            self.invulnerable_timer -= dt
            if self.invulnerable_timer <= 0.0:
                self.invulnerable_timer = 0.0
                self.is_invulnerable = False

        # Update shield regeneration
        if self.max_shield > 0.0 and self.current_shield < self.max_shield:
            if self.shield_regen_timer > 0.0:
                self.shield_regen_timer -= dt
            else:
                self.current_shield = min(self.max_shield, self.current_shield + self.shield_regen_rate * dt)

    def take_damage(self, amount: float, ignore_shield: bool = False) -> float:
        """Apply damage payload. Shield absorbs damage first."""
        if self.is_dead or self.is_invulnerable or amount <= 0.0:
            return 0.0

        # Reset shield regen cooldown
        self.shield_regen_timer = self.shield_regen_delay

        remaining_damage = amount

        # Shield absorption
        if not ignore_shield and self.current_shield > 0.0:
            if self.current_shield >= remaining_damage:
                self.current_shield -= remaining_damage
                return amount
            else:
                remaining_damage -= self.current_shield
                self.current_shield = 0.0

        # Direct Health reduction
        self.current_health -= remaining_damage

        if self.current_health <= 0.0:
            self.current_health = 0.0
            self.is_dead = True
            if self.on_death_callback:
                self.on_death_callback()

        return amount

    def heal(self, amount: float) -> float:
        """Heal health points up to max_health."""
        if self.is_dead or amount <= 0.0:
            return 0.0
        actual_heal = min(amount, self.max_health - self.current_health)
        self.current_health += actual_heal
        return actual_heal

    def restore_shield(self, amount: float) -> float:
        """Restore shield points up to max_shield."""
        if self.is_dead or amount <= 0.0 or self.max_shield <= 0.0:
            return 0.0
        actual_restore = min(amount, self.max_shield - self.current_shield)
        self.current_shield += actual_restore
        return actual_restore

    def set_invulnerable(self, duration: float) -> None:
        """Grant invulnerability for duration in seconds."""
        self.invulnerable_timer = duration
        self.is_invulnerable = True

    def health_percentage(self) -> float:
        """Return ratio of current health to max health."""
        return self.current_health / self.max_health if self.max_health > 0 else 0.0

    def shield_percentage(self) -> float:
        """Return ratio of current shield to max shield."""
        return self.current_shield / self.max_shield if self.max_shield > 0 else 0.0
