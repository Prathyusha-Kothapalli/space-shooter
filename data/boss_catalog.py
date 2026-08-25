"""Boss Catalog containing 50 flagship boss specifications."""
from typing import Dict, Any, List, Tuple
class BossPhaseSpec:
    def __init__(self, phase_number: int, health_threshold: float, attack_pattern: str, attack_interval: float, speed_mult: float, enraged: bool):
        self.phase_number = phase_number; self.health_threshold = health_threshold; self.attack_pattern = attack_pattern; self.attack_interval = attack_interval; self.speed_mult = speed_mult; self.enraged = enraged
class BossSpec:
    def __init__(self, boss_id: str, name: str, title: str, max_health: float, score_reward: int, xp_reward: int, collision_radius: float, primary_color: Tuple[int, int, int], phases: List[BossPhaseSpec]):
        self.boss_id = boss_id; self.name = name; self.title = title; self.max_health = max_health; self.score_reward = score_reward; self.xp_reward = xp_reward; self.collision_radius = collision_radius; self.primary_color = primary_color; self.phases = phases
class BossCatalog:
    BOSSES: Dict[str, BossSpec] = {}
BossCatalog.BOSSES["BOSS_FLAGSHIP_01"] = BossSpec("BOSS_FLAGSHIP_01", "Apex Dreadnought 1", "Overlord 1", 1500.0, 6000, 1200, 61.0, (37, 83, 101), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_02"] = BossSpec("BOSS_FLAGSHIP_02", "Apex Dreadnought 2", "Overlord 2", 2000.0, 7000, 1400, 62.0, (74, 166, 202), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_03"] = BossSpec("BOSS_FLAGSHIP_03", "Apex Dreadnought 3", "Overlord 3", 2500.0, 8000, 1600, 63.0, (111, 249, 47), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_04"] = BossSpec("BOSS_FLAGSHIP_04", "Apex Dreadnought 4", "Overlord 4", 3000.0, 9000, 1800, 64.0, (148, 76, 148), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_05"] = BossSpec("BOSS_FLAGSHIP_05", "Apex Dreadnought 5", "Overlord 5", 3500.0, 10000, 2000, 65.0, (185, 159, 249), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_06"] = BossSpec("BOSS_FLAGSHIP_06", "Apex Dreadnought 6", "Overlord 6", 4000.0, 11000, 2200, 66.0, (222, 242, 94), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_07"] = BossSpec("BOSS_FLAGSHIP_07", "Apex Dreadnought 7", "Overlord 7", 4500.0, 12000, 2400, 67.0, (3, 69, 195), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_08"] = BossSpec("BOSS_FLAGSHIP_08", "Apex Dreadnought 8", "Overlord 8", 5000.0, 13000, 2600, 68.0, (40, 152, 40), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_09"] = BossSpec("BOSS_FLAGSHIP_09", "Apex Dreadnought 9", "Overlord 9", 5500.0, 14000, 2800, 69.0, (77, 235, 141), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_10"] = BossSpec("BOSS_FLAGSHIP_10", "Apex Dreadnought 10", "Overlord 10", 6000.0, 15000, 3000, 70.0, (114, 62, 242), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_11"] = BossSpec("BOSS_FLAGSHIP_11", "Apex Dreadnought 11", "Overlord 11", 6500.0, 16000, 3200, 71.0, (151, 145, 87), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_12"] = BossSpec("BOSS_FLAGSHIP_12", "Apex Dreadnought 12", "Overlord 12", 7000.0, 17000, 3400, 72.0, (188, 228, 188), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_13"] = BossSpec("BOSS_FLAGSHIP_13", "Apex Dreadnought 13", "Overlord 13", 7500.0, 18000, 3600, 73.0, (225, 55, 33), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_14"] = BossSpec("BOSS_FLAGSHIP_14", "Apex Dreadnought 14", "Overlord 14", 8000.0, 19000, 3800, 74.0, (6, 138, 134), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_15"] = BossSpec("BOSS_FLAGSHIP_15", "Apex Dreadnought 15", "Overlord 15", 8500.0, 20000, 4000, 75.0, (43, 221, 235), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_16"] = BossSpec("BOSS_FLAGSHIP_16", "Apex Dreadnought 16", "Overlord 16", 9000.0, 21000, 4200, 76.0, (80, 48, 80), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_17"] = BossSpec("BOSS_FLAGSHIP_17", "Apex Dreadnought 17", "Overlord 17", 9500.0, 22000, 4400, 77.0, (117, 131, 181), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_18"] = BossSpec("BOSS_FLAGSHIP_18", "Apex Dreadnought 18", "Overlord 18", 10000.0, 23000, 4600, 78.0, (154, 214, 26), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_19"] = BossSpec("BOSS_FLAGSHIP_19", "Apex Dreadnought 19", "Overlord 19", 10500.0, 24000, 4800, 79.0, (191, 41, 127), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_20"] = BossSpec("BOSS_FLAGSHIP_20", "Apex Dreadnought 20", "Overlord 20", 11000.0, 25000, 5000, 80.0, (228, 124, 228), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_21"] = BossSpec("BOSS_FLAGSHIP_21", "Apex Dreadnought 21", "Overlord 21", 11500.0, 26000, 5200, 81.0, (9, 207, 73), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_22"] = BossSpec("BOSS_FLAGSHIP_22", "Apex Dreadnought 22", "Overlord 22", 12000.0, 27000, 5400, 82.0, (46, 34, 174), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_23"] = BossSpec("BOSS_FLAGSHIP_23", "Apex Dreadnought 23", "Overlord 23", 12500.0, 28000, 5600, 83.0, (83, 117, 19), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_24"] = BossSpec("BOSS_FLAGSHIP_24", "Apex Dreadnought 24", "Overlord 24", 13000.0, 29000, 5800, 84.0, (120, 200, 120), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_25"] = BossSpec("BOSS_FLAGSHIP_25", "Apex Dreadnought 25", "Overlord 25", 13500.0, 30000, 6000, 85.0, (157, 27, 221), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_26"] = BossSpec("BOSS_FLAGSHIP_26", "Apex Dreadnought 26", "Overlord 26", 14000.0, 31000, 6200, 86.0, (194, 110, 66), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_27"] = BossSpec("BOSS_FLAGSHIP_27", "Apex Dreadnought 27", "Overlord 27", 14500.0, 32000, 6400, 87.0, (231, 193, 167), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_28"] = BossSpec("BOSS_FLAGSHIP_28", "Apex Dreadnought 28", "Overlord 28", 15000.0, 33000, 6600, 88.0, (12, 20, 12), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_29"] = BossSpec("BOSS_FLAGSHIP_29", "Apex Dreadnought 29", "Overlord 29", 15500.0, 34000, 6800, 89.0, (49, 103, 113), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_30"] = BossSpec("BOSS_FLAGSHIP_30", "Apex Dreadnought 30", "Overlord 30", 16000.0, 35000, 7000, 90.0, (86, 186, 214), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_31"] = BossSpec("BOSS_FLAGSHIP_31", "Apex Dreadnought 31", "Overlord 31", 16500.0, 36000, 7200, 91.0, (123, 13, 59), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_32"] = BossSpec("BOSS_FLAGSHIP_32", "Apex Dreadnought 32", "Overlord 32", 17000.0, 37000, 7400, 92.0, (160, 96, 160), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_33"] = BossSpec("BOSS_FLAGSHIP_33", "Apex Dreadnought 33", "Overlord 33", 17500.0, 38000, 7600, 93.0, (197, 179, 5), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_34"] = BossSpec("BOSS_FLAGSHIP_34", "Apex Dreadnought 34", "Overlord 34", 18000.0, 39000, 7800, 94.0, (234, 6, 106), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_35"] = BossSpec("BOSS_FLAGSHIP_35", "Apex Dreadnought 35", "Overlord 35", 18500.0, 40000, 8000, 95.0, (15, 89, 207), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_36"] = BossSpec("BOSS_FLAGSHIP_36", "Apex Dreadnought 36", "Overlord 36", 19000.0, 41000, 8200, 96.0, (52, 172, 52), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_37"] = BossSpec("BOSS_FLAGSHIP_37", "Apex Dreadnought 37", "Overlord 37", 19500.0, 42000, 8400, 97.0, (89, 255, 153), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_38"] = BossSpec("BOSS_FLAGSHIP_38", "Apex Dreadnought 38", "Overlord 38", 20000.0, 43000, 8600, 98.0, (126, 82, 254), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_39"] = BossSpec("BOSS_FLAGSHIP_39", "Apex Dreadnought 39", "Overlord 39", 20500.0, 44000, 8800, 99.0, (163, 165, 99), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_40"] = BossSpec("BOSS_FLAGSHIP_40", "Apex Dreadnought 40", "Overlord 40", 21000.0, 45000, 9000, 100.0, (200, 248, 200), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_41"] = BossSpec("BOSS_FLAGSHIP_41", "Apex Dreadnought 41", "Overlord 41", 21500.0, 46000, 9200, 101.0, (237, 75, 45), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_42"] = BossSpec("BOSS_FLAGSHIP_42", "Apex Dreadnought 42", "Overlord 42", 22000.0, 47000, 9400, 102.0, (18, 158, 146), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_43"] = BossSpec("BOSS_FLAGSHIP_43", "Apex Dreadnought 43", "Overlord 43", 22500.0, 48000, 9600, 103.0, (55, 241, 247), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_44"] = BossSpec("BOSS_FLAGSHIP_44", "Apex Dreadnought 44", "Overlord 44", 23000.0, 49000, 9800, 104.0, (92, 68, 92), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_45"] = BossSpec("BOSS_FLAGSHIP_45", "Apex Dreadnought 45", "Overlord 45", 23500.0, 50000, 10000, 105.0, (129, 151, 193), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_46"] = BossSpec("BOSS_FLAGSHIP_46", "Apex Dreadnought 46", "Overlord 46", 24000.0, 51000, 10200, 106.0, (166, 234, 38), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_47"] = BossSpec("BOSS_FLAGSHIP_47", "Apex Dreadnought 47", "Overlord 47", 24500.0, 52000, 10400, 107.0, (203, 61, 139), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_48"] = BossSpec("BOSS_FLAGSHIP_48", "Apex Dreadnought 48", "Overlord 48", 25000.0, 53000, 10600, 108.0, (240, 144, 240), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_49"] = BossSpec("BOSS_FLAGSHIP_49", "Apex Dreadnought 49", "Overlord 49", 25500.0, 54000, 10800, 109.0, (21, 227, 85), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

BossCatalog.BOSSES["BOSS_FLAGSHIP_50"] = BossSpec("BOSS_FLAGSHIP_50", "Apex Dreadnought 50", "Overlord 50", 26000.0, 55000, 11000, 110.0, (58, 54, 186), [BossPhaseSpec(1, 1.0, "BURST", 1.8, 1.0, False), BossPhaseSpec(2, 0.5, "FAN", 1.0, 1.5, True)])

