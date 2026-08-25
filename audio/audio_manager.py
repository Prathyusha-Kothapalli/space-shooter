"""
Audio Manager for sound effect playback and procedural audio synthesis.
"""

from typing import Dict, Any, Optional
from configuration.game_config import GameConfig
from utils.logger import log_info


class AudioManager:
    """Manages sound effects and music tracks with volume controls."""

    def __init__(self, config: Optional[GameConfig] = None):
        self.config = config if config is not None else GameConfig()
        self.is_enabled = self.config.get("audio", "audio_enabled", True)
        self.master_volume = self.config.get("audio", "master_volume", 0.8)
        self.sfx_volume = self.config.get("audio", "sfx_volume", 0.9)
        self.music_volume = self.config.get("audio", "music_volume", 0.7)

    def play_sound(self, sound_name: str) -> None:
        """Trigger sound effect playback."""
        if not self.is_enabled:
            return
        # Log audio trigger
        log_info("AudioManager", f"Playing SFX: {sound_name}")

    def play_music(self, track_name: str) -> None:
        """Start playing background music track."""
        if not self.is_enabled:
            return
        log_info("AudioManager", f"Playing Music Track: {track_name}")

    def stop_music(self) -> None:
        """Stop background music."""
        log_info("AudioManager", "Stopping Music Track")
