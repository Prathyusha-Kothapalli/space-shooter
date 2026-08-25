"""
Timer, stopwatch, and cooldown helpers for game object timing.
"""

from typing import Callable, Optional


class Timer:
    """Countdown timer with optional completion callback."""
    def __init__(self, duration: float, callback: Optional[Callable[[], None]] = None, auto_restart: bool = False):
        self.duration = float(duration)
        self.time_remaining = float(duration)
        self.callback = callback
        self.auto_restart = auto_restart
        self.is_running = False
        self.is_finished = False

    def start(self) -> None:
        """Start or reset timer."""
        self.time_remaining = self.duration
        self.is_running = True
        self.is_finished = False

    def stop(self) -> None:
        """Stop timer."""
        self.is_running = False

    def update(self, dt: float) -> None:
        """Advance timer by delta time."""
        if not self.is_running:
            return

        self.time_remaining -= dt
        if self.time_remaining <= 0.0:
            self.time_remaining = 0.0
            self.is_finished = True
            
            if self.callback:
                self.callback()

            if self.auto_restart:
                self.start()
            else:
                self.is_running = False

    def progress(self) -> float:
        """Return timer progress from 0.0 (started) to 1.0 (finished)."""
        if self.duration <= 0.0:
            return 1.0
        return 1.0 - (self.time_remaining / self.duration)


class Cooldown:
    """Cooldown tracking class for weapons, skills, and actions."""
    def __init__(self, cooldown_time: float):
        self.cooldown_time = float(cooldown_time)
        self.timer = 0.0

    def update(self, dt: float) -> None:
        """Decrease remaining cooldown."""
        if self.timer > 0.0:
            self.timer = max(0.0, self.timer - dt)

    def is_ready(self) -> bool:
        """Check if action is ready."""
        return self.timer <= 0.0

    def trigger(self) -> bool:
        """Trigger action and start cooldown if ready."""
        if self.is_ready():
            self.timer = self.cooldown_time
            return True
        return False

    def reset(self) -> None:
        """Reset cooldown immediately."""
        self.timer = 0.0
