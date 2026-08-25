"""
Settings Manager wrapper for game options and volume controls.
"""

from configuration.game_config import GameConfig


class SettingsManager:
    """Manages system settings updates."""

    def __init__(self, config: GameConfig):
        self.config = config

    def set_master_volume(self, volume: float) -> None:
        self.config.set("audio", "master_volume", max(0.0, min(1.0, volume)))

    def set_sfx_volume(self, volume: float) -> None:
        self.config.set("audio", "sfx_volume", max(0.0, min(1.0, volume)))

    def set_music_volume(self, volume: float) -> None:
        self.config.set("audio", "music_volume", max(0.0, min(1.0, volume)))

    def set_difficulty(self, difficulty: str) -> None:
        self.config.set("gameplay", "difficulty", difficulty)

    def save_settings(self) -> bool:
        return self.config.save()
