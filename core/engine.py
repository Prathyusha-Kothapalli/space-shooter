"""
Core Engine initializer and main game loop coordinator.
Provides platform rendering abstraction and game loop driver.
"""

import sys
import time
from typing import Optional

from configuration.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FPS, WINDOW_TITLE
from configuration.game_config import GameConfig
from core.clock import GameClock
from core.input_manager import InputManager
from core.state_machine import StateMachine
from core.event_dispatcher import EventDispatcher
from utils.logger import log_info, log_error


class Engine:
    """Core Engine controller driving main loop and system managers."""

    def __init__(self, config: Optional[GameConfig] = None):
        log_info("Engine", "Initializing Starlight Vanguard Space Shooter Engine...")
        self.config = config if config is not None else GameConfig()
        
        self.clock = GameClock(target_fps=self.config.get("graphics", "fps_cap", TARGET_FPS))
        self.input_manager = InputManager()
        self.state_machine = StateMachine()
        self.event_dispatcher = EventDispatcher.get_instance()
        
        self.is_running = False
        self.headless_mode = False
        self.surface = None

    def initialize(self, headless: bool = False) -> bool:
        """Initialize engine subsystems and rendering surface."""
        self.headless_mode = headless
        
        if not self.headless_mode:
            try:
                import pygame
                pygame.init()
                pygame.font.init()
                pygame.mixer.init()
                
                flags = 0
                if self.config.get("graphics", "fullscreen", False):
                    flags |= pygame.FULLSCREEN
                if self.config.get("graphics", "vsync", True):
                    flags |= pygame.DOUBLEBUF

                width = self.config.get("graphics", "width", SCREEN_WIDTH)
                height = self.config.get("graphics", "height", SCREEN_HEIGHT)
                
                self.surface = pygame.display.set_mode((width, height), flags)
                pygame.display.set_caption(WINDOW_TITLE)
                log_info("Engine", f"Pygame Display Surface Initialized: {width}x{height}")
            except Exception as e:
                log_error("Engine", f"Pygame Display init failed: {e}. Defaulting to Headless Mode.")
                self.headless_mode = True

        self.is_running = True
        return True

    def run(self) -> None:
        """Execute main game loop."""
        log_info("Engine", "Starting Game Loop.")
        
        while self.is_running:
            dt = self.clock.tick()
            self._handle_events()
            self._update(dt)
            self._render()

        self._shutdown()

    def _handle_events(self) -> None:
        """Process OS window and input events."""
        if not self.headless_mode:
            import pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    self.input_manager.process_raw_key_down(event.key)
                elif event.type == pygame.KEYUP:
                    self.input_manager.process_raw_key_up(event.key)
                elif event.type == pygame.MOUSEMOTION:
                    self.input_manager.process_mouse_move(event.pos[0], event.pos[1])
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.input_manager.process_mouse_button_down(event.button)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.input_manager.process_mouse_button_up(event.button)

        self.state_machine.handle_input(self.input_manager)

    def _update(self, dt: float) -> None:
        """Update game loop logic."""
        self.state_machine.update(dt)
        self.input_manager.update_frame()

    def _render(self) -> None:
        """Render active state."""
        if not self.headless_mode and self.surface:
            import pygame
            self.surface.fill((10, 12, 20))
            self.state_machine.render(self.surface)
            pygame.display.flip()

    def stop(self) -> None:
        """Signal engine to break loop."""
        self.is_running = False

    def _shutdown(self) -> None:
        """Clean up resources on engine shutdown."""
        log_info("Engine", "Shutting down engine...")
        if not self.headless_mode:
            try:
                import pygame
                pygame.quit()
            except Exception:
                pass
