"""
Global Constants and Engine Configurations for 2D Space Shooter.
Contains screen settings, physics parameters, color palettes, layer depth definitions,
and core gameplay balance matrices.
"""

# Screen & Window Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_FPS = 60
WINDOW_TITLE = "Starlight Vanguard - 2D Space Shooter"

# Color Palette (RGB Tuples)
COLOR_BLACK = (10, 12, 20)
COLOR_WHITE = (245, 245, 250)
COLOR_CYAN = (0, 230, 255)
COLOR_NEON_BLUE = (30, 144, 255)
COLOR_PURPLE = (155, 89, 182)
COLOR_MAGENTA = (255, 0, 128)
COLOR_CRIMSON = (220, 20, 60)
COLOR_RED = (255, 50, 50)
COLOR_ORANGE = (255, 140, 0)
COLOR_YELLOW = (255, 215, 0)
COLOR_LIME = (50, 205, 50)
COLOR_GREEN = (0, 255, 128)
COLOR_DARK_GRAY = (30, 35, 45)
COLOR_MID_GRAY = (60, 68, 85)
COLOR_LIGHT_GRAY = (180, 190, 205)
COLOR_GOLD = (255, 215, 0)
COLOR_HUD_BG = (15, 20, 30, 200)

# Render Layer Depths
LAYER_BACKGROUND = 0
LAYER_STARFIELD_FAR = 1
LAYER_STARFIELD_NEAR = 2
LAYER_DEBRIS = 3
LAYER_POWERUPS = 4
LAYER_PROJECTILES_ENEMY = 5
LAYER_PROJECTILES_PLAYER = 6
LAYER_ENEMIES = 7
LAYER_BOSS = 8
LAYER_PLAYER = 9
LAYER_EFFECTS = 10
LAYER_EXPLOSIONS = 11
LAYER_HUD = 12
LAYER_OVERLAY = 13

# Game States
STATE_MENU = "MENU"
STATE_GAMEPLAY = "GAMEPLAY"
STATE_PAUSE = "PAUSE"
STATE_UPGRADE_TREE = "UPGRADE_TREE"
STATE_GAME_OVER = "GAME_OVER"
STATE_VICTORY = "VICTORY"
STATE_ACHIEVEMENTS = "ACHIEVEMENTS"
STATE_SETTINGS = "SETTINGS"
STATE_STATS = "STATS"

# Difficulty Levels
DIFFICULTY_EASY = "EASY"
DIFFICULTY_NORMAL = "NORMAL"
DIFFICULTY_HARD = "HARD"

DIFFICULTY_SCALERS = {
    DIFFICULTY_EASY: {
        "enemy_health_mult": 0.8,
        "enemy_damage_mult": 0.7,
        "enemy_speed_mult": 0.85,
        "spawn_rate_mult": 0.8,
        "player_damage_mult": 1.25,
        "score_mult": 0.8,
        "xp_mult": 1.0,
    },
    DIFFICULTY_NORMAL: {
        "enemy_health_mult": 1.0,
        "enemy_damage_mult": 1.0,
        "enemy_speed_mult": 1.0,
        "spawn_rate_mult": 1.0,
        "player_damage_mult": 1.0,
        "score_mult": 1.0,
        "xp_mult": 1.0,
    },
    DIFFICULTY_HARD: {
        "enemy_health_mult": 1.4,
        "enemy_damage_mult": 1.5,
        "enemy_speed_mult": 1.2,
        "spawn_rate_mult": 1.3,
        "player_damage_mult": 0.9,
        "score_mult": 1.5,
        "xp_mult": 1.3,
    }
}

# Player Balance Constants
PLAYER_DEFAULT_SPEED = 380.0
PLAYER_MAX_HEALTH = 100.0
PLAYER_MAX_SHIELD = 100.0
PLAYER_SHIELD_REGEN_RATE = 12.0  # per second
PLAYER_SHIELD_REGEN_DELAY = 3.0   # seconds after taking hit
PLAYER_DEFAULT_LIVES = 3
PLAYER_INVINSIBILITY_DURATION = 2.0  # seconds on respawn

# Weapon Types
WEAPON_PULSE_CANNON = "PULSE_CANNON"
WEAPON_SPREAD_SHOT = "SPREAD_SHOT"
WEAPON_HEAVY_PLASMA = "HEAVY_PLASMA"
WEAPON_HOMING_MISSILES = "HOMING_MISSILES"
WEAPON_QUANTUM_RAILGUN = "QUANTUM_RAILGUN"
WEAPON_BEAM_CANNON = "BEAM_CANNON"

# Enemy Types
ENEMY_SCOUT = "SCOUT"
ENEMY_INTERCEPTOR = "INTERCEPTOR"
ENEMY_CRUISER = "CRUISER"
ENEMY_BOMBER = "BOMBER"
ENEMY_STEALTH = "STEALTH"

# Boss Types
BOSS_VOID_DREADNOUGHT = "VOID_DREADNOUGHT"
BOSS_STARLIGHT_CARRIER = "STARLIGHT_CARRIER"

# Power-up Types
POWERUP_HEALTH = "HEALTH"
POWERUP_SHIELD = "SHIELD"
POWERUP_RAPID_FIRE = "RAPID_FIRE"
POWERUP_DOUBLE_DAMAGE = "DOUBLE_DAMAGE"
POWERUP_SPEED_BOOST = "SPEED_BOOST"
POWERUP_EMP_SHOCKWAVE = "EMP_SHOCKWAVE"
POWERUP_MAGNET = "MAGNET"

POWERUP_DURATION_DEFAULT = 8.0  # seconds

# Collision Categories
CATEGORY_PLAYER = 0x0001
CATEGORY_PLAYER_PROJECTILE = 0x0002
CATEGORY_ENEMY = 0x0004
CATEGORY_ENEMY_PROJECTILE = 0x0008
CATEGORY_POWERUP = 0x0010
CATEGORY_BOSS = 0x0020
