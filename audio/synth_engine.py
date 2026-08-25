"""
Procedural Waveform Audio Synthesizer Engine.
Generates math-based audio buffers (Sine, Square, Sawtooth, Triangle, White Noise).
"""

import math
import random
from typing import List, Tuple


class WaveformType:
    SINE = "SINE"
    SQUARE = "SQUARE"
    SAWTOOTH = "SAWTOOTH"
    TRIANGLE = "TRIANGLE"
    NOISE = "NOISE"


class AudioBufferSynth:
    """Software audio synthesizer producing PCM audio sample arrays."""

    @staticmethod
    def generate_tone(
        frequency: float,
        duration: float,
        waveform: str = WaveformType.SINE,
        sample_rate: int = 44100,
        volume: float = 0.8,
        freq_slide: float = 0.0
    ) -> List[float]:
        """Generate raw PCM audio sample float array (-1.0 to 1.0)."""
        num_samples = int(sample_rate * duration)
        samples: List[float] = []

        curr_freq = frequency

        for i in range(num_samples):
            t = i / sample_rate
            # Frequency slide modifier
            if freq_slide != 0.0:
                curr_freq = max(20.0, frequency + freq_slide * t)

            phase = 2.0 * math.pi * curr_freq * t

            # Envelope ADSR decay
            envelope = 1.0 - (i / num_samples)

            if waveform == WaveformType.SINE:
                sample_val = math.sin(phase)
            elif waveform == WaveformType.SQUARE:
                sample_val = 1.0 if math.sin(phase) >= 0 else -1.0
            elif waveform == WaveformType.SAWTOOTH:
                sample_val = 2.0 * (t * curr_freq - math.floor(0.5 + t * curr_freq))
            elif waveform == WaveformType.TRIANGLE:
                sample_val = 2.0 * abs(2.0 * (t * curr_freq - math.floor(0.5 + t * curr_freq))) - 1.0
            elif waveform == WaveformType.NOISE:
                sample_val = random.uniform(-1.0, 1.0)
            else:
                sample_val = math.sin(phase)

            final_sample = sample_val * envelope * volume
            samples.append(max(-1.0, min(1.0, final_sample)))

        return samples
