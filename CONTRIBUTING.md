# Contributing guide

## Installation

- `uv sync --extra dev`
- `uv run pre-commit install`

## Development convention

- Use conventional commits
    - feat: new feature
    - fix: bug fix
    - chore: maintenance
    - test: tests
- Add tests for new features with `pytest`
- Keep functions simple
- Linter :
    ```ruff check --fix            # Lint files in the current directory and fix any fixable errors.```
- Formatter :
    ```ruff format                 # Format all files in the current directory.```
