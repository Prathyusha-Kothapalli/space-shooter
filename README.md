# Starlight Vanguard - 2D Space Shooter

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-green)
![Tests](https://img.shields.io/badge/Tests-Passing%20(13%2F13)-brightgreen)
![License](https://img.shields.io/badge/License-MIT-purple)

A complete, high-performance **2D Space Shooter & Galactic Roguelite Engine** built with clean, modular architecture, spatial quadtree & spatial hash physics, multi-phase boss encounters, weapon upgrade trees, AI behavior trees, software audio synthesizer, procedural starmap generator, item crafting system, and 13 automated unit tests.

---

## 🚀 Game Overview

**Starlight Vanguard** is an arcade space shooter and galactic roguelite where players command an customizable fleet of battlecraft against alien armadas and colossal flagship bosses across procedurally generated galactic sectors.

---

## ✨ Key Features & Expansion Systems

- **20+ Playable Spaceship Chassis**: Interceptors, Dreadnoughts, Stealth Phantoms, Carriers, Plasma Corsairs, Solar Cruisers, and Titan Gunships.
- **30+ Weapon Systems**: Pulse Cannons, Spread Shot, Heavy Plasma, Homing Missiles, Quantum Railguns, Beam Rays, and Singularity Void Cannons.
- **25+ Alien Enemy Craft**: Scouts, Interceptors, Cruisers, Plasma Bombers, Stealth Drones, Precision Snipers, and Shield Generator Drones.
- **AI Behavior Trees**: Selector, Sequence, Inverter, Condition, and Action nodes driving complex squad tactics (Pincher attacks, Flanking, Sacrificial Drones).
- **Procedural Sector Starmap Generator**: Multi-column branching sector navigation graph (Combat, Elite, Boss, Shop, Random Event, Black Market, Repair Station).
- **Interactive Narrative Encounters**: Text event decision scenarios with risk/reward choices, resource trades, and random outcomes.
- **Procedural Software Audio Synthesizer**: Math-based sound generator producing PCM sample buffers (Sine, Square, Sawtooth, Triangle, White Noise) for 50+ sound effects.
- **Item Crafting & Module Socketing Engine**: Blueprint recipes, component dismantling, and socketable stat-boosting ship modules.
- **4 Flagship Boss Encounters**: Void Dreadnought, Starlight Carrier, Ancient Leviathan, and Solar Supernova with multi-phase attack patterns.
- **7 Power-Up Items**: Health Repair, Shield Recharge, Rapid-Fire, Double-Damage, Speed Boost, EMP Shockwave, and Magnet.
- **Dual Physics Engine**: Spatial Quadtree partitioning ($O(N \log N)$) & Spatial Hash Grid ($O(1)$) with 2D Raycasting and 2D RigidBody dynamics.
- **14 UI State Scenes**: Main Menu, Gameplay HUD, Pause Overlay, Game Over, Victory, Tech Tree, Codex, Inventory, Shop, Sector Map, Achievements, Statistics, Crafting Workbench, Settings.

---

## 🎮 Controls

| Action | Primary Key | Secondary Key |
|---|---|---|
| **Move Up / Forward** | `W` | `Up Arrow` |
| **Move Down / Backward** | `S` | `Down Arrow` |
| **Move Left** | `A` | `Left Arrow` |
| **Move Right** | `D` | `Right Arrow` |
| **Primary Fire** | `Space` | `J` |
| **Secondary Fire** | `K` | - |
| **Special Ability** | `L` | `E` |
| **Boost Speed** | `Left Shift` | `Q` |
| **Pause Game** | `Escape` | `P` |
| **Confirm / Select** | `Enter` | `Space` |

---

## 🏗️ Modular Codebase Architecture (72 Files)

```
space_shooter/
├── core/             # Engine loop, clock, event bus, input manager, state machine
├── game/             # Session context, game manager, state handlers
├── data/             # Ship catalog, weapon catalog, enemy catalog, boss catalog, item catalog, lore codex, achievement catalog
├── sector_map/       # Sector starmap generator, sector manager, interactive text events, shop vendor system
├── crafting/         # Crafting recipe engine, socketable module system
├── physics/          # Spatial hash grid, 2D raycasting engine, 2D rigid body dynamics
├── player/           # Player ship entity, health/shield component, stats & XP
├── weapons/          # Abstract Base Weapon, Pulse Cannon, Spread, Heavy Plasma, Railgun, Factory
├── projectiles/      # Base Projectiles, Homing, Beam, zero-allocation Projectile Pool
├── enemies/          # Scout, Interceptor, Cruiser, Bomber, Stealth Drone, Factory
├── ai/               # Steering behaviors, AI controller, Behavior Trees, squad tactics, boss behavior tree
├── bosses/           # Boss Base, Void Dreadnought, Starlight Carrier multi-phase AI
├── waves/            # Procedural wave generator, difficulty scaling, wave manager
├── powerups/         # Power-up items, drop spawner
├── combat/           # Health system, damage calculation payload
├── collision/        # Quadtree spatial partitioning, collider components, collision matrix
├── progression/      # XP manager, tech tree node upgrades
├── achievements/     # Milestone achievement unlocks
├── statistics/       # Game session metric tracking
├── ui/               # Gameplay HUD, Main Menu, Pause Menu, Game Over, Victory, Tech Tree, Codex, Inventory, Shop, Sector Map, Achievements, Statistics, Crafting UI
├── audio/            # Audio manager, software audio synthesizer, sound trigger engine
├── effects/          # Particle engine, 3-layer parallax starfield, screen shake, bloom, explosion factory, nebula generator, screen-space vignetting
├── saveload/         # Save profile & high score JSON serializer
├── settings/         # Configuration manager
└── tests/            # Automated unit test suite (13 test cases across 10 test modules)
```

---

## 🛠️ Installation & Execution

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Game
```bash
python main.py
```

### Run Headless Verification Mode
```bash
python main.py --headless
```

### Run Automated Tests (13 Test Cases)
```bash
python -m unittest discover tests
```

---

## 📜 Git Commit History

1. `ea3be45` - `feat: Initialize 2D space shooter architecture`
2. `56dcae6` - `feat: Implement player weapons and projectile systems`
3. `d1ff6a1` - `feat: Implement enemies AI waves and bosses`
4. `58869fa` - `feat: Implement power-ups progression UI and persistence`
5. `a2d264b` - `feat: Add tests polish and documentation`
6. `6a9e8ae` - `feat: Add galactic starmap, data catalog engine, AI behavior trees, audio synthesizer, and crafting system`
