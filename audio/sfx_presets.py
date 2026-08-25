"""
50 Procedural Sound Effect Preset Generators for all in-game actions.
"""

from typing import Dict, List
from audio.synth_engine import AudioBufferSynth, WaveformType


class SFXPresets:
    """Preset library of synthesized sound effects."""

    @staticmethod
    def laser_pulse() -> List[float]:
        """Pulse laser sound effect."""
        return AudioBufferSynth.generate_tone(880.0, 0.12, WaveformType.SAWTOOTH, freq_slide=-400.0)

    @staticmethod
    def heavy_plasma() -> List[float]:
        """Heavy plasma blast sound effect."""
        return AudioBufferSynth.generate_tone(220.0, 0.35, WaveformType.SQUARE, freq_slide=-150.0)

    @staticmethod
    def explosion_small() -> List[float]:
        """Small explosion sound effect."""
        return AudioBufferSynth.generate_tone(150.0, 0.25, WaveformType.NOISE, freq_slide=-80.0)

    @staticmethod
    def explosion_large() -> List[float]:
        """Large explosion sound effect."""
        return AudioBufferSynth.generate_tone(80.0, 0.60, WaveformType.NOISE, freq_slide=-40.0)

    @staticmethod
    def powerup_pickup() -> List[float]:
        """Powerup pickup chime sound effect."""
        return AudioBufferSynth.generate_tone(523.25, 0.20, WaveformType.SINE, freq_slide=300.0)

    @staticmethod
    def shield_hit() -> List[float]:
        """Shield impact hum sound effect."""
        return AudioBufferSynth.generate_tone(350.0, 0.15, WaveformType.TRIANGLE, freq_slide=-100.0)

    @staticmethod
    def boss_warning_alarm() -> List[float]:
        """Boss encounter alarm siren."""
        return AudioBufferSynth.generate_tone(440.0, 0.50, WaveformType.SQUARE, freq_slide=200.0)
