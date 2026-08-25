"""Craftable Components and Item Catalog containing 150 item definitions."""
from typing import Dict, Any, List
class ItemSpec:
    def __init__(self, item_id: str, name: str, category: str, rarity: str, description: str, credit_value: int, stat_modifiers: Dict[str, float]):
        self.item_id = item_id; self.name = name; self.category = category; self.rarity = rarity; self.description = description; self.credit_value = credit_value; self.stat_modifiers = stat_modifiers
class ItemCatalog:
    ITEMS: Dict[str, ItemSpec] = {}

    @classmethod
    def get_item(cls, item_id: str) -> ItemSpec:
        if item_id in cls.ITEMS:
            return cls.ITEMS[item_id]
        return ItemSpec(item_id, item_id, "Material", "COMMON", "Crafted item", 100, {})

ItemCatalog.ITEMS["ITEM_COMPONENT_001"] = ItemSpec("ITEM_COMPONENT_001", "Salvage Module 001", "Material", "RARE", "High-tech component 1 salvaged from defeated alien flagships.", 150, {"damage": 0.060000000000000005, "shield": 12.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_002"] = ItemSpec("ITEM_COMPONENT_002", "Salvage Module 002", "Material", "RARE", "High-tech component 2 salvaged from defeated alien flagships.", 200, {"damage": 0.07, "shield": 14.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_003"] = ItemSpec("ITEM_COMPONENT_003", "Salvage Module 003", "Material", "RARE", "High-tech component 3 salvaged from defeated alien flagships.", 250, {"damage": 0.08, "shield": 16.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_004"] = ItemSpec("ITEM_COMPONENT_004", "Salvage Module 004", "Material", "RARE", "High-tech component 4 salvaged from defeated alien flagships.", 300, {"damage": 0.09, "shield": 18.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_005"] = ItemSpec("ITEM_COMPONENT_005", "Salvage Module 005", "Material", "RARE", "High-tech component 5 salvaged from defeated alien flagships.", 350, {"damage": 0.1, "shield": 20.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_006"] = ItemSpec("ITEM_COMPONENT_006", "Salvage Module 006", "Material", "RARE", "High-tech component 6 salvaged from defeated alien flagships.", 400, {"damage": 0.11, "shield": 22.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_007"] = ItemSpec("ITEM_COMPONENT_007", "Salvage Module 007", "Material", "RARE", "High-tech component 7 salvaged from defeated alien flagships.", 450, {"damage": 0.12000000000000001, "shield": 24.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_008"] = ItemSpec("ITEM_COMPONENT_008", "Salvage Module 008", "Material", "RARE", "High-tech component 8 salvaged from defeated alien flagships.", 500, {"damage": 0.13, "shield": 26.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_009"] = ItemSpec("ITEM_COMPONENT_009", "Salvage Module 009", "Material", "RARE", "High-tech component 9 salvaged from defeated alien flagships.", 550, {"damage": 0.14, "shield": 28.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_010"] = ItemSpec("ITEM_COMPONENT_010", "Salvage Module 010", "Material", "RARE", "High-tech component 10 salvaged from defeated alien flagships.", 600, {"damage": 0.15000000000000002, "shield": 30.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_011"] = ItemSpec("ITEM_COMPONENT_011", "Salvage Module 011", "Material", "RARE", "High-tech component 11 salvaged from defeated alien flagships.", 650, {"damage": 0.16, "shield": 32.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_012"] = ItemSpec("ITEM_COMPONENT_012", "Salvage Module 012", "Material", "RARE", "High-tech component 12 salvaged from defeated alien flagships.", 700, {"damage": 0.16999999999999998, "shield": 34.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_013"] = ItemSpec("ITEM_COMPONENT_013", "Salvage Module 013", "Material", "RARE", "High-tech component 13 salvaged from defeated alien flagships.", 750, {"damage": 0.18, "shield": 36.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_014"] = ItemSpec("ITEM_COMPONENT_014", "Salvage Module 014", "Material", "RARE", "High-tech component 14 salvaged from defeated alien flagships.", 800, {"damage": 0.19, "shield": 38.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_015"] = ItemSpec("ITEM_COMPONENT_015", "Salvage Module 015", "Material", "RARE", "High-tech component 15 salvaged from defeated alien flagships.", 850, {"damage": 0.2, "shield": 40.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_016"] = ItemSpec("ITEM_COMPONENT_016", "Salvage Module 016", "Material", "RARE", "High-tech component 16 salvaged from defeated alien flagships.", 900, {"damage": 0.21000000000000002, "shield": 42.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_017"] = ItemSpec("ITEM_COMPONENT_017", "Salvage Module 017", "Material", "RARE", "High-tech component 17 salvaged from defeated alien flagships.", 950, {"damage": 0.22000000000000003, "shield": 44.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_018"] = ItemSpec("ITEM_COMPONENT_018", "Salvage Module 018", "Material", "RARE", "High-tech component 18 salvaged from defeated alien flagships.", 1000, {"damage": 0.22999999999999998, "shield": 46.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_019"] = ItemSpec("ITEM_COMPONENT_019", "Salvage Module 019", "Material", "RARE", "High-tech component 19 salvaged from defeated alien flagships.", 1050, {"damage": 0.24, "shield": 48.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_020"] = ItemSpec("ITEM_COMPONENT_020", "Salvage Module 020", "Material", "RARE", "High-tech component 20 salvaged from defeated alien flagships.", 1100, {"damage": 0.25, "shield": 50.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_021"] = ItemSpec("ITEM_COMPONENT_021", "Salvage Module 021", "Material", "RARE", "High-tech component 21 salvaged from defeated alien flagships.", 1150, {"damage": 0.26, "shield": 52.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_022"] = ItemSpec("ITEM_COMPONENT_022", "Salvage Module 022", "Material", "RARE", "High-tech component 22 salvaged from defeated alien flagships.", 1200, {"damage": 0.27, "shield": 54.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_023"] = ItemSpec("ITEM_COMPONENT_023", "Salvage Module 023", "Material", "RARE", "High-tech component 23 salvaged from defeated alien flagships.", 1250, {"damage": 0.28, "shield": 56.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_024"] = ItemSpec("ITEM_COMPONENT_024", "Salvage Module 024", "Material", "RARE", "High-tech component 24 salvaged from defeated alien flagships.", 1300, {"damage": 0.29, "shield": 58.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_025"] = ItemSpec("ITEM_COMPONENT_025", "Salvage Module 025", "Material", "RARE", "High-tech component 25 salvaged from defeated alien flagships.", 1350, {"damage": 0.3, "shield": 60.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_026"] = ItemSpec("ITEM_COMPONENT_026", "Salvage Module 026", "Material", "RARE", "High-tech component 26 salvaged from defeated alien flagships.", 1400, {"damage": 0.31, "shield": 62.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_027"] = ItemSpec("ITEM_COMPONENT_027", "Salvage Module 027", "Material", "RARE", "High-tech component 27 salvaged from defeated alien flagships.", 1450, {"damage": 0.32, "shield": 64.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_028"] = ItemSpec("ITEM_COMPONENT_028", "Salvage Module 028", "Material", "RARE", "High-tech component 28 salvaged from defeated alien flagships.", 1500, {"damage": 0.33, "shield": 66.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_029"] = ItemSpec("ITEM_COMPONENT_029", "Salvage Module 029", "Material", "RARE", "High-tech component 29 salvaged from defeated alien flagships.", 1550, {"damage": 0.33999999999999997, "shield": 68.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_030"] = ItemSpec("ITEM_COMPONENT_030", "Salvage Module 030", "Material", "RARE", "High-tech component 30 salvaged from defeated alien flagships.", 1600, {"damage": 0.35, "shield": 70.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_031"] = ItemSpec("ITEM_COMPONENT_031", "Salvage Module 031", "Material", "RARE", "High-tech component 31 salvaged from defeated alien flagships.", 1650, {"damage": 0.36, "shield": 72.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_032"] = ItemSpec("ITEM_COMPONENT_032", "Salvage Module 032", "Material", "RARE", "High-tech component 32 salvaged from defeated alien flagships.", 1700, {"damage": 0.37, "shield": 74.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_033"] = ItemSpec("ITEM_COMPONENT_033", "Salvage Module 033", "Material", "RARE", "High-tech component 33 salvaged from defeated alien flagships.", 1750, {"damage": 0.38, "shield": 76.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_034"] = ItemSpec("ITEM_COMPONENT_034", "Salvage Module 034", "Material", "RARE", "High-tech component 34 salvaged from defeated alien flagships.", 1800, {"damage": 0.39, "shield": 78.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_035"] = ItemSpec("ITEM_COMPONENT_035", "Salvage Module 035", "Material", "RARE", "High-tech component 35 salvaged from defeated alien flagships.", 1850, {"damage": 0.4, "shield": 80.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_036"] = ItemSpec("ITEM_COMPONENT_036", "Salvage Module 036", "Material", "RARE", "High-tech component 36 salvaged from defeated alien flagships.", 1900, {"damage": 0.41, "shield": 82.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_037"] = ItemSpec("ITEM_COMPONENT_037", "Salvage Module 037", "Material", "RARE", "High-tech component 37 salvaged from defeated alien flagships.", 1950, {"damage": 0.42, "shield": 84.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_038"] = ItemSpec("ITEM_COMPONENT_038", "Salvage Module 038", "Material", "RARE", "High-tech component 38 salvaged from defeated alien flagships.", 2000, {"damage": 0.43, "shield": 86.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_039"] = ItemSpec("ITEM_COMPONENT_039", "Salvage Module 039", "Material", "RARE", "High-tech component 39 salvaged from defeated alien flagships.", 2050, {"damage": 0.44, "shield": 88.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_040"] = ItemSpec("ITEM_COMPONENT_040", "Salvage Module 040", "Material", "RARE", "High-tech component 40 salvaged from defeated alien flagships.", 2100, {"damage": 0.45, "shield": 90.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_041"] = ItemSpec("ITEM_COMPONENT_041", "Salvage Module 041", "Material", "RARE", "High-tech component 41 salvaged from defeated alien flagships.", 2150, {"damage": 0.46, "shield": 92.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_042"] = ItemSpec("ITEM_COMPONENT_042", "Salvage Module 042", "Material", "RARE", "High-tech component 42 salvaged from defeated alien flagships.", 2200, {"damage": 0.47, "shield": 94.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_043"] = ItemSpec("ITEM_COMPONENT_043", "Salvage Module 043", "Material", "RARE", "High-tech component 43 salvaged from defeated alien flagships.", 2250, {"damage": 0.48, "shield": 96.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_044"] = ItemSpec("ITEM_COMPONENT_044", "Salvage Module 044", "Material", "RARE", "High-tech component 44 salvaged from defeated alien flagships.", 2300, {"damage": 0.49, "shield": 98.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_045"] = ItemSpec("ITEM_COMPONENT_045", "Salvage Module 045", "Material", "RARE", "High-tech component 45 salvaged from defeated alien flagships.", 2350, {"damage": 0.5, "shield": 100.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_046"] = ItemSpec("ITEM_COMPONENT_046", "Salvage Module 046", "Material", "RARE", "High-tech component 46 salvaged from defeated alien flagships.", 2400, {"damage": 0.51, "shield": 102.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_047"] = ItemSpec("ITEM_COMPONENT_047", "Salvage Module 047", "Material", "RARE", "High-tech component 47 salvaged from defeated alien flagships.", 2450, {"damage": 0.52, "shield": 104.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_048"] = ItemSpec("ITEM_COMPONENT_048", "Salvage Module 048", "Material", "RARE", "High-tech component 48 salvaged from defeated alien flagships.", 2500, {"damage": 0.53, "shield": 106.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_049"] = ItemSpec("ITEM_COMPONENT_049", "Salvage Module 049", "Material", "RARE", "High-tech component 49 salvaged from defeated alien flagships.", 2550, {"damage": 0.54, "shield": 108.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_050"] = ItemSpec("ITEM_COMPONENT_050", "Salvage Module 050", "Material", "RARE", "High-tech component 50 salvaged from defeated alien flagships.", 2600, {"damage": 0.55, "shield": 110.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_051"] = ItemSpec("ITEM_COMPONENT_051", "Salvage Module 051", "Material", "RARE", "High-tech component 51 salvaged from defeated alien flagships.", 2650, {"damage": 0.56, "shield": 112.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_052"] = ItemSpec("ITEM_COMPONENT_052", "Salvage Module 052", "Material", "RARE", "High-tech component 52 salvaged from defeated alien flagships.", 2700, {"damage": 0.5700000000000001, "shield": 114.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_053"] = ItemSpec("ITEM_COMPONENT_053", "Salvage Module 053", "Material", "RARE", "High-tech component 53 salvaged from defeated alien flagships.", 2750, {"damage": 0.5800000000000001, "shield": 116.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_054"] = ItemSpec("ITEM_COMPONENT_054", "Salvage Module 054", "Material", "RARE", "High-tech component 54 salvaged from defeated alien flagships.", 2800, {"damage": 0.5900000000000001, "shield": 118.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_055"] = ItemSpec("ITEM_COMPONENT_055", "Salvage Module 055", "Material", "RARE", "High-tech component 55 salvaged from defeated alien flagships.", 2850, {"damage": 0.6000000000000001, "shield": 120.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_056"] = ItemSpec("ITEM_COMPONENT_056", "Salvage Module 056", "Material", "RARE", "High-tech component 56 salvaged from defeated alien flagships.", 2900, {"damage": 0.6100000000000001, "shield": 122.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_057"] = ItemSpec("ITEM_COMPONENT_057", "Salvage Module 057", "Material", "RARE", "High-tech component 57 salvaged from defeated alien flagships.", 2950, {"damage": 0.6200000000000001, "shield": 124.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_058"] = ItemSpec("ITEM_COMPONENT_058", "Salvage Module 058", "Material", "RARE", "High-tech component 58 salvaged from defeated alien flagships.", 3000, {"damage": 0.63, "shield": 126.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_059"] = ItemSpec("ITEM_COMPONENT_059", "Salvage Module 059", "Material", "RARE", "High-tech component 59 salvaged from defeated alien flagships.", 3050, {"damage": 0.64, "shield": 128.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_060"] = ItemSpec("ITEM_COMPONENT_060", "Salvage Module 060", "Material", "RARE", "High-tech component 60 salvaged from defeated alien flagships.", 3100, {"damage": 0.65, "shield": 130.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_061"] = ItemSpec("ITEM_COMPONENT_061", "Salvage Module 061", "Material", "RARE", "High-tech component 61 salvaged from defeated alien flagships.", 3150, {"damage": 0.66, "shield": 132.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_062"] = ItemSpec("ITEM_COMPONENT_062", "Salvage Module 062", "Material", "RARE", "High-tech component 62 salvaged from defeated alien flagships.", 3200, {"damage": 0.67, "shield": 134.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_063"] = ItemSpec("ITEM_COMPONENT_063", "Salvage Module 063", "Material", "RARE", "High-tech component 63 salvaged from defeated alien flagships.", 3250, {"damage": 0.68, "shield": 136.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_064"] = ItemSpec("ITEM_COMPONENT_064", "Salvage Module 064", "Material", "RARE", "High-tech component 64 salvaged from defeated alien flagships.", 3300, {"damage": 0.6900000000000001, "shield": 138.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_065"] = ItemSpec("ITEM_COMPONENT_065", "Salvage Module 065", "Material", "RARE", "High-tech component 65 salvaged from defeated alien flagships.", 3350, {"damage": 0.7000000000000001, "shield": 140.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_066"] = ItemSpec("ITEM_COMPONENT_066", "Salvage Module 066", "Material", "RARE", "High-tech component 66 salvaged from defeated alien flagships.", 3400, {"damage": 0.7100000000000001, "shield": 142.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_067"] = ItemSpec("ITEM_COMPONENT_067", "Salvage Module 067", "Material", "RARE", "High-tech component 67 salvaged from defeated alien flagships.", 3450, {"damage": 0.7200000000000001, "shield": 144.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_068"] = ItemSpec("ITEM_COMPONENT_068", "Salvage Module 068", "Material", "RARE", "High-tech component 68 salvaged from defeated alien flagships.", 3500, {"damage": 0.7300000000000001, "shield": 146.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_069"] = ItemSpec("ITEM_COMPONENT_069", "Salvage Module 069", "Material", "RARE", "High-tech component 69 salvaged from defeated alien flagships.", 3550, {"damage": 0.7400000000000001, "shield": 148.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_070"] = ItemSpec("ITEM_COMPONENT_070", "Salvage Module 070", "Material", "RARE", "High-tech component 70 salvaged from defeated alien flagships.", 3600, {"damage": 0.7500000000000001, "shield": 150.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_071"] = ItemSpec("ITEM_COMPONENT_071", "Salvage Module 071", "Material", "RARE", "High-tech component 71 salvaged from defeated alien flagships.", 3650, {"damage": 0.76, "shield": 152.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_072"] = ItemSpec("ITEM_COMPONENT_072", "Salvage Module 072", "Material", "RARE", "High-tech component 72 salvaged from defeated alien flagships.", 3700, {"damage": 0.77, "shield": 154.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_073"] = ItemSpec("ITEM_COMPONENT_073", "Salvage Module 073", "Material", "RARE", "High-tech component 73 salvaged from defeated alien flagships.", 3750, {"damage": 0.78, "shield": 156.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_074"] = ItemSpec("ITEM_COMPONENT_074", "Salvage Module 074", "Material", "RARE", "High-tech component 74 salvaged from defeated alien flagships.", 3800, {"damage": 0.79, "shield": 158.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_075"] = ItemSpec("ITEM_COMPONENT_075", "Salvage Module 075", "Material", "RARE", "High-tech component 75 salvaged from defeated alien flagships.", 3850, {"damage": 0.8, "shield": 160.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_076"] = ItemSpec("ITEM_COMPONENT_076", "Salvage Module 076", "Material", "RARE", "High-tech component 76 salvaged from defeated alien flagships.", 3900, {"damage": 0.81, "shield": 162.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_077"] = ItemSpec("ITEM_COMPONENT_077", "Salvage Module 077", "Material", "RARE", "High-tech component 77 salvaged from defeated alien flagships.", 3950, {"damage": 0.8200000000000001, "shield": 164.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_078"] = ItemSpec("ITEM_COMPONENT_078", "Salvage Module 078", "Material", "RARE", "High-tech component 78 salvaged from defeated alien flagships.", 4000, {"damage": 0.8300000000000001, "shield": 166.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_079"] = ItemSpec("ITEM_COMPONENT_079", "Salvage Module 079", "Material", "RARE", "High-tech component 79 salvaged from defeated alien flagships.", 4050, {"damage": 0.8400000000000001, "shield": 168.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_080"] = ItemSpec("ITEM_COMPONENT_080", "Salvage Module 080", "Material", "RARE", "High-tech component 80 salvaged from defeated alien flagships.", 4100, {"damage": 0.8500000000000001, "shield": 170.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_081"] = ItemSpec("ITEM_COMPONENT_081", "Salvage Module 081", "Material", "RARE", "High-tech component 81 salvaged from defeated alien flagships.", 4150, {"damage": 0.8600000000000001, "shield": 172.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_082"] = ItemSpec("ITEM_COMPONENT_082", "Salvage Module 082", "Material", "RARE", "High-tech component 82 salvaged from defeated alien flagships.", 4200, {"damage": 0.8700000000000001, "shield": 174.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_083"] = ItemSpec("ITEM_COMPONENT_083", "Salvage Module 083", "Material", "RARE", "High-tech component 83 salvaged from defeated alien flagships.", 4250, {"damage": 0.8800000000000001, "shield": 176.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_084"] = ItemSpec("ITEM_COMPONENT_084", "Salvage Module 084", "Material", "RARE", "High-tech component 84 salvaged from defeated alien flagships.", 4300, {"damage": 0.89, "shield": 178.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_085"] = ItemSpec("ITEM_COMPONENT_085", "Salvage Module 085", "Material", "RARE", "High-tech component 85 salvaged from defeated alien flagships.", 4350, {"damage": 0.9, "shield": 180.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_086"] = ItemSpec("ITEM_COMPONENT_086", "Salvage Module 086", "Material", "RARE", "High-tech component 86 salvaged from defeated alien flagships.", 4400, {"damage": 0.91, "shield": 182.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_087"] = ItemSpec("ITEM_COMPONENT_087", "Salvage Module 087", "Material", "RARE", "High-tech component 87 salvaged from defeated alien flagships.", 4450, {"damage": 0.92, "shield": 184.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_088"] = ItemSpec("ITEM_COMPONENT_088", "Salvage Module 088", "Material", "RARE", "High-tech component 88 salvaged from defeated alien flagships.", 4500, {"damage": 0.93, "shield": 186.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_089"] = ItemSpec("ITEM_COMPONENT_089", "Salvage Module 089", "Material", "RARE", "High-tech component 89 salvaged from defeated alien flagships.", 4550, {"damage": 0.9400000000000001, "shield": 188.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_090"] = ItemSpec("ITEM_COMPONENT_090", "Salvage Module 090", "Material", "RARE", "High-tech component 90 salvaged from defeated alien flagships.", 4600, {"damage": 0.9500000000000001, "shield": 190.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_091"] = ItemSpec("ITEM_COMPONENT_091", "Salvage Module 091", "Material", "RARE", "High-tech component 91 salvaged from defeated alien flagships.", 4650, {"damage": 0.9600000000000001, "shield": 192.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_092"] = ItemSpec("ITEM_COMPONENT_092", "Salvage Module 092", "Material", "RARE", "High-tech component 92 salvaged from defeated alien flagships.", 4700, {"damage": 0.9700000000000001, "shield": 194.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_093"] = ItemSpec("ITEM_COMPONENT_093", "Salvage Module 093", "Material", "RARE", "High-tech component 93 salvaged from defeated alien flagships.", 4750, {"damage": 0.9800000000000001, "shield": 196.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_094"] = ItemSpec("ITEM_COMPONENT_094", "Salvage Module 094", "Material", "RARE", "High-tech component 94 salvaged from defeated alien flagships.", 4800, {"damage": 0.9900000000000001, "shield": 198.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_095"] = ItemSpec("ITEM_COMPONENT_095", "Salvage Module 095", "Material", "RARE", "High-tech component 95 salvaged from defeated alien flagships.", 4850, {"damage": 1.0, "shield": 200.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_096"] = ItemSpec("ITEM_COMPONENT_096", "Salvage Module 096", "Material", "RARE", "High-tech component 96 salvaged from defeated alien flagships.", 4900, {"damage": 1.01, "shield": 202.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_097"] = ItemSpec("ITEM_COMPONENT_097", "Salvage Module 097", "Material", "RARE", "High-tech component 97 salvaged from defeated alien flagships.", 4950, {"damage": 1.02, "shield": 204.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_098"] = ItemSpec("ITEM_COMPONENT_098", "Salvage Module 098", "Material", "RARE", "High-tech component 98 salvaged from defeated alien flagships.", 5000, {"damage": 1.03, "shield": 206.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_099"] = ItemSpec("ITEM_COMPONENT_099", "Salvage Module 099", "Material", "RARE", "High-tech component 99 salvaged from defeated alien flagships.", 5050, {"damage": 1.04, "shield": 208.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_100"] = ItemSpec("ITEM_COMPONENT_100", "Salvage Module 100", "Material", "RARE", "High-tech component 100 salvaged from defeated alien flagships.", 5100, {"damage": 1.05, "shield": 210.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_101"] = ItemSpec("ITEM_COMPONENT_101", "Salvage Module 101", "Material", "RARE", "High-tech component 101 salvaged from defeated alien flagships.", 5150, {"damage": 1.06, "shield": 212.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_102"] = ItemSpec("ITEM_COMPONENT_102", "Salvage Module 102", "Material", "RARE", "High-tech component 102 salvaged from defeated alien flagships.", 5200, {"damage": 1.07, "shield": 214.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_103"] = ItemSpec("ITEM_COMPONENT_103", "Salvage Module 103", "Material", "RARE", "High-tech component 103 salvaged from defeated alien flagships.", 5250, {"damage": 1.08, "shield": 216.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_104"] = ItemSpec("ITEM_COMPONENT_104", "Salvage Module 104", "Material", "RARE", "High-tech component 104 salvaged from defeated alien flagships.", 5300, {"damage": 1.09, "shield": 218.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_105"] = ItemSpec("ITEM_COMPONENT_105", "Salvage Module 105", "Material", "RARE", "High-tech component 105 salvaged from defeated alien flagships.", 5350, {"damage": 1.1, "shield": 220.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_106"] = ItemSpec("ITEM_COMPONENT_106", "Salvage Module 106", "Material", "RARE", "High-tech component 106 salvaged from defeated alien flagships.", 5400, {"damage": 1.11, "shield": 222.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_107"] = ItemSpec("ITEM_COMPONENT_107", "Salvage Module 107", "Material", "RARE", "High-tech component 107 salvaged from defeated alien flagships.", 5450, {"damage": 1.12, "shield": 224.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_108"] = ItemSpec("ITEM_COMPONENT_108", "Salvage Module 108", "Material", "RARE", "High-tech component 108 salvaged from defeated alien flagships.", 5500, {"damage": 1.1300000000000001, "shield": 226.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_109"] = ItemSpec("ITEM_COMPONENT_109", "Salvage Module 109", "Material", "RARE", "High-tech component 109 salvaged from defeated alien flagships.", 5550, {"damage": 1.1400000000000001, "shield": 228.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_110"] = ItemSpec("ITEM_COMPONENT_110", "Salvage Module 110", "Material", "RARE", "High-tech component 110 salvaged from defeated alien flagships.", 5600, {"damage": 1.1500000000000001, "shield": 230.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_111"] = ItemSpec("ITEM_COMPONENT_111", "Salvage Module 111", "Material", "RARE", "High-tech component 111 salvaged from defeated alien flagships.", 5650, {"damage": 1.1600000000000001, "shield": 232.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_112"] = ItemSpec("ITEM_COMPONENT_112", "Salvage Module 112", "Material", "RARE", "High-tech component 112 salvaged from defeated alien flagships.", 5700, {"damage": 1.1700000000000002, "shield": 234.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_113"] = ItemSpec("ITEM_COMPONENT_113", "Salvage Module 113", "Material", "RARE", "High-tech component 113 salvaged from defeated alien flagships.", 5750, {"damage": 1.1800000000000002, "shield": 236.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_114"] = ItemSpec("ITEM_COMPONENT_114", "Salvage Module 114", "Material", "RARE", "High-tech component 114 salvaged from defeated alien flagships.", 5800, {"damage": 1.1900000000000002, "shield": 238.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_115"] = ItemSpec("ITEM_COMPONENT_115", "Salvage Module 115", "Material", "RARE", "High-tech component 115 salvaged from defeated alien flagships.", 5850, {"damage": 1.2000000000000002, "shield": 240.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_116"] = ItemSpec("ITEM_COMPONENT_116", "Salvage Module 116", "Material", "RARE", "High-tech component 116 salvaged from defeated alien flagships.", 5900, {"damage": 1.21, "shield": 242.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_117"] = ItemSpec("ITEM_COMPONENT_117", "Salvage Module 117", "Material", "RARE", "High-tech component 117 salvaged from defeated alien flagships.", 5950, {"damage": 1.22, "shield": 244.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_118"] = ItemSpec("ITEM_COMPONENT_118", "Salvage Module 118", "Material", "RARE", "High-tech component 118 salvaged from defeated alien flagships.", 6000, {"damage": 1.23, "shield": 246.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_119"] = ItemSpec("ITEM_COMPONENT_119", "Salvage Module 119", "Material", "RARE", "High-tech component 119 salvaged from defeated alien flagships.", 6050, {"damage": 1.24, "shield": 248.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_120"] = ItemSpec("ITEM_COMPONENT_120", "Salvage Module 120", "Material", "RARE", "High-tech component 120 salvaged from defeated alien flagships.", 6100, {"damage": 1.25, "shield": 250.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_121"] = ItemSpec("ITEM_COMPONENT_121", "Salvage Module 121", "Material", "RARE", "High-tech component 121 salvaged from defeated alien flagships.", 6150, {"damage": 1.26, "shield": 252.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_122"] = ItemSpec("ITEM_COMPONENT_122", "Salvage Module 122", "Material", "RARE", "High-tech component 122 salvaged from defeated alien flagships.", 6200, {"damage": 1.27, "shield": 254.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_123"] = ItemSpec("ITEM_COMPONENT_123", "Salvage Module 123", "Material", "RARE", "High-tech component 123 salvaged from defeated alien flagships.", 6250, {"damage": 1.28, "shield": 256.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_124"] = ItemSpec("ITEM_COMPONENT_124", "Salvage Module 124", "Material", "RARE", "High-tech component 124 salvaged from defeated alien flagships.", 6300, {"damage": 1.29, "shield": 258.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_125"] = ItemSpec("ITEM_COMPONENT_125", "Salvage Module 125", "Material", "RARE", "High-tech component 125 salvaged from defeated alien flagships.", 6350, {"damage": 1.3, "shield": 260.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_126"] = ItemSpec("ITEM_COMPONENT_126", "Salvage Module 126", "Material", "RARE", "High-tech component 126 salvaged from defeated alien flagships.", 6400, {"damage": 1.31, "shield": 262.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_127"] = ItemSpec("ITEM_COMPONENT_127", "Salvage Module 127", "Material", "RARE", "High-tech component 127 salvaged from defeated alien flagships.", 6450, {"damage": 1.32, "shield": 264.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_128"] = ItemSpec("ITEM_COMPONENT_128", "Salvage Module 128", "Material", "RARE", "High-tech component 128 salvaged from defeated alien flagships.", 6500, {"damage": 1.33, "shield": 266.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_129"] = ItemSpec("ITEM_COMPONENT_129", "Salvage Module 129", "Material", "RARE", "High-tech component 129 salvaged from defeated alien flagships.", 6550, {"damage": 1.34, "shield": 268.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_130"] = ItemSpec("ITEM_COMPONENT_130", "Salvage Module 130", "Material", "RARE", "High-tech component 130 salvaged from defeated alien flagships.", 6600, {"damage": 1.35, "shield": 270.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_131"] = ItemSpec("ITEM_COMPONENT_131", "Salvage Module 131", "Material", "RARE", "High-tech component 131 salvaged from defeated alien flagships.", 6650, {"damage": 1.36, "shield": 272.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_132"] = ItemSpec("ITEM_COMPONENT_132", "Salvage Module 132", "Material", "RARE", "High-tech component 132 salvaged from defeated alien flagships.", 6700, {"damage": 1.37, "shield": 274.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_133"] = ItemSpec("ITEM_COMPONENT_133", "Salvage Module 133", "Material", "RARE", "High-tech component 133 salvaged from defeated alien flagships.", 6750, {"damage": 1.3800000000000001, "shield": 276.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_134"] = ItemSpec("ITEM_COMPONENT_134", "Salvage Module 134", "Material", "RARE", "High-tech component 134 salvaged from defeated alien flagships.", 6800, {"damage": 1.3900000000000001, "shield": 278.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_135"] = ItemSpec("ITEM_COMPONENT_135", "Salvage Module 135", "Material", "RARE", "High-tech component 135 salvaged from defeated alien flagships.", 6850, {"damage": 1.4000000000000001, "shield": 280.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_136"] = ItemSpec("ITEM_COMPONENT_136", "Salvage Module 136", "Material", "RARE", "High-tech component 136 salvaged from defeated alien flagships.", 6900, {"damage": 1.4100000000000001, "shield": 282.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_137"] = ItemSpec("ITEM_COMPONENT_137", "Salvage Module 137", "Material", "RARE", "High-tech component 137 salvaged from defeated alien flagships.", 6950, {"damage": 1.4200000000000002, "shield": 284.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_138"] = ItemSpec("ITEM_COMPONENT_138", "Salvage Module 138", "Material", "RARE", "High-tech component 138 salvaged from defeated alien flagships.", 7000, {"damage": 1.4300000000000002, "shield": 286.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_139"] = ItemSpec("ITEM_COMPONENT_139", "Salvage Module 139", "Material", "RARE", "High-tech component 139 salvaged from defeated alien flagships.", 7050, {"damage": 1.4400000000000002, "shield": 288.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_140"] = ItemSpec("ITEM_COMPONENT_140", "Salvage Module 140", "Material", "RARE", "High-tech component 140 salvaged from defeated alien flagships.", 7100, {"damage": 1.4500000000000002, "shield": 290.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_141"] = ItemSpec("ITEM_COMPONENT_141", "Salvage Module 141", "Material", "RARE", "High-tech component 141 salvaged from defeated alien flagships.", 7150, {"damage": 1.46, "shield": 292.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_142"] = ItemSpec("ITEM_COMPONENT_142", "Salvage Module 142", "Material", "RARE", "High-tech component 142 salvaged from defeated alien flagships.", 7200, {"damage": 1.47, "shield": 294.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_143"] = ItemSpec("ITEM_COMPONENT_143", "Salvage Module 143", "Material", "RARE", "High-tech component 143 salvaged from defeated alien flagships.", 7250, {"damage": 1.48, "shield": 296.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_144"] = ItemSpec("ITEM_COMPONENT_144", "Salvage Module 144", "Material", "RARE", "High-tech component 144 salvaged from defeated alien flagships.", 7300, {"damage": 1.49, "shield": 298.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_145"] = ItemSpec("ITEM_COMPONENT_145", "Salvage Module 145", "Material", "RARE", "High-tech component 145 salvaged from defeated alien flagships.", 7350, {"damage": 1.5, "shield": 300.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_146"] = ItemSpec("ITEM_COMPONENT_146", "Salvage Module 146", "Material", "RARE", "High-tech component 146 salvaged from defeated alien flagships.", 7400, {"damage": 1.51, "shield": 302.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_147"] = ItemSpec("ITEM_COMPONENT_147", "Salvage Module 147", "Material", "RARE", "High-tech component 147 salvaged from defeated alien flagships.", 7450, {"damage": 1.52, "shield": 304.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_148"] = ItemSpec("ITEM_COMPONENT_148", "Salvage Module 148", "Material", "RARE", "High-tech component 148 salvaged from defeated alien flagships.", 7500, {"damage": 1.53, "shield": 306.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_149"] = ItemSpec("ITEM_COMPONENT_149", "Salvage Module 149", "Material", "RARE", "High-tech component 149 salvaged from defeated alien flagships.", 7550, {"damage": 1.54, "shield": 308.0})

ItemCatalog.ITEMS["ITEM_COMPONENT_150"] = ItemSpec("ITEM_COMPONENT_150", "Salvage Module 150", "Material", "RARE", "High-tech component 150 salvaged from defeated alien flagships.", 7600, {"damage": 1.55, "shield": 310.0})

