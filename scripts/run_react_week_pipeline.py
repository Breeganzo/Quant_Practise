from __future__ import annotations

import argparse
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class CommandResult:
    command: str
    return_code: int
    stdout: str
    stderr: str


@dataclass
class WeekAgentResult:
    week: str
    observe: dict[str, object]
    reason: dict[str, object]
    act: list[dict[str, object]]
    verify: dict[str, object]
    status: str


def run_command(command: list[str], cwd: Path) -> CommandResult:
    process = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    return CommandResult(
        command=" ".join(command),
        return_code=process.returncode,
        stdout=process.stdout,
        stderr=process.stderr,
    )


def weekday_lesson_paths(root: Path, week: str) -> list[Path]:
    week_dir = root / "curriculum" / "weeks" / week
    return [week_dir / f"day-{day_no:02d}" / "lesson.md" for day_no in range(1, 6)]


def observe_week(root: Path, week: str) -> dict[str, object]:
    lessons = weekday_lesson_paths(root, week)
    existing_lessons = sum(1 for path in lessons if path.exists())
    extension_present = 0
    solved_problem_4_present = 0

    for lesson in lessons:
        if not lesson.exists():
            continue
        text = lesson.read_text(encoding="utf-8")
        if "## 2-Hour Extension Track (Required)" in text:
            extension_present += 1
        if "### Solved Problem 4" in text:
            solved_problem_4_present += 1

    notebook_dir = root / "notebooks" / week
    notebook_count = len(list(notebook_dir.glob("*.ipynb"))) if notebook_dir.exists() else 0

    return {
        "weekday_lessons_found": existing_lessons,
        "extension_present": extension_present,
        "solved_problem_4_present": solved_problem_4_present,
        "notebooks_found": notebook_count,
    }


def reason_week(observe: dict[str, object]) -> dict[str, object]:
    gaps: list[str] = []
    if observe["weekday_lessons_found"] != 5:
        gaps.append("missing_weekday_lessons")
    if observe["extension_present"] != 5:
        gaps.append("missing_6h_extension")
    if observe["solved_problem_4_present"] != 5:
        gaps.append("missing_solved_problem_4")
    if observe["notebooks_found"] < 8:
        gaps.append("missing_week_notebooks")

    return {
        "gaps": gaps,
        "ready_for_act": len(gaps) == 0,
    }


def verify_week(root: Path, week: str) -> dict[str, object]:
    lessons = weekday_lesson_paths(root, week)
    extension_ok = 0
    solved_problem_ok = 0

    for lesson in lessons:
        if not lesson.exists():
            continue
        text = lesson.read_text(encoding="utf-8")
        if "## 2-Hour Extension Track (Required)" in text and "6-hour" in text.lower():
            extension_ok += 1
        if "### Solved Problem 4" in text:
            solved_problem_ok += 1

    report_path = root / "data" / "processed" / "reports" / f"{week}-notebooks.json"
    notebook_failures = None
    if report_path.exists():
        report = json.loads(report_path.read_text(encoding="utf-8"))
        notebook_failures = int(report.get("failed", 0))

    return {
        "extension_ok": extension_ok,
        "solved_problem_4_ok": solved_problem_ok,
        "notebook_report_found": report_path.exists(),
        "notebook_failures": notebook_failures,
    }


def run_week_agent(
    root: Path,
    week: str,
    execute_notebooks: bool,
    export_assets: bool,
) -> WeekAgentResult:
    observe = observe_week(root, week)
    reason = reason_week(observe)
    act_results: list[dict[str, object]] = []

    base_commands: list[list[str]] = [
        ["uv", "run", "python", "scripts/enhance_weekday_lessons.py", "--week", week],
        ["uv", "run", "python", "scripts/generate_all_week_notebooks.py", "--week", week],
    ]

    if execute_notebooks:
        base_commands.append(
            [
                "uv",
                "run",
                "python",
                "scripts/run_notebooks.py",
                "--week",
                week,
                "--continue-on-error",
                "--write-report",
                f"data/processed/reports/{week}-notebooks.json",
            ]
        )

    if export_assets:
        base_commands.append(
            [
                "uv",
                "run",
                "python",
                "scripts/export_assets.py",
                "--week",
                week,
                "--write-manifest",
                f"data/processed/reports/{week}-exports.json",
            ]
        )

    for command in base_commands:
        result = run_command(command, cwd=root)
        act_results.append(asdict(result))
        if result.return_code != 0:
            verify = verify_week(root, week)
            return WeekAgentResult(
                week=week,
                observe=observe,
                reason=reason,
                act=act_results,
                verify=verify,
                status="failed",
            )

    verify = verify_week(root, week)
    status = "passed"
    if verify["extension_ok"] != 5 or verify["solved_problem_4_ok"] != 5:
        status = "failed"
    if verify["notebook_failures"] not in (None, 0):
        status = "failed"

    return WeekAgentResult(
        week=week,
        observe=observe,
        reason=reason,
        act=act_results,
        verify=verify,
        status=status,
    )


def parse_weeks(weeks: str) -> list[str]:
    if weeks == "all":
        return [f"week-{week_no:02d}" for week_no in range(1, 25)]

    out: list[str] = []
    for part in weeks.split(","):
        token = part.strip()
        if not token:
            continue
        if token.startswith("week-"):
            out.append(token)
            continue
        week_no = int(token)
        out.append(f"week-{week_no:02d}")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ReAct-style week agents over curriculum pipeline")
    parser.add_argument(
        "--weeks",
        type=str,
        default="all",
        help="all or comma-separated list like week-01,week-02 or 1,2",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=24,
        help="Maximum concurrent week agents",
    )
    parser.add_argument(
        "--skip-execute",
        action="store_true",
        help="Skip notebook execution step",
    )
    parser.add_argument(
        "--skip-export",
        action="store_true",
        help="Skip export step",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    (root / "data" / "processed" / "reports").mkdir(parents=True, exist_ok=True)

    weeks = parse_weeks(args.weeks)
    results: list[WeekAgentResult] = []

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map = {
            executor.submit(
                run_week_agent,
                root,
                week,
                not args.skip_execute,
                not args.skip_export,
            ): week
            for week in weeks
        }

        for future in as_completed(future_map):
            week = future_map[future]
            result = future.result()
            results.append(result)
            print(f"[{result.status.upper()}] {week}")

    results.sort(key=lambda item: item.week)
    payload = {
        "weeks": weeks,
        "workers": args.workers,
        "skip_execute": args.skip_execute,
        "skip_export": args.skip_export,
        "passed": sum(1 for item in results if item.status == "passed"),
        "failed": sum(1 for item in results if item.status == "failed"),
        "results": [asdict(item) for item in results],
    }

    report_path = root / "data" / "processed" / "react_week_pipeline_report.json"
    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Pipeline report written: {report_path.relative_to(root)}")

    if payload["failed"]:
        raise SystemExit(f"Week pipeline completed with failures: {payload['failed']}")


if __name__ == "__main__":
    main()
