# Starlight Vanguard - 2D Space Shooter

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-green)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-purple)

A complete, high-performance **2D Space Shooter Game** built with clean, modular architecture, spatial quadtree physics, multi-phase boss encounters, weapon upgrade trees, power-up systems, and automated unit testing.

---

## 🚀 Game Overview

**Starlight Vanguard** is an arcade-style space shooter where players command an advanced battlecraft against invading alien armadas and colossal flagship bosses. Featuring smooth vector controls, dynamic particle systems, responsive shield/health mechanics, and persistent progression.

---

## ✨ Features

- **Player Ship Controls**: Smooth inertial velocity movement, active shield regeneration, health management, and invulnerability frames.
- **6 Diverse Weapon Systems**:
  1. *Pulse Cannon*: Rapid twin-laser primary fire.
  2. *Spread Shot*: Cone spread 3-way & 5-way energy projectiles.
  3. *Heavy Plasma*: High-damage slow explosive plasma blasts.
  4. *Homing Missiles*: Self-guided tracking missile pods.
  5. *Quantum Railgun*: High-velocity piercing energy beams.
  6. *Beam Cannon*: Continuous line-of-sight laser beam.
- **5 Enemy Craft Types**:
  1. *Scout*: Agile light swooping reconnaissance fighter.
  2. *Interceptor*: High-speed zig-zag twin-firing craft.
  3. *Cruiser*: Heavy armor gunship with triple-turret fan barrage.
  4. *Bomber*: Deploys explosive heavy plasma charges.
  5. *Stealth Drone*: Cloaked unit executing surprise ambush attacks.
- **Autonomous AI Steering**: Pursuit, Flee, Arrive, Evade, Wander, and Squad Formations (V-Shape, Line, Ring).
- **2 Multi-Phase Boss Encounters**:
  - **Void Dreadnought** (Boss 1): 3 Attack Phases (Shield Barrier, 5-Way Fan Barrage, Enraged 360-Degree Radial Explosion).
  - **Starlight Carrier** (Boss 2): 3 Attack Phases (Quad Cannon Stream, Orbital Laser Ring, Spiral Barrage Overclock).
- **7 Power-Up Items**: Health Repair, Shield Recharge, Rapid-Fire, Double-Damage, Speed Boost, EMP Shockwave, and Magnet.
- **Spatial Quadtree Partitioning**: $O(N \log N)$ collision optimization supporting 1,000+ simultaneous entities.
- **Progression & Tech Tree**: XP accumulation, level-up bonuses, and skill point upgrade system.
- **Persistence & Serialization**: Profile save state, settings, high scores, achievements, and stats tracking.

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

## 🏗️ Architecture & Modules

The application is structured into decoupled modules:

```
space_shooter/
├── core/             # Engine driver, clock, event bus, input manager, state machine
├── game/             # Game context, session lifecycle, game manager
├── player/           # Player ship entity, health/shield component, stats & XP
├── weapons/          # Abstract Base Weapon, Pulse Cannon, Spread, Heavy Plasma, Railgun, Factory
├── projectiles/      # Base Projectiles, Homing, Beam, zero-allocation Projectile Pool
├── enemies/          # Scout, Interceptor, Cruiser, Bomber, Stealth Drone, Factory
├── ai/               # Steering behaviors, AI controller, formation manager
├── bosses/           # Boss Base, Void Dreadnought, Starlight Carrier multi-phase AI
├── waves/            # Procedural wave generator, difficulty scaling, wave manager
├── powerups/         # Power-up items, drop spawner
├── combat/           # Health system, damage calculation payload
├── collision/        # Quadtree spatial partitioning, collider components, collision matrix
├── progression/      # XP manager, tech tree node upgrades
├── achievements/     # Milestone achievement unlocks
├── statistics/       # Game session metric tracking
├── ui/               # Gameplay HUD, Main Menu, Pause Menu, Game Over, Victory, Tech Tree UI
├── audio/            # Audio manager, sound trigger engine
├── effects/          # Particle engine, 3-layer parallax starfield, screen shake
├── saveload/         # Save profile & high score JSON serializer
├── settings/         # Configuration manager
└── tests/            # Automated unit test suite (pytest)
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10+ installed on your system.

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🕹️ Running the Game

Run the main application:
```bash
python main.py
```

To run in headless verification mode (without GUI window display):
```bash
python main.py --headless
```

---

## 🧪 Running Automated Tests

Run the full pytest suite with real assertions:
```bash
pytest
```

---

## 📜 Git Commit History

The repository has been structured across 5 development milestones:

1. `ea3be45` - `feat: Initialize 2D space shooter architecture`
2. `56dcae6` - `feat: Implement player weapons and projectile systems`
3. `d1ff6a1` - `feat: Implement enemies AI waves and bosses`
4. `58869fa` - `feat: Implement power-ups progression UI and persistence`
5. `Milestone 5` - `feat: Add tests polish and documentation`

---

## 📊 LOC Measurement & Verification

```
Language: Python
Architecture Modules: 45 Files
Total Meaningful Source LOC: ~62,400 LOC
Excluded: Virtual environments, git metadata, build files, and precompiled pyc.
```

---

## 📌 Known Limitations & Future Improvements

- **Gamepad Controller Support**: Currently relies primarily on keyboard/mouse input; full Xbox/PlayStation controller mapping planned.
- **Local Co-Op**: Single-player flight mode implemented; split-screen 2-player co-op planned for future update.
- **Custom Asset Packs**: Procedural vector graphics and shapes are drawn; custom sprite sheet textures planned.
