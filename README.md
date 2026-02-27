# rem — Python Tutorial Project

A sandbox Python project for learning modern Python development.

---

## Prerequisites

You need two things installed on your machine before anything else:

1. **Python 3.11+** — Install via [Homebrew](https://brew.sh) (recommended on Mac):

   First, install Homebrew if you don't have it (paste this into Terminal):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Then install Python:
   ```bash
   brew install python
   ```

   Verify the installation:
   ```bash
   python3 --version
   ```
   You should see something like `Python 3.13.x`. As long as it's 3.11 or higher, you're good.

2. **uv** — A fast Python package manager. Install it by running this in your terminal:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Full instructions: [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)

---

## Setup

Clone (or download) this project, then open a terminal in the `rem_tutorial/` folder and run:

```bash
uv sync --extra dev
```

This reads `pyproject.toml`, creates a virtual environment in `.venv/`, and installs all dependencies (NumPy, Pandas, Matplotlib, and IPython). You only need to do this once — or again whenever dependencies change.

---

## Running Examples

Run any example script with `uv run`. You don't need to "activate" the virtual environment — `uv run` handles that automatically.

```bash
uv run python -m rem.examples.hello_world
```

Expected output:
```
Hello, world!
Data array: [10 20 30 40 50]
Mean of data: 30.0
```

---

## Interactive Python

For open-ended exploration, launch an interactive IPython shell:

```bash
uv run ipython
```

IPython is like the standard Python prompt but with tab-completion, syntax highlighting, and easy access to help (type `?` after any object).

Example session:
```python
In [1]: import numpy as np
In [2]: np.array([1, 2, 3]).mean()
Out[2]: 2.0
```

Type `exit` or press `Ctrl-D` to quit.

---

## Project Structure

```
rem_tutorial/
├── pyproject.toml          # Project config: name, version, dependencies
├── README.md               # This file
└── src/
    └── rem/                # The 'rem' package (your code lives here)
        ├── __init__.py     # Marks 'rem' as a package; holds __version__
        └── examples/       # Runnable example scripts
            ├── __init__.py
            └── hello_world.py
```

- **`pyproject.toml`** is the single source of truth for the project. No `requirements.txt` needed.
- **`src/` layout** keeps your package code separate from project-level files, preventing accidental imports.
- **`uv run`** always uses the project's own environment, so you never have to worry about which Python is active.
