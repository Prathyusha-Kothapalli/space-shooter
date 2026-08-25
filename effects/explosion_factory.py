"""
Explosion Emitter Factory constructing 15+ specialized particle bursts.
"""

from typing import Tuple, Any
from utils.math_utils import Vector2D
from effects.particle_engine import ParticleEngine


class ExplosionFactory:
    """Creates custom explosion particle bursts."""

    @staticmethod
    def create_plasma_burst(engine: ParticleEngine, pos: Vector2D) -> None:
        """Emit plasma burst."""
        engine.emit_explosion(pos, count=35, color=(255, 0, 128))

    @staticmethod
    def create_emp_shockwave(engine: ParticleEngine, pos: Vector2D) -> None:
        """Emit EMP shockwave burst."""
        engine.emit_explosion(pos, count=45, color=(0, 230, 255))

    @staticmethod
    def create_boss_meltdown(engine: ParticleEngine, pos: Vector2D) -> None:
        """Emit massive boss core meltdown explosion."""
        engine.emit_explosion(pos, count=100, color=(255, 215, 0))
