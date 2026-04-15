# Contributing guide

## Installation

```bash
uv sync --extra dev
uv run pre-commit install
```

## Running tests

```bash
uv run pytest -v
```

## Development conventions

- Use conventional commits
    - `feat:` new feature
    - `fix:` bug fix
    - `chore:` maintenance
    - `test:` tests
- Add tests for new features with `pytest`
- Keep functions simple and minimal
- Linter: `ruff check --fix`
- Formatter: `ruff format`

## Layered architecture

```
src/cyrano/
├── io.py                        # File I/O (FCS reading)
├── services/                    # Business logic (shared between CLI and GUI)
│   ├── summarize_fcs.py         # FCS summary, channel extraction, well extraction
│   └── analyze_plate.py         # 96-well plate scanning and heatmap plotting
├── cli/                         # CLI layer (click commands)
│   ├── main.py                  # Entry point, click group
│   ├── explore.py               # cyrano explore
│   ├── compare.py               # cyrano compare
│   └── analyze.py               # cyrano analyze
└── gui/                         # GUI layer (Streamlit)
    ├── app.py                   # Entry point, tab routing
    ├── explore.py               # Explore tab
    ├── compare.py               # Compare tab
    └── analyze.py               # Analyze tab
```

The key principle: **services** contain all shared logic. CLI and GUI are thin presentation layers that call into services. When adding a new feature, start by implementing it in services, then wire it into both CLI and GUI.