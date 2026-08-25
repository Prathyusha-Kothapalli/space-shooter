"""Weapon Catalog containing 100 weapon specifications."""
from typing import Dict, Any, List, Tuple
class WeaponSpec:
    def __init__(self, weapon_id: str, name: str, category: str, description: str, damage: float, fire_rate: float, heat_per_shot: float, energy_cost: float, projectile_speed: float, projectile_count: int, spread_angle: float, damage_type: str, crit_chance: float, crit_mult: float, unlock_tier: int, color_rgb: Tuple[int, int, int], recoil_force: float, splash_radius: float, pierce_count: int, homing_turn_rate: float):
        self.weapon_id = weapon_id; self.name = name; self.category = category; self.description = description; self.damage = damage; self.fire_rate = fire_rate; self.heat_per_shot = heat_per_shot; self.energy_cost = energy_cost; self.projectile_speed = projectile_speed; self.projectile_count = projectile_count; self.spread_angle = spread_angle; self.damage_type = damage_type; self.crit_chance = crit_chance; self.crit_mult = crit_mult; self.unlock_tier = unlock_tier; self.color_rgb = color_rgb; self.recoil_force = recoil_force; self.splash_radius = splash_radius; self.pierce_count = pierce_count; self.homing_turn_rate = homing_turn_rate
class WeaponCatalog:
    WEAPONS: Dict[str, WeaponSpec] = {}
