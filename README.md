# rem — Python Tutorial Project

A sandbox Python project for learning modern Python development.

> **New here?** Follow these steps in order:
> 1. [Prerequisites](#prerequisites) — install Git, Python, and uv
> 2. [Getting the Code](#getting-the-code) — clone the repository to your machine
> 3. [Setup](#setup) — install project dependencies

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running Examples](#running-examples)
- [Interactive Python](#interactive-python)
- [Formatting](#formatting)
- [Project Structure](#project-structure)
- [Getting the Code](#getting-the-code)

---

## Prerequisites

You need three things installed on your machine before anything else:

1. **Git** — Install via [Homebrew](https://brew.sh) (recommended on Mac):

   First, install Homebrew if you don't have it (paste this into Terminal):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Then install Git:
   ```bash
   brew install git
   ```

   Verify the installation:
   ```bash
   git --version
   ```
   You should see something like `git version 2.x.x`.

2. **Python 3.11+** — Install via Homebrew:

   ```bash
   brew install python
   ```

   Verify the installation:
   ```bash
   python3 --version
   ```
   You should see something like `Python 3.13.x`. As long as it's 3.11 or higher, you're good.

3. **uv** — A fast Python package manager. Install it by running this in your terminal:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Full instructions: [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)

---

## Setup

Once you have the code (see [Getting the Code](#getting-the-code)), open a terminal in the `rem_tutorial/` folder and run:

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

## Formatting

This project uses [Black](https://black.readthedocs.io/) to automatically format code to a consistent style.

**Run it manually** from the `rem_tutorial/` folder:

```bash
uv run black src/
```

Black will reformat any files that need changes and tell you what it touched.

**In VSCode** — formatting happens automatically on every save. The first time you open the project, VSCode will prompt you to install the recommended extensions; accept the prompt and install the **Black Formatter** extension (`ms-python.black-formatter`). After that, just save a file (`Cmd-S`) and Black will tidy it up instantly.

You can also trigger formatting manually at any time with `Shift-Alt-F` (or `Shift-Option-F` on Mac).

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

---

## Getting the Code

### 1. Set up SSH authentication with GitHub

Cloning over SSH is the recommended approach. If you haven't done this before, follow GitHub's official guide:

[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

The guide walks you through creating a key pair and uploading the public key to your GitHub account. You only need to do this once per machine.

### 2. Clone the repository

Navigate to the folder where you'd like to keep the project (e.g. your home directory or a `projects/` folder), then run:

```bash
git clone git@github.com:lmanuelli/rem_tutorial.git
```

This creates a `rem_tutorial/` folder with all the code inside. Then:

```bash
cd rem_tutorial
```

From here, continue with [Setup](#setup).
