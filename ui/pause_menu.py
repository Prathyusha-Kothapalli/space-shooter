"""
Pause Menu overlay state.
"""

from typing import Optional, Dict, Any
from core.state_machine import BaseState
from configuration.constants import STATE_PAUSE, STATE_GAMEPLAY, STATE_MENU, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE, COLOR_CYAN


class PauseMenuState(BaseState):
    """Pause Menu state."""

    def __init__(self):
        super().__init__(STATE_PAUSE)

    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_input(self, input_manager: Any) -> None:
        if input_manager.is_action_just_pressed("PAUSE"):
            if self.state_machine:
                self.state_machine.change_state(STATE_GAMEPLAY)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: any) -> None:
        try:
            import pygame
            # Overlay dim background
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            surface.blit(overlay, (0, 0))

            font = pygame.font.SysFont("arial", 36, bold=True)
            txt = font.render("GAME PAUSED - Press ESC to Resume", True, COLOR_CYAN)
            surface.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, SCREEN_HEIGHT // 2))
        except Exception:
            pass
