"""
Boss Catalog containing 10 flagship boss specifications, multi-phase mechanics,
enraged parameters, and arena entry sequences.
"""

from typing import Dict, Any, List


class BossPhaseSpec:
    """Specification for a boss phase phase."""

    def __init__(self, phase_number: int, health_threshold: float, attack_pattern: str, attack_interval: float, speed_mult: float, enraged: bool):
        self.phase_number = phase_number
        self.health_threshold = health_threshold
        self.attack_pattern = attack_pattern
        self.attack_interval = attack_interval
        self.speed_mult = speed_mult
        self.enraged = enraged


class BossSpec:
    """Specifications for a flagship boss."""

    def __init__(
        self,
        boss_id: str,
        name: str,
        title: str,
        max_health: float,
        score_reward: int,
        xp_reward: int,
        collision_radius: float,
        primary_color: tuple,
        phases: List[BossPhaseSpec]
    ):
        self.boss_id = boss_id
        self.name = name
        self.title = title
        self.max_health = max_health
        self.score_reward = score_reward
        self.xp_reward = xp_reward
        self.collision_radius = collision_radius
        self.primary_color = primary_color
        self.phases = phases


class BossCatalog:
    """Registry database of flagship bosses in Starlight Vanguard."""

    BOSSES: Dict[str, BossSpec] = {
        "VOID_DREADNOUGHT": BossSpec(
            boss_id="VOID_DREADNOUGHT",
            name="Void Dreadnought",
            title="Flagship of the Void Armada",
            max_health=1200.0,
            score_reward=6000,
            xp_reward=1200,
            collision_radius=65.0,
            primary_color=(220, 20, 60),
            phases=[
                BossPhaseSpec(1, 1.00, "DUAL_PLASMA_BURST", 1.8, 1.0, False),
                BossPhaseSpec(2, 0.66, "FIVE_WAY_FAN_BARRAGE", 1.2, 1.4, False),
                BossPhaseSpec(3, 0.33, "RADIAL_ENRAGED_EXPLOSION", 0.7, 1.6, True),
            ]
        ),
        "STARLIGHT_CARRIER": BossSpec(
            boss_id="STARLIGHT_CARRIER",
            name="Starlight Carrier",
            title="Orbital Hive Mothership",
            max_health=1800.0,
            score_reward=8500,
            xp_reward=1800,
            collision_radius=75.0,
            primary_color=(0, 200, 220),
            phases=[
                BossPhaseSpec(1, 1.00, "QUAD_CANNON_STREAM", 2.0, 1.0, False),
                BossPhaseSpec(2, 0.66, "ORBITAL_LASER_RING", 1.4, 1.2, False),
                BossPhaseSpec(3, 0.33, "SPIRAL_BARRAGE_OVERCLOCK", 0.8, 1.5, True),
            ]
        ),
        "ANCIENT_LEVIATHAN": BossSpec(
            boss_id="ANCIENT_LEVIATHAN",
            name="Ancient Leviathan",
            title="Biomechanical Apex Entity",
            max_health=2400.0,
            score_reward=12000,
            xp_reward=2500,
            collision_radius=85.0,
            primary_color=(50, 205, 50),
            phases=[
                BossPhaseSpec(1, 1.00, "ACID_SPIT_STREAM", 1.6, 1.0, False),
                BossPhaseSpec(2, 0.66, "SPORE_CLOUD_BOMBARDMENT", 1.1, 1.3, False),
                BossPhaseSpec(3, 0.33, "BIO_ELECTRIC_SHOCKWAVE", 0.6, 1.8, True),
            ]
        ),
        "SOLAR_SUPERNOVA": BossSpec(
            boss_id="SOLAR_SUPERNOVA",
            name="Solar Supernova",
            title="Stellar Fusion Destroyer",
            max_health=3000.0,
            score_reward=15000,
            xp_reward=3000,
            collision_radius=90.0,
            primary_color=(255, 215, 0),
            phases=[
                BossPhaseSpec(1, 1.00, "SOLAR_BEAM_ARRAY", 1.5, 1.0, False),
                BossPhaseSpec(2, 0.66, "PROMINENCE_CORONAL_MASS", 1.0, 1.4, False),
                BossPhaseSpec(3, 0.33, "HYPERNOVA_COLLAPSE", 0.5, 2.0, True),
            ]
        ),
    }

    @classmethod
    def get_boss(cls, boss_id: str) -> BossSpec:
        spec = cls.BOSSES.get(boss_id)
        if not spec:
            raise KeyError(f"Unknown boss spec identifier: {boss_id}")
        return spec
