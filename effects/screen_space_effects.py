"""
Screen Space Post-Processing Effects (Warp Speed Lines, Low-Health Red Vignette).
"""

from typing import Any
from configuration.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class ScreenSpaceEffects:
    """Renders full-screen post-processing overlays."""

    @staticmethod
    def render_low_health_vignette(surface: any, health_percentage: float) -> None:
        """Render pulsing red screen border vignette when health is dangerously low (< 30%)."""
        if health_percentage >= 0.30:
            return
        try:
            import pygame
            alpha = int((0.30 - health_percentage) / 0.30 * 160)
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(overlay, (255, 0, 0, alpha), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 20)
            surface.blit(overlay, (0, 0))
        except Exception:
            pass
