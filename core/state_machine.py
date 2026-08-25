"""
Finite State Machine architecture for managing overall game flow and active scenes.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
from utils.logger import log_info


class BaseState(ABC):
    """Abstract base class for all game states."""

    def __init__(self, name: str):
        self.name = name
        self.state_machine: Optional['StateMachine'] = None

    @abstractmethod
    def enter(self, params: Optional[Dict[str, Any]] = None) -> None:
        """Called when state is entered."""
        pass

    @abstractmethod
    def exit(self) -> None:
        """Called when state is exited."""
        pass

    @abstractmethod
    def handle_input(self, input_manager: Any) -> None:
        """Process user input."""
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update state logic."""
        pass

    @abstractmethod
    def render(self, surface: Any) -> None:
        """Render state visuals."""
        pass


class StateMachine:
    """Manages active states, transitions, and state lifecycles."""

    def __init__(self):
        self.states: Dict[str, BaseState] = {}
        self.current_state: Optional[BaseState] = None
        self.previous_state_name: Optional[str] = None

    def add_state(self, state: BaseState) -> None:
        """Register a state instance."""
        state.state_machine = self
        self.states[state.name] = state

    def change_state(self, name: str, params: Optional[Dict[str, Any]] = None) -> None:
        """Transition from current state to target state."""
        if name not in self.states:
            raise KeyError(f"State '{name}' not registered in StateMachine.")

        if self.current_state:
            self.previous_state_name = self.current_state.name
            log_info("StateMachine", f"Exiting state: {self.current_state.name}")
            self.current_state.exit()

        self.current_state = self.states[name]
        log_info("StateMachine", f"Entering state: {name}")
        self.current_state.enter(params)

    def handle_input(self, input_manager: Any) -> None:
        """Delegate input handling to active state."""
        if self.current_state:
            self.current_state.handle_input(input_manager)

    def update(self, dt: float) -> None:
        """Delegate update logic to active state."""
        if self.current_state:
            self.current_state.update(dt)

    def render(self, surface: Any) -> None:
        """Delegate rendering to active state."""
        if self.current_state:
            self.current_state.render(surface)
