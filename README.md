# 9GAMES [BETA]

![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/library-pygame-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active%20development-orange?style=for-the-badge)

> **9GAMES** is a collection of 2D pixel-art mini-games made with Pygame. Right now it has two games: **Los Santos** and **Alley Berserk**. Start them from a launcher window and play in a game window.

---

## Games

### Los Santos (thief vs. police) [BETA]
You play a thief in the city. Collect all **20 coins** while a police officer chases you across the map. If the police catch you, it's **BUSTED**.

- The police follow you all the time, but you are a little faster (5 vs. 4 pixels per frame).
- Collect all 20 coins to win.

### Alley Berserk [BETA]
A dark alley with a hooded, masked fighter who carries an axe. Walk around the alley and swing the axe with the mouse.

---

## Controls

| Key / Button | Action |
|---|---|
| `W` `A` `S` `D` | Move |
| Left mouse button | Attack (Alley Berserk) |
| `Q` | Continue after BUSTED (Los Santos) |
| `E` | Exit after YOU WON (Los Santos) |

---

## Features

- **Sprite animation:** walk and attack frames loaded from folders and played in order.
- **Collision detection:** coin pickup and police catch using `pygame.Rect`.
- **Game states:** playing, `BUSTED`, and `YOU WON` screens, with a blurred background and a dark overlay.
- **Audio:** background music with `pygame.mixer`, paused on BUSTED and a separate sound on win.
- **Transparent sprites:** colorkey and alpha transparency for characters and coins.

---

## Requirements

- Python 3.10 or newer
- `pygame` (or `pygame-ce`)
- `customtkinter` and `Pillow` (for the launcher window)

---

## Install

```bash
git clone https://github.com/ScuizzyBytes/Los-Santos-Mini-Game.git
cd Los-Santos-Mini-Game
```

On Ubuntu, `pip install` outside a virtual environment gives an `externally-managed-environment` error. Use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame-ce customtkinter pillow
```

## Run

Start the game **from the project folder**, because the images and sounds use relative paths:

```bash
python main.py
```

If you get `FileNotFoundError` or you can't see images, check two things:
1. You started the program from the project folder (`pwd` shows where you are).
2. The file names match exactly. Ubuntu is case-sensitive, so `Icon.png` and `icon.png` are different files.

---

## Project structure

```
Los-Santos-Mini-Game/
├── main.py        # launcher
├── games/         # the two games: Los Santos and Alley Berserk
├── assests/       # images and sounds
├── .gitignore
└── README.md
```

---

## Status

Both games are in **beta**. Things are still changing, so you may find bugs.

## License

MIT
