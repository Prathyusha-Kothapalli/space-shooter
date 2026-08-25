"""
Factory Pattern for constructing and configuring weapon instances.
"""

from typing import Dict, Type
from weapons.weapon_base import Weapon
from weapons.pulse_cannon import PulseCannon
from weapons.spread_shot import SpreadShot
from weapons.heavy_plasma import HeavyPlasma
from weapons.homing_missiles import HomingMissilePod
from weapons.quantum_railgun import QuantumRailgun
from weapons.beam_cannon import BeamCannon
from configuration.constants import (
    WEAPON_PULSE_CANNON, WEAPON_SPREAD_SHOT, WEAPON_HEAVY_PLASMA,
    WEAPON_HOMING_MISSILES, WEAPON_QUANTUM_RAILGUN, WEAPON_BEAM_CANNON
)


class WeaponFactory:
    """Instantiates registered weapon classes by name identifier."""

    _REGISTRY: Dict[str, Type[Weapon]] = {
        WEAPON_PULSE_CANNON: PulseCannon,
        WEAPON_SPREAD_SHOT: SpreadShot,
        WEAPON_HEAVY_PLASMA: HeavyPlasma,
        WEAPON_HOMING_MISSILES: HomingMissilePod,
        WEAPON_QUANTUM_RAILGUN: QuantumRailgun,
        WEAPON_BEAM_CANNON: BeamCannon,
    }

    @classmethod
    def create_weapon(cls, weapon_type: str) -> Weapon:
        """Create and return a new Weapon instance."""
        weapon_cls = cls._REGISTRY.get(weapon_type)
        if weapon_cls is None:
            raise ValueError(f"Unknown weapon type identifier: {weapon_type}")
        return weapon_cls()
