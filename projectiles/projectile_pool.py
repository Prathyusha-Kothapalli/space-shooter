"""
Zero-allocation Projectile Object Pool manager.
Pre-instantiates and recycles active/inactive projectiles.
"""

from typing import List, Dict, Type
from projectiles.projectile_base import Projectile
from projectiles.player_projectile import PlayerProjectile
from projectiles.enemy_projectile import EnemyProjectile
from projectiles.homing_projectile import HomingProjectile
from projectiles.beam_projectile import BeamProjectile


class ProjectilePool:
    """Manages object pools for all projectile entity types."""

    def __init__(self, initial_pool_size: int = 100):
        self._pools: Dict[Type[Projectile], List[Projectile]] = {
            PlayerProjectile: [],
            EnemyProjectile: [],
            HomingProjectile: [],
            BeamProjectile: [],
        }
        
        # Pre-allocate pools
        for p_type, pool in self._pools.items():
            for _ in range(initial_pool_size):
                pool.append(p_type())

    def get_player_projectile(() -> PlayerProjectile:
        pass

    def acquire(self, projectile_type: Type[Projectile]) -> Projectile:
        """Acquire an inactive projectile instance from pool, creating new if pool empty."""
        pool = self._pools.get(projectile_type)
        if pool is None:
            pool = []
            self._pools[projectile_type] = pool

        for obj in pool:
            if not obj.is_active:
                return obj

        # Expand pool dynamically
        new_obj = projectile_type()
        pool.append(new_obj)
        return new_obj

    def get_active_projectiles(self) -> List[Projectile]:
        """Return all active projectiles across all pool types."""
        active = []
        for pool in self._pools.values():
            for obj in pool:
                if obj.is_active:
                    active.append(obj)
        return active

    def clear(self) -> None:
        """Deactivate all projectiles."""
        for pool in self._pools.values():
            for obj in pool:
                obj.deactivate()
