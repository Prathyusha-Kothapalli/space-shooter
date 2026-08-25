"""
Victory Screen State.
"""

from typing import Optional, Dict, Any
from core.state_machine import BaseState
from configuration.constants import STATE_VICTORY, STATE_MENU, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_GOLD, COLOR_GREEN, COLOR_WHITE


class VictoryState(BaseState):
    """Victory celebration state."""

    def __init__(self):
        super().__init__(STATE_VICTORY)
        self.score = 0

    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        if params:
            self.score = params.get("score", 0)

    def exit(self) -> None:
        pass

    def handle_input(self, input_manager: Any) -> None:
        if input_manager.is_action_just_pressed("CONFIRM"):
            if self.state_machine:
                self.state_machine.change_state(STATE_MENU)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: any) -> None:
        try:
            import pygame
            font_title = pygame.font.SysFont("arial", 48, bold=True)
            font_body = pygame.font.SysFont("arial", 24)

            t1 = font_title.render("VICTORY! SECTOR CLEARED", True, COLOR_GREEN)
            t2 = font_body.render(f"Final Score: {self.score:,}", True, COLOR_GOLD)
            t3 = font_body.render("Press [ENTER] to return to Main Menu", True, COLOR_WHITE)

            surface.blit(t1, (SCREEN_WIDTH // 2 - t1.get_width() // 2, 240))
            surface.blit(t2, (SCREEN_WIDTH // 2 - t2.get_width() // 2, 320))
            surface.blit(t3, (SCREEN_WIDTH // 2 - t3.get_width() // 2, 420))
        except Exception:
            pass
