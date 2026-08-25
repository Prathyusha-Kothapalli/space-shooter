"""
Crafting Recipe Engine and Component Inventory Manager.
"""

from typing import Dict, List, Any, Optional
from data.item_catalog import ItemCatalog, ItemSpec


class Recipe:
    """Blueprint recipe definition."""

    def __init__(self, recipe_id: str, name: str, result_item_id: str, ingredients: Dict[str, int]):
        self.recipe_id = recipe_id
        self.name = name
        self.result_item_id = result_item_id
        self.ingredients = ingredients


class CraftingManager:
    """Manages player crafting blueprints and inventory disassembly."""

    RECIPES: Dict[str, Recipe] = {
        "RECIPE_SHIELD_CAPACITOR": Recipe(
            recipe_id="RECIPE_SHIELD_CAPACITOR",
            name="Shield Capacitor Blueprint",
            result_item_id="SHIELD_CAPACITOR",
            ingredients={"TITANIUM_PLATING": 2, "PLASMA_INJECTOR": 1}
        ),
        "RECIPE_QUANTUM_PROCESSOR": Recipe(
            recipe_id="RECIPE_QUANTUM_PROCESSOR",
            name="Quantum Processor Blueprint",
            result_item_id="QUANTUM_PROCESSOR",
            ingredients={"PLASMA_INJECTOR": 2, "SHIELD_CAPACITOR": 1}
        ),
    }

    def __init__(self):
        self.item_inventory: Dict[str, int] = {}

    def add_item(self, item_id: str, count: int = 1) -> None:
        self.item_inventory[item_id] = self.item_inventory.get(item_id, 0) + count

    def remove_item(self, item_id: str, count: int = 1) -> bool:
        if self.item_inventory.get(item_id, 0) >= count:
            self.item_inventory[item_id] -= count
            return True
        return False

    def can_craft(self, recipe_id: str) -> bool:
        recipe = self.RECIPES.get(recipe_id)
        if not recipe:
            return False
        for ingredient_id, required_count in recipe.ingredients.items():
            if self.item_inventory.get(ingredient_id, 0) < required_count:
                return False
        return True

    def craft_item(self, recipe_id: str) -> Optional[ItemSpec]:
        """Craft item if ingredients are available."""
        if not self.can_craft(recipe_id):
            return None

        recipe = self.RECIPES[recipe_id]
        for ingredient_id, required_count in recipe.ingredients.items():
            self.remove_item(ingredient_id, required_count)

        self.add_item(recipe.result_item_id, 1)
        return ItemCatalog.get_item(recipe.result_item_id)
