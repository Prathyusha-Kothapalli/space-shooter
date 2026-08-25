"""
Asset definitions, procedural sprite generator parameters, and color palettes.
"""

from typing import Dict, Any, Tuple

# Ship & Sprite procedural definitions
SHIP_PALETTES: Dict[str, Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]] = {
    "PLAYER": ((0, 230, 255), (30, 144, 255), (240, 245, 255)),
    "SCOUT": ((255, 50, 50), (200, 20, 20), (255, 200, 200)),
    "INTERCEPTOR": ((255, 140, 0), (220, 80, 0), (255, 230, 150)),
    "CRUISER": ((155, 89, 182), (100, 40, 130), (230, 190, 255)),
    "BOMBER": ((50, 205, 50), (20, 140, 20), (200, 255, 200)),
    "STEALTH": ((100, 110, 125), (40, 45, 55), (180, 195, 210)),
    "VOID_DREADNOUGHT": ((220, 20, 60), (120, 10, 30), (255, 180, 200)),
    "STARLIGHT_CARRIER": ((0, 200, 220), (10, 100, 140), (200, 255, 255)),
}

WEAPON_VISUAL_SPECS: Dict[str, Dict[str, Any]] = {
    "PULSE_CANNON": {
        "color": (0, 255, 255),
        "size": (6, 16),
        "glow_radius": 8,
        "trail": True,
    },
    "SPREAD_SHOT": {
        "color": (255, 215, 0),
        "size": (5, 12),
        "glow_radius": 6,
        "trail": False,
    },
    "HEAVY_PLASMA": {
        "color": (255, 0, 128),
        "size": (14, 24),
        "glow_radius": 16,
        "trail": True,
    },
    "HOMING_MISSILES": {
        "color": (255, 140, 0),
        "size": (8, 18),
        "glow_radius": 10,
        "trail": True,
    },
    "QUANTUM_RAILGUN": {
        "color": (180, 100, 255),
        "size": (4, 40),
        "glow_radius": 12,
        "trail": True,
    },
    "BEAM_CANNON": {
        "color": (50, 255, 150),
        "size": (16, 720),
        "glow_radius": 20,
        "trail": False,
    }
}
