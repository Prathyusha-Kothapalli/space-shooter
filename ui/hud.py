"""
In-Game Gameplay HUD overlay renderer.
Displays player health/shield bars, score, combo streak, active weapon, lives, wave info.
"""

from typing import Any
from configuration.constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_CYAN, COLOR_GREEN, COLOR_GOLD, COLOR_WHITE, COLOR_RED


class GameplayHUD:
    """Renders head-up display metrics on screen."""

    def __init__(self):
        pass

    def render(self, surface: any, game_context: Any, player: Any) -> None:
        """Render HUD indicators."""
        try:
            import pygame
            font_lg = pygame.font.SysFont("arial", 24, bold=True)
            font_sm = pygame.font.SysFont("arial", 16)

            # 1. Health & Shield Bars (Top Left)
            if player and hasattr(player, 'health'):
                hp_pct = player.health.health_percentage()
                sh_pct = player.health.shield_percentage()

                # Health Bar
                pygame.draw.rect(surface, (40, 45, 55), (20, 20, 200, 16))
                pygame.draw.rect(surface, COLOR_GREEN, (20, 20, int(200 * hp_pct), 16))
                lbl_hp = font_sm.render(f"HP: {int(player.health.current_health)}/{int(player.health.max_health)}", True, COLOR_WHITE)
                surface.blit(lbl_hp, (25, 18))

                # Shield Bar
                pygame.draw.rect(surface, (40, 45, 55), (20, 42, 200, 12))
                pygame.draw.rect(surface, COLOR_CYAN, (20, 42, int(200 * sh_pct), 12))

            # 2. Score & High Score (Top Center)
            txt_score = font_lg.render(f"SCORE: {game_context.score:,}", True, COLOR_GOLD)
            surface.blit(txt_score, (SCREEN_WIDTH // 2 - txt_score.get_width() // 2, 15))

            # 3. Wave & Combo Multiplier (Top Right)
            txt_wave = font_lg.render(f"WAVE {game_context.current_wave}", True, COLOR_WHITE)
            surface.blit(txt_wave, (SCREEN_WIDTH - txt_wave.get_width() - 20, 15))

            if game_context.combo_multiplier > 1.0:
                txt_combo = font_sm.render(f"COMBO x{game_context.combo_multiplier:.1f}", True, COLOR_CYAN)
                surface.blit(txt_combo, (SCREEN_WIDTH - txt_combo.get_width() - 20, 45))

            # 4. Active Weapon Slot (Bottom Left)
            if player and hasattr(player, 'active_weapon'):
                w_name = player.active_weapon.name
                txt_weapon = font_sm.render(f"WEAPON: {w_name} [Lvl {player.active_weapon.level}]", True, COLOR_WHITE)
                surface.blit(txt_weapon, (20, SCREEN_HEIGHT - 35))

            # 5. Lives Icons (Bottom Right)
            if player:
                txt_lives = font_sm.render(f"LIVES: {player.lives}", True, COLOR_RED)
                surface.blit(txt_lives, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 35))

        except Exception:
            pass
