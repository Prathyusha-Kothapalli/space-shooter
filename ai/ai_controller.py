"""
AI Controller managing perception, state transitions, and attack behaviors.
"""

from enum import Enum
from typing import Optional, Any
from utils.math_utils import Vector2D
from ai.steering_behaviors import SteeringBehaviors


class AIState(Enum):
    PATROL = "PATROL"
    ENGAGE = "ENGAGE"
    FLANK = "FLANK"
    EVADE = "EVADE"


class AIController:
    """Controls AI logic states and computes navigation vectors for enemy ships."""

    def __init__(self, owner: Any, perception_range: float = 600.0):
        self.owner = owner
        self.perception_range = perception_range
        self.state = AIState.PATROL
        self.state_timer = 0.0

    def update(self, dt: float, player_target: Optional[Any]) -> Vector2D:
        """Update AI state and return combined steering force."""
        self.state_timer += dt

        if not player_target or not hasattr(player_target, 'position'):
            self.state = AIState.PATROL
            return SteeringBehaviors.wander(self.owner.velocity)

        dist_to_player = self.owner.position.distance_to(player_target.position)

        # State transition evaluation
        if dist_to_player > self.perception_range:
            self.state = AIState.PATROL
        elif self.owner.health.health_percentage() < 0.25:
            self.state = AIState.EVADE
        elif dist_to_player < 200.0:
            self.state = AIState.FLANK
        else:
            self.state = AIState.ENGAGE

        # Compute force based on active AIState
        if self.state == AIState.PATROL:
            return SteeringBehaviors.wander(self.owner.velocity)
        elif self.state == AIState.ENGAGE:
            return SteeringBehaviors.pursuit(self.owner.position, self.owner.velocity, player_target.position, player_target.velocity, self.owner.max_speed)
        elif self.state == AIState.FLANK:
            flank_pos = player_target.position + Vector2D(150.0 if self.owner.position.x > player_target.position.x else -150.0, 50.0)
            return SteeringBehaviors.arrive(self.owner.position, self.owner.velocity, flank_pos, self.owner.max_speed)
        elif self.state == AIState.EVADE:
            return SteeringBehaviors.evade(self.owner.position, self.owner.velocity, player_target.position, player_target.velocity, self.owner.max_speed)

        return Vector2D.zero()
