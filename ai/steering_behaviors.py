"""
Autonomous Steering Behaviors Engine (Seek, Flee, Arrive, Wander, Pursuit, Evade).
"""

import math
import random
from utils.math_utils import Vector2D, clamp


class SteeringBehaviors:
    """Calculates steering forces for autonomous enemy AI entities."""

    @staticmethod
    def seek(position: Vector2D, velocity: Vector2D, target: Vector2D, max_speed: float) -> Vector2D:
        """Calculate Seek steering force towards target point."""
        desired_velocity = (target - position).normalize() * max_speed
        return desired_velocity - velocity

    @staticmethod
    def flee(position: Vector2D, velocity: Vector2D, target: Vector2D, max_speed: float) -> Vector2D:
        """Calculate Flee steering force away from target point."""
        desired_velocity = (position - target).normalize() * max_speed
        return desired_velocity - velocity

    @staticmethod
    def arrive(position: Vector2D, velocity: Vector2D, target: Vector2D, max_speed: float, slowing_radius: float = 150.0) -> Vector2D:
        """Calculate Arrive steering force with smooth deceleration."""
        target_offset = target - position
        distance = target_offset.length()

        if distance == 0:
            return -velocity

        if distance < slowing_radius:
            ramped_speed = max_speed * (distance / slowing_radius)
            desired_velocity = target_offset * (ramped_speed / distance)
        else:
            desired_velocity = target_offset * (max_speed / distance)

        return desired_velocity - velocity

    @staticmethod
    def wander(velocity: Vector2D, wander_radius: float = 40.0, wander_distance: float = 80.0, wander_jitter: float = 15.0) -> Vector2D:
        """Calculate organic Wander steering force using circle perturbation."""
        random_angle = random.uniform(0, math.pi * 2)
        circle_center = velocity.normalize() * wander_distance
        displacement = Vector2D(math.cos(random_angle), math.sin(random_angle)) * wander_radius
        return circle_center + displacement

    @staticmethod
    def pursuit(position: Vector2D, velocity: Vector2D, target_pos: Vector2D, target_vel: Vector2D, max_speed: float) -> Vector2D:
        """Calculate Pursuit steering force predicting target's future trajectory."""
        distance = position.distance_to(target_pos)
        lookahead = distance / max_speed if max_speed > 0 else 0.0
        predicted_target = target_pos + target_vel * lookahead
        return SteeringBehaviors.seek(position, velocity, predicted_target, max_speed)

    @staticmethod
    def evade(position: Vector2D, velocity: Vector2D, target_pos: Vector2D, target_vel: Vector2D, max_speed: float) -> Vector2D:
        """Calculate Evade steering force predicting target's future trajectory."""
        distance = position.distance_to(target_pos)
        lookahead = distance / max_speed if max_speed > 0 else 0.0
        predicted_target = target_pos + target_vel * lookahead
        return SteeringBehaviors.flee(position, velocity, predicted_target, max_speed)
