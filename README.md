# 🌴 Los Santos Mini Game (Pygame Edition)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Library-Pygame-green?style=for-the-badge&logo=pygame)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=for-the-badge)

> **High-octane arcade action right in your terminal.** Evade the LAPD, grab as many coins as possible, and escape before you get busted!

---

## 🎮 Game Overview

**Los Santos** is a fast-paced 2D arcade mini-game built with **Pygame**. You play as a thief navigating the urban sprawl of Los Santos. Your goal is simple: gather all the coins scattered across the map while evading relentless police patrols.

---

## 🔥 Key Technical Features

* **Dynamic Asset Processing:** Clean programmatic sprite manipulation using `pygame.PixelArray` and `map_rgb()` to isolate, strip multi-color backgrounds, and recolor internal highlights on the fly.
* **Full Inventory & Reset Logic:** Real-time collision detection handling coin collection, inventory clearing, and state resets (`Busted` vs `Win`).
* **Randomized Spawns:** Procedural coordinate distribution for stars/coins across custom map boundaries.
* **Audio System:** Integrated background music using `pygame.mixer` with state-based pause/unpause controls.

---

## 🚀 Quick Start (Launch in 30 seconds)

### 1. Clone the repository
```bash
git clone [https://github.com/ScuizzyBytes/Los-Santos-Mini-Game.git](https://github.com/ScuizzyBytes/Los-Santos-Mini-Game.git)
cd Los-Santos-Mini-Game
