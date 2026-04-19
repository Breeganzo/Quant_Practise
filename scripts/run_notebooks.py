from __future__ import annotations

import argparse
import json
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


def execute_with_report(path: Path, timeout: int) -> dict[str, object]:
    record: dict[str, object] = {
        "notebook": str(path),
        "status": "passed",
        "error": None,
    }
    try:
        execute_notebook(path, timeout=timeout)
    except Exception as exc:  # pragma: no cover - runtime failures depend on env/data
        record["status"] = "failed"
        record["error"] = str(exc)
    return record


def main() -> None:
    # Use a non-interactive backend so notebook plots execute reliably in headless runs.
    os.environ.setdefault("MPLBACKEND", "Agg")

    parser = argparse.ArgumentParser(description="Execute notebooks for one week or all weeks.")
    parser.add_argument("--week", type=str, default="week-01", help="Week folder name, e.g. week-01")
    parser.add_argument("--all", action="store_true", help="Execute every notebook under notebooks/")
    parser.add_argument("--timeout", type=int, default=900, help="Notebook cell execution timeout")
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue executing remaining notebooks when one fails",
    )
    parser.add_argument(
        "--write-report",
        type=str,
        default="",
        help="Optional path to write JSON execution report",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    week = None if args.all else args.week
    notebooks = collect_notebooks(root, week)

    if not notebooks:
        raise SystemExit("No notebooks found for the selected target.")

    print(f"Executing {len(notebooks)} notebook(s)...")
    report: dict[str, object] = {
        "target": "all" if args.all else args.week,
        "timeout": args.timeout,
        "total": len(notebooks),
        "passed": 0,
        "failed": 0,
        "results": [],
    }

    for nb_path in notebooks:
        print(f"- Running {nb_path.relative_to(root)}")
        result = execute_with_report(nb_path, timeout=args.timeout)
        report["results"].append(result)
        if result["status"] == "passed":
            report["passed"] += 1
            continue

        report["failed"] += 1
        if not args.continue_on_error:
            if args.write_report:
                report_path = Path(args.write_report)
                if not report_path.is_absolute():
                    report_path = root / report_path
                report_path.parent.mkdir(parents=True, exist_ok=True)
                report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
            raise SystemExit(f"Notebook execution failed: {result['notebook']}: {result['error']}")

    if args.write_report:
        report_path = Path(args.write_report)
        if not report_path.is_absolute():
            report_path = root / report_path
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Execution report written to {report_path.relative_to(root)}")

    if report["failed"]:
        raise SystemExit(f"Notebook execution completed with failures: {report['failed']}")

    print("Notebook execution completed successfully.")


if __name__ == "__main__":
    main()
