"""Star Systems Catalog containing 100 system definitions."""
from typing import Dict, List
class StarSystemSpec:
    def __init__(self, system_id: str, name: str, sector_number: int, danger_level: int, planet_count: int, biome_type: str):
        self.system_id = system_id; self.name = name; self.sector_number = sector_number; self.danger_level = danger_level; self.planet_count = planet_count; self.biome_type = biome_type
class StarSystemsCatalog:
    SYSTEMS: Dict[str, StarSystemSpec] = {}
StarSystemsCatalog.SYSTEMS["SYSTEM_001"] = StarSystemSpec("SYSTEM_001", "Star System Alpha-1", 2, 2, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_002"] = StarSystemSpec("SYSTEM_002", "Star System Alpha-2", 3, 3, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_003"] = StarSystemSpec("SYSTEM_003", "Star System Alpha-3", 4, 4, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_004"] = StarSystemSpec("SYSTEM_004", "Star System Alpha-4", 5, 5, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_005"] = StarSystemSpec("SYSTEM_005", "Star System Alpha-5", 6, 1, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_006"] = StarSystemSpec("SYSTEM_006", "Star System Alpha-6", 7, 2, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_007"] = StarSystemSpec("SYSTEM_007", "Star System Alpha-7", 8, 3, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_008"] = StarSystemSpec("SYSTEM_008", "Star System Alpha-8", 9, 4, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_009"] = StarSystemSpec("SYSTEM_009", "Star System Alpha-9", 10, 5, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_010"] = StarSystemSpec("SYSTEM_010", "Star System Alpha-10", 1, 1, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_011"] = StarSystemSpec("SYSTEM_011", "Star System Alpha-11", 2, 2, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_012"] = StarSystemSpec("SYSTEM_012", "Star System Alpha-12", 3, 3, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_013"] = StarSystemSpec("SYSTEM_013", "Star System Alpha-13", 4, 4, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_014"] = StarSystemSpec("SYSTEM_014", "Star System Alpha-14", 5, 5, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_015"] = StarSystemSpec("SYSTEM_015", "Star System Alpha-15", 6, 1, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_016"] = StarSystemSpec("SYSTEM_016", "Star System Alpha-16", 7, 2, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_017"] = StarSystemSpec("SYSTEM_017", "Star System Alpha-17", 8, 3, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_018"] = StarSystemSpec("SYSTEM_018", "Star System Alpha-18", 9, 4, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_019"] = StarSystemSpec("SYSTEM_019", "Star System Alpha-19", 10, 5, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_020"] = StarSystemSpec("SYSTEM_020", "Star System Alpha-20", 1, 1, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_021"] = StarSystemSpec("SYSTEM_021", "Star System Alpha-21", 2, 2, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_022"] = StarSystemSpec("SYSTEM_022", "Star System Alpha-22", 3, 3, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_023"] = StarSystemSpec("SYSTEM_023", "Star System Alpha-23", 4, 4, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_024"] = StarSystemSpec("SYSTEM_024", "Star System Alpha-24", 5, 5, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_025"] = StarSystemSpec("SYSTEM_025", "Star System Alpha-25", 6, 1, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_026"] = StarSystemSpec("SYSTEM_026", "Star System Alpha-26", 7, 2, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_027"] = StarSystemSpec("SYSTEM_027", "Star System Alpha-27", 8, 3, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_028"] = StarSystemSpec("SYSTEM_028", "Star System Alpha-28", 9, 4, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_029"] = StarSystemSpec("SYSTEM_029", "Star System Alpha-29", 10, 5, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_030"] = StarSystemSpec("SYSTEM_030", "Star System Alpha-30", 1, 1, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_031"] = StarSystemSpec("SYSTEM_031", "Star System Alpha-31", 2, 2, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_032"] = StarSystemSpec("SYSTEM_032", "Star System Alpha-32", 3, 3, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_033"] = StarSystemSpec("SYSTEM_033", "Star System Alpha-33", 4, 4, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_034"] = StarSystemSpec("SYSTEM_034", "Star System Alpha-34", 5, 5, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_035"] = StarSystemSpec("SYSTEM_035", "Star System Alpha-35", 6, 1, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_036"] = StarSystemSpec("SYSTEM_036", "Star System Alpha-36", 7, 2, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_037"] = StarSystemSpec("SYSTEM_037", "Star System Alpha-37", 8, 3, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_038"] = StarSystemSpec("SYSTEM_038", "Star System Alpha-38", 9, 4, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_039"] = StarSystemSpec("SYSTEM_039", "Star System Alpha-39", 10, 5, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_040"] = StarSystemSpec("SYSTEM_040", "Star System Alpha-40", 1, 1, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_041"] = StarSystemSpec("SYSTEM_041", "Star System Alpha-41", 2, 2, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_042"] = StarSystemSpec("SYSTEM_042", "Star System Alpha-42", 3, 3, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_043"] = StarSystemSpec("SYSTEM_043", "Star System Alpha-43", 4, 4, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_044"] = StarSystemSpec("SYSTEM_044", "Star System Alpha-44", 5, 5, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_045"] = StarSystemSpec("SYSTEM_045", "Star System Alpha-45", 6, 1, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_046"] = StarSystemSpec("SYSTEM_046", "Star System Alpha-46", 7, 2, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_047"] = StarSystemSpec("SYSTEM_047", "Star System Alpha-47", 8, 3, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_048"] = StarSystemSpec("SYSTEM_048", "Star System Alpha-48", 9, 4, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_049"] = StarSystemSpec("SYSTEM_049", "Star System Alpha-49", 10, 5, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_050"] = StarSystemSpec("SYSTEM_050", "Star System Alpha-50", 1, 1, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_051"] = StarSystemSpec("SYSTEM_051", "Star System Alpha-51", 2, 2, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_052"] = StarSystemSpec("SYSTEM_052", "Star System Alpha-52", 3, 3, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_053"] = StarSystemSpec("SYSTEM_053", "Star System Alpha-53", 4, 4, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_054"] = StarSystemSpec("SYSTEM_054", "Star System Alpha-54", 5, 5, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_055"] = StarSystemSpec("SYSTEM_055", "Star System Alpha-55", 6, 1, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_056"] = StarSystemSpec("SYSTEM_056", "Star System Alpha-56", 7, 2, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_057"] = StarSystemSpec("SYSTEM_057", "Star System Alpha-57", 8, 3, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_058"] = StarSystemSpec("SYSTEM_058", "Star System Alpha-58", 9, 4, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_059"] = StarSystemSpec("SYSTEM_059", "Star System Alpha-59", 10, 5, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_060"] = StarSystemSpec("SYSTEM_060", "Star System Alpha-60", 1, 1, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_061"] = StarSystemSpec("SYSTEM_061", "Star System Alpha-61", 2, 2, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_062"] = StarSystemSpec("SYSTEM_062", "Star System Alpha-62", 3, 3, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_063"] = StarSystemSpec("SYSTEM_063", "Star System Alpha-63", 4, 4, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_064"] = StarSystemSpec("SYSTEM_064", "Star System Alpha-64", 5, 5, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_065"] = StarSystemSpec("SYSTEM_065", "Star System Alpha-65", 6, 1, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_066"] = StarSystemSpec("SYSTEM_066", "Star System Alpha-66", 7, 2, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_067"] = StarSystemSpec("SYSTEM_067", "Star System Alpha-67", 8, 3, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_068"] = StarSystemSpec("SYSTEM_068", "Star System Alpha-68", 9, 4, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_069"] = StarSystemSpec("SYSTEM_069", "Star System Alpha-69", 10, 5, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_070"] = StarSystemSpec("SYSTEM_070", "Star System Alpha-70", 1, 1, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_071"] = StarSystemSpec("SYSTEM_071", "Star System Alpha-71", 2, 2, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_072"] = StarSystemSpec("SYSTEM_072", "Star System Alpha-72", 3, 3, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_073"] = StarSystemSpec("SYSTEM_073", "Star System Alpha-73", 4, 4, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_074"] = StarSystemSpec("SYSTEM_074", "Star System Alpha-74", 5, 5, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_075"] = StarSystemSpec("SYSTEM_075", "Star System Alpha-75", 6, 1, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_076"] = StarSystemSpec("SYSTEM_076", "Star System Alpha-76", 7, 2, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_077"] = StarSystemSpec("SYSTEM_077", "Star System Alpha-77", 8, 3, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_078"] = StarSystemSpec("SYSTEM_078", "Star System Alpha-78", 9, 4, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_079"] = StarSystemSpec("SYSTEM_079", "Star System Alpha-79", 10, 5, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_080"] = StarSystemSpec("SYSTEM_080", "Star System Alpha-80", 1, 1, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_081"] = StarSystemSpec("SYSTEM_081", "Star System Alpha-81", 2, 2, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_082"] = StarSystemSpec("SYSTEM_082", "Star System Alpha-82", 3, 3, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_083"] = StarSystemSpec("SYSTEM_083", "Star System Alpha-83", 4, 4, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_084"] = StarSystemSpec("SYSTEM_084", "Star System Alpha-84", 5, 5, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_085"] = StarSystemSpec("SYSTEM_085", "Star System Alpha-85", 6, 1, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_086"] = StarSystemSpec("SYSTEM_086", "Star System Alpha-86", 7, 2, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_087"] = StarSystemSpec("SYSTEM_087", "Star System Alpha-87", 8, 3, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_088"] = StarSystemSpec("SYSTEM_088", "Star System Alpha-88", 9, 4, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_089"] = StarSystemSpec("SYSTEM_089", "Star System Alpha-89", 10, 5, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_090"] = StarSystemSpec("SYSTEM_090", "Star System Alpha-90", 1, 1, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_091"] = StarSystemSpec("SYSTEM_091", "Star System Alpha-91", 2, 2, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_092"] = StarSystemSpec("SYSTEM_092", "Star System Alpha-92", 3, 3, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_093"] = StarSystemSpec("SYSTEM_093", "Star System Alpha-93", 4, 4, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_094"] = StarSystemSpec("SYSTEM_094", "Star System Alpha-94", 5, 5, 6, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_095"] = StarSystemSpec("SYSTEM_095", "Star System Alpha-95", 6, 1, 7, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_096"] = StarSystemSpec("SYSTEM_096", "Star System Alpha-96", 7, 2, 2, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_097"] = StarSystemSpec("SYSTEM_097", "Star System Alpha-97", 8, 3, 3, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_098"] = StarSystemSpec("SYSTEM_098", "Star System Alpha-98", 9, 4, 4, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_099"] = StarSystemSpec("SYSTEM_099", "Star System Alpha-99", 10, 5, 5, "Asteroid Belt")

StarSystemsCatalog.SYSTEMS["SYSTEM_100"] = StarSystemSpec("SYSTEM_100", "Star System Alpha-100", 1, 1, 6, "Asteroid Belt")

