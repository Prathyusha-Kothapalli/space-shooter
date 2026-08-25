"""Achievement Catalog containing 150 achievement definitions."""
from typing import Dict, List
class AchievementSpec:
    def __init__(self, ach_id: str, title: str, description: str, category: str, score_points: int, icon_tag: str):
        self.ach_id = ach_id; self.title = title; self.description = description; self.category = category; self.score_points = score_points; self.icon_tag = icon_tag
class AchievementCatalog:
    ACHIEVEMENTS: Dict[str, AchievementSpec] = {}
AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_001"] = AchievementSpec("ACHIEVEMENT_001", "Galactic Milestone 001", "Achieve operational milestone target 1 in active combat scenarios.", "Combat", 15, "ICON_TAG_1")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_002"] = AchievementSpec("ACHIEVEMENT_002", "Galactic Milestone 002", "Achieve operational milestone target 2 in active combat scenarios.", "Combat", 20, "ICON_TAG_2")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_003"] = AchievementSpec("ACHIEVEMENT_003", "Galactic Milestone 003", "Achieve operational milestone target 3 in active combat scenarios.", "Combat", 25, "ICON_TAG_3")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_004"] = AchievementSpec("ACHIEVEMENT_004", "Galactic Milestone 004", "Achieve operational milestone target 4 in active combat scenarios.", "Combat", 30, "ICON_TAG_4")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_005"] = AchievementSpec("ACHIEVEMENT_005", "Galactic Milestone 005", "Achieve operational milestone target 5 in active combat scenarios.", "Combat", 35, "ICON_TAG_5")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_006"] = AchievementSpec("ACHIEVEMENT_006", "Galactic Milestone 006", "Achieve operational milestone target 6 in active combat scenarios.", "Combat", 40, "ICON_TAG_6")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_007"] = AchievementSpec("ACHIEVEMENT_007", "Galactic Milestone 007", "Achieve operational milestone target 7 in active combat scenarios.", "Combat", 45, "ICON_TAG_7")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_008"] = AchievementSpec("ACHIEVEMENT_008", "Galactic Milestone 008", "Achieve operational milestone target 8 in active combat scenarios.", "Combat", 50, "ICON_TAG_8")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_009"] = AchievementSpec("ACHIEVEMENT_009", "Galactic Milestone 009", "Achieve operational milestone target 9 in active combat scenarios.", "Combat", 55, "ICON_TAG_9")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_010"] = AchievementSpec("ACHIEVEMENT_010", "Galactic Milestone 010", "Achieve operational milestone target 10 in active combat scenarios.", "Combat", 60, "ICON_TAG_10")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_011"] = AchievementSpec("ACHIEVEMENT_011", "Galactic Milestone 011", "Achieve operational milestone target 11 in active combat scenarios.", "Combat", 65, "ICON_TAG_11")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_012"] = AchievementSpec("ACHIEVEMENT_012", "Galactic Milestone 012", "Achieve operational milestone target 12 in active combat scenarios.", "Combat", 70, "ICON_TAG_12")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_013"] = AchievementSpec("ACHIEVEMENT_013", "Galactic Milestone 013", "Achieve operational milestone target 13 in active combat scenarios.", "Combat", 75, "ICON_TAG_13")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_014"] = AchievementSpec("ACHIEVEMENT_014", "Galactic Milestone 014", "Achieve operational milestone target 14 in active combat scenarios.", "Combat", 80, "ICON_TAG_14")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_015"] = AchievementSpec("ACHIEVEMENT_015", "Galactic Milestone 015", "Achieve operational milestone target 15 in active combat scenarios.", "Combat", 85, "ICON_TAG_15")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_016"] = AchievementSpec("ACHIEVEMENT_016", "Galactic Milestone 016", "Achieve operational milestone target 16 in active combat scenarios.", "Combat", 90, "ICON_TAG_16")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_017"] = AchievementSpec("ACHIEVEMENT_017", "Galactic Milestone 017", "Achieve operational milestone target 17 in active combat scenarios.", "Combat", 95, "ICON_TAG_17")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_018"] = AchievementSpec("ACHIEVEMENT_018", "Galactic Milestone 018", "Achieve operational milestone target 18 in active combat scenarios.", "Combat", 100, "ICON_TAG_18")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_019"] = AchievementSpec("ACHIEVEMENT_019", "Galactic Milestone 019", "Achieve operational milestone target 19 in active combat scenarios.", "Combat", 105, "ICON_TAG_19")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_020"] = AchievementSpec("ACHIEVEMENT_020", "Galactic Milestone 020", "Achieve operational milestone target 20 in active combat scenarios.", "Combat", 110, "ICON_TAG_20")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_021"] = AchievementSpec("ACHIEVEMENT_021", "Galactic Milestone 021", "Achieve operational milestone target 21 in active combat scenarios.", "Combat", 115, "ICON_TAG_21")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_022"] = AchievementSpec("ACHIEVEMENT_022", "Galactic Milestone 022", "Achieve operational milestone target 22 in active combat scenarios.", "Combat", 120, "ICON_TAG_22")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_023"] = AchievementSpec("ACHIEVEMENT_023", "Galactic Milestone 023", "Achieve operational milestone target 23 in active combat scenarios.", "Combat", 125, "ICON_TAG_23")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_024"] = AchievementSpec("ACHIEVEMENT_024", "Galactic Milestone 024", "Achieve operational milestone target 24 in active combat scenarios.", "Combat", 130, "ICON_TAG_24")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_025"] = AchievementSpec("ACHIEVEMENT_025", "Galactic Milestone 025", "Achieve operational milestone target 25 in active combat scenarios.", "Combat", 135, "ICON_TAG_25")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_026"] = AchievementSpec("ACHIEVEMENT_026", "Galactic Milestone 026", "Achieve operational milestone target 26 in active combat scenarios.", "Combat", 140, "ICON_TAG_26")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_027"] = AchievementSpec("ACHIEVEMENT_027", "Galactic Milestone 027", "Achieve operational milestone target 27 in active combat scenarios.", "Combat", 145, "ICON_TAG_27")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_028"] = AchievementSpec("ACHIEVEMENT_028", "Galactic Milestone 028", "Achieve operational milestone target 28 in active combat scenarios.", "Combat", 150, "ICON_TAG_28")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_029"] = AchievementSpec("ACHIEVEMENT_029", "Galactic Milestone 029", "Achieve operational milestone target 29 in active combat scenarios.", "Combat", 155, "ICON_TAG_29")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_030"] = AchievementSpec("ACHIEVEMENT_030", "Galactic Milestone 030", "Achieve operational milestone target 30 in active combat scenarios.", "Combat", 160, "ICON_TAG_30")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_031"] = AchievementSpec("ACHIEVEMENT_031", "Galactic Milestone 031", "Achieve operational milestone target 31 in active combat scenarios.", "Combat", 165, "ICON_TAG_31")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_032"] = AchievementSpec("ACHIEVEMENT_032", "Galactic Milestone 032", "Achieve operational milestone target 32 in active combat scenarios.", "Combat", 170, "ICON_TAG_32")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_033"] = AchievementSpec("ACHIEVEMENT_033", "Galactic Milestone 033", "Achieve operational milestone target 33 in active combat scenarios.", "Combat", 175, "ICON_TAG_33")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_034"] = AchievementSpec("ACHIEVEMENT_034", "Galactic Milestone 034", "Achieve operational milestone target 34 in active combat scenarios.", "Combat", 180, "ICON_TAG_34")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_035"] = AchievementSpec("ACHIEVEMENT_035", "Galactic Milestone 035", "Achieve operational milestone target 35 in active combat scenarios.", "Combat", 185, "ICON_TAG_35")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_036"] = AchievementSpec("ACHIEVEMENT_036", "Galactic Milestone 036", "Achieve operational milestone target 36 in active combat scenarios.", "Combat", 190, "ICON_TAG_36")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_037"] = AchievementSpec("ACHIEVEMENT_037", "Galactic Milestone 037", "Achieve operational milestone target 37 in active combat scenarios.", "Combat", 195, "ICON_TAG_37")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_038"] = AchievementSpec("ACHIEVEMENT_038", "Galactic Milestone 038", "Achieve operational milestone target 38 in active combat scenarios.", "Combat", 200, "ICON_TAG_38")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_039"] = AchievementSpec("ACHIEVEMENT_039", "Galactic Milestone 039", "Achieve operational milestone target 39 in active combat scenarios.", "Combat", 205, "ICON_TAG_39")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_040"] = AchievementSpec("ACHIEVEMENT_040", "Galactic Milestone 040", "Achieve operational milestone target 40 in active combat scenarios.", "Combat", 210, "ICON_TAG_40")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_041"] = AchievementSpec("ACHIEVEMENT_041", "Galactic Milestone 041", "Achieve operational milestone target 41 in active combat scenarios.", "Combat", 215, "ICON_TAG_41")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_042"] = AchievementSpec("ACHIEVEMENT_042", "Galactic Milestone 042", "Achieve operational milestone target 42 in active combat scenarios.", "Combat", 220, "ICON_TAG_42")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_043"] = AchievementSpec("ACHIEVEMENT_043", "Galactic Milestone 043", "Achieve operational milestone target 43 in active combat scenarios.", "Combat", 225, "ICON_TAG_43")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_044"] = AchievementSpec("ACHIEVEMENT_044", "Galactic Milestone 044", "Achieve operational milestone target 44 in active combat scenarios.", "Combat", 230, "ICON_TAG_44")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_045"] = AchievementSpec("ACHIEVEMENT_045", "Galactic Milestone 045", "Achieve operational milestone target 45 in active combat scenarios.", "Combat", 235, "ICON_TAG_45")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_046"] = AchievementSpec("ACHIEVEMENT_046", "Galactic Milestone 046", "Achieve operational milestone target 46 in active combat scenarios.", "Combat", 240, "ICON_TAG_46")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_047"] = AchievementSpec("ACHIEVEMENT_047", "Galactic Milestone 047", "Achieve operational milestone target 47 in active combat scenarios.", "Combat", 245, "ICON_TAG_47")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_048"] = AchievementSpec("ACHIEVEMENT_048", "Galactic Milestone 048", "Achieve operational milestone target 48 in active combat scenarios.", "Combat", 250, "ICON_TAG_48")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_049"] = AchievementSpec("ACHIEVEMENT_049", "Galactic Milestone 049", "Achieve operational milestone target 49 in active combat scenarios.", "Combat", 255, "ICON_TAG_49")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_050"] = AchievementSpec("ACHIEVEMENT_050", "Galactic Milestone 050", "Achieve operational milestone target 50 in active combat scenarios.", "Combat", 260, "ICON_TAG_50")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_051"] = AchievementSpec("ACHIEVEMENT_051", "Galactic Milestone 051", "Achieve operational milestone target 51 in active combat scenarios.", "Combat", 265, "ICON_TAG_51")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_052"] = AchievementSpec("ACHIEVEMENT_052", "Galactic Milestone 052", "Achieve operational milestone target 52 in active combat scenarios.", "Combat", 270, "ICON_TAG_52")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_053"] = AchievementSpec("ACHIEVEMENT_053", "Galactic Milestone 053", "Achieve operational milestone target 53 in active combat scenarios.", "Combat", 275, "ICON_TAG_53")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_054"] = AchievementSpec("ACHIEVEMENT_054", "Galactic Milestone 054", "Achieve operational milestone target 54 in active combat scenarios.", "Combat", 280, "ICON_TAG_54")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_055"] = AchievementSpec("ACHIEVEMENT_055", "Galactic Milestone 055", "Achieve operational milestone target 55 in active combat scenarios.", "Combat", 285, "ICON_TAG_55")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_056"] = AchievementSpec("ACHIEVEMENT_056", "Galactic Milestone 056", "Achieve operational milestone target 56 in active combat scenarios.", "Combat", 290, "ICON_TAG_56")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_057"] = AchievementSpec("ACHIEVEMENT_057", "Galactic Milestone 057", "Achieve operational milestone target 57 in active combat scenarios.", "Combat", 295, "ICON_TAG_57")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_058"] = AchievementSpec("ACHIEVEMENT_058", "Galactic Milestone 058", "Achieve operational milestone target 58 in active combat scenarios.", "Combat", 300, "ICON_TAG_58")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_059"] = AchievementSpec("ACHIEVEMENT_059", "Galactic Milestone 059", "Achieve operational milestone target 59 in active combat scenarios.", "Combat", 305, "ICON_TAG_59")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_060"] = AchievementSpec("ACHIEVEMENT_060", "Galactic Milestone 060", "Achieve operational milestone target 60 in active combat scenarios.", "Combat", 310, "ICON_TAG_60")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_061"] = AchievementSpec("ACHIEVEMENT_061", "Galactic Milestone 061", "Achieve operational milestone target 61 in active combat scenarios.", "Combat", 315, "ICON_TAG_61")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_062"] = AchievementSpec("ACHIEVEMENT_062", "Galactic Milestone 062", "Achieve operational milestone target 62 in active combat scenarios.", "Combat", 320, "ICON_TAG_62")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_063"] = AchievementSpec("ACHIEVEMENT_063", "Galactic Milestone 063", "Achieve operational milestone target 63 in active combat scenarios.", "Combat", 325, "ICON_TAG_63")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_064"] = AchievementSpec("ACHIEVEMENT_064", "Galactic Milestone 064", "Achieve operational milestone target 64 in active combat scenarios.", "Combat", 330, "ICON_TAG_64")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_065"] = AchievementSpec("ACHIEVEMENT_065", "Galactic Milestone 065", "Achieve operational milestone target 65 in active combat scenarios.", "Combat", 335, "ICON_TAG_65")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_066"] = AchievementSpec("ACHIEVEMENT_066", "Galactic Milestone 066", "Achieve operational milestone target 66 in active combat scenarios.", "Combat", 340, "ICON_TAG_66")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_067"] = AchievementSpec("ACHIEVEMENT_067", "Galactic Milestone 067", "Achieve operational milestone target 67 in active combat scenarios.", "Combat", 345, "ICON_TAG_67")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_068"] = AchievementSpec("ACHIEVEMENT_068", "Galactic Milestone 068", "Achieve operational milestone target 68 in active combat scenarios.", "Combat", 350, "ICON_TAG_68")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_069"] = AchievementSpec("ACHIEVEMENT_069", "Galactic Milestone 069", "Achieve operational milestone target 69 in active combat scenarios.", "Combat", 355, "ICON_TAG_69")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_070"] = AchievementSpec("ACHIEVEMENT_070", "Galactic Milestone 070", "Achieve operational milestone target 70 in active combat scenarios.", "Combat", 360, "ICON_TAG_70")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_071"] = AchievementSpec("ACHIEVEMENT_071", "Galactic Milestone 071", "Achieve operational milestone target 71 in active combat scenarios.", "Combat", 365, "ICON_TAG_71")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_072"] = AchievementSpec("ACHIEVEMENT_072", "Galactic Milestone 072", "Achieve operational milestone target 72 in active combat scenarios.", "Combat", 370, "ICON_TAG_72")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_073"] = AchievementSpec("ACHIEVEMENT_073", "Galactic Milestone 073", "Achieve operational milestone target 73 in active combat scenarios.", "Combat", 375, "ICON_TAG_73")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_074"] = AchievementSpec("ACHIEVEMENT_074", "Galactic Milestone 074", "Achieve operational milestone target 74 in active combat scenarios.", "Combat", 380, "ICON_TAG_74")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_075"] = AchievementSpec("ACHIEVEMENT_075", "Galactic Milestone 075", "Achieve operational milestone target 75 in active combat scenarios.", "Combat", 385, "ICON_TAG_75")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_076"] = AchievementSpec("ACHIEVEMENT_076", "Galactic Milestone 076", "Achieve operational milestone target 76 in active combat scenarios.", "Combat", 390, "ICON_TAG_76")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_077"] = AchievementSpec("ACHIEVEMENT_077", "Galactic Milestone 077", "Achieve operational milestone target 77 in active combat scenarios.", "Combat", 395, "ICON_TAG_77")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_078"] = AchievementSpec("ACHIEVEMENT_078", "Galactic Milestone 078", "Achieve operational milestone target 78 in active combat scenarios.", "Combat", 400, "ICON_TAG_78")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_079"] = AchievementSpec("ACHIEVEMENT_079", "Galactic Milestone 079", "Achieve operational milestone target 79 in active combat scenarios.", "Combat", 405, "ICON_TAG_79")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_080"] = AchievementSpec("ACHIEVEMENT_080", "Galactic Milestone 080", "Achieve operational milestone target 80 in active combat scenarios.", "Combat", 410, "ICON_TAG_80")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_081"] = AchievementSpec("ACHIEVEMENT_081", "Galactic Milestone 081", "Achieve operational milestone target 81 in active combat scenarios.", "Combat", 415, "ICON_TAG_81")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_082"] = AchievementSpec("ACHIEVEMENT_082", "Galactic Milestone 082", "Achieve operational milestone target 82 in active combat scenarios.", "Combat", 420, "ICON_TAG_82")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_083"] = AchievementSpec("ACHIEVEMENT_083", "Galactic Milestone 083", "Achieve operational milestone target 83 in active combat scenarios.", "Combat", 425, "ICON_TAG_83")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_084"] = AchievementSpec("ACHIEVEMENT_084", "Galactic Milestone 084", "Achieve operational milestone target 84 in active combat scenarios.", "Combat", 430, "ICON_TAG_84")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_085"] = AchievementSpec("ACHIEVEMENT_085", "Galactic Milestone 085", "Achieve operational milestone target 85 in active combat scenarios.", "Combat", 435, "ICON_TAG_85")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_086"] = AchievementSpec("ACHIEVEMENT_086", "Galactic Milestone 086", "Achieve operational milestone target 86 in active combat scenarios.", "Combat", 440, "ICON_TAG_86")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_087"] = AchievementSpec("ACHIEVEMENT_087", "Galactic Milestone 087", "Achieve operational milestone target 87 in active combat scenarios.", "Combat", 445, "ICON_TAG_87")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_088"] = AchievementSpec("ACHIEVEMENT_088", "Galactic Milestone 088", "Achieve operational milestone target 88 in active combat scenarios.", "Combat", 450, "ICON_TAG_88")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_089"] = AchievementSpec("ACHIEVEMENT_089", "Galactic Milestone 089", "Achieve operational milestone target 89 in active combat scenarios.", "Combat", 455, "ICON_TAG_89")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_090"] = AchievementSpec("ACHIEVEMENT_090", "Galactic Milestone 090", "Achieve operational milestone target 90 in active combat scenarios.", "Combat", 460, "ICON_TAG_90")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_091"] = AchievementSpec("ACHIEVEMENT_091", "Galactic Milestone 091", "Achieve operational milestone target 91 in active combat scenarios.", "Combat", 465, "ICON_TAG_91")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_092"] = AchievementSpec("ACHIEVEMENT_092", "Galactic Milestone 092", "Achieve operational milestone target 92 in active combat scenarios.", "Combat", 470, "ICON_TAG_92")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_093"] = AchievementSpec("ACHIEVEMENT_093", "Galactic Milestone 093", "Achieve operational milestone target 93 in active combat scenarios.", "Combat", 475, "ICON_TAG_93")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_094"] = AchievementSpec("ACHIEVEMENT_094", "Galactic Milestone 094", "Achieve operational milestone target 94 in active combat scenarios.", "Combat", 480, "ICON_TAG_94")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_095"] = AchievementSpec("ACHIEVEMENT_095", "Galactic Milestone 095", "Achieve operational milestone target 95 in active combat scenarios.", "Combat", 485, "ICON_TAG_95")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_096"] = AchievementSpec("ACHIEVEMENT_096", "Galactic Milestone 096", "Achieve operational milestone target 96 in active combat scenarios.", "Combat", 490, "ICON_TAG_96")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_097"] = AchievementSpec("ACHIEVEMENT_097", "Galactic Milestone 097", "Achieve operational milestone target 97 in active combat scenarios.", "Combat", 495, "ICON_TAG_97")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_098"] = AchievementSpec("ACHIEVEMENT_098", "Galactic Milestone 098", "Achieve operational milestone target 98 in active combat scenarios.", "Combat", 500, "ICON_TAG_98")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_099"] = AchievementSpec("ACHIEVEMENT_099", "Galactic Milestone 099", "Achieve operational milestone target 99 in active combat scenarios.", "Combat", 505, "ICON_TAG_99")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_100"] = AchievementSpec("ACHIEVEMENT_100", "Galactic Milestone 100", "Achieve operational milestone target 100 in active combat scenarios.", "Combat", 510, "ICON_TAG_100")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_101"] = AchievementSpec("ACHIEVEMENT_101", "Galactic Milestone 101", "Achieve operational milestone target 101 in active combat scenarios.", "Combat", 515, "ICON_TAG_101")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_102"] = AchievementSpec("ACHIEVEMENT_102", "Galactic Milestone 102", "Achieve operational milestone target 102 in active combat scenarios.", "Combat", 520, "ICON_TAG_102")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_103"] = AchievementSpec("ACHIEVEMENT_103", "Galactic Milestone 103", "Achieve operational milestone target 103 in active combat scenarios.", "Combat", 525, "ICON_TAG_103")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_104"] = AchievementSpec("ACHIEVEMENT_104", "Galactic Milestone 104", "Achieve operational milestone target 104 in active combat scenarios.", "Combat", 530, "ICON_TAG_104")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_105"] = AchievementSpec("ACHIEVEMENT_105", "Galactic Milestone 105", "Achieve operational milestone target 105 in active combat scenarios.", "Combat", 535, "ICON_TAG_105")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_106"] = AchievementSpec("ACHIEVEMENT_106", "Galactic Milestone 106", "Achieve operational milestone target 106 in active combat scenarios.", "Combat", 540, "ICON_TAG_106")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_107"] = AchievementSpec("ACHIEVEMENT_107", "Galactic Milestone 107", "Achieve operational milestone target 107 in active combat scenarios.", "Combat", 545, "ICON_TAG_107")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_108"] = AchievementSpec("ACHIEVEMENT_108", "Galactic Milestone 108", "Achieve operational milestone target 108 in active combat scenarios.", "Combat", 550, "ICON_TAG_108")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_109"] = AchievementSpec("ACHIEVEMENT_109", "Galactic Milestone 109", "Achieve operational milestone target 109 in active combat scenarios.", "Combat", 555, "ICON_TAG_109")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_110"] = AchievementSpec("ACHIEVEMENT_110", "Galactic Milestone 110", "Achieve operational milestone target 110 in active combat scenarios.", "Combat", 560, "ICON_TAG_110")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_111"] = AchievementSpec("ACHIEVEMENT_111", "Galactic Milestone 111", "Achieve operational milestone target 111 in active combat scenarios.", "Combat", 565, "ICON_TAG_111")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_112"] = AchievementSpec("ACHIEVEMENT_112", "Galactic Milestone 112", "Achieve operational milestone target 112 in active combat scenarios.", "Combat", 570, "ICON_TAG_112")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_113"] = AchievementSpec("ACHIEVEMENT_113", "Galactic Milestone 113", "Achieve operational milestone target 113 in active combat scenarios.", "Combat", 575, "ICON_TAG_113")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_114"] = AchievementSpec("ACHIEVEMENT_114", "Galactic Milestone 114", "Achieve operational milestone target 114 in active combat scenarios.", "Combat", 580, "ICON_TAG_114")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_115"] = AchievementSpec("ACHIEVEMENT_115", "Galactic Milestone 115", "Achieve operational milestone target 115 in active combat scenarios.", "Combat", 585, "ICON_TAG_115")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_116"] = AchievementSpec("ACHIEVEMENT_116", "Galactic Milestone 116", "Achieve operational milestone target 116 in active combat scenarios.", "Combat", 590, "ICON_TAG_116")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_117"] = AchievementSpec("ACHIEVEMENT_117", "Galactic Milestone 117", "Achieve operational milestone target 117 in active combat scenarios.", "Combat", 595, "ICON_TAG_117")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_118"] = AchievementSpec("ACHIEVEMENT_118", "Galactic Milestone 118", "Achieve operational milestone target 118 in active combat scenarios.", "Combat", 600, "ICON_TAG_118")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_119"] = AchievementSpec("ACHIEVEMENT_119", "Galactic Milestone 119", "Achieve operational milestone target 119 in active combat scenarios.", "Combat", 605, "ICON_TAG_119")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_120"] = AchievementSpec("ACHIEVEMENT_120", "Galactic Milestone 120", "Achieve operational milestone target 120 in active combat scenarios.", "Combat", 610, "ICON_TAG_120")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_121"] = AchievementSpec("ACHIEVEMENT_121", "Galactic Milestone 121", "Achieve operational milestone target 121 in active combat scenarios.", "Combat", 615, "ICON_TAG_121")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_122"] = AchievementSpec("ACHIEVEMENT_122", "Galactic Milestone 122", "Achieve operational milestone target 122 in active combat scenarios.", "Combat", 620, "ICON_TAG_122")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_123"] = AchievementSpec("ACHIEVEMENT_123", "Galactic Milestone 123", "Achieve operational milestone target 123 in active combat scenarios.", "Combat", 625, "ICON_TAG_123")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_124"] = AchievementSpec("ACHIEVEMENT_124", "Galactic Milestone 124", "Achieve operational milestone target 124 in active combat scenarios.", "Combat", 630, "ICON_TAG_124")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_125"] = AchievementSpec("ACHIEVEMENT_125", "Galactic Milestone 125", "Achieve operational milestone target 125 in active combat scenarios.", "Combat", 635, "ICON_TAG_125")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_126"] = AchievementSpec("ACHIEVEMENT_126", "Galactic Milestone 126", "Achieve operational milestone target 126 in active combat scenarios.", "Combat", 640, "ICON_TAG_126")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_127"] = AchievementSpec("ACHIEVEMENT_127", "Galactic Milestone 127", "Achieve operational milestone target 127 in active combat scenarios.", "Combat", 645, "ICON_TAG_127")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_128"] = AchievementSpec("ACHIEVEMENT_128", "Galactic Milestone 128", "Achieve operational milestone target 128 in active combat scenarios.", "Combat", 650, "ICON_TAG_128")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_129"] = AchievementSpec("ACHIEVEMENT_129", "Galactic Milestone 129", "Achieve operational milestone target 129 in active combat scenarios.", "Combat", 655, "ICON_TAG_129")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_130"] = AchievementSpec("ACHIEVEMENT_130", "Galactic Milestone 130", "Achieve operational milestone target 130 in active combat scenarios.", "Combat", 660, "ICON_TAG_130")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_131"] = AchievementSpec("ACHIEVEMENT_131", "Galactic Milestone 131", "Achieve operational milestone target 131 in active combat scenarios.", "Combat", 665, "ICON_TAG_131")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_132"] = AchievementSpec("ACHIEVEMENT_132", "Galactic Milestone 132", "Achieve operational milestone target 132 in active combat scenarios.", "Combat", 670, "ICON_TAG_132")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_133"] = AchievementSpec("ACHIEVEMENT_133", "Galactic Milestone 133", "Achieve operational milestone target 133 in active combat scenarios.", "Combat", 675, "ICON_TAG_133")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_134"] = AchievementSpec("ACHIEVEMENT_134", "Galactic Milestone 134", "Achieve operational milestone target 134 in active combat scenarios.", "Combat", 680, "ICON_TAG_134")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_135"] = AchievementSpec("ACHIEVEMENT_135", "Galactic Milestone 135", "Achieve operational milestone target 135 in active combat scenarios.", "Combat", 685, "ICON_TAG_135")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_136"] = AchievementSpec("ACHIEVEMENT_136", "Galactic Milestone 136", "Achieve operational milestone target 136 in active combat scenarios.", "Combat", 690, "ICON_TAG_136")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_137"] = AchievementSpec("ACHIEVEMENT_137", "Galactic Milestone 137", "Achieve operational milestone target 137 in active combat scenarios.", "Combat", 695, "ICON_TAG_137")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_138"] = AchievementSpec("ACHIEVEMENT_138", "Galactic Milestone 138", "Achieve operational milestone target 138 in active combat scenarios.", "Combat", 700, "ICON_TAG_138")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_139"] = AchievementSpec("ACHIEVEMENT_139", "Galactic Milestone 139", "Achieve operational milestone target 139 in active combat scenarios.", "Combat", 705, "ICON_TAG_139")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_140"] = AchievementSpec("ACHIEVEMENT_140", "Galactic Milestone 140", "Achieve operational milestone target 140 in active combat scenarios.", "Combat", 710, "ICON_TAG_140")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_141"] = AchievementSpec("ACHIEVEMENT_141", "Galactic Milestone 141", "Achieve operational milestone target 141 in active combat scenarios.", "Combat", 715, "ICON_TAG_141")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_142"] = AchievementSpec("ACHIEVEMENT_142", "Galactic Milestone 142", "Achieve operational milestone target 142 in active combat scenarios.", "Combat", 720, "ICON_TAG_142")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_143"] = AchievementSpec("ACHIEVEMENT_143", "Galactic Milestone 143", "Achieve operational milestone target 143 in active combat scenarios.", "Combat", 725, "ICON_TAG_143")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_144"] = AchievementSpec("ACHIEVEMENT_144", "Galactic Milestone 144", "Achieve operational milestone target 144 in active combat scenarios.", "Combat", 730, "ICON_TAG_144")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_145"] = AchievementSpec("ACHIEVEMENT_145", "Galactic Milestone 145", "Achieve operational milestone target 145 in active combat scenarios.", "Combat", 735, "ICON_TAG_145")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_146"] = AchievementSpec("ACHIEVEMENT_146", "Galactic Milestone 146", "Achieve operational milestone target 146 in active combat scenarios.", "Combat", 740, "ICON_TAG_146")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_147"] = AchievementSpec("ACHIEVEMENT_147", "Galactic Milestone 147", "Achieve operational milestone target 147 in active combat scenarios.", "Combat", 745, "ICON_TAG_147")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_148"] = AchievementSpec("ACHIEVEMENT_148", "Galactic Milestone 148", "Achieve operational milestone target 148 in active combat scenarios.", "Combat", 750, "ICON_TAG_148")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_149"] = AchievementSpec("ACHIEVEMENT_149", "Galactic Milestone 149", "Achieve operational milestone target 149 in active combat scenarios.", "Combat", 755, "ICON_TAG_149")

AchievementCatalog.ACHIEVEMENTS["ACHIEVEMENT_150"] = AchievementSpec("ACHIEVEMENT_150", "Galactic Milestone 150", "Achieve operational milestone target 150 in active combat scenarios.", "Combat", 760, "ICON_TAG_150")

