"""
Dynamic Camera Screen Shake Effect Manager.
"""

import random
from utils.math_utils import Vector2D


class ScreenShake:
    """Manages impact camera vibration offset."""

    def __init__(self):
        self.intensity = 0.0
        self.duration = 0.0
        self.timer = 0.0
        self.offset = Vector2D.zero()

    def add_shake(self, intensity: float, duration: float = 0.3) -> None:
        """Trigger camera screen shake."""
        self.intensity = max(self.intensity, intensity)
        self.duration = max(self.duration, duration)
        self.timer = self.duration

    def update(self, dt: float) -> Vector2D:
        """Update shake offset vector."""
        if self.timer > 0.0:
            self.timer -= dt
            progress = self.timer / self.duration if self.duration > 0 else 0.0
            current_int = self.intensity * progress

            self.offset.x = random.uniform(-current_int, current_int)
            self.offset.y = random.uniform(-current_int, current_int)

            if self.timer <= 0.0:
                self.offset = Vector2D.zero()
                self.intensity = 0.0
        else:
            self.offset = Vector2D.zero()

        return self.offset
