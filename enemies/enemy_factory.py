"""
Factory Pattern for constructing enemy ship entities.
"""

from typing import Dict, Type
from enemies.enemy_base import Enemy
from enemies.scout_enemy import ScoutEnemy
from enemies.interceptor_enemy import InterceptorEnemy
from enemies.cruiser_enemy import CruiserEnemy
from enemies.bomber_enemy import BomberEnemy
from enemies.stealth_drone import StealthDroneEnemy
from configuration.constants import (
    ENEMY_SCOUT, ENEMY_INTERCEPTOR, ENEMY_CRUISER,
    ENEMY_BOMBER, ENEMY_STEALTH
)


class EnemyFactory:
    """Instantiates enemy craft objects by enemy type identifier."""

    _REGISTRY: Dict[str, Type[Enemy]] = {
        ENEMY_SCOUT: ScoutEnemy,
        ENEMY_INTERCEPTOR: InterceptorEnemy,
        ENEMY_CRUISER: CruiserEnemy,
        ENEMY_BOMBER: BomberEnemy,
        ENEMY_STEALTH: StealthDroneEnemy,
    }

    @classmethod
    def create_enemy(cls, enemy_type: str) -> Enemy:
        """Create and return a new Enemy instance."""
        enemy_cls = cls._REGISTRY.get(enemy_type)
        if enemy_cls is None:
            raise ValueError(f"Unknown enemy type identifier: {enemy_type}")
        return enemy_cls()
