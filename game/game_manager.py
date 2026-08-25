"""
Game Manager controlling overall session lifecycle, state registrations,
and top-level orchestration.
"""

from typing import Optional
from core.engine import Engine
from game.game_context import GameContext
from utils.logger import log_info


class GameManager:
    """High-level game lifecycle coordinator."""

    def __init__(self, engine: Optional[Engine] = None):
        self.engine = engine if engine is not None else Engine()
        self.context = GameContext(config=self.engine.config)

    def setup(self, headless: bool = False) -> None:
        """Initialize engine and register core game states."""
        log_info("GameManager", "Setting up Game Manager...")
        self.engine.initialize(headless=headless)

    def start(self) -> None:
        """Start game loop."""
        log_info("GameManager", "Starting Starlight Vanguard Space Shooter.")
        self.engine.run()
