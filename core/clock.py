"""
Clock & Delta Time regulator. Manages frame rate limits, delta time calculation,
and frame performance tracking.
"""

import time
from typing import List


class GameClock:
    """High precision frame rate clock and delta time counter."""
    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self.target_frame_time = 1.0 / float(target_fps) if target_fps > 0 else 0.0
        self.last_time = time.perf_counter()
        self.delta_time = 0.0
        self.elapsed_time = 0.0
        self.frame_count = 0
        self.fps_history: List[float] = []
        self.current_fps = float(target_fps)

    def tick(self) -> float:
        """Advance clock by one frame, return delta time in seconds."""
        current_time = time.perf_counter()
        frame_time = current_time - self.last_time

        # Sleep to cap target FPS if frame rendered faster
        if self.target_frame_time > 0 and frame_time < self.target_frame_time:
            sleep_time = self.target_frame_time - frame_time
            time.sleep(sleep_time)
            current_time = time.perf_counter()
            frame_time = current_time - self.last_time

        # Cap delta time to prevent physics explosions on lag spikes (max 100ms)
        self.delta_time = min(frame_time, 0.1)
        self.last_time = current_time
        self.elapsed_time += self.delta_time
        self.frame_count += 1

        # Calculate FPS
        if self.delta_time > 0:
            inst_fps = 1.0 / self.delta_time
            self.fps_history.append(inst_fps)
            if len(self.fps_history) > 30:
                self.fps_history.pop(0)
            self.current_fps = sum(self.fps_history) / len(self.fps_history)

        return self.delta_time

    def get_fps(self) -> float:
        """Return average FPS over recent frames."""
        return self.current_fps
