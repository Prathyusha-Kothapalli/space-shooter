"""
Event Dispatcher system for decoupling game components using Publish/Subscribe pattern.
"""

from typing import Dict, List, Callable, Any
from utils.logger import log_info, log_error


class Event:
    """Represents a game event payload."""
    def __init__(self, event_type: str, data: Any = None):
        self.type = event_type
        self.data = data


class EventDispatcher:
    """Central event bus manager."""
    _instance = None

    def __init__(self):
        self._listeners: Dict[str, List[Callable[[Event], None]]] = {}

    @classmethod
    def get_instance(cls) -> 'EventDispatcher':
        if cls._instance is None:
            cls._instance = EventDispatcher()
        return cls._instance

    def subscribe(self, event_type: str, callback: Callable[[Event], None]) -> None:
        """Subscribe a listener callback to an event type."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        if callback not in self._listeners[event_type]:
            self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable[[Event], None]) -> None:
        """Unsubscribe a listener callback."""
        if event_type in self._listeners and callback in self._listeners[event_type]:
            self._listeners[event_type].remove(callback)

    def dispatch(self, event_type: str, data: Any = None) -> None:
        """Dispatch event to all subscribed listeners."""
        event = Event(event_type, data)
        if event_type in self._listeners:
            for listener in list(self._listeners[event_type]):
                try:
                    listener(event)
                except Exception as e:
                    log_error("EventDispatcher", f"Error in listener for event '{event_type}': {e}")

    def clear(self) -> None:
        """Remove all subscribers."""
        self._listeners.clear()
