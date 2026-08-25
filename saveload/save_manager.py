"""
Save Game & Persistent High Score Data Serializer.
"""

import json
import os
from typing import Dict, Any


class SaveManager:
    """Handles JSON serialization and loading of game profiles and high scores."""

    SAVE_PATH = "savegame.json"

    @classmethod
    def save_profile(cls, profile_data: Dict[str, Any], filepath: str = SAVE_PATH) -> bool:
        """Save profile dict to JSON file."""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(profile_data, f, indent=4)
            return True
        except Exception as e:
            print(f"[SaveManager] Save failed: {e}")
            return False

    @classmethod
    def load_profile(cls, filepath: str = SAVE_PATH) -> Dict[str, Any]:
        """Load profile dict from JSON file."""
        if not os.path.exists(filepath):
            return {
                "high_score": 0,
                "unlocked_weapons": ["PULSE_CANNON", "SPREAD_SHOT"],
                "achievements": [],
                "lifetime_kills": 0,
            }
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[SaveManager] Load failed: {e}")
            return {"high_score": 0}
