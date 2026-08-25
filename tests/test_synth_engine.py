"""
Test 10: Audio Synthesizer waveform generation assertions.
"""

import unittest
from audio.synth_engine import AudioBufferSynth, WaveformType


class TestSynthEngine(unittest.TestCase):
    def test_waveform_generation(self):
        """Verify synthesizer produces expected PCM sample float array length and range."""
        duration = 0.1
        sample_rate = 44100
        samples = AudioBufferSynth.generate_tone(440.0, duration, WaveformType.SINE, sample_rate=sample_rate)

        expected_count = int(sample_rate * duration)
        self.assertEqual(len(samples), expected_count)

        # Verify all samples bounded between -1.0 and 1.0
        for val in samples:
            self.assertTrue(-1.0 <= val <= 1.0)


if __name__ == "__main__":
    unittest.main()
