"""
Main Entry Point for Starlight Vanguard - 2D Space Shooter.
"""

import sys
from game.game_manager import GameManager
from ui.main_menu import MainMenuState
from ui.pause_menu import PauseMenuState
from ui.game_over_ui import GameOverState
from ui.victory_ui import VictoryState
from ui.tech_tree_ui import TechTreeState
from ui.settings_ui import SettingsUIState
from ui.codex_ui import CodexUIState
from ui.inventory_ui import InventoryUIState
from ui.shop_ui import ShopUIState
from ui.sector_map_ui import SectorMapUIState
from ui.achievements_ui import AchievementsUIState
from ui.statistics_ui import StatisticsUIState
from ui.crafting_ui import CraftingUIState
from core.state_machine import BaseState
from configuration.constants import (
    STATE_MENU, STATE_GAMEPLAY, STATE_PAUSE, STATE_GAME_OVER,
    STATE_VICTORY, STATE_UPGRADE_TREE, STATE_SETTINGS, STATE_ACHIEVEMENTS, STATE_STATS
)
from utils.logger import log_info


class GameplayState(BaseState):
    """Active Gameplay State."""

    def __init__(self, game_context: any):
        super().__init__(STATE_GAMEPLAY)
        self.context = game_context

    def enter(self, params: any = None) -> None:
        log_info("GameplayState", "Entering active gameplay session.")

    def exit(self) -> None:
        pass

    def handle_input(self, input_manager: any) -> None:
        if input_manager.is_action_just_pressed("PAUSE"):
            if self.state_machine:
                self.state_machine.change_state(STATE_PAUSE)

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: any) -> None:
        pass


def main():
    """Application entry point."""
    log_info("Main", "Starting Starlight Vanguard Space Shooter Application...")
    
    headless_mode = "--headless" in sys.argv
    
    gm = GameManager()
    gm.setup(headless=headless_mode)

    # Register All Game State Scenes
    gm.engine.state_machine.add_state(MainMenuState())
    gm.engine.state_machine.add_state(GameplayState(gm.context))
    gm.engine.state_machine.add_state(PauseMenuState())
    gm.engine.state_machine.add_state(GameOverState())
    gm.engine.state_machine.add_state(VictoryState())
    gm.engine.state_machine.add_state(TechTreeState())
    gm.engine.state_machine.add_state(SettingsUIState())
    gm.engine.state_machine.add_state(CodexUIState())
    gm.engine.state_machine.add_state(InventoryUIState())
    gm.engine.state_machine.add_state(ShopUIState())
    gm.engine.state_machine.add_state(SectorMapUIState())
    gm.engine.state_machine.add_state(AchievementsUIState())
    gm.engine.state_machine.add_state(StatisticsUIState())
    gm.engine.state_machine.add_state(CraftingUIState())

    # Set Initial State to Main Menu
    gm.engine.state_machine.change_state(STATE_MENU)

    if not headless_mode:
        gm.start()
    else:
        log_info("Main", "Headless mode setup completed successfully.")


if __name__ == "__main__":
    main()
