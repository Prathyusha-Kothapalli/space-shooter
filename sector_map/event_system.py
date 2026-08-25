"""
Interactive Text Event System for random space encounter scenarios.
"""

import random
from typing import Dict, List, Any, Callable, Optional



class EventChoice:
    """Represents a selectable choice in an interactive text event."""

    def __init__(self, choice_text: str, requirement: Optional[str] = None, outcome_callback: Optional[Callable[[Any], str]] = None):
        self.choice_text = choice_text
        self.requirement = requirement
        self.outcome_callback = outcome_callback


class TextEvent:
    """Encapsulates a narrative space encounter scenario."""

    def __init__(self, event_id: str, title: str, description: str, choices: List[EventChoice]):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.choices = choices


class EventSystem:
    """Manager for generating and resolving space event encounters."""

    EVENTS: Dict[str, TextEvent] = {
        "DERELICT_FREIGHTER": TextEvent(
            event_id="DERELICT_FREIGHTER",
            title="Derelict Cargo Freighter",
            description="Your scanners detect a drifting cargo freighter with operational emergency lights. No lifesigns detected.",
            choices=[
                EventChoice(
                    choice_text="Send boarding party to salvage cargo.",
                    outcome_callback=lambda ctx: "Your crew salvaged 500 Credits and a Hyper-Shield Capacitor Core!" if random.random() < 0.7 else "Automated defense turrets activated! Took 20 hull damage."
                ),
                EventChoice(
                    choice_text="Perform long-range sensor scan.",
                    outcome_callback=lambda ctx: "Scans revealed a hidden Plasma Injector module!"
                ),
                EventChoice(
                    choice_text="Ignore freighter and move on.",
                    outcome_callback=lambda ctx: "You safely bypassed the drift site."
                ),
            ]
        ),
        "DISTRESS_BEACON": TextEvent(
            event_id="DISTRESS_BEACON",
            title="Encrypted Distress Beacon",
            description="A high-frequency distress beacon echoes from inside a nearby asteroid field.",
            choices=[
                EventChoice(
                    choice_text="Investigate distress signal location.",
                    outcome_callback=lambda ctx: "You rescued a stranded Vanguard engineer! Earned 1 Skill Point." if random.random() < 0.6 else "It was a pirate trap! Ambushed by pirate corsairs!"
                ),
                EventChoice(
                    choice_text="Log beacon position and jump away.",
                    outcome_callback=lambda ctx: "You recorded the coordinates and continued your mission."
                ),
            ]
        ),
    }

    @classmethod
    def get_random_event(cls) -> TextEvent:
        """Select a random event scenario."""
        event_key = random.choice(list(cls.EVENTS.keys()))
        return cls.EVENTS[event_key]
