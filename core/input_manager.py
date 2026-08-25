"""
Input Manager for key states, mouse state, and action queries.
"""

from typing import Set, Tuple, Dict
from utils.math_utils import Vector2D
from configuration.keybindings import Keybindings, ActionInputs


class InputManager:
    """Tracks raw keyboard & mouse state and maps them to high-level game actions."""

    def __init__(self, keybindings: Keybindings = None):
        self.keybindings = keybindings if keybindings is not None else Keybindings()
        
        self._keys_pressed_current: Set[int] = set()
        self._keys_pressed_previous: Set[int] = set()
        
        self.mouse_position = Vector2D(0, 0)
        self._mouse_buttons_current: Set[int] = set()
        self._mouse_buttons_previous: Set[int] = set()

    def process_raw_key_down(self, key_code: int) -> None:
        """Record key press down event."""
        self._keys_pressed_current.add(key_code)

    def process_raw_key_up(self, key_code: int) -> None:
        """Record key release event."""
        self._keys_pressed_current.discard(key_code)

    def process_mouse_move(self, x: float, y: float) -> None:
        """Update mouse position."""
        self.mouse_position.x = x
        self.mouse_position.y = y

    def process_mouse_button_down(self, button: int) -> None:
        """Record mouse button press."""
        self._mouse_buttons_current.add(button)

    def process_mouse_button_up(self, button: int) -> None:
        """Record mouse button release."""
        self._mouse_buttons_current.discard(button)

    def update_frame(self) -> None:
        """Copy current states to previous states at end of frame cycle."""
        self._keys_pressed_previous = set(self._keys_pressed_current)
        self._mouse_buttons_previous = set(self._mouse_buttons_current)
        self.keybindings.update_from_keys(self._keys_pressed_current)

    def is_action_pressed(self, action: str) -> bool:
        """Check if high-level action is held down."""
        return self.keybindings.is_action_active(action)

    def is_action_just_pressed(self, action: str) -> bool:
        """Check if action was pressed down on this specific frame."""
        key_codes = self.keybindings.key_map.get(action, [])
        for key in key_codes:
            if key in self._keys_pressed_current and key not in self._keys_pressed_previous:
                return True
        return False

    def is_key_pressed(self, key_code: int) -> bool:
        """Check if raw key is held down."""
        return key_code in self._keys_pressed_current

    def is_key_just_pressed(self, key_code: int) -> bool:
        """Check if raw key was pressed down this frame."""
        return key_code in self._keys_pressed_current and key_code not in self._keys_pressed_previous

    def is_mouse_button_pressed(self, button: int) -> bool:
        """Check if mouse button is held down."""
        return button in self._mouse_buttons_current

    def is_mouse_button_just_pressed(self, button: int) -> bool:
        """Check if mouse button was clicked this frame."""
        return button in self._mouse_buttons_current and button not in self._mouse_buttons_previous
