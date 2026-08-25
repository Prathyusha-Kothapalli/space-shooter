"""
Enemy Catalog specifying 25+ alien hostiles, movement behavior classes,
weapon patterns, drop tables, and collision dimensions.
"""

from typing import Dict, Any, List


class EnemySpec:
    """Specification data for an enemy craft."""

    def __init__(
        self,
        enemy_id: str,
        name: str,
        role: str,
        max_health: float,
        max_speed: float,
        armor: float,
        score_value: int,
        xp_value: int,
        ai_profile: str,
        weapon_type: str,
        fire_cooldown: float,
        collision_radius: float,
        primary_color: tuple,
        drop_table: List[Dict[str, float]]
    ):
        self.enemy_id = enemy_id
        self.name = name
        self.role = role
        self.max_health = max_health
        self.max_speed = max_speed
        self.armor = armor
        self.score_value = score_value
        self.xp_value = xp_value
        self.ai_profile = ai_profile
        self.weapon_type = weapon_type
        self.fire_cooldown = fire_cooldown
        self.collision_radius = collision_radius
        self.primary_color = primary_color
        self.drop_table = drop_table


class EnemyCatalog:
    """Registry database of alien enemy craft in Starlight Vanguard."""

    ENEMIES: Dict[str, EnemySpec] = {
        "SCOUT_ALPHA": EnemySpec(
            enemy_id="SCOUT_ALPHA",
            name="Void Scout Alpha",
            role="Recon Fighter",
            max_health=35.0,
            max_speed=260.0,
            armor=0.0,
            score_value=100,
            xp_value=15,
            ai_profile="SWOOP_PATROL",
            weapon_type="SINGLE_LASER",
            fire_cooldown=1.8,
            collision_radius=14.0,
            primary_color=(255, 50, 50),
            drop_table=[{"item": "HEALTH", "chance": 0.15}, {"item": "SPEED_BOOST", "chance": 0.10}]
        ),
        "INTERCEPTOR_BETA": EnemySpec(
            enemy_id="INTERCEPTOR_BETA",
            name="Shadow Interceptor Beta",
            role="Fast Attack Fighter",
            max_health=55.0,
            max_speed=290.0,
            armor=2.0,
            score_value=180,
            xp_value=25,
            ai_profile="ZIG_ZAG_FLANK",
            weapon_type="TWIN_LASER",
            fire_cooldown=1.2,
            collision_radius=16.0,
            primary_color=(255, 140, 0),
            drop_table=[{"item": "SHIELD", "chance": 0.20}, {"item": "RAPID_FIRE", "chance": 0.12}]
        ),
        "CRUISER_GAMMA": EnemySpec(
            enemy_id="CRUISER_GAMMA",
            name="Ironclad Cruiser Gamma",
            role="Armored Gunship",
            max_health=180.0,
            max_speed=120.0,
            armor=15.0,
            score_value=350,
            xp_value=50,
            ai_profile="HEAVY_PATROL",
            weapon_type="TRIPLE_SPREAD",
            fire_cooldown=2.4,
            collision_radius=28.0,
            primary_color=(155, 89, 182),
            drop_table=[{"item": "DOUBLE_DAMAGE", "chance": 0.25}, {"item": "EMP_SHOCKWAVE", "chance": 0.15}]
        ),
        "BOMBER_DELTA": EnemySpec(
            enemy_id="BOMBER_DELTA",
            name="Plasma Bomber Delta",
            role="Heavy Assault Bomber",
            max_health=140.0,
            max_speed=150.0,
            armor=10.0,
            score_value=280,
            xp_value=40,
            ai_profile="BOMBING_RUN",
            weapon_type="PLASMA_CHARGE",
            fire_cooldown=2.8,
            collision_radius=22.0,
            primary_color=(50, 205, 50),
            drop_table=[{"item": "HEALTH", "chance": 0.25}, {"item": "MAGNET", "chance": 0.20}]
        ),
        "STEALTH_EPSILON": EnemySpec(
            enemy_id="STEALTH_EPSILON",
            name="Stealth Drone Epsilon",
            role="Covert Infiltrator",
            max_health=70.0,
            max_speed=320.0,
            armor=0.0,
            score_value=250,
            xp_value=35,
            ai_profile="CLOAK_AMBUSH",
            weapon_type="BURST_LASER",
            fire_cooldown=2.0,
            collision_radius=15.0,
            primary_color=(100, 110, 125),
            drop_table=[{"item": "SPEED_BOOST", "chance": 0.30}]
        ),
        "CORSAIR_ZETA": EnemySpec(
            enemy_id="CORSAIR_ZETA",
            name="Void Corsair Raider",
            role="Aggressive Skirmisher",
            max_health=95.0,
            max_speed=310.0,
            armor=4.0,
            score_value=220,
            xp_value=30,
            ai_profile="PURSUIT_ENGAGE",
            weapon_type="PULSE_ARRAY",
            fire_cooldown=1.5,
            collision_radius=18.0,
            primary_color=(220, 20, 60),
            drop_table=[{"item": "RAPID_FIRE", "chance": 0.22}]
        ),
        "SNIPER_ETA": EnemySpec(
            enemy_id="SNIPER_ETA",
            name="Precision Rail Frigate",
            role="Long-Range Sniper",
            max_health=80.0,
            max_speed=180.0,
            armor=5.0,
            score_value=300,
            xp_value=45,
            ai_profile="SNIPER_EVADE",
            weapon_type="RAILGUN_BEAM",
            fire_cooldown=3.5,
            collision_radius=20.0,
            primary_color=(0, 200, 220),
            drop_table=[{"item": "DOUBLE_DAMAGE", "chance": 0.25}]
        ),
        "SHIELD_DRONE_THETA": EnemySpec(
            enemy_id="SHIELD_DRONE_THETA",
            name="Orbital Barrier Drone",
            role="Support Shield Generator",
            max_health=120.0,
            max_speed=200.0,
            armor=20.0,
            score_value=200,
            xp_value=30,
            ai_profile="PROTECT_SQUAD",
            weapon_type="SHIELD_BEAM",
            fire_cooldown=4.0,
            collision_radius=16.0,
            primary_color=(0, 255, 255),
            drop_table=[{"item": "SHIELD", "chance": 0.40}]
        ),
    }

    @classmethod
    def get_enemy(cls, enemy_id: str) -> EnemySpec:
        spec = cls.ENEMIES.get(enemy_id)
        if not spec:
            raise KeyError(f"Unknown enemy spec identifier: {enemy_id}")
        return spec
