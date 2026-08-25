"""
Boss 2: Starlight Carrier mothership.
Features 3 distinct multi-phase attack patterns.
"""

from typing import List, Optional, Any
from bosses.boss_base import Boss
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_CYAN, COLOR_GOLD


class StarlightCarrier(Boss):
    """Starlight Carrier mothership boss."""

    def __init__(self):
        super().__init__(boss_name="STARLIGHT CARRIER", max_health=1800.0, score_value=8500, xp_value=1800)
        self.collider.radius = 75.0
        self.attack_timer = 0.0

    def _on_phase_change(self, new_phase: int) -> None:
        if new_phase == 2:
            self.health.restore_shield(300.0)
        elif new_phase == 3:
            self.velocity.x *= 1.5

    def execute_phase_attacks(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        fired = []
        self.attack_timer += dt

        interval = 2.0 if self.current_phase == 1 else (1.4 if self.current_phase == 2 else 0.8)

        if self.attack_timer >= interval:
            self.attack_timer = 0.0

            dir_to_player = Vector2D.down()
            if player_target and hasattr(player_target, 'position'):
                dir_to_player = (player_target.position - self.position).normalize()

            if self.current_phase == 1:
                # Phase 1: Heavy Quad Cannon Stream
                for offset_x in (-50, -20, 20, 50):
                    p: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                    p.spawn(self.position + Vector2D(offset_x, 45), dir_to_player * 420.0, damage=18.0)
                    fired.append(p)

            elif self.current_phase == 2:
                # Phase 2: Orbital Laser Ring
                for i in range(6):
                    angle = i * (6.28318 / 6)
                    p_dir = Vector2D(1, 0).rotate(angle)
                    p: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                    p.spawn(self.position, p_dir * 480.0, damage=24.0)
                    fired.append(p)

            elif self.current_phase == 3:
                # Phase 3: Spiral Barrage Overclock
                for i in range(12):
                    angle = (self.phase_timer * 3.0) + i * (6.28318 / 12)
                    p_dir = Vector2D(1, 0).rotate(angle)
                    p: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                    p.spawn(self.position, p_dir * 520.0, damage=28.0)
                    fired.append(p)

        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            color = COLOR_GOLD if self.is_enraged else COLOR_CYAN
            pygame.draw.polygon(surface, color, [
                (int(self.position.x), int(self.position.y + 70)),
                (int(self.position.x - 75), int(self.position.y - 40)),
                (int(self.position.x + 75), int(self.position.y - 40))
            ])
        except Exception:
            pass
