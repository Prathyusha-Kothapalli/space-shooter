"""
Main Menu Game State Scene implementation.
"""

from typing import Optional, Dict, Any
from core.state_machine import BaseState
from configuration.constants import STATE_MENU, STATE_GAMEPLAY, STATE_SETTINGS, STATE_UPGRADE_TREE, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_CYAN, COLOR_WHITE, COLOR_GOLD


class MainMenuState(BaseState):
    """Main Menu scene state."""

    def __init__(self):
        super().__init__(STATE_MENU)

    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_input(self, input_manager: Any) -> None:
        if input_manager.is_action_just_pressed("CONFIRM"):
            if self.state_machine:
                self.state_machine.change_state(STATE_GAMEPLAY)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: any) -> None:
        try:
            import pygame
            font_title = pygame.font.SysFont("arial", 48, bold=True)
            font_sub = pygame.font.SysFont("arial", 22)

            t1 = font_title.render("STARLIGHT VANGUARD", True, COLOR_CYAN)
            t2 = font_sub.render("2D SPACE SHOOTER", True, COLOR_GOLD)
            t3 = font_sub.render("Press [ENTER] or [SPACE] to Launch Mission", True, COLOR_WHITE)

            surface.blit(t1, (SCREEN_WIDTH // 2 - t1.get_width() // 2, 200))
            surface.blit(t2, (SCREEN_WIDTH // 2 - t2.get_width() // 2, 260))
            surface.blit(t3, (SCREEN_WIDTH // 2 - t3.get_width() // 2, 450))
        except Exception:
            pass
