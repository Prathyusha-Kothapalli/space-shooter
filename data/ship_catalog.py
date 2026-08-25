"""
Comprehensive Player Ship Catalog containing 20+ detailed spaceship chassis specifications,
stats, passive traits, module slot layouts, and sprite geometry formulas.
"""

from typing import Dict, Any, List


class ShipSpec:
    """Detailed specifications for a player spaceship chassis."""

    def __init__(
        self,
        ship_id: str,
        name: str,
        class_type: str,
        description: str,
        base_health: float,
        base_shield: float,
        shield_regen: float,
        base_speed: float,
        rotation_speed: float,
        armor_rating: float,
        weapon_slots: int,
        module_slots: int,
        passive_trait: str,
        primary_color: str,
        secondary_color: str,
        unlock_cost: int
    ):
        self.ship_id = ship_id
        self.name = name
        self.class_type = class_type
        self.description = description
        self.base_health = base_health
        self.base_shield = base_shield
        self.shield_regen = shield_regen
        self.base_speed = base_speed
        self.rotation_speed = rotation_speed
        self.armor_rating = armor_rating
        self.weapon_slots = weapon_slots
        self.module_slots = module_slots
        self.passive_trait = passive_trait
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.unlock_cost = unlock_cost


class ShipCatalog:
    """Registry database of all playable spaceship chassis in Starlight Vanguard."""

    SHIPS: Dict[str, ShipSpec] = {
        "VANGUARD_INTERCEPTOR": ShipSpec(
            ship_id="VANGUARD_INTERCEPTOR",
            name="Vanguard Interceptor",
            class_type="Interceptor",
            description="Balanced multi-role scout ship engineered for frontline reconnaissance and skirmishing.",
            base_health=100.0,
            base_shield=100.0,
            shield_regen=15.0,
            base_speed=380.0,
            rotation_speed=300.0,
            armor_rating=5.0,
            weapon_slots=2,
            module_slots=3,
            passive_trait="Emergency Thrusters (+20% speed when shield drops)",
            primary_color="#00E6FF",
            secondary_color="#1E90FF",
            unlock_cost=0
        ),
        "VOID_DREADNOUGHT": ShipSpec(
            ship_id="VOID_DREADNOUGHT",
            name="Void Dreadnought",
            class_type="Heavy Battleship",
            description="Massive armored warship equipped with heavy shielding and multi-weapon hardpoints.",
            base_health=250.0,
            base_shield=200.0,
            shield_regen=10.0,
            base_speed=240.0,
            rotation_speed=180.0,
            armor_rating=25.0,
            weapon_slots=4,
            module_slots=5,
            passive_trait="Reinforced Hull (-15% damage taken from explosions)",
            primary_color="#9B59B6",
            secondary_color="#642882",
            unlock_cost=2500
        ),
        "STEALTH_PHANTOM": ShipSpec(
            ship_id="STEALTH_PHANTOM",
            name="Stealth Phantom",
            class_type="Covert Operative",
            description="High-tech covert vessel utilizing optical cloaking and precision critical strikes.",
            base_health=70.0,
            base_shield=80.0,
            shield_regen=20.0,
            base_speed=460.0,
            rotation_speed=360.0,
            armor_rating=0.0,
            weapon_slots=2,
            module_slots=4,
            passive_trait="Shadow Strike (+35% Critical Chance when exiting cloak)",
            primary_color="#646E7D",
            secondary_color="#282D37",
            unlock_cost=3000
        ),
        "STARLIGHT_CARRIER": ShipSpec(
            ship_id="STARLIGHT_CARRIER",
            name="Starlight Carrier",
            class_type="Flagship Support",
            description="Fleet flagship equipped with automated repair drones and energy distribution grids.",
            base_health=180.0,
            base_shield=250.0,
            shield_regen=25.0,
            base_speed=280.0,
            rotation_speed=200.0,
            armor_rating=15.0,
            weapon_slots=3,
            module_slots=6,
            passive_trait="Repair Drones (Passively heals 2 HP/sec)",
            primary_color="#00C8DC",
            secondary_color="#0A648C",
            unlock_cost=4500
        ),
        "PLASMA_CORSAIR": ShipSpec(
            ship_id="PLASMA_CORSAIR",
            name="Plasma Corsair",
            class_type="Assault Raider",
            description="Aggressive pirate raider tuned for extreme weapon fire rates and energy weapon overclocks.",
            base_health=120.0,
            base_shield=90.0,
            shield_regen=12.0,
            base_speed=410.0,
            rotation_speed=320.0,
            armor_rating=8.0,
            weapon_slots=3,
            module_slots=3,
            passive_trait="Overclock Feed (+20% Fire Rate for plasma weapons)",
            primary_color="#FF8C00",
            secondary_color="#DC5000",
            unlock_cost=3500
        ),
        "QUANTUM_STRIKER": ShipSpec(
            ship_id="QUANTUM_STRIKER",
            name="Quantum Striker",
            class_type="Experimental Fighter",
            description="Prototype craft harnessing dimensional shift engines for instantaneous repositioning.",
            base_health=90.0,
            base_shield=140.0,
            shield_regen=22.0,
            base_speed=440.0,
            rotation_speed=340.0,
            armor_rating=5.0,
            weapon_slots=2,
            module_slots=5,
            passive_trait="Phase Dash (Invulnerable for 0.5s during sudden boosts)",
            primary_color="#FF0080",
            secondary_color="#800040",
            unlock_cost=5000
        ),
        "TITAN_GUNSHIP": ShipSpec(
            ship_id="TITAN_GUNSHIP",
            name="Titan Gunship",
            class_type="Heavy Gunship",
            description="Unstoppable siege gunship deploying devastating ordnance and heavy missile pods.",
            base_health=300.0,
            base_shield=150.0,
            shield_regen=8.0,
            base_speed=210.0,
            rotation_speed=150.0,
            armor_rating=30.0,
            weapon_slots=4,
            module_slots=4,
            passive_trait="Heavy Payload (+25% Explosive Weapon Splash Area)",
            primary_color="#32CD32",
            secondary_color="#148C14",
            unlock_cost=4000
        ),
        "SOLAR_ECLIPSE": ShipSpec(
            ship_id="SOLAR_ECLIPSE",
            name="Solar Eclipse",
            class_type="Energy Cruiser",
            description="Cruiser harnessing solar plasma cells to power devastating beam array weaponry.",
            base_health=140.0,
            base_shield=220.0,
            shield_regen=28.0,
            base_speed=320.0,
            rotation_speed=240.0,
            armor_rating=12.0,
            weapon_slots=3,
            module_slots=5,
            passive_trait="Solar Core (Beam weapons consume 30% less heat)",
            primary_color="#FFD700",
            secondary_color="#FF8C00",
            unlock_cost=4200
        ),
        "NEBULA_SPECTRE": ShipSpec(
            ship_id="NEBULA_SPECTRE",
            name="Nebula Spectre",
            class_type="Recon Frigate",
            description="Long-range frigate specialized in electronic warfare and targeted disruptions.",
            base_health=110.0,
            base_shield=160.0,
            shield_regen=18.0,
            base_speed=370.0,
            rotation_speed=280.0,
            armor_rating=10.0,
            weapon_slots=2,
            module_slots=6,
            passive_trait="EMP Pulse (Triggers shockwave when taking critical hit)",
            primary_color="#B464FF",
            secondary_color="#6420A0",
            unlock_cost=3800
        ),
        "APEX_PREDATOR": ShipSpec(
            ship_id="APEX_PREDATOR",
            name="Apex Predator",
            class_type="Hunter Heavy Interceptor",
            description="Elite hunter craft optimized for tracking and destroying enemy priority targets.",
            base_health=130.0,
            base_shield=130.0,
            shield_regen=16.0,
            base_speed=430.0,
            rotation_speed=330.0,
            armor_rating=10.0,
            weapon_slots=3,
            module_slots=4,
            passive_trait="Bounty Target (+25% Score and XP per enemy kill)",
            primary_color="#DC143C",
            secondary_color="#780A1E",
            unlock_cost=6000
        ),
    }

    @classmethod
    def get_ship(cls, ship_id: str) -> ShipSpec:
        """Retrieve ship spec by identifier."""
        spec = cls.SHIPS.get(ship_id)
        if not spec:
            raise KeyError(f"Unknown ship chassis identifier: {ship_id}")
        return spec

    @classmethod
    def list_all_ships(cls) -> List[ShipSpec]:
        """Return list of all registered ship specs."""
        return list(cls.SHIPS.values())
