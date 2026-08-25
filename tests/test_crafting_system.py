"""
Test 8: Crafting Recipe Validation and Component Inventory assertions.
"""

import unittest
from crafting.crafting_manager import CraftingManager


class TestCraftingSystem(unittest.TestCase):
    def test_crafting_recipe(self):
        """Verify adding ingredients permits item crafting and removes components."""
        cm = CraftingManager()

        # Cannot craft initially
        self.assertFalse(cm.can_craft("RECIPE_SHIELD_CAPACITOR"))

        # Add ingredients
        cm.add_item("TITANIUM_PLATING", 2)
        cm.add_item("PLASMA_INJECTOR", 1)

        self.assertTrue(cm.can_craft("RECIPE_SHIELD_CAPACITOR"))

        # Execute craft
        result_item = cm.craft_item("RECIPE_SHIELD_CAPACITOR")
        self.assertIsNotNone(result_item)
        self.assertEqual(result_item.item_id, "SHIELD_CAPACITOR")
        self.assertEqual(cm.item_inventory.get("TITANIUM_PLATING", 0), 0)


if __name__ == "__main__":
    unittest.main()
