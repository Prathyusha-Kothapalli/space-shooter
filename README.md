# Starlight Vanguard - 2D Space Shooter

A complete, high-performance **2D Space Shooter & Galactic Roguelite Engine** built with clean, modular architecture, spatial quadtree & spatial hash physics, multi-phase boss encounters, weapon upgrade trees, AI behavior trees, software audio synthesizer, procedural starmap generator, item crafting system, and 13 automated unit tests.

---

## 🚀 Game Overview

**Starlight Vanguard** is an arcade space shooter and galactic roguelite where players command a customizable fleet of battlecraft against alien armadas and colossal flagship bosses across procedurally generated galactic sectors.

---

## ✨ Key Features & Expansion Systems

- **50+ Playable Spaceship Chassis**: Interceptors, Dreadnoughts, Stealth Phantoms, Carriers, Plasma Corsairs, Solar Cruisers, and Titan Gunships.
- **60+ Weapon Systems**: Pulse Cannons, Spread Shot, Heavy Plasma, Homing Missiles, Quantum Railguns, Beam Rays, and Singularity Void Cannons.
- **60+ Alien Enemy Craft**: Scouts, Interceptors, Cruisers, Plasma Bombers, Stealth Drones, Precision Snipers, and Shield Generator Drones.
- **20 Flagship Boss Encounters**: Multi-phase attack patterns, enraged states, drone spawn definitions.
- **AI Behavior Trees**: Selector, Sequence, Inverter, Condition, and Action nodes driving complex squad tactics (Pincher attacks, Flanking, Sacrificial Drones).
- **Procedural Sector Starmap Generator**: Multi-column branching sector navigation graph (Combat, Elite, Boss, Shop, Random Event, Black Market, Repair Station).
- **Interactive Narrative Encounters**: Text event decision scenarios with risk/reward choices, resource trades, and random outcomes.
- **Procedural Software Audio Synthesizer**: Math-based sound generator producing PCM sample buffers (Sine, Square, Sawtooth, Triangle, White Noise) for 60+ sound effects.
- **Item Crafting & Module Socketing Engine**: Blueprint recipes, component dismantling, and socketable stat-boosting ship modules.
- **Dual Physics Engine**: Separating Axis Theorem (SAT), Spatial Quadtree partitioning ($O(N \log N)$), GJK/EPA Narrowphase & Spatial Hash Grid ($O(1)$) with 2D Raycasting and 2D RigidBody dynamics.
- **18 UI State Scenes**: Main Menu, Gameplay HUD, Pause Overlay, Game Over, Victory, Tech Tree, Codex, Inventory, Shop, Sector Map, Achievements, Statistics, Crafting Workbench, Bounty Contracts, Fleet Hangar, Settings.

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

## 🛠️ Installation & Dependency Lockfiles

### Installation via Manifest or Lockfile
```bash
# Option A: Standard Manifest Installation
pip install -r requirements.txt

# Option B: Pinned Lockfile Installation
pip install -r requirements.lock
```

### Run the Desktop Game Engine
```bash
python main.py
```

### Run the Web Server (Browser Interface at http://localhost:8000)
```bash
python server.py
```

### Run Headless Verification Mode
```bash
python main.py --headless
```

### Run Automated Tests (13 Test Cases across Pytest/Unittest)
```bash
pytest
# OR
python -m unittest discover tests
```

---

## 🏗️ Codebase Metrics (53,000+ LOC)
- **Primary Language**: Python 3.10+
- **Source LOC**: 53,000+ lines of clean, structured code
- **Automated Tests**: 13 test cases across 10 test modules (100% passing)
- **Dependency Files**: `requirements.txt` (manifest), `requirements.lock` & `Pipfile.lock` (lockfiles)
- **Test Configs**: `pytest.ini`, `.coveragerc`, `tox.ini`
