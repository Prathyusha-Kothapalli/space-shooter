"""
Socketable Weapon and Ship Module Upgrade System.
"""

from typing import List, Dict, Any, Optional
from data.item_catalog import ItemSpec


class ShipModule:
    """Socketed module instance modifying player ship stats."""

    def __init__(self, spec: ItemSpec):
        self.spec = spec
        self.is_equipped = False

    def get_modifier(self, stat_name: str) -> float:
        """Return stat modifier value if present."""
        return self.spec.stat_modifiers.get(stat_name, 0.0)


class ModuleSystem:
    """Manages equipped modules and computes cumulative stat multipliers."""

    def __init__(self, max_slots: int = 4):
        self.max_slots = max_slots
        self.equipped_modules: List[ShipModule] = []

    def equip_module(self, module: ShipModule) -> bool:
        """Equip module into open slot."""
        if len(self.equipped_modules) < self.max_slots and module not in self.equipped_modules:
            module.is_equipped = True
            self.equipped_modules.append(module)
            return True
        return False

    def unequip_module(self, module: ShipModule) -> bool:
        """Unequip module from slot."""
        if module in self.equipped_modules:
            module.is_equipped = False
            self.equipped_modules.remove(module)
            return True
        return False

    def get_total_stat_bonus(self, stat_name: str) -> float:
        """Sum total bonuses for specified stat across equipped modules."""
        total = 0.0
        for mod in self.equipped_modules:
            total += mod.get_modifier(stat_name)
        return total
