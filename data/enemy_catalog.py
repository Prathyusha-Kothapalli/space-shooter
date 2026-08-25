"""Enemy Catalog specifying 100 alien hostiles."""
from typing import Dict, Any, List, Tuple
class EnemySpec:
    def __init__(self, enemy_id: str, name: str, role: str, max_health: float, max_speed: float, armor: float, score_value: int, xp_value: int, ai_profile: str, weapon_type: str, fire_cooldown: float, collision_radius: float, primary_color: Tuple[int, int, int], drop_table: List[Dict[str, float]], shield_capacity: float, evasion_chance: float, threat_rating: int):
        self.enemy_id = enemy_id; self.name = name; self.role = role; self.max_health = max_health; self.max_speed = max_speed; self.armor = armor; self.score_value = score_value; self.xp_value = xp_value; self.ai_profile = ai_profile; self.weapon_type = weapon_type; self.fire_cooldown = fire_cooldown; self.collision_radius = collision_radius; self.primary_color = primary_color; self.drop_table = drop_table; self.shield_capacity = shield_capacity; self.evasion_chance = evasion_chance; self.threat_rating = threat_rating
class EnemyCatalog:
    ENEMIES: Dict[str, EnemySpec] = {}
EnemyCatalog.ENEMIES["ENEMY_UNIT_001"] = EnemySpec("ENEMY_UNIT_001", "Hostile Unit 001", "Scout", 34.0, 279.0, 1.0, 120, 18, "PATROL", "LASER", 1.99, 14.2, (29, 53, 71), [{"item": "HEALTH", "chance": 0.2}], 22.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_002"] = EnemySpec("ENEMY_UNIT_002", "Hostile Unit 002", "Scout", 38.0, 278.0, 2.0, 140, 21, "PATROL", "LASER", 1.98, 14.4, (58, 106, 142), [{"item": "HEALTH", "chance": 0.2}], 24.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_003"] = EnemySpec("ENEMY_UNIT_003", "Hostile Unit 003", "Scout", 42.0, 277.0, 3.0, 160, 24, "PATROL", "LASER", 1.97, 14.6, (87, 159, 213), [{"item": "HEALTH", "chance": 0.2}], 26.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_004"] = EnemySpec("ENEMY_UNIT_004", "Hostile Unit 004", "Scout", 46.0, 276.0, 4.0, 180, 27, "PATROL", "LASER", 1.96, 14.8, (116, 212, 28), [{"item": "HEALTH", "chance": 0.2}], 28.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_005"] = EnemySpec("ENEMY_UNIT_005", "Hostile Unit 005", "Scout", 50.0, 275.0, 5.0, 200, 30, "PATROL", "LASER", 1.95, 15.0, (145, 9, 99), [{"item": "HEALTH", "chance": 0.2}], 30.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_006"] = EnemySpec("ENEMY_UNIT_006", "Hostile Unit 006", "Scout", 54.0, 274.0, 6.0, 220, 33, "PATROL", "LASER", 1.94, 15.2, (174, 62, 170), [{"item": "HEALTH", "chance": 0.2}], 32.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_007"] = EnemySpec("ENEMY_UNIT_007", "Hostile Unit 007", "Scout", 58.0, 273.0, 7.0, 240, 36, "PATROL", "LASER", 1.93, 15.4, (203, 115, 241), [{"item": "HEALTH", "chance": 0.2}], 34.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_008"] = EnemySpec("ENEMY_UNIT_008", "Hostile Unit 008", "Scout", 62.0, 272.0, 8.0, 260, 39, "PATROL", "LASER", 1.92, 15.6, (232, 168, 56), [{"item": "HEALTH", "chance": 0.2}], 36.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_009"] = EnemySpec("ENEMY_UNIT_009", "Hostile Unit 009", "Scout", 66.0, 271.0, 9.0, 280, 42, "PATROL", "LASER", 1.91, 15.8, (5, 221, 127), [{"item": "HEALTH", "chance": 0.2}], 38.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_010"] = EnemySpec("ENEMY_UNIT_010", "Hostile Unit 010", "Scout", 70.0, 270.0, 0.0, 300, 45, "PATROL", "LASER", 1.9, 16.0, (34, 18, 198), [{"item": "HEALTH", "chance": 0.2}], 40.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_011"] = EnemySpec("ENEMY_UNIT_011", "Hostile Unit 011", "Scout", 74.0, 269.0, 1.0, 320, 48, "PATROL", "LASER", 1.89, 16.2, (63, 71, 13), [{"item": "HEALTH", "chance": 0.2}], 42.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_012"] = EnemySpec("ENEMY_UNIT_012", "Hostile Unit 012", "Scout", 78.0, 268.0, 2.0, 340, 51, "PATROL", "LASER", 1.88, 16.4, (92, 124, 84), [{"item": "HEALTH", "chance": 0.2}], 44.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_013"] = EnemySpec("ENEMY_UNIT_013", "Hostile Unit 013", "Scout", 82.0, 267.0, 3.0, 360, 54, "PATROL", "LASER", 1.87, 16.6, (121, 177, 155), [{"item": "HEALTH", "chance": 0.2}], 46.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_014"] = EnemySpec("ENEMY_UNIT_014", "Hostile Unit 014", "Scout", 86.0, 266.0, 4.0, 380, 57, "PATROL", "LASER", 1.8599999999999999, 16.8, (150, 230, 226), [{"item": "HEALTH", "chance": 0.2}], 48.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_015"] = EnemySpec("ENEMY_UNIT_015", "Hostile Unit 015", "Scout", 90.0, 265.0, 5.0, 400, 60, "PATROL", "LASER", 1.85, 17.0, (179, 27, 41), [{"item": "HEALTH", "chance": 0.2}], 50.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_016"] = EnemySpec("ENEMY_UNIT_016", "Hostile Unit 016", "Scout", 94.0, 264.0, 6.0, 420, 63, "PATROL", "LASER", 1.84, 17.2, (208, 80, 112), [{"item": "HEALTH", "chance": 0.2}], 52.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_017"] = EnemySpec("ENEMY_UNIT_017", "Hostile Unit 017", "Scout", 98.0, 263.0, 7.0, 440, 66, "PATROL", "LASER", 1.83, 17.4, (237, 133, 183), [{"item": "HEALTH", "chance": 0.2}], 54.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_018"] = EnemySpec("ENEMY_UNIT_018", "Hostile Unit 018", "Scout", 102.0, 262.0, 8.0, 460, 69, "PATROL", "LASER", 1.82, 17.6, (10, 186, 254), [{"item": "HEALTH", "chance": 0.2}], 56.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_019"] = EnemySpec("ENEMY_UNIT_019", "Hostile Unit 019", "Scout", 106.0, 261.0, 9.0, 480, 72, "PATROL", "LASER", 1.81, 17.8, (39, 239, 69), [{"item": "HEALTH", "chance": 0.2}], 58.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_020"] = EnemySpec("ENEMY_UNIT_020", "Hostile Unit 020", "Scout", 110.0, 260.0, 0.0, 500, 75, "PATROL", "LASER", 1.8, 18.0, (68, 36, 140), [{"item": "HEALTH", "chance": 0.2}], 60.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_021"] = EnemySpec("ENEMY_UNIT_021", "Hostile Unit 021", "Scout", 114.0, 259.0, 1.0, 520, 78, "PATROL", "LASER", 1.79, 18.2, (97, 89, 211), [{"item": "HEALTH", "chance": 0.2}], 62.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_022"] = EnemySpec("ENEMY_UNIT_022", "Hostile Unit 022", "Scout", 118.0, 258.0, 2.0, 540, 81, "PATROL", "LASER", 1.78, 18.4, (126, 142, 26), [{"item": "HEALTH", "chance": 0.2}], 64.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_023"] = EnemySpec("ENEMY_UNIT_023", "Hostile Unit 023", "Scout", 122.0, 257.0, 3.0, 560, 84, "PATROL", "LASER", 1.77, 18.6, (155, 195, 97), [{"item": "HEALTH", "chance": 0.2}], 66.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_024"] = EnemySpec("ENEMY_UNIT_024", "Hostile Unit 024", "Scout", 126.0, 256.0, 4.0, 580, 87, "PATROL", "LASER", 1.76, 18.8, (184, 248, 168), [{"item": "HEALTH", "chance": 0.2}], 68.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_025"] = EnemySpec("ENEMY_UNIT_025", "Hostile Unit 025", "Scout", 130.0, 255.0, 5.0, 600, 90, "PATROL", "LASER", 1.75, 19.0, (213, 45, 239), [{"item": "HEALTH", "chance": 0.2}], 70.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_026"] = EnemySpec("ENEMY_UNIT_026", "Hostile Unit 026", "Scout", 134.0, 254.0, 6.0, 620, 93, "PATROL", "LASER", 1.74, 19.2, (242, 98, 54), [{"item": "HEALTH", "chance": 0.2}], 72.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_027"] = EnemySpec("ENEMY_UNIT_027", "Hostile Unit 027", "Scout", 138.0, 253.0, 7.0, 640, 96, "PATROL", "LASER", 1.73, 19.4, (15, 151, 125), [{"item": "HEALTH", "chance": 0.2}], 74.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_028"] = EnemySpec("ENEMY_UNIT_028", "Hostile Unit 028", "Scout", 142.0, 252.0, 8.0, 660, 99, "PATROL", "LASER", 1.72, 19.6, (44, 204, 196), [{"item": "HEALTH", "chance": 0.2}], 76.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_029"] = EnemySpec("ENEMY_UNIT_029", "Hostile Unit 029", "Scout", 146.0, 251.0, 9.0, 680, 102, "PATROL", "LASER", 1.71, 19.8, (73, 1, 11), [{"item": "HEALTH", "chance": 0.2}], 78.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_030"] = EnemySpec("ENEMY_UNIT_030", "Hostile Unit 030", "Scout", 150.0, 250.0, 0.0, 700, 105, "PATROL", "LASER", 1.7, 20.0, (102, 54, 82), [{"item": "HEALTH", "chance": 0.2}], 80.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_031"] = EnemySpec("ENEMY_UNIT_031", "Hostile Unit 031", "Scout", 154.0, 249.0, 1.0, 720, 108, "PATROL", "LASER", 1.69, 20.2, (131, 107, 153), [{"item": "HEALTH", "chance": 0.2}], 82.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_032"] = EnemySpec("ENEMY_UNIT_032", "Hostile Unit 032", "Scout", 158.0, 248.0, 2.0, 740, 111, "PATROL", "LASER", 1.68, 20.4, (160, 160, 224), [{"item": "HEALTH", "chance": 0.2}], 84.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_033"] = EnemySpec("ENEMY_UNIT_033", "Hostile Unit 033", "Scout", 162.0, 247.0, 3.0, 760, 114, "PATROL", "LASER", 1.67, 20.6, (189, 213, 39), [{"item": "HEALTH", "chance": 0.2}], 86.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_034"] = EnemySpec("ENEMY_UNIT_034", "Hostile Unit 034", "Scout", 166.0, 246.0, 4.0, 780, 117, "PATROL", "LASER", 1.66, 20.8, (218, 10, 110), [{"item": "HEALTH", "chance": 0.2}], 88.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_035"] = EnemySpec("ENEMY_UNIT_035", "Hostile Unit 035", "Scout", 170.0, 245.0, 5.0, 800, 120, "PATROL", "LASER", 1.65, 21.0, (247, 63, 181), [{"item": "HEALTH", "chance": 0.2}], 90.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_036"] = EnemySpec("ENEMY_UNIT_036", "Hostile Unit 036", "Scout", 174.0, 244.0, 6.0, 820, 123, "PATROL", "LASER", 1.6400000000000001, 21.2, (20, 116, 252), [{"item": "HEALTH", "chance": 0.2}], 92.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_037"] = EnemySpec("ENEMY_UNIT_037", "Hostile Unit 037", "Scout", 178.0, 243.0, 7.0, 840, 126, "PATROL", "LASER", 1.63, 21.4, (49, 169, 67), [{"item": "HEALTH", "chance": 0.2}], 94.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_038"] = EnemySpec("ENEMY_UNIT_038", "Hostile Unit 038", "Scout", 182.0, 242.0, 8.0, 860, 129, "PATROL", "LASER", 1.62, 21.6, (78, 222, 138), [{"item": "HEALTH", "chance": 0.2}], 96.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_039"] = EnemySpec("ENEMY_UNIT_039", "Hostile Unit 039", "Scout", 186.0, 241.0, 9.0, 880, 132, "PATROL", "LASER", 1.6099999999999999, 21.8, (107, 19, 209), [{"item": "HEALTH", "chance": 0.2}], 98.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_040"] = EnemySpec("ENEMY_UNIT_040", "Hostile Unit 040", "Scout", 190.0, 240.0, 0.0, 900, 135, "PATROL", "LASER", 1.6, 22.0, (136, 72, 24), [{"item": "HEALTH", "chance": 0.2}], 100.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_041"] = EnemySpec("ENEMY_UNIT_041", "Hostile Unit 041", "Scout", 194.0, 239.0, 1.0, 920, 138, "PATROL", "LASER", 1.5899999999999999, 22.200000000000003, (165, 125, 95), [{"item": "HEALTH", "chance": 0.2}], 102.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_042"] = EnemySpec("ENEMY_UNIT_042", "Hostile Unit 042", "Scout", 198.0, 238.0, 2.0, 940, 141, "PATROL", "LASER", 1.58, 22.4, (194, 178, 166), [{"item": "HEALTH", "chance": 0.2}], 104.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_043"] = EnemySpec("ENEMY_UNIT_043", "Hostile Unit 043", "Scout", 202.0, 237.0, 3.0, 960, 144, "PATROL", "LASER", 1.57, 22.6, (223, 231, 237), [{"item": "HEALTH", "chance": 0.2}], 106.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_044"] = EnemySpec("ENEMY_UNIT_044", "Hostile Unit 044", "Scout", 206.0, 236.0, 4.0, 980, 147, "PATROL", "LASER", 1.56, 22.8, (252, 28, 52), [{"item": "HEALTH", "chance": 0.2}], 108.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_045"] = EnemySpec("ENEMY_UNIT_045", "Hostile Unit 045", "Scout", 210.0, 235.0, 5.0, 1000, 150, "PATROL", "LASER", 1.55, 23.0, (25, 81, 123), [{"item": "HEALTH", "chance": 0.2}], 110.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_046"] = EnemySpec("ENEMY_UNIT_046", "Hostile Unit 046", "Scout", 214.0, 234.0, 6.0, 1020, 153, "PATROL", "LASER", 1.54, 23.200000000000003, (54, 134, 194), [{"item": "HEALTH", "chance": 0.2}], 112.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_047"] = EnemySpec("ENEMY_UNIT_047", "Hostile Unit 047", "Scout", 218.0, 233.0, 7.0, 1040, 156, "PATROL", "LASER", 1.53, 23.4, (83, 187, 9), [{"item": "HEALTH", "chance": 0.2}], 114.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_048"] = EnemySpec("ENEMY_UNIT_048", "Hostile Unit 048", "Scout", 222.0, 232.0, 8.0, 1060, 159, "PATROL", "LASER", 1.52, 23.6, (112, 240, 80), [{"item": "HEALTH", "chance": 0.2}], 116.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_049"] = EnemySpec("ENEMY_UNIT_049", "Hostile Unit 049", "Scout", 226.0, 231.0, 9.0, 1080, 162, "PATROL", "LASER", 1.51, 23.8, (141, 37, 151), [{"item": "HEALTH", "chance": 0.2}], 118.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_050"] = EnemySpec("ENEMY_UNIT_050", "Hostile Unit 050", "Scout", 230.0, 230.0, 0.0, 1100, 165, "PATROL", "LASER", 1.5, 24.0, (170, 90, 222), [{"item": "HEALTH", "chance": 0.2}], 120.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_051"] = EnemySpec("ENEMY_UNIT_051", "Hostile Unit 051", "Scout", 234.0, 229.0, 1.0, 1120, 168, "PATROL", "LASER", 1.49, 24.200000000000003, (199, 143, 37), [{"item": "HEALTH", "chance": 0.2}], 122.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_052"] = EnemySpec("ENEMY_UNIT_052", "Hostile Unit 052", "Scout", 238.0, 228.0, 2.0, 1140, 171, "PATROL", "LASER", 1.48, 24.4, (228, 196, 108), [{"item": "HEALTH", "chance": 0.2}], 124.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_053"] = EnemySpec("ENEMY_UNIT_053", "Hostile Unit 053", "Scout", 242.0, 227.0, 3.0, 1160, 174, "PATROL", "LASER", 1.47, 24.6, (1, 249, 179), [{"item": "HEALTH", "chance": 0.2}], 126.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_054"] = EnemySpec("ENEMY_UNIT_054", "Hostile Unit 054", "Scout", 246.0, 226.0, 4.0, 1180, 177, "PATROL", "LASER", 1.46, 24.8, (30, 46, 250), [{"item": "HEALTH", "chance": 0.2}], 128.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_055"] = EnemySpec("ENEMY_UNIT_055", "Hostile Unit 055", "Scout", 250.0, 225.0, 5.0, 1200, 180, "PATROL", "LASER", 1.45, 25.0, (59, 99, 65), [{"item": "HEALTH", "chance": 0.2}], 130.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_056"] = EnemySpec("ENEMY_UNIT_056", "Hostile Unit 056", "Scout", 254.0, 224.0, 6.0, 1220, 183, "PATROL", "LASER", 1.44, 25.200000000000003, (88, 152, 136), [{"item": "HEALTH", "chance": 0.2}], 132.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_057"] = EnemySpec("ENEMY_UNIT_057", "Hostile Unit 057", "Scout", 258.0, 223.0, 7.0, 1240, 186, "PATROL", "LASER", 1.43, 25.4, (117, 205, 207), [{"item": "HEALTH", "chance": 0.2}], 134.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_058"] = EnemySpec("ENEMY_UNIT_058", "Hostile Unit 058", "Scout", 262.0, 222.0, 8.0, 1260, 189, "PATROL", "LASER", 1.42, 25.6, (146, 2, 22), [{"item": "HEALTH", "chance": 0.2}], 136.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_059"] = EnemySpec("ENEMY_UNIT_059", "Hostile Unit 059", "Scout", 266.0, 221.0, 9.0, 1280, 192, "PATROL", "LASER", 1.4100000000000001, 25.8, (175, 55, 93), [{"item": "HEALTH", "chance": 0.2}], 138.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_060"] = EnemySpec("ENEMY_UNIT_060", "Hostile Unit 060", "Scout", 270.0, 220.0, 0.0, 1300, 195, "PATROL", "LASER", 1.4, 26.0, (204, 108, 164), [{"item": "HEALTH", "chance": 0.2}], 140.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_061"] = EnemySpec("ENEMY_UNIT_061", "Hostile Unit 061", "Scout", 274.0, 219.0, 1.0, 1320, 198, "PATROL", "LASER", 1.3900000000000001, 26.200000000000003, (233, 161, 235), [{"item": "HEALTH", "chance": 0.2}], 142.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_062"] = EnemySpec("ENEMY_UNIT_062", "Hostile Unit 062", "Scout", 278.0, 218.0, 2.0, 1340, 201, "PATROL", "LASER", 1.38, 26.4, (6, 214, 50), [{"item": "HEALTH", "chance": 0.2}], 144.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_063"] = EnemySpec("ENEMY_UNIT_063", "Hostile Unit 063", "Scout", 282.0, 217.0, 3.0, 1360, 204, "PATROL", "LASER", 1.37, 26.6, (35, 11, 121), [{"item": "HEALTH", "chance": 0.2}], 146.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_064"] = EnemySpec("ENEMY_UNIT_064", "Hostile Unit 064", "Scout", 286.0, 216.0, 4.0, 1380, 207, "PATROL", "LASER", 1.3599999999999999, 26.8, (64, 64, 192), [{"item": "HEALTH", "chance": 0.2}], 148.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_065"] = EnemySpec("ENEMY_UNIT_065", "Hostile Unit 065", "Scout", 290.0, 215.0, 5.0, 1400, 210, "PATROL", "LASER", 1.35, 27.0, (93, 117, 7), [{"item": "HEALTH", "chance": 0.2}], 150.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_066"] = EnemySpec("ENEMY_UNIT_066", "Hostile Unit 066", "Scout", 294.0, 214.0, 6.0, 1420, 213, "PATROL", "LASER", 1.3399999999999999, 27.200000000000003, (122, 170, 78), [{"item": "HEALTH", "chance": 0.2}], 152.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_067"] = EnemySpec("ENEMY_UNIT_067", "Hostile Unit 067", "Scout", 298.0, 213.0, 7.0, 1440, 216, "PATROL", "LASER", 1.33, 27.4, (151, 223, 149), [{"item": "HEALTH", "chance": 0.2}], 154.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_068"] = EnemySpec("ENEMY_UNIT_068", "Hostile Unit 068", "Scout", 302.0, 212.0, 8.0, 1460, 219, "PATROL", "LASER", 1.3199999999999998, 27.6, (180, 20, 220), [{"item": "HEALTH", "chance": 0.2}], 156.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_069"] = EnemySpec("ENEMY_UNIT_069", "Hostile Unit 069", "Scout", 306.0, 211.0, 9.0, 1480, 222, "PATROL", "LASER", 1.31, 27.8, (209, 73, 35), [{"item": "HEALTH", "chance": 0.2}], 158.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_070"] = EnemySpec("ENEMY_UNIT_070", "Hostile Unit 070", "Scout", 310.0, 210.0, 0.0, 1500, 225, "PATROL", "LASER", 1.2999999999999998, 28.0, (238, 126, 106), [{"item": "HEALTH", "chance": 0.2}], 160.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_071"] = EnemySpec("ENEMY_UNIT_071", "Hostile Unit 071", "Scout", 314.0, 209.0, 1.0, 1520, 228, "PATROL", "LASER", 1.29, 28.200000000000003, (11, 179, 177), [{"item": "HEALTH", "chance": 0.2}], 162.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_072"] = EnemySpec("ENEMY_UNIT_072", "Hostile Unit 072", "Scout", 318.0, 208.0, 2.0, 1540, 231, "PATROL", "LASER", 1.28, 28.4, (40, 232, 248), [{"item": "HEALTH", "chance": 0.2}], 164.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_073"] = EnemySpec("ENEMY_UNIT_073", "Hostile Unit 073", "Scout", 322.0, 207.0, 3.0, 1560, 234, "PATROL", "LASER", 1.27, 28.6, (69, 29, 63), [{"item": "HEALTH", "chance": 0.2}], 166.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_074"] = EnemySpec("ENEMY_UNIT_074", "Hostile Unit 074", "Scout", 326.0, 206.0, 4.0, 1580, 237, "PATROL", "LASER", 1.26, 28.8, (98, 82, 134), [{"item": "HEALTH", "chance": 0.2}], 168.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_075"] = EnemySpec("ENEMY_UNIT_075", "Hostile Unit 075", "Scout", 330.0, 205.0, 5.0, 1600, 240, "PATROL", "LASER", 1.25, 29.0, (127, 135, 205), [{"item": "HEALTH", "chance": 0.2}], 170.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_076"] = EnemySpec("ENEMY_UNIT_076", "Hostile Unit 076", "Scout", 334.0, 204.0, 6.0, 1620, 243, "PATROL", "LASER", 1.24, 29.200000000000003, (156, 188, 20), [{"item": "HEALTH", "chance": 0.2}], 172.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_077"] = EnemySpec("ENEMY_UNIT_077", "Hostile Unit 077", "Scout", 338.0, 203.0, 7.0, 1640, 246, "PATROL", "LASER", 1.23, 29.4, (185, 241, 91), [{"item": "HEALTH", "chance": 0.2}], 174.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_078"] = EnemySpec("ENEMY_UNIT_078", "Hostile Unit 078", "Scout", 342.0, 202.0, 8.0, 1660, 249, "PATROL", "LASER", 1.22, 29.6, (214, 38, 162), [{"item": "HEALTH", "chance": 0.2}], 176.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_079"] = EnemySpec("ENEMY_UNIT_079", "Hostile Unit 079", "Scout", 346.0, 201.0, 9.0, 1680, 252, "PATROL", "LASER", 1.21, 29.8, (243, 91, 233), [{"item": "HEALTH", "chance": 0.2}], 178.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_080"] = EnemySpec("ENEMY_UNIT_080", "Hostile Unit 080", "Scout", 350.0, 200.0, 0.0, 1700, 255, "PATROL", "LASER", 1.2, 30.0, (16, 144, 48), [{"item": "HEALTH", "chance": 0.2}], 180.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_081"] = EnemySpec("ENEMY_UNIT_081", "Hostile Unit 081", "Scout", 354.0, 199.0, 1.0, 1720, 258, "PATROL", "LASER", 1.19, 30.2, (45, 197, 119), [{"item": "HEALTH", "chance": 0.2}], 182.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_082"] = EnemySpec("ENEMY_UNIT_082", "Hostile Unit 082", "Scout", 358.0, 198.0, 2.0, 1740, 261, "PATROL", "LASER", 1.18, 30.400000000000002, (74, 250, 190), [{"item": "HEALTH", "chance": 0.2}], 184.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_083"] = EnemySpec("ENEMY_UNIT_083", "Hostile Unit 083", "Scout", 362.0, 197.0, 3.0, 1760, 264, "PATROL", "LASER", 1.17, 30.6, (103, 47, 5), [{"item": "HEALTH", "chance": 0.2}], 186.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_084"] = EnemySpec("ENEMY_UNIT_084", "Hostile Unit 084", "Scout", 366.0, 196.0, 4.0, 1780, 267, "PATROL", "LASER", 1.1600000000000001, 30.8, (132, 100, 76), [{"item": "HEALTH", "chance": 0.2}], 188.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_085"] = EnemySpec("ENEMY_UNIT_085", "Hostile Unit 085", "Scout", 370.0, 195.0, 5.0, 1800, 270, "PATROL", "LASER", 1.15, 31.0, (161, 153, 147), [{"item": "HEALTH", "chance": 0.2}], 190.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_086"] = EnemySpec("ENEMY_UNIT_086", "Hostile Unit 086", "Scout", 374.0, 194.0, 6.0, 1820, 273, "PATROL", "LASER", 1.1400000000000001, 31.2, (190, 206, 218), [{"item": "HEALTH", "chance": 0.2}], 192.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_087"] = EnemySpec("ENEMY_UNIT_087", "Hostile Unit 087", "Scout", 378.0, 193.0, 7.0, 1840, 276, "PATROL", "LASER", 1.13, 31.400000000000002, (219, 3, 33), [{"item": "HEALTH", "chance": 0.2}], 194.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_088"] = EnemySpec("ENEMY_UNIT_088", "Hostile Unit 088", "Scout", 382.0, 192.0, 8.0, 1860, 279, "PATROL", "LASER", 1.12, 31.6, (248, 56, 104), [{"item": "HEALTH", "chance": 0.2}], 196.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_089"] = EnemySpec("ENEMY_UNIT_089", "Hostile Unit 089", "Scout", 386.0, 191.0, 9.0, 1880, 282, "PATROL", "LASER", 1.1099999999999999, 31.8, (21, 109, 175), [{"item": "HEALTH", "chance": 0.2}], 198.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_090"] = EnemySpec("ENEMY_UNIT_090", "Hostile Unit 090", "Scout", 390.0, 190.0, 0.0, 1900, 285, "PATROL", "LASER", 1.1, 32.0, (50, 162, 246), [{"item": "HEALTH", "chance": 0.2}], 200.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_091"] = EnemySpec("ENEMY_UNIT_091", "Hostile Unit 091", "Scout", 394.0, 189.0, 1.0, 1920, 288, "PATROL", "LASER", 1.0899999999999999, 32.2, (79, 215, 61), [{"item": "HEALTH", "chance": 0.2}], 202.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_092"] = EnemySpec("ENEMY_UNIT_092", "Hostile Unit 092", "Scout", 398.0, 188.0, 2.0, 1940, 291, "PATROL", "LASER", 1.08, 32.400000000000006, (108, 12, 132), [{"item": "HEALTH", "chance": 0.2}], 204.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_093"] = EnemySpec("ENEMY_UNIT_093", "Hostile Unit 093", "Scout", 402.0, 187.0, 3.0, 1960, 294, "PATROL", "LASER", 1.0699999999999998, 32.6, (137, 65, 203), [{"item": "HEALTH", "chance": 0.2}], 206.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_094"] = EnemySpec("ENEMY_UNIT_094", "Hostile Unit 094", "Scout", 406.0, 186.0, 4.0, 1980, 297, "PATROL", "LASER", 1.06, 32.8, (166, 118, 18), [{"item": "HEALTH", "chance": 0.2}], 208.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_095"] = EnemySpec("ENEMY_UNIT_095", "Hostile Unit 095", "Scout", 410.0, 185.0, 5.0, 2000, 300, "PATROL", "LASER", 1.0499999999999998, 33.0, (195, 171, 89), [{"item": "HEALTH", "chance": 0.2}], 210.0, 0.05, 1)