WeaponCatalog.WEAPONS["WEAPON_MODEL_001"] = WeaponSpec("WEAPON_MODEL_001", "Ordnance Mark 1", "Pulse", "High output weapon variant 1.", 17.5, 9.0, 3.5, 2.5, 610.0, 2, 0.1, "ENERGY", 0.060000000000000005, 1.6, 2, (17, 31, 47), 5.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_002"] = WeaponSpec("WEAPON_MODEL_002", "Ordnance Mark 2", "Pulse", "High output weapon variant 2.", 20.0, 8.0, 4.0, 3.0, 620.0, 3, 0.2, "ENERGY", 0.07, 1.7, 3, (34, 62, 94), 5.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_003"] = WeaponSpec("WEAPON_MODEL_003", "Ordnance Mark 3", "Pulse", "High output weapon variant 3.", 22.5, 7.0, 4.5, 3.5, 630.0, 4, 0.30000000000000004, "ENERGY", 0.08, 1.8, 4, (51, 93, 141), 5.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_004"] = WeaponSpec("WEAPON_MODEL_004", "Ordnance Mark 4", "Pulse", "High output weapon variant 4.", 25.0, 6.0, 5.0, 4.0, 640.0, 1, 0.4, "ENERGY", 0.09, 1.9, 5, (68, 124, 188), 5.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_005"] = WeaponSpec("WEAPON_MODEL_005", "Ordnance Mark 5", "Pulse", "High output weapon variant 5.", 27.5, 10.0, 5.5, 4.5, 650.0, 2, 0.0, "ENERGY", 0.1, 2.0, 1, (85, 155, 235), 6.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_006"] = WeaponSpec("WEAPON_MODEL_006", "Ordnance Mark 6", "Pulse", "High output weapon variant 6.", 30.0, 9.0, 6.0, 5.0, 660.0, 3, 0.1, "ENERGY", 0.11, 2.1, 2, (102, 186, 26), 6.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_007"] = WeaponSpec("WEAPON_MODEL_007", "Ordnance Mark 7", "Pulse", "High output weapon variant 7.", 32.5, 8.0, 6.5, 5.5, 670.0, 4, 0.2, "ENERGY", 0.12000000000000001, 2.2, 3, (119, 217, 73), 6.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_008"] = WeaponSpec("WEAPON_MODEL_008", "Ordnance Mark 8", "Pulse", "High output weapon variant 8.", 35.0, 7.0, 7.0, 6.0, 680.0, 1, 0.30000000000000004, "ENERGY", 0.13, 2.3, 4, (136, 248, 120), 6.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_009"] = WeaponSpec("WEAPON_MODEL_009", "Ordnance Mark 9", "Pulse", "High output weapon variant 9.", 37.5, 6.0, 7.5, 6.5, 690.0, 2, 0.4, "ENERGY", 0.14, 2.4, 5, (153, 23, 167), 6.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_010"] = WeaponSpec("WEAPON_MODEL_010", "Ordnance Mark 10", "Pulse", "High output weapon variant 10.", 40.0, 10.0, 8.0, 7.0, 700.0, 3, 0.0, "ENERGY", 0.15000000000000002, 2.5, 1, (170, 54, 214), 7.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_011"] = WeaponSpec("WEAPON_MODEL_011", "Ordnance Mark 11", "Pulse", "High output weapon variant 11.", 42.5, 9.0, 8.5, 7.5, 710.0, 4, 0.1, "ENERGY", 0.16, 2.6, 2, (187, 85, 5), 7.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_012"] = WeaponSpec("WEAPON_MODEL_012", "Ordnance Mark 12", "Pulse", "High output weapon variant 12.", 45.0, 8.0, 9.0, 8.0, 720.0, 1, 0.2, "ENERGY", 0.16999999999999998, 2.7, 3, (204, 116, 52), 7.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_013"] = WeaponSpec("WEAPON_MODEL_013", "Ordnance Mark 13", "Pulse", "High output weapon variant 13.", 47.5, 7.0, 9.5, 8.5, 730.0, 2, 0.30000000000000004, "ENERGY", 0.18, 2.8, 4, (221, 147, 99), 7.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_014"] = WeaponSpec("WEAPON_MODEL_014", "Ordnance Mark 14", "Pulse", "High output weapon variant 14.", 50.0, 6.0, 10.0, 9.0, 740.0, 3, 0.4, "ENERGY", 0.19, 2.9000000000000004, 5, (238, 178, 146), 7.800000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_015"] = WeaponSpec("WEAPON_MODEL_015", "Ordnance Mark 15", "Pulse", "High output weapon variant 15.", 52.5, 10.0, 10.5, 9.5, 750.0, 4, 0.0, "ENERGY", 0.2, 3.0, 1, (255, 209, 193), 8.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_016"] = WeaponSpec("WEAPON_MODEL_016", "Ordnance Mark 16", "Pulse", "High output weapon variant 16.", 55.0, 9.0, 11.0, 10.0, 760.0, 1, 0.1, "ENERGY", 0.21000000000000002, 3.1, 2, (16, 240, 240), 8.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_017"] = WeaponSpec("WEAPON_MODEL_017", "Ordnance Mark 17", "Pulse", "High output weapon variant 17.", 57.5, 8.0, 11.5, 10.5, 770.0, 2, 0.2, "ENERGY", 0.22000000000000003, 3.2, 3, (33, 15, 31), 8.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_018"] = WeaponSpec("WEAPON_MODEL_018", "Ordnance Mark 18", "Pulse", "High output weapon variant 18.", 60.0, 7.0, 12.0, 11.0, 780.0, 3, 0.30000000000000004, "ENERGY", 0.22999999999999998, 3.3, 4, (50, 46, 78), 8.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_019"] = WeaponSpec("WEAPON_MODEL_019", "Ordnance Mark 19", "Pulse", "High output weapon variant 19.", 62.5, 6.0, 12.5, 11.5, 790.0, 4, 0.4, "ENERGY", 0.24, 3.4000000000000004, 5, (67, 77, 125), 8.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_020"] = WeaponSpec("WEAPON_MODEL_020", "Ordnance Mark 20", "Pulse", "High output weapon variant 20.", 65.0, 10.0, 13.0, 12.0, 800.0, 1, 0.0, "ENERGY", 0.25, 3.5, 1, (84, 108, 172), 9.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_021"] = WeaponSpec("WEAPON_MODEL_021", "Ordnance Mark 21", "Pulse", "High output weapon variant 21.", 67.5, 9.0, 13.5, 12.5, 810.0, 2, 0.1, "ENERGY", 0.26, 3.6, 2, (101, 139, 219), 9.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_022"] = WeaponSpec("WEAPON_MODEL_022", "Ordnance Mark 22", "Pulse", "High output weapon variant 22.", 70.0, 8.0, 14.0, 13.0, 820.0, 3, 0.2, "ENERGY", 0.27, 3.7, 3, (118, 170, 10), 9.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_023"] = WeaponSpec("WEAPON_MODEL_023", "Ordnance Mark 23", "Pulse", "High output weapon variant 23.", 72.5, 7.0, 14.5, 13.5, 830.0, 4, 0.30000000000000004, "ENERGY", 0.28, 3.8000000000000003, 4, (135, 201, 57), 9.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_024"] = WeaponSpec("WEAPON_MODEL_024", "Ordnance Mark 24", "Pulse", "High output weapon variant 24.", 75.0, 6.0, 15.0, 14.0, 840.0, 1, 0.4, "ENERGY", 0.29, 3.9000000000000004, 5, (152, 232, 104), 9.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_025"] = WeaponSpec("WEAPON_MODEL_025", "Ordnance Mark 25", "Pulse", "High output weapon variant 25.", 77.5, 10.0, 15.5, 14.5, 850.0, 2, 0.0, "ENERGY", 0.3, 4.0, 1, (169, 7, 151), 10.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_026"] = WeaponSpec("WEAPON_MODEL_026", "Ordnance Mark 26", "Pulse", "High output weapon variant 26.", 80.0, 9.0, 16.0, 15.0, 860.0, 3, 0.1, "ENERGY", 0.31, 4.1, 2, (186, 38, 198), 10.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_027"] = WeaponSpec("WEAPON_MODEL_027", "Ordnance Mark 27", "Pulse", "High output weapon variant 27.", 82.5, 8.0, 16.5, 15.5, 870.0, 4, 0.2, "ENERGY", 0.32, 4.2, 3, (203, 69, 245), 10.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_028"] = WeaponSpec("WEAPON_MODEL_028", "Ordnance Mark 28", "Pulse", "High output weapon variant 28.", 85.0, 7.0, 17.0, 16.0, 880.0, 1, 0.30000000000000004, "ENERGY", 0.33, 4.300000000000001, 4, (220, 100, 36), 10.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_029"] = WeaponSpec("WEAPON_MODEL_029", "Ordnance Mark 29", "Pulse", "High output weapon variant 29.", 87.5, 6.0, 17.5, 16.5, 890.0, 2, 0.4, "ENERGY", 0.33999999999999997, 4.4, 5, (237, 131, 83), 10.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_030"] = WeaponSpec("WEAPON_MODEL_030", "Ordnance Mark 30", "Pulse", "High output weapon variant 30.", 90.0, 10.0, 18.0, 17.0, 900.0, 3, 0.0, "ENERGY", 0.35, 4.5, 1, (254, 162, 130), 11.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_031"] = WeaponSpec("WEAPON_MODEL_031", "Ordnance Mark 31", "Pulse", "High output weapon variant 31.", 92.5, 9.0, 18.5, 17.5, 910.0, 4, 0.1, "ENERGY", 0.36, 4.6, 2, (15, 193, 177), 11.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_032"] = WeaponSpec("WEAPON_MODEL_032", "Ordnance Mark 32", "Pulse", "High output weapon variant 32.", 95.0, 8.0, 19.0, 18.0, 920.0, 1, 0.2, "ENERGY", 0.37, 4.7, 3, (32, 224, 224), 11.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_033"] = WeaponSpec("WEAPON_MODEL_033", "Ordnance Mark 33", "Pulse", "High output weapon variant 33.", 97.5, 7.0, 19.5, 18.5, 930.0, 2, 0.30000000000000004, "ENERGY", 0.38, 4.800000000000001, 4, (49, 255, 15), 11.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_034"] = WeaponSpec("WEAPON_MODEL_034", "Ordnance Mark 34", "Pulse", "High output weapon variant 34.", 100.0, 6.0, 20.0, 19.0, 940.0, 3, 0.4, "ENERGY", 0.39, 4.9, 5, (66, 30, 62), 11.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_035"] = WeaponSpec("WEAPON_MODEL_035", "Ordnance Mark 35", "Pulse", "High output weapon variant 35.", 102.5, 10.0, 20.5, 19.5, 950.0, 4, 0.0, "ENERGY", 0.4, 5.0, 1, (83, 61, 109), 12.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_036"] = WeaponSpec("WEAPON_MODEL_036", "Ordnance Mark 36", "Pulse", "High output weapon variant 36.", 105.0, 9.0, 21.0, 20.0, 960.0, 1, 0.1, "ENERGY", 0.41, 5.1, 2, (100, 92, 156), 12.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_037"] = WeaponSpec("WEAPON_MODEL_037", "Ordnance Mark 37", "Pulse", "High output weapon variant 37.", 107.5, 8.0, 21.5, 20.5, 970.0, 2, 0.2, "ENERGY", 0.42, 5.2, 3, (117, 123, 203), 12.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_038"] = WeaponSpec("WEAPON_MODEL_038", "Ordnance Mark 38", "Pulse", "High output weapon variant 38.", 110.0, 7.0, 22.0, 21.0, 980.0, 3, 0.30000000000000004, "ENERGY", 0.43, 5.300000000000001, 4, (134, 154, 250), 12.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_039"] = WeaponSpec("WEAPON_MODEL_039", "Ordnance Mark 39", "Pulse", "High output weapon variant 39.", 112.5, 6.0, 22.5, 21.5, 990.0, 4, 0.4, "ENERGY", 0.44, 5.4, 5, (151, 185, 41), 12.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_040"] = WeaponSpec("WEAPON_MODEL_040", "Ordnance Mark 40", "Pulse", "High output weapon variant 40.", 115.0, 10.0, 23.0, 22.0, 1000.0, 1, 0.0, "ENERGY", 0.45, 5.5, 1, (168, 216, 88), 13.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_041"] = WeaponSpec("WEAPON_MODEL_041", "Ordnance Mark 41", "Pulse", "High output weapon variant 41.", 117.5, 9.0, 23.5, 22.5, 1010.0, 2, 0.1, "ENERGY", 0.46, 5.6000000000000005, 2, (185, 247, 135), 13.200000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_042"] = WeaponSpec("WEAPON_MODEL_042", "Ordnance Mark 42", "Pulse", "High output weapon variant 42.", 120.0, 8.0, 24.0, 23.0, 1020.0, 3, 0.2, "ENERGY", 0.47, 5.7, 3, (202, 22, 182), 13.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_043"] = WeaponSpec("WEAPON_MODEL_043", "Ordnance Mark 43", "Pulse", "High output weapon variant 43.", 122.5, 7.0, 24.5, 23.5, 1030.0, 4, 0.30000000000000004, "ENERGY", 0.48, 5.8, 4, (219, 53, 229), 13.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_044"] = WeaponSpec("WEAPON_MODEL_044", "Ordnance Mark 44", "Pulse", "High output weapon variant 44.", 125.0, 6.0, 25.0, 24.0, 1040.0, 1, 0.4, "ENERGY", 0.49, 5.9, 5, (236, 84, 20), 13.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_045"] = WeaponSpec("WEAPON_MODEL_045", "Ordnance Mark 45", "Pulse", "High output weapon variant 45.", 127.5, 10.0, 25.5, 24.5, 1050.0, 2, 0.0, "ENERGY", 0.5, 6.0, 1, (253, 115, 67), 14.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_046"] = WeaponSpec("WEAPON_MODEL_046", "Ordnance Mark 46", "Pulse", "High output weapon variant 46.", 130.0, 9.0, 26.0, 25.0, 1060.0, 3, 0.1, "ENERGY", 0.51, 6.1000000000000005, 2, (14, 146, 114), 14.200000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_047"] = WeaponSpec("WEAPON_MODEL_047", "Ordnance Mark 47", "Pulse", "High output weapon variant 47.", 132.5, 8.0, 26.5, 25.5, 1070.0, 4, 0.2, "ENERGY", 0.52, 6.2, 3, (31, 177, 161), 14.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_048"] = WeaponSpec("WEAPON_MODEL_048", "Ordnance Mark 48", "Pulse", "High output weapon variant 48.", 135.0, 7.0, 27.0, 26.0, 1080.0, 1, 0.30000000000000004, "ENERGY", 0.53, 6.300000000000001, 4, (48, 208, 208), 14.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_049"] = WeaponSpec("WEAPON_MODEL_049", "Ordnance Mark 49", "Pulse", "High output weapon variant 49.", 137.5, 6.0, 27.5, 26.5, 1090.0, 2, 0.4, "ENERGY", 0.54, 6.4, 5, (65, 239, 255), 14.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_050"] = WeaponSpec("WEAPON_MODEL_050", "Ordnance Mark 50", "Pulse", "High output weapon variant 50.", 140.0, 10.0, 28.0, 27.0, 1100.0, 3, 0.0, "ENERGY", 0.55, 6.5, 1, (82, 14, 46), 15.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_051"] = WeaponSpec("WEAPON_MODEL_051", "Ordnance Mark 51", "Pulse", "High output weapon variant 51.", 142.5, 9.0, 28.5, 27.5, 1110.0, 4, 0.1, "ENERGY", 0.56, 6.6000000000000005, 2, (99, 45, 93), 15.200000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_052"] = WeaponSpec("WEAPON_MODEL_052", "Ordnance Mark 52", "Pulse", "High output weapon variant 52.", 145.0, 8.0, 29.0, 28.0, 1120.0, 1, 0.2, "ENERGY", 0.5700000000000001, 6.7, 3, (116, 76, 140), 15.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_053"] = WeaponSpec("WEAPON_MODEL_053", "Ordnance Mark 53", "Pulse", "High output weapon variant 53.", 147.5, 7.0, 29.5, 28.5, 1130.0, 2, 0.30000000000000004, "ENERGY", 0.5800000000000001, 6.800000000000001, 4, (133, 107, 187), 15.600000000000001, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_054"] = WeaponSpec("WEAPON_MODEL_054", "Ordnance Mark 54", "Pulse", "High output weapon variant 54.", 150.0, 6.0, 30.0, 29.0, 1140.0, 3, 0.4, "ENERGY", 0.5900000000000001, 6.9, 5, (150, 138, 234), 15.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_055"] = WeaponSpec("WEAPON_MODEL_055", "Ordnance Mark 55", "Pulse", "High output weapon variant 55.", 152.5, 10.0, 30.5, 29.5, 1150.0, 4, 0.0, "ENERGY", 0.6000000000000001, 7.0, 1, (167, 169, 25), 16.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_056"] = WeaponSpec("WEAPON_MODEL_056", "Ordnance Mark 56", "Pulse", "High output weapon variant 56.", 155.0, 9.0, 31.0, 30.0, 1160.0, 1, 0.1, "ENERGY", 0.6100000000000001, 7.1000000000000005, 2, (184, 200, 72), 16.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_057"] = WeaponSpec("WEAPON_MODEL_057", "Ordnance Mark 57", "Pulse", "High output weapon variant 57.", 157.5, 8.0, 31.5, 30.5, 1170.0, 2, 0.2, "ENERGY", 0.6200000000000001, 7.2, 3, (201, 231, 119), 16.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_058"] = WeaponSpec("WEAPON_MODEL_058", "Ordnance Mark 58", "Pulse", "High output weapon variant 58.", 160.0, 7.0, 32.0, 31.0, 1180.0, 3, 0.30000000000000004, "ENERGY", 0.63, 7.300000000000001, 4, (218, 6, 166), 16.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_059"] = WeaponSpec("WEAPON_MODEL_059", "Ordnance Mark 59", "Pulse", "High output weapon variant 59.", 162.5, 6.0, 32.5, 31.5, 1190.0, 4, 0.4, "ENERGY", 0.64, 7.4, 5, (235, 37, 213), 16.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_060"] = WeaponSpec("WEAPON_MODEL_060", "Ordnance Mark 60", "Pulse", "High output weapon variant 60.", 165.0, 10.0, 33.0, 32.0, 1200.0, 1, 0.0, "ENERGY", 0.65, 7.5, 1, (252, 68, 4), 17.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_061"] = WeaponSpec("WEAPON_MODEL_061", "Ordnance Mark 61", "Pulse", "High output weapon variant 61.", 167.5, 9.0, 33.5, 32.5, 1210.0, 2, 0.1, "ENERGY", 0.66, 7.6000000000000005, 2, (13, 99, 51), 17.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_062"] = WeaponSpec("WEAPON_MODEL_062", "Ordnance Mark 62", "Pulse", "High output weapon variant 62.", 170.0, 8.0, 34.0, 33.0, 1220.0, 3, 0.2, "ENERGY", 0.67, 7.7, 3, (30, 130, 98), 17.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_063"] = WeaponSpec("WEAPON_MODEL_063", "Ordnance Mark 63", "Pulse", "High output weapon variant 63.", 172.5, 7.0, 34.5, 33.5, 1230.0, 4, 0.30000000000000004, "ENERGY", 0.68, 7.800000000000001, 4, (47, 161, 145), 17.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_064"] = WeaponSpec("WEAPON_MODEL_064", "Ordnance Mark 64", "Pulse", "High output weapon variant 64.", 175.0, 6.0, 35.0, 34.0, 1240.0, 1, 0.4, "ENERGY", 0.6900000000000001, 7.9, 5, (64, 192, 192), 17.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_065"] = WeaponSpec("WEAPON_MODEL_065", "Ordnance Mark 65", "Pulse", "High output weapon variant 65.", 177.5, 10.0, 35.5, 34.5, 1250.0, 2, 0.0, "ENERGY", 0.7000000000000001, 8.0, 1, (81, 223, 239), 18.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_066"] = WeaponSpec("WEAPON_MODEL_066", "Ordnance Mark 66", "Pulse", "High output weapon variant 66.", 180.0, 9.0, 36.0, 35.0, 1260.0, 3, 0.1, "ENERGY", 0.7100000000000001, 8.100000000000001, 2, (98, 254, 30), 18.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_067"] = WeaponSpec("WEAPON_MODEL_067", "Ordnance Mark 67", "Pulse", "High output weapon variant 67.", 182.5, 8.0, 36.5, 35.5, 1270.0, 4, 0.2, "ENERGY", 0.7200000000000001, 8.2, 3, (115, 29, 77), 18.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_068"] = WeaponSpec("WEAPON_MODEL_068", "Ordnance Mark 68", "Pulse", "High output weapon variant 68.", 185.0, 7.0, 37.0, 36.0, 1280.0, 1, 0.30000000000000004, "ENERGY", 0.7300000000000001, 8.3, 4, (132, 60, 124), 18.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_069"] = WeaponSpec("WEAPON_MODEL_069", "Ordnance Mark 69", "Pulse", "High output weapon variant 69.", 187.5, 6.0, 37.5, 36.5, 1290.0, 2, 0.4, "ENERGY", 0.7400000000000001, 8.4, 5, (149, 91, 171), 18.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_070"] = WeaponSpec("WEAPON_MODEL_070", "Ordnance Mark 70", "Pulse", "High output weapon variant 70.", 190.0, 10.0, 38.0, 37.0, 1300.0, 3, 0.0, "ENERGY", 0.7500000000000001, 8.5, 1, (166, 122, 218), 19.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_071"] = WeaponSpec("WEAPON_MODEL_071", "Ordnance Mark 71", "Pulse", "High output weapon variant 71.", 192.5, 9.0, 38.5, 37.5, 1310.0, 4, 0.1, "ENERGY", 0.76, 8.600000000000001, 2, (183, 153, 9), 19.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_072"] = WeaponSpec("WEAPON_MODEL_072", "Ordnance Mark 72", "Pulse", "High output weapon variant 72.", 195.0, 8.0, 39.0, 38.0, 1320.0, 1, 0.2, "ENERGY", 0.77, 8.7, 3, (200, 184, 56), 19.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_073"] = WeaponSpec("WEAPON_MODEL_073", "Ordnance Mark 73", "Pulse", "High output weapon variant 73.", 197.5, 7.0, 39.5, 38.5, 1330.0, 2, 0.30000000000000004, "ENERGY", 0.78, 8.8, 4, (217, 215, 103), 19.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_074"] = WeaponSpec("WEAPON_MODEL_074", "Ordnance Mark 74", "Pulse", "High output weapon variant 74.", 200.0, 6.0, 40.0, 39.0, 1340.0, 3, 0.4, "ENERGY", 0.79, 8.9, 5, (234, 246, 150), 19.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_075"] = WeaponSpec("WEAPON_MODEL_075", "Ordnance Mark 75", "Pulse", "High output weapon variant 75.", 202.5, 10.0, 40.5, 39.5, 1350.0, 4, 0.0, "ENERGY", 0.8, 9.0, 1, (251, 21, 197), 20.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_076"] = WeaponSpec("WEAPON_MODEL_076", "Ordnance Mark 76", "Pulse", "High output weapon variant 76.", 205.0, 9.0, 41.0, 40.0, 1360.0, 1, 0.1, "ENERGY", 0.81, 9.100000000000001, 2, (12, 52, 244), 20.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_077"] = WeaponSpec("WEAPON_MODEL_077", "Ordnance Mark 77", "Pulse", "High output weapon variant 77.", 207.5, 8.0, 41.5, 40.5, 1370.0, 2, 0.2, "ENERGY", 0.8200000000000001, 9.2, 3, (29, 83, 35), 20.4, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_078"] = WeaponSpec("WEAPON_MODEL_078", "Ordnance Mark 78", "Pulse", "High output weapon variant 78.", 210.0, 7.0, 42.0, 41.0, 1380.0, 3, 0.30000000000000004, "ENERGY", 0.8300000000000001, 9.3, 4, (46, 114, 82), 20.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_079"] = WeaponSpec("WEAPON_MODEL_079", "Ordnance Mark 79", "Pulse", "High output weapon variant 79.", 212.5, 6.0, 42.5, 41.5, 1390.0, 4, 0.4, "ENERGY", 0.8400000000000001, 9.4, 5, (63, 145, 129), 20.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_080"] = WeaponSpec("WEAPON_MODEL_080", "Ordnance Mark 80", "Pulse", "High output weapon variant 80.", 215.0, 10.0, 43.0, 42.0, 1400.0, 1, 0.0, "ENERGY", 0.8500000000000001, 9.5, 1, (80, 176, 176), 21.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_081"] = WeaponSpec("WEAPON_MODEL_081", "Ordnance Mark 81", "Pulse", "High output weapon variant 81.", 217.5, 9.0, 43.5, 42.5, 1410.0, 2, 0.1, "ENERGY", 0.8600000000000001, 9.6, 2, (97, 207, 223), 21.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_082"] = WeaponSpec("WEAPON_MODEL_082", "Ordnance Mark 82", "Pulse", "High output weapon variant 82.", 220.0, 8.0, 44.0, 43.0, 1420.0, 3, 0.2, "ENERGY", 0.8700000000000001, 9.700000000000001, 3, (114, 238, 14), 21.400000000000002, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_083"] = WeaponSpec("WEAPON_MODEL_083", "Ordnance Mark 83", "Pulse", "High output weapon variant 83.", 222.5, 7.0, 44.5, 43.5, 1430.0, 4, 0.30000000000000004, "ENERGY", 0.8800000000000001, 9.8, 4, (131, 13, 61), 21.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_084"] = WeaponSpec("WEAPON_MODEL_084", "Ordnance Mark 84", "Pulse", "High output weapon variant 84.", 225.0, 6.0, 45.0, 44.0, 1440.0, 1, 0.4, "ENERGY", 0.89, 9.9, 5, (148, 44, 108), 21.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_085"] = WeaponSpec("WEAPON_MODEL_085", "Ordnance Mark 85", "Pulse", "High output weapon variant 85.", 227.5, 10.0, 45.5, 44.5, 1450.0, 2, 0.0, "ENERGY", 0.9, 10.0, 1, (165, 75, 155), 22.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_086"] = WeaponSpec("WEAPON_MODEL_086", "Ordnance Mark 86", "Pulse", "High output weapon variant 86.", 230.0, 9.0, 46.0, 45.0, 1460.0, 3, 0.1, "ENERGY", 0.91, 10.1, 2, (182, 106, 202), 22.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_087"] = WeaponSpec("WEAPON_MODEL_087", "Ordnance Mark 87", "Pulse", "High output weapon variant 87.", 232.5, 8.0, 46.5, 45.5, 1470.0, 4, 0.2, "ENERGY", 0.92, 10.200000000000001, 3, (199, 137, 249), 22.400000000000002, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_088"] = WeaponSpec("WEAPON_MODEL_088", "Ordnance Mark 88", "Pulse", "High output weapon variant 88.", 235.0, 7.0, 47.0, 46.0, 1480.0, 1, 0.30000000000000004, "ENERGY", 0.93, 10.3, 4, (216, 168, 40), 22.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_089"] = WeaponSpec("WEAPON_MODEL_089", "Ordnance Mark 89", "Pulse", "High output weapon variant 89.", 237.5, 6.0, 47.5, 46.5, 1490.0, 2, 0.4, "ENERGY", 0.9400000000000001, 10.4, 5, (233, 199, 87), 22.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_090"] = WeaponSpec("WEAPON_MODEL_090", "Ordnance Mark 90", "Pulse", "High output weapon variant 90.", 240.0, 10.0, 48.0, 47.0, 1500.0, 3, 0.0, "ENERGY", 0.9500000000000001, 10.5, 1, (250, 230, 134), 23.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_091"] = WeaponSpec("WEAPON_MODEL_091", "Ordnance Mark 91", "Pulse", "High output weapon variant 91.", 242.5, 9.0, 48.5, 47.5, 1510.0, 4, 0.1, "ENERGY", 0.9600000000000001, 10.6, 2, (11, 5, 181), 23.2, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_092"] = WeaponSpec("WEAPON_MODEL_092", "Ordnance Mark 92", "Pulse", "High output weapon variant 92.", 245.0, 8.0, 49.0, 48.0, 1520.0, 1, 0.2, "ENERGY", 0.9700000000000001, 10.700000000000001, 3, (28, 36, 228), 23.400000000000002, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_093"] = WeaponSpec("WEAPON_MODEL_093", "Ordnance Mark 93", "Pulse", "High output weapon variant 93.", 247.5, 7.0, 49.5, 48.5, 1530.0, 2, 0.30000000000000004, "ENERGY", 0.9800000000000001, 10.8, 4, (45, 67, 19), 23.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_094"] = WeaponSpec("WEAPON_MODEL_094", "Ordnance Mark 94", "Pulse", "High output weapon variant 94.", 250.0, 6.0, 50.0, 49.0, 1540.0, 3, 0.4, "ENERGY", 0.9900000000000001, 10.9, 5, (62, 98, 66), 23.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_095"] = WeaponSpec("WEAPON_MODEL_095", "Ordnance Mark 95", "Pulse", "High output weapon variant 95.", 252.5, 10.0, 50.5, 49.5, 1550.0, 4, 0.0, "ENERGY", 1.0, 11.0, 1, (79, 129, 113), 24.0, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_096"] = WeaponSpec("WEAPON_MODEL_096", "Ordnance Mark 96", "Pulse", "High output weapon variant 96.", 255.0, 9.0, 51.0, 50.0, 1560.0, 1, 0.1, "ENERGY", 1.01, 11.100000000000001, 2, (96, 160, 160), 24.200000000000003, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_097"] = WeaponSpec("WEAPON_MODEL_097", "Ordnance Mark 97", "Pulse", "High output weapon variant 97.", 257.5, 8.0, 51.5, 50.5, 1570.0, 2, 0.2, "ENERGY", 1.02, 11.200000000000001, 3, (113, 191, 207), 24.400000000000002, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_098"] = WeaponSpec("WEAPON_MODEL_098", "Ordnance Mark 98", "Pulse", "High output weapon variant 98.", 260.0, 7.0, 52.0, 51.0, 1580.0, 3, 0.30000000000000004, "ENERGY", 1.03, 11.3, 4, (130, 222, 254), 24.6, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_099"] = WeaponSpec("WEAPON_MODEL_099", "Ordnance Mark 99", "Pulse", "High output weapon variant 99.", 262.5, 6.0, 52.5, 51.5, 1590.0, 4, 0.4, "ENERGY", 1.04, 11.4, 5, (147, 253, 45), 24.8, 0.0, 1, 0.0)

WeaponCatalog.WEAPONS["WEAPON_MODEL_100"] = WeaponSpec("WEAPON_MODEL_100", "Ordnance Mark 100", "Pulse", "High output weapon variant 100.", 265.0, 10.0, 53.0, 52.0, 1600.0, 1, 0.0, "ENERGY", 1.05, 11.5, 1, (164, 28, 92), 25.0, 0.0, 1, 0.0)

