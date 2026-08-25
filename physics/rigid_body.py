"""
2D RigidBody physics component handling velocity, acceleration, forces, drag, and rotation.
"""

from utils.math_utils import Vector2D, clamp


class RigidBody2D:
    """2D RigidBody physics dynamics component."""

    def __init__(self, owner: any, mass: float = 1.0, linear_drag: float = 0.95):
        self.owner = owner
        self.mass = max(0.1, float(mass))
        self.linear_drag = float(linear_drag)
        self.velocity = Vector2D.zero()
        self.acceleration = Vector2D.zero()
        self.force_accumulator = Vector2D.zero()
        self.angular_velocity = 0.0
        self.torque_accumulator = 0.0

    def add_force(self, force: Vector2D) -> None:
        """Apply force vector to rigid body."""
        self.force_accumulator += force

    def add_impulse(self, impulse: Vector2D) -> None:
        """Apply instant velocity impulse."""
        self.velocity += impulse / self.mass

    def update(self, dt: float) -> None:
        """Integrate forces and update owner position."""
        if not hasattr(self.owner, 'position'):
            return

        # Acceleration = Force / Mass
        self.acceleration = self.force_accumulator / self.mass
        self.velocity += self.acceleration * dt
        self.velocity *= self.linear_drag  # Apply drag dampening

        # Integrate Position
        self.owner.position += self.velocity * dt

        # Reset forces
        self.force_accumulator = Vector2D.zero()
