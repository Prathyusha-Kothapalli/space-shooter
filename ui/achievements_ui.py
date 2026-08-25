"""
Achievements List and Milestone Progress UI State.
"""

from typing import Optional, Dict, Any
from core.state_machine import BaseState
from configuration.constants import STATE_ACHIEVEMENTS, STATE_MENU, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_GOLD, COLOR_WHITE


class AchievementsUIState(BaseState):
    """Achievements List scene."""

    def __init__(self):
        super().__init__(STATE_ACHIEVEMENTS)

    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_input(self, input_manager: Any) -> None:
        if input_manager.is_action_just_pressed("CANCEL"):
            if self.state_machine:
                self.state_machine.change_state(STATE_MENU)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: any) -> None:
        try:
            import pygame
            font_title = pygame.font.SysFont("arial", 36, bold=True)
            font_body = pygame.font.SysFont("arial", 20)

            t1 = font_title.render("ACHIEVEMENTS & MILESTONES", True, COLOR_GOLD)
            t2 = font_body.render("Press [ESC] to Return to Menu", True, COLOR_WHITE)

            surface.blit(t1, (SCREEN_WIDTH // 2 - t1.get_width() // 2, 80))
            surface.blit(t2, (SCREEN_WIDTH // 2 - t2.get_width() // 2, 140))
        except Exception:
            pass
