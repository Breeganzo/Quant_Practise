from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


EXTENSION_HEADING = "## 2-Hour Extension Track (Required)"
REFLECTION_HEADING = "## Reflection Question"
CODING_HEADING = "## Coding Walkthrough"
SOLVED_PROBLEM_4_HEADING = "### Solved Problem 4: Position sizing with volatility guardrail"


@dataclass
class LessonUpdate:
    path: Path
    extension_added: bool = False
    solved_problem_added: bool = False


def iter_weekday_lessons(root: Path, week: str) -> list[Path]:
    weeks_root = root / "curriculum" / "weeks"
    week_dirs: list[Path] = []
    if week == "all":
        week_dirs = sorted(weeks_root.glob("week-*"))
    else:
        week_path = weeks_root / week
        if not week_path.exists():
            raise SystemExit(f"Week folder not found: {week}")
        week_dirs = [week_path]

    out: list[Path] = []
    for week_dir in week_dirs:
        for day_no in range(1, 6):
            lesson_path = week_dir / f"day-{day_no:02d}" / "lesson.md"
            if lesson_path.exists():
                out.append(lesson_path)
    return out


def week_day_from_path(path: Path) -> tuple[int, int]:
    week_match = re.search(r"week-(\d{2})", str(path))
    day_match = re.search(r"day-(\d{2})", str(path))
    if not week_match or not day_match:
        return 0, 0
    return int(week_match.group(1)), int(day_match.group(1))


def extension_block(week_no: int, day_no: int) -> str:
    return "\n".join(
        [
            EXTENSION_HEADING,
            "",
            "This section upgrades the day to a full 6-hour study model: 4-hour core lesson + 2-hour required extension.",
            "",
            "- **Extension Block A (45 min):** Real-market case expansion.",
            "  - Re-run today's workflow on one additional asset and one stress regime window.",
            "  - Document one regime-specific failure mode and one mitigation rule.",
            "- **Extension Block B (45 min):** Production-quality coding refinement.",
            "  - Add one assertion for data integrity and one assertion for risk limits.",
            "  - Save a short result table with assumptions, metric values, and decision rationale.",
            "- **Extension Block C (30 min):** Interview simulation and review.",
            "  - Deliver a 60-second PM pitch and a 60-second risk-manager response.",
            "  - Include one numeric example from Week "
            f"{week_no:02d} Day {day_no:02d} to prove notation fluency.",
            "",
            "Extension completion checks:",
            "- [ ] Stress-regime comparison completed",
            "- [ ] Production guardrail assertions added and passed",
            "- [ ] Interview simulation recorded with one numeric example",
            "",
        ]
    )


def solved_problem_4_block(week_no: int, day_no: int) -> str:
    vol = 0.16 + week_no * 0.002 + day_no * 0.001
    target_vol = 0.20
    position_multiplier = target_vol / vol
    clipped = min(1.0, max(0.2, position_multiplier))
    return "\n".join(
        [
            SOLVED_PROBLEM_4_HEADING,
            "Given:",
            f"- Strategy annualized volatility estimate is {vol:.3f}.",
            f"- Portfolio risk budget target is {target_vol:.2f}.",
            "- Position multiplier rule: scale = target_vol / strategy_vol, clipped to [0.20, 1.00].",
            "Solution:",
            "1. Compute raw scale = target_vol / strategy_vol.",
            f"2. raw_scale = {target_vol:.2f}/{vol:.3f} = {position_multiplier:.4f}.",
            f"3. clipped_scale = min(1.00, max(0.20, {position_multiplier:.4f})) = {clipped:.4f}.",
            f"Final answer: Position multiplier = {clipped:.4f}.",
            "Common trap: Ignoring volatility regime shifts and applying static position size in stressed markets.",
            "Interpretation: State how this guardrail changes gross exposure before deployment.",
            "",
        ]
    )


def ensure_extension(text: str, week_no: int, day_no: int) -> tuple[str, bool]:
    if EXTENSION_HEADING in text:
        return text, False

    block = extension_block(week_no, day_no)
    if REFLECTION_HEADING in text:
        return text.replace(REFLECTION_HEADING, block + REFLECTION_HEADING, 1), True

    return text.rstrip() + "\n\n" + block, True


def ensure_solved_problem_4(text: str, week_no: int, day_no: int) -> tuple[str, bool]:
    if SOLVED_PROBLEM_4_HEADING in text or "### Solved Problem 4" in text:
        return text, False

    block = solved_problem_4_block(week_no, day_no)
    if CODING_HEADING in text:
        return text.replace(CODING_HEADING, block + CODING_HEADING, 1), True

    return text.rstrip() + "\n\n" + block, True


def update_lesson(path: Path, dry_run: bool) -> LessonUpdate:
    week_no, day_no = week_day_from_path(path)
    original = path.read_text(encoding="utf-8")

    updated = original
    updated, extension_added = ensure_extension(updated, week_no, day_no)
    updated, solved_problem_added = ensure_solved_problem_4(updated, week_no, day_no)

    if updated != original and not dry_run:
        path.write_text(updated, encoding="utf-8")

    return LessonUpdate(
        path=path,
        extension_added=extension_added,
        solved_problem_added=solved_problem_added,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Enhance weekday lessons for 6-hour model and depth gates")
    parser.add_argument("--week", type=str, default="all", help="Target week (e.g. week-01) or all")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    lesson_paths = iter_weekday_lessons(root, args.week)

    updates = [update_lesson(path, dry_run=args.dry_run) for path in lesson_paths]

    report = {
        "target": args.week,
        "total_weekday_lessons": len(updates),
        "extension_added": sum(1 for u in updates if u.extension_added),
        "solved_problem_4_added": sum(1 for u in updates if u.solved_problem_added),
        "dry_run": args.dry_run,
        "updated_files": [
            str(u.path.relative_to(root))
            for u in updates
            if u.extension_added or u.solved_problem_added
        ],
    }

    report_path = root / "data" / "processed" / "lesson_enhancement_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    print(f"Report written: {report_path.relative_to(root)}")


if __name__ == "__main__":
    main()
