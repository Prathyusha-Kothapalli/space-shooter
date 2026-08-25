"""
Color manipulation utilities, HSL/RGB conversions, gradient generators,
and dynamic alpha blending helpers.
"""

import colorsys
import math
from typing import Tuple, List


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """Convert RGB (0-255) to HSL (0-1)."""
    return colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)


def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """Convert HSL (0-1) to RGB (0-255)."""
    r, g, b = colorsys.hls_to_rgb(h % 1.0, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))


def lerp_color(color1: Tuple[int, int, int], color2: Tuple[int, int, int], factor: float) -> Tuple[int, int, int]:
    """Linearly interpolate between two RGB colors."""
    factor = max(0.0, min(1.0, factor))
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
        int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor),
    )


def generate_color_gradient(start_color: Tuple[int, int, int], end_color: Tuple[int, int, int], steps: int) -> List[Tuple[int, int, int]]:
    """Generate a multi-step color gradient array."""
    if steps <= 1:
        return [start_color]
    return [lerp_color(start_color, end_color, i / (steps - 1)) for i in range(steps)]


def pulse_color(base_color: Tuple[int, int, int], target_color: Tuple[int, int, int], time_sec: float, frequency: float = 2.0) -> Tuple[int, int, int]:
    """Calculate pulsating color between base and target color using sine wave."""
    factor = (math.sin(time_sec * frequency * math.pi * 2.0) + 1.0) * 0.5
    return lerp_color(base_color, target_color, factor)


def hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    """Convert HEX string to RGB tuple."""
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
