"""
Boss 1: Void Dreadnought flagship.
Features 3 distinct multi-phase attack patterns.
"""

from typing import List, Optional, Any
from bosses.boss_base import Boss
from projectiles.enemy_projectile import EnemyProjectile
from utils.math_utils import Vector2D
from configuration.constants import COLOR_CRIMSON, COLOR_MAGENTA


class VoidDreadnought(Boss):
    """Void Dreadnought flagship boss."""

    def __init__(self):
        super().__init__(boss_name="VOID DREADNOUGHT", max_health=1200.0, score_value=6000, xp_value=1200)
        self.collider.radius = 65.0
        self.attack_timer = 0.0

    def _on_phase_change(self, new_phase: int) -> None:
        if new_phase == 2:
            self.velocity.x *= 1.4
        elif new_phase == 3:
            self.velocity.x *= 1.6

    def execute_phase_attacks(self, dt: float, player_target: Optional[Any], projectile_pool: Any) -> List[Any]:
        fired = []
        self.attack_timer += dt

        interval = 1.8 if self.current_phase == 1 else (1.2 if self.current_phase == 2 else 0.7)

        if self.attack_timer >= interval:
            self.attack_timer = 0.0

            dir_to_player = Vector2D.down()
            if player_target and hasattr(player_target, 'position'):
                dir_to_player = (player_target.position - self.position).normalize()

            if self.current_phase == 1:
                # Phase 1: Heavy Dual Plasma Burst
                p1: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                p1.spawn(self.position + Vector2D(-30, 40), dir_to_player * 400.0, damage=20.0)

                p2: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                p2.spawn(self.position + Vector2D(30, 40), dir_to_player * 400.0, damage=20.0)
                fired.extend([p1, p2])

            elif self.current_phase == 2:
                # Phase 2: 5-Way Fan Barrage
                for i in range(5):
                    angle = -0.5 + i * 0.25
                    p_dir = dir_to_player.rotate(angle)
                    proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                    proj.spawn(self.position + Vector2D(0, 40), p_dir * 450.0, damage=22.0)
                    fired.append(proj)

            elif self.current_phase == 3:
                # Phase 3: Enraged 360-Degree Radial Explosion
                for i in range(8):
                    angle = i * (6.28318 / 8)
                    p_dir = Vector2D(1, 0).rotate(angle)
                    proj: EnemyProjectile = projectile_pool.acquire(EnemyProjectile)
                    proj.spawn(self.position, p_dir * 500.0, damage=25.0)
                    fired.append(proj)

        return fired

    def render(self, surface: any) -> None:
        if not self.is_active:
            return
        try:
            import pygame
            color = COLOR_MAGENTA if self.is_enraged else COLOR_CRIMSON
            pygame.draw.circle(surface, color, self.position.to_int_tuple(), 65)
            pygame.draw.circle(surface, (255, 255, 255), self.position.to_int_tuple(), 65, 3)
        except Exception:
            pass
