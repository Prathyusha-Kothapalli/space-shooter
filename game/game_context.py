"""
GameContext container holding shared service references, active session state,
score trackers, difficulty modifiers, and subsystem lookup.
"""

from typing import Optional, Any
from configuration.constants import DIFFICULTY_NORMAL, DIFFICULTY_SCALERS
from configuration.game_config import GameConfig
from core.event_dispatcher import EventDispatcher


class GameContext:
    """Central context object passed through active game states."""

    def __init__(self, config: Optional[GameConfig] = None):
        self.config = config if config is not None else GameConfig()
        self.event_dispatcher = EventDispatcher.get_instance()
        
        self.difficulty = self.config.get("gameplay", "difficulty", DIFFICULTY_NORMAL)
        self.difficulty_scalers = DIFFICULTY_SCALERS.get(self.difficulty, DIFFICULTY_SCALERS[DIFFICULTY_NORMAL])
        
        # Session State
        self.score = 0
        self.high_score = 0
        self.combo_multiplier = 1.0
        self.combo_streak = 0
        self.current_wave = 1
        self.enemies_killed = 0
        self.bosses_defeated = 0
        self.time_elapsed = 0.0
        
        # Subsystem References
        self.audio_manager: Optional[Any] = None
        self.effects_manager: Optional[Any] = None
        self.progression_manager: Optional[Any] = None
        self.achievement_manager: Optional[Any] = None
        self.statistics_manager: Optional[Any] = None
        self.save_manager: Optional[Any] = None

    def reset_session(self) -> None:
        """Reset match statistics for new run."""
        self.score = 0
        self.combo_multiplier = 1.0
        self.combo_streak = 0
        self.current_wave = 1
        self.enemies_killed = 0
        self.bosses_defeated = 0
        self.time_elapsed = 0.0

    def add_score(self, amount: int) -> int:
        """Add score weighted by active combo multiplier and difficulty."""
        scaled_amount = int(amount * self.combo_multiplier * self.difficulty_scalers["score_mult"])
        self.score += scaled_amount
        if self.score > self.high_score:
            self.high_score = self.score
        return scaled_amount

    def register_kill(self) -> None:
        """Increment kill streak and update combo multiplier."""
        self.enemies_killed += 1
        self.combo_streak += 1
        self.combo_multiplier = min(5.0, 1.0 + (self.combo_streak // 5) * 0.5)

    def reset_combo(self) -> None:
        """Reset active combo multiplier on taking hit."""
        self.combo_streak = 0
        self.combo_multiplier = 1.0
