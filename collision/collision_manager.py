"""
Collision Manager running Quadtree checks across player, enemies, projectiles, and powerups.
"""

from typing import List, Tuple, Callable, Dict, Set
from utils.math_utils import Vector2D
from collision.quadtree import Quadtree, QuadtreeRect, QuadtreeItem
from collision.collider import Collider
from configuration.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    CATEGORY_PLAYER, CATEGORY_PLAYER_PROJECTILE,
    CATEGORY_ENEMY, CATEGORY_ENEMY_PROJECTILE,
    CATEGORY_POWERUP, CATEGORY_BOSS
)


class CollisionManager:
    """Manages spatial partitioning and handles collision pairs."""

    def __init__(self):
        bounds = QuadtreeRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.quadtree = Quadtree(bounds, max_objects=12, max_levels=5)
        self.colliders: List[Collider] = []

    def register_collider(self, collider: Collider) -> None:
        """Register collider component."""
        if collider not in self.colliders:
            self.colliders.append(collider)

    def unregister_collider(self, collider: Collider) -> None:
        """Unregister collider component."""
        if collider in self.colliders:
            self.colliders.remove(collider)

    def clear(self) -> None:
        """Clear all registered colliders."""
        self.colliders.clear()
        self.quadtree.clear()

    def update_and_check(self, on_collision_callback: Callable[[Collider, Collider], None]) -> None:
        """Rebuild Quadtree and process all active colliders."""
        self.quadtree.clear()

        # Re-insert active colliders
        active_colliders = [c for c in self.colliders if c.is_active and hasattr(c.owner, 'is_active') and c.owner.is_active]
        
        for c in active_colliders:
            pos = c.get_position()
            item = QuadtreeItem(c, pos, c.radius)
            self.quadtree.insert(item)

        checked_pairs: Set[Tuple[int, int]] = set()

        for c1 in active_colliders:
            pos1 = c1.get_position()
            search_area = QuadtreeRect(pos1.x - c1.radius * 2, pos1.y - c1.radius * 2, c1.radius * 4, c1.radius * 4)
            candidates = self.quadtree.query(search_area)

            for item in candidates:
                c2: Collider = item.obj
                if c1 is c2:
                    continue

                pair_id = (min(id(c1), id(c2)), max(id(c1), id(c2)))
                if pair_id in checked_pairs:
                    continue

                checked_pairs.add(pair_id)

                # Category Filtering Matrix check
                if self._can_collide(c1.category, c2.category):
                    if c1.intersects(c2):
                        on_collision_callback(c1, c2)

    def _can_collide(self, cat1: int, cat2: int) -> bool:
        """Check if two collision categories interact."""
        # Player Projectile vs Enemy / Boss
        if (cat1 == CATEGORY_PLAYER_PROJECTILE and cat2 in (CATEGORY_ENEMY, CATEGORY_BOSS)) or \
           (cat2 == CATEGORY_PLAYER_PROJECTILE and cat1 in (CATEGORY_ENEMY, CATEGORY_BOSS)):
            return True
        # Enemy Projectile vs Player
        if (cat1 == CATEGORY_ENEMY_PROJECTILE and cat2 == CATEGORY_PLAYER) or \
           (cat2 == CATEGORY_ENEMY_PROJECTILE and cat1 == CATEGORY_PLAYER):
            return True
        # Player vs Enemy / Boss
        if (cat1 == CATEGORY_PLAYER and cat2 in (CATEGORY_ENEMY, CATEGORY_BOSS)) or \
           (cat2 == CATEGORY_PLAYER and cat1 in (CATEGORY_ENEMY, CATEGORY_BOSS)):
            return True
        # Player vs Powerup
        if (cat1 == CATEGORY_PLAYER and cat2 == CATEGORY_POWERUP) or \
           (cat2 == CATEGORY_PLAYER and cat1 == CATEGORY_POWERUP):
            return True

        return False
