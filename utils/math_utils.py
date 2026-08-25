"""
High-performance 2D Vector mathematics, geometry calculations,
spatial transforms, interpolation, and collision helpers.
"""

import math
from typing import Tuple, Union, List, Optional


class Vector2D:
    """2D Vector representation with rich vector arithmetic operations."""
    __slots__ = ('x', 'y')

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[float, int]) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[float, int]) -> 'Vector2D':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[float, int]) -> 'Vector2D':
        if scalar == 0:
            return Vector2D(0.0, 0.0)
        return Vector2D(self.x / scalar, self.y / scalar)

    def __neg__(self) -> 'Vector2D':
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return math.isclose(self.x, other.x, abs_tol=1e-6) and math.isclose(self.y, other.y, abs_tol=1e-6)

    def length(self) -> float:
        """Return magnitude of the vector."""
        return math.hypot(self.x, self.y)

    def length_squared(self) -> float:
        """Return squared magnitude of vector (avoids square root)."""
        return self.x * self.x + self.y * self.y

    def normalize(self) -> 'Vector2D':
        """Return unit length vector in same direction."""
        mag = self.length()
        if mag == 0:
            return Vector2D(0.0, 0.0)
        return Vector2D(self.x / mag, self.y / mag)

    def dot(self, other: 'Vector2D') -> float:
        """Return dot product with another vector."""
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Vector2D') -> float:
        """Return 2D cross product magnitude."""
        return self.x * other.y - self.y * other.x

    def distance_to(self, other: 'Vector2D') -> float:
        """Calculate Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def distance_squared_to(self, other: 'Vector2D') -> float:
        """Calculate squared distance to another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy

    def angle(self) -> float:
        """Return angle in radians relative to positive X-axis."""
        return math.atan2(self.y, self.x)

    def angle_degrees(self) -> float:
        """Return angle in degrees relative to positive X-axis."""
        return math.degrees(self.angle())

    def angle_to(self, other: 'Vector2D') -> float:
        """Return angle between vector and target vector in radians."""
        dot_p = clamp(self.normalize().dot(other.normalize()), -1.0, 1.0)
        return math.acos(dot_p)

    def rotate(self, angle_radians: float) -> 'Vector2D':
        """Rotate vector by given angle in radians."""
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        return Vector2D(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )

    def lerp(self, target: 'Vector2D', t: float) -> 'Vector2D':
        """Linear interpolation towards target vector."""
        t = clamp(t, 0.0, 1.0)
        return Vector2D(
            self.x + (target.x - self.x) * t,
            self.y + (target.y - self.y) * t
        )

    def clamp_magnitude(self, max_length: float) -> 'Vector2D':
        """Limit maximum magnitude of the vector."""
        mag_sq = self.length_squared()
        if mag_sq > max_length * max_length and mag_sq > 0:
            scale = max_length / math.sqrt(mag_sq)
            return Vector2D(self.x * scale, self.y * scale)
        return Vector2D(self.x, self.y)

    def to_tuple(self) -> Tuple[float, float]:
        """Convert to (x, y) tuple."""
        return (self.x, self.y)

    def to_int_tuple(self) -> Tuple[int, int]:
        """Convert to rounded integer (x, y) tuple."""
        return (int(round(self.x)), int(round(self.y)))

    @staticmethod
    def zero() -> 'Vector2D':
        return Vector2D(0.0, 0.0)

    @staticmethod
    def up() -> 'Vector2D':
        return Vector2D(0.0, -1.0)

    @staticmethod
    def down() -> 'Vector2D':
        return Vector2D(0.0, 1.0)

    @staticmethod
    def left() -> 'Vector2D':
        return Vector2D(-1.0, 0.0)

    @staticmethod
    def right() -> 'Vector2D':
        return Vector2D(1.0, 0.0)


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp float value between min and max boundaries."""
    return max(min_val, min(value, max_val))


def lerp(start: float, end: float, t: float) -> float:
    """Linear interpolation between start and end values."""
    return start + (end - start) * clamp(t, 0.0, 1.0)


def smoothstep(start: float, end: float, t: float) -> float:
    """Hermite smooth interpolation between 0 and 1."""
    t = clamp((t - start) / (end - start), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def circle_intersects_circle(pos1: Vector2D, r1: float, pos2: Vector2D, r2: float) -> bool:
    """Check collision between two bounding circles."""
    dist_sq = pos1.distance_squared_to(pos2)
    radius_sum = r1 + r2
    return dist_sq <= (radius_sum * radius_sum)


def aabb_intersects_aabb(
    pos1: Vector2D, size1: Vector2D,
    pos2: Vector2D, size2: Vector2D
) -> bool:
    """Check collision between two Axis-Aligned Bounding Boxes (AABB)."""
    return (
        pos1.x < pos2.x + size2.x and
        pos1.x + size1.x > pos2.x and
        pos1.y < pos2.y + size2.y and
        pos1.y + size1.y > pos2.y
    )


def point_inside_circle(point: Vector2D, circle_center: Vector2D, radius: float) -> bool:
    """Check if point lies within bounding circle."""
    return point.distance_squared_to(circle_center) <= (radius * radius)
