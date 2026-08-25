"""
Lore Database & Sector Codex containing worldbuilding narrative entries.
"""

from typing import Dict, List


class LoreEntry:
    """Represents a codex entry."""
    def __init__(self, entry_id: str, title: str, category: str, content: str):
        self.entry_id = entry_id
        self.title = title
        self.category = category
        self.content = content


class LoreDatabase:
    """Codex database of universe lore, factions, and alien taxonomy."""

    ENTRIES: Dict[str, LoreEntry] = {
        "FACTION_VANGUARD": LoreEntry(
            entry_id="FACTION_VANGUARD",
            title="The Starlight Vanguard Initiative",
            category="Factions",
            content="Formed after the First Void War, the Starlight Vanguard is an elite coalition of pilot aces, engineers, and tactical commanders dedicated to defending human colonies against alien armadas."
        ),
        "FACTION_VOID_ARMADA": LoreEntry(
            entry_id="FACTION_VOID_ARMADA",
            title="The Void Swarm Syndicate",
            category="Factions",
            content="An aggressive empire of bio-synthetic armadas originating from dark nebula space, seeking to assimilate planetary core energy."
        ),
        "SECTOR_ORION_REACH": LoreEntry(
            entry_id="SECTOR_ORION_REACH",
            title="Orion Outer Reach",
            category="Sectors",
            content="A hazardous frontier sector dense with asteroid fields, derelict starbases, and rogue pirate outposts."
        ),
    }

    @classmethod
    def get_entry(cls, entry_id: str) -> LoreEntry:
        return cls.ENTRIES.get(entry_id)
