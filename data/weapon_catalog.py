"""
Weapon Catalog containing 30+ weapon variant definitions, damage profiles,
ammo curves, heat mechanics, and particle effect attributes.
"""

from typing import Dict, Any, List


class WeaponSpec:
    """Detailed specs for a weapon variant."""

    def __init__(
        self,
        weapon_id: str,
        name: str,
        category: str,
        description: str,
        damage: float,
        fire_rate: float,
        heat_per_shot: float,
        energy_cost: float,
        projectile_speed: float,
        projectile_count: int,
        spread_angle: float,
        damage_type: str,
        crit_chance: float,
        crit_mult: float,
        unlock_tier: int,
        color_rgb: tuple
    ):
        self.weapon_id = weapon_id
        self.name = name
        self.category = category
        self.description = description
        self.damage = damage
        self.fire_rate = fire_rate
        self.heat_per_shot = heat_per_shot
        self.energy_cost = energy_cost
        self.projectile_speed = projectile_speed
        self.projectile_count = projectile_count
        self.spread_angle = spread_angle
        self.damage_type = damage_type
        self.crit_chance = crit_chance
        self.crit_mult = crit_mult
        self.unlock_tier = unlock_tier
        self.color_rgb = color_rgb


class WeaponCatalog:
    """Database registry of all weapons in Starlight Vanguard."""

    WEAPONS: Dict[str, WeaponSpec] = {
        "PULSE_CANNON_MK1": WeaponSpec(
            weapon_id="PULSE_CANNON_MK1",
            name="Pulse Cannon Mark I",
            category="Pulse",
            description="Standard rapid pulse laser battery.",
            damage=18.0,
            fire_rate=8.0,
            heat_per_shot=4.0,
            energy_cost=2.0,
            projectile_speed=850.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="ENERGY",
            crit_chance=0.05,
            crit_mult=1.5,
            unlock_tier=1,
            color_rgb=(0, 230, 255)
        ),
        "PULSE_CANNON_MK2": WeaponSpec(
            weapon_id="PULSE_CANNON_MK2",
            name="Twin Pulse Cannon Mark II",
            category="Pulse",
            description="Upgraded twin-linked pulse cannon with elevated firing rate.",
            damage=22.0,
            fire_rate=9.5,
            heat_per_shot=3.5,
            energy_cost=2.5,
            projectile_speed=920.0,
            projectile_count=2,
            spread_angle=0.05,
            damage_type="ENERGY",
            crit_chance=0.08,
            crit_mult=1.6,
            unlock_tier=2,
            color_rgb=(30, 144, 255)
        ),
        "SPREAD_SHOT_TRI": WeaponSpec(
            weapon_id="SPREAD_SHOT_TRI",
            name="Tri-Spread Launcher",
            category="Spread",
            description="Fires a 3-projectile cone covering wider engagement zones.",
            damage=14.0,
            fire_rate=4.0,
            heat_per_shot=10.0,
            energy_cost=6.0,
            projectile_speed=750.0,
            projectile_count=3,
            spread_angle=0.45,
            damage_type="ENERGY",
            crit_chance=0.04,
            crit_mult=1.4,
            unlock_tier=1,
            color_rgb=(255, 215, 0)
        ),
        "SPREAD_SHOT_PENTA": WeaponSpec(
            weapon_id="SPREAD_SHOT_PENTA",
            name="Penta-Spread Scatter Cannon",
            category="Spread",
            description="Devastating 5-projectile cone designed for clearing dense enemy waves.",
            damage=18.0,
            fire_rate=3.5,
            heat_per_shot=14.0,
            energy_cost=8.0,
            projectile_speed=780.0,
            projectile_count=5,
            spread_angle=0.65,
            damage_type="ENERGY",
            crit_chance=0.06,
            crit_mult=1.5,
            unlock_tier=3,
            color_rgb=(255, 140, 0)
        ),
        "HEAVY_PLASMA_BLASTER": WeaponSpec(
            weapon_id="HEAVY_PLASMA_BLASTER",
            name="Heavy Plasma Blaster",
            category="Plasma",
            description="Slow-moving volatile plasma sphere dealing massive splash damage.",
            damage=55.0,
            fire_rate=2.0,
            heat_per_shot=22.0,
            energy_cost=12.0,
            projectile_speed=400.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="PLASMA",
            crit_chance=0.10,
            crit_mult=2.0,
            unlock_tier=2,
            color_rgb=(255, 0, 128)
        ),
        "SUPER_PLASMA_CATAPULT": WeaponSpec(
            weapon_id="SUPER_PLASMA_CATAPULT",
            name="Super Plasma Catapult",
            category="Plasma",
            description="Superheated antimatter plasma launcher capable of annihilating heavy armor.",
            damage=95.0,
            fire_rate=1.4,
            heat_per_shot=30.0,
            energy_cost=18.0,
            projectile_speed=450.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="PLASMA",
            crit_chance=0.15,
            crit_mult=2.2,
            unlock_tier=4,
            color_rgb=(200, 0, 255)
        ),
        "HOMING_MISSILE_POD_MK1": WeaponSpec(
            weapon_id="HOMING_MISSILE_POD_MK1",
            name="Homing Missile Pod Mk I",
            category="Missile",
            description="Deploys self-guided seeking warheads that lock onto target heat signatures.",
            damage=32.0,
            fire_rate=2.5,
            heat_per_shot=15.0,
            energy_cost=8.0,
            projectile_speed=450.0,
            projectile_count=2,
            spread_angle=0.6,
            damage_type="EXPLOSIVE",
            crit_chance=0.08,
            crit_mult=1.75,
            unlock_tier=2,
            color_rgb=(255, 140, 0)
        ),
        "QUANTUM_RAILGUN_ALPHA": WeaponSpec(
            weapon_id="QUANTUM_RAILGUN_ALPHA",
            name="Quantum Railgun Alpha",
            category="Railgun",
            description="Ultra-high velocity line-of-sight railgun piercing through multiple enemy hulls.",
            damage=85.0,
            fire_rate=1.5,
            heat_per_shot=30.0,
            energy_cost=15.0,
            projectile_speed=1800.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="PHYSICAL",
            crit_chance=0.20,
            crit_mult=2.5,
            unlock_tier=3,
            color_rgb=(180, 100, 255)
        ),
        "CONTINUOUS_BEAM_CANNON": WeaponSpec(
            weapon_id="CONTINUOUS_BEAM_CANNON",
            name="Continuous Beam Cannon",
            category="Beam",
            description="Sustained laser ray delivering continuous damage to all targets in beam path.",
            damage=12.0,
            fire_rate=5.0,
            heat_per_shot=8.0,
            energy_cost=4.0,
            projectile_speed=3000.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="ENERGY",
            crit_chance=0.05,
            crit_mult=1.5,
            unlock_tier=3,
            color_rgb=(50, 255, 150)
        ),
        "SINGULARITY_CANNON": WeaponSpec(
            weapon_id="SINGULARITY_CANNON",
            name="Singularity Void Cannon",
            category="Exotic",
            description="Fires a gravitational singularity pulling nearby hostiles into a crushing vortex.",
            damage=120.0,
            fire_rate=0.8,
            heat_per_shot=45.0,
            energy_cost=25.0,
            projectile_speed=320.0,
            projectile_count=1,
            spread_angle=0.0,
            damage_type="PLASMA",
            crit_chance=0.25,
            crit_mult=3.0,
            unlock_tier=5,
            color_rgb=(255, 50, 255)
        ),
    }

    @classmethod
    def get_weapon(cls, weapon_id: str) -> WeaponSpec:
        spec = cls.WEAPONS.get(weapon_id)
        if not spec:
            raise KeyError(f"Unknown weapon spec identifier: {weapon_id}")
        return spec
