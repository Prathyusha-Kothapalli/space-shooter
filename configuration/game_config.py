"""
Game Configuration Manager. Handles persistent configuration options
such as audio volume, graphics settings, keybindings, and user preferences.
"""

import json
import os
from typing import Dict, Any


class GameConfig:
    """Manages game settings and persists preferences to disk."""
    
    DEFAULT_CONFIG: Dict[str, Any] = {
        "graphics": {
            "width": 1280,
            "height": 720,
            "fullscreen": False,
            "vsync": True,
            "fps_cap": 60,
            "particles_quality": "HIGH",  # LOW, MEDIUM, HIGH
            "screen_shake": True,
        },
        "audio": {
            "master_volume": 0.8,
            "sfx_volume": 0.9,
            "music_volume": 0.7,
            "audio_enabled": True,
        },
        "gameplay": {
            "difficulty": "NORMAL",
            "show_fps": False,
            "damage_numbers": True,
            "auto_fire": False,
        },
        "controls": {
            "move_up": "K_w",
            "move_down": "K_s",
            "move_left": "K_a",
            "move_right": "K_d",
            "primary_fire": "K_SPACE",
            "secondary_fire": "K_j",
            "special_ability": "K_k",
            "pause": "K_ESCAPE",
        }
    }

    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.data: Dict[str, Any] = self.DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> None:
        """Load configuration from JSON file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    self._deep_merge(self.data, loaded)
            except Exception as e:
                print(f"[Config] Failed to load config file: {e}. Using defaults.")

    def save(self) -> bool:
        """Save active configuration to JSON file."""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"[Config] Failed to save config file: {e}")
            return False

    def get(self, category: str, key: str, default: Any = None) -> Any:
        """Retrieve config value safely."""
        return self.data.get(category, {}).get(key, default)

    def set(self, category: str, key: str, value: Any) -> None:
        """Set config value and trigger auto-save."""
        if category not in self.data:
            self.data[category] = {}
        self.data[category][key] = value

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> None:
        """Merge configuration recursively."""
        for k, v in override.items():
            if isinstance(v, dict) and k in base and isinstance(base[k], dict):
                self._deep_merge(base[k], v)
            else:
                base[k] = v
