"""
Game Over Summary Screen State.
"""

from typing import Optional, Dict, Any
from core.state_machine import BaseState
from configuration.constants import STATE_GAME_OVER, STATE_GAMEPLAY, STATE_MENU, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_RED, COLOR_WHITE, COLOR_GOLD


class GameOverState(BaseState):
    """Game Over summary state."""

    def __init__(self):
        super().__init__(STATE_GAME_OVER)
        self.final_score = 0
        self.final_wave = 1

    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        if params:
            self.final_score = params.get("score", 0)
            self.final_wave = params.get("wave", 1)

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
            font_title = pygame.font.SysFont("arial", 44, bold=True)
            font_body = pygame.font.SysFont("arial", 22)

            t1 = font_title.render("MISSION FAILED - GAME OVER", True, COLOR_RED)
            t2 = font_body.render(f"Final Score: {self.final_score:,}", True, COLOR_GOLD)
            t3 = font_body.render(f"Waves Survived: {self.final_wave}", True, COLOR_WHITE)
            t4 = font_body.render("Press [ENTER] to Restart Mission", True, COLOR_WHITE)

            surface.blit(t1, (SCREEN_WIDTH // 2 - t1.get_width() // 2, 220))
            surface.blit(t2, (SCREEN_WIDTH // 2 - t2.get_width() // 2, 300))
            surface.blit(t3, (SCREEN_WIDTH // 2 - t3.get_width() // 2, 340))
            surface.blit(t4, (SCREEN_WIDTH // 2 - t4.get_width() // 2, 440))
        except Exception:
            pass
