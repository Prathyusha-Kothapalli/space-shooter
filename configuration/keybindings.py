"""
Keybindings Mapper for Keyboard and Gamepad inputs.
Provides input action lookup abstractions.
"""

from typing import Dict, Set, List


class ActionInputs:
    """Action constant identifiers."""
    MOVE_UP = "MOVE_UP"
    MOVE_DOWN = "MOVE_DOWN"
    MOVE_LEFT = "MOVE_LEFT"
    MOVE_RIGHT = "MOVE_RIGHT"
    PRIMARY_FIRE = "PRIMARY_FIRE"
    SECONDARY_FIRE = "SECONDARY_FIRE"
    SPECIAL_ABILITY = "SPECIAL_ABILITY"
    BOOST = "BOOST"
    PAUSE = "PAUSE"
    CONFIRM = "CONFIRM"
    CANCEL = "CANCEL"


class Keybindings:
    """Manages input mappings from raw keys to high-level game actions."""
    
    DEFAULT_KEYMAP: Dict[str, List[int]] = {
        ActionInputs.MOVE_UP: [119, 1073741906],      # W, Up Arrow
        ActionInputs.MOVE_DOWN: [115, 1073741905],    # S, Down Arrow
        ActionInputs.MOVE_LEFT: [97, 1073741904],     # A, Left Arrow
        ActionInputs.MOVE_RIGHT: [100, 1073741903],   # D, Right Arrow
        ActionInputs.PRIMARY_FIRE: [32, 106],         # Space, J
        ActionInputs.SECONDARY_FIRE: [107],           # K
        ActionInputs.SPECIAL_ABILITY: [108, 101],     # L, E
        ActionInputs.BOOST: [1073742049, 113],        # Left Shift, Q
        ActionInputs.PAUSE: [27, 112],                # Escape, P
        ActionInputs.CONFIRM: [13, 32],               # Return, Space
        ActionInputs.CANCEL: [27, 98],                # Escape, B
    }

    def __init__(self, key_map: Dict[str, List[int]] = None):
        self.key_map = key_map if key_map is not None else self.DEFAULT_KEYMAP.copy()
        self.active_actions: Set[str] = set()

    def update_from_keys(self, pressed_keys: Set[int]) -> Set[str]:
        """Update active high-level actions based on set of currently pressed keys."""
        self.active_actions.clear()
        for action, key_codes in self.key_map.items():
            for key in key_codes:
                if key in pressed_keys:
                    self.active_actions.add(action)
                    break
        return self.active_actions

    def is_action_active(self, action: str) -> bool:
        """Check if a specific action is triggered."""
        return action in self.active_actions

    def remap_key(self, action: str, new_key_code: int) -> None:
        """Remap an action to a new primary key code."""
        if action in self.key_map:
            self.key_map[action] = [new_key_code]
