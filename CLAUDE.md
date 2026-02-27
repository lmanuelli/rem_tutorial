# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install all dependencies (including dev extras like ipython)
uv sync --extra dev

# Run a script
uv run python -m rem.examples.hello_world

# Interactive Python shell
uv run ipython

# Check the installed package version
uv run python -c "import rem; print(rem.__version__)"

# Format all source code
uv run black src/

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_imports.py
```

## Before Committing

Always run these two commands before committing, and ensure both pass:

```bash
uv run black src/
uv run pytest
```

## Writing Tests

Add tests for any new code you write. Test files live in `tests/` and must be named `test_*.py`. Each test is a plain function named `test_*` — no classes needed.

## Architecture

This is a `src/` layout Python package. The package root is `src/rem/`; all new modules go under there. The `src/` layout means the package is only importable after `uv sync` installs it — never import directly from the project root.

**Adding a new example:** create a file under `src/rem/examples/`, give it a `main()` function and an `if __name__ == "__main__": main()` guard, then run it with `uv run python -m rem.examples.<name>`.

**Adding a dependency:** add it to the `dependencies` list in `pyproject.toml`, then run `uv sync` to update the lockfile.

**Dev dependencies** (tools for development, not needed by the package itself) go in `[project.optional-dependencies] dev`.