EnemyCatalog.ENEMIES["ENEMY_UNIT_096"] = EnemySpec("ENEMY_UNIT_096", "Hostile Unit 096", "Scout", 414.0, 184.0, 6.0, 2020, 303, "PATROL", "LASER", 1.04, 33.2, (224, 224, 160), [{"item": "HEALTH", "chance": 0.2}], 212.0, 0.05, 2)

EnemyCatalog.ENEMIES["ENEMY_UNIT_097"] = EnemySpec("ENEMY_UNIT_097", "Hostile Unit 097", "Scout", 418.0, 183.0, 7.0, 2040, 306, "PATROL", "LASER", 1.03, 33.400000000000006, (253, 21, 231), [{"item": "HEALTH", "chance": 0.2}], 214.0, 0.05, 3)

EnemyCatalog.ENEMIES["ENEMY_UNIT_098"] = EnemySpec("ENEMY_UNIT_098", "Hostile Unit 098", "Scout", 422.0, 182.0, 8.0, 2060, 309, "PATROL", "LASER", 1.02, 33.6, (26, 74, 46), [{"item": "HEALTH", "chance": 0.2}], 216.0, 0.05, 4)

EnemyCatalog.ENEMIES["ENEMY_UNIT_099"] = EnemySpec("ENEMY_UNIT_099", "Hostile Unit 099", "Scout", 426.0, 181.0, 9.0, 2080, 312, "PATROL", "LASER", 1.01, 33.8, (55, 127, 117), [{"item": "HEALTH", "chance": 0.2}], 218.0, 0.05, 5)

EnemyCatalog.ENEMIES["ENEMY_UNIT_100"] = EnemySpec("ENEMY_UNIT_100", "Hostile Unit 100", "Scout", 430.0, 180.0, 0.0, 2100, 315, "PATROL", "LASER", 1.0, 34.0, (84, 180, 188), [{"item": "HEALTH", "chance": 0.2}], 220.0, 0.05, 1)

