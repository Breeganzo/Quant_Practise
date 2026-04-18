from __future__ import annotations

import argparse
import os
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbformat.validator import normalize


def collect_notebooks(root: Path, week: str | None) -> list[Path]:
    notebook_root = root / "notebooks"
    if week:
        paths = sorted((notebook_root / week).glob("*.ipynb"))
    else:
        paths = sorted(notebook_root.glob("week-*/**/*.ipynb"))
    return [p for p in paths if ".ipynb_checkpoints" not in str(p)]


def execute_notebook(path: Path, timeout: int = 900) -> None:
    with path.open("r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Ensure notebook metadata/cell IDs are normalized for stable execution.
    _changes, nb = normalize(nb)

    client = NotebookClient(nb, timeout=timeout, kernel_name="python3")
    client.execute()

    with path.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)


def main() -> None:
    # Use a non-interactive backend so notebook plots execute reliably in headless runs.
    os.environ.setdefault("MPLBACKEND", "Agg")

    parser = argparse.ArgumentParser(description="Execute notebooks for one week or all weeks.")
    parser.add_argument("--week", type=str, default="week-01", help="Week folder name, e.g. week-01")
    parser.add_argument("--all", action="store_true", help="Execute every notebook under notebooks/")
    parser.add_argument("--timeout", type=int, default=900, help="Notebook cell execution timeout")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    week = None if args.all else args.week
    notebooks = collect_notebooks(root, week)

    if not notebooks:
        raise SystemExit("No notebooks found for the selected target.")

    print(f"Executing {len(notebooks)} notebook(s)...")
    for nb_path in notebooks:
        print(f"- Running {nb_path.relative_to(root)}")
        execute_notebook(nb_path, timeout=args.timeout)

    print("Notebook execution completed successfully.")


if __name__ == "__main__":
    main()
