"""
Master UI Manager holding UI component references and state delegation.
"""

from typing import Dict, Any
from ui.hud import GameplayHUD


class UIManager:
    """Manages active UI views."""

    def __init__(self):
        self.hud = GameplayHUD()

    def render_hud(self, surface: any, game_context: Any, player: Any) -> None:
        self.hud.render(surface, game_context, player)
