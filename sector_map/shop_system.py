"""
In-game Shop and Vendor Economy System.
"""

from typing import List, Dict, Any, Optional
from data.weapon_catalog import WeaponCatalog, WeaponSpec
from data.item_catalog import ItemCatalog, ItemSpec


class ShopItem:
    """Item available for purchase in Sector Shop."""
    def __init__(self, item_id: str, name: str, category: str, price: int, payload: Any):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.payload = payload
        self.purchased = False


class ShopSystem:
    """Manages vendor shop inventory and transactions."""

    def __init__(self):
        self.inventory: List[ShopItem] = []
        self.refresh_shop()

    def refresh_shop(self) -> None:
        """Generate random vendor inventory listing."""
        self.inventory.clear()

        # Add Weapons
        w1 = WeaponCatalog.get_weapon("PULSE_CANNON_MK2")
        self.inventory.append(ShopItem(w1.weapon_id, w1.name, "WEAPON", 800, w1))

        w2 = WeaponCatalog.get_weapon("HEAVY_PLASMA_BLASTER")
        self.inventory.append(ShopItem(w2.weapon_id, w2.name, "WEAPON", 1200, w2))

        # Add Modules
        m1 = ItemCatalog.get_item("SHIELD_CAPACITOR")
        self.inventory.append(ShopItem(m1.item_id, m1.name, "MODULE", 850, m1))

        # Add Hull Repair Service
        self.inventory.append(ShopItem("REPAIR_HULL_50", "Hull Repair (50 HP)", "SERVICE", 300, 50.0))

    def buy_item(self, index: int, player_credits: int) -> Optional[ShopItem]:
        """Process purchase transaction if player has sufficient credits."""
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            if not item.purchased and player_credits >= item.price:
                item.purchased = True
                return item
        return None
