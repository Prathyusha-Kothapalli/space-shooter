"""
Craftable Components, Blueprints, and Inventory Item Catalog.
"""

from typing import Dict, Any, List


class ItemSpec:
    """Specification for an inventory item or crafting ingredient."""

    def __init__(
        self,
        item_id: str,
        name: str,
        category: str,
        rarity: str,
        description: str,
        credit_value: int,
        stat_modifiers: Dict[str, float]
    ):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.rarity = rarity
        self.description = description
        self.credit_value = credit_value
        self.stat_modifiers = stat_modifiers


class ItemCatalog:
    """Database of craftable components, modules, and salvage items."""

    ITEMS: Dict[str, ItemSpec] = {
        "TITANIUM_PLATING": ItemSpec(
            item_id="TITANIUM_PLATING",
            name="Reinforced Titanium Alloy Plating",
            category="Crafting Material",
            rarity="COMMON",
            description="High-density structural alloy used for ship hull armor reinforcement.",
            credit_value=150,
            stat_modifiers={"armor": 2.0}
        ),
        "PLASMA_INJECTOR": ItemSpec(
            item_id="PLASMA_INJECTOR",
            name="Supercharged Plasma Injector",
            category="Weapon Component",
            rarity="UNCOMMON",
            description="Increases plasma energy acceleration and damage output.",
            credit_value=400,
            stat_modifiers={"plasma_damage": 0.15}
        ),
        "SHIELD_CAPACITOR": ItemSpec(
            item_id="SHIELD_CAPACITOR",
            name="Hyper-Shield Capacitor Core",
            category="Shield Component",
            rarity="RARE",
            description="Boosts maximum shield capacity and reduces regeneration delay.",
            credit_value=850,
            stat_modifiers={"max_shield": 30.0, "shield_regen_delay": -0.5}
        ),
        "QUANTUM_PROCESSOR": ItemSpec(
            item_id="QUANTUM_PROCESSOR",
            name="Quantum Target Processor",
            category="Avionics",
            rarity="EPIC",
            description="Advanced targeting computer granting elevated critical strike chance.",
            credit_value=1500,
            stat_modifiers={"crit_chance": 0.08, "crit_multiplier": 0.25}
        ),
        "DARK_MATTER_CELL": ItemSpec(
            item_id="DARK_MATTER_CELL",
            name="Dark Matter Energy Cell",
            category="Power Core",
            rarity="LEGENDARY",
            description="Exotic power core reducing weapon heat accumulation drastically.",
            credit_value=3500,
            stat_modifiers={"heat_dissipation": 0.30, "speed_boost": 0.10}
        ),
    }

    @classmethod
    def get_item(cls, item_id: str) -> ItemSpec:
        spec = cls.ITEMS.get(item_id)
        if not spec:
            raise KeyError(f"Unknown item identifier: {item_id}")
        return spec
