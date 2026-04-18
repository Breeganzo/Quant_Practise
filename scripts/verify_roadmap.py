from __future__ import annotations

import json
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    curriculum_index = root / "curriculum" / "curriculum-index.json"
    web_curriculum_index = root / "web" / "public" / "data" / "curriculum.json"

    if not curriculum_index.exists():
        fail("Missing curriculum/curriculum-index.json")
    if not web_curriculum_index.exists():
        fail("Missing web/public/data/curriculum.json")

    index = json.loads(curriculum_index.read_text(encoding="utf-8"))
    weeks = index.get("weeks", [])
    if len(weeks) != 24:
        fail(f"Expected 24 weeks, found {len(weeks)}")

    missing_lessons = 0
    duration_issues: list[str] = []

    for week in weeks:
        week_no = week.get("week")
        days = week.get("days", [])
        if len(days) != 7:
            fail(f"Week {week_no} does not have 7 days")

        for day in days:
            day_no = day.get("day")
            expected_hours = 4 if day_no <= 5 else 2
            if day.get("durationHours") != expected_hours:
                duration_issues.append(
                    f"week-{week_no:02d} day-{day_no:02d} has {day.get('durationHours')}h"
                )

            lesson_path = root / "web" / "public" / day.get("lessonPath", "")
            if not lesson_path.exists():
                missing_lessons += 1

    if duration_issues:
        fail("Duration mismatches: " + "; ".join(duration_issues[:10]))

    if missing_lessons:
        fail(f"Missing lesson markdown files in web/public/content: {missing_lessons}")

    notebooks = sorted((root / "notebooks").glob("week-*/week-*-learning.ipynb"))
    if len(notebooks) != 24:
        fail(f"Expected 24 learning notebooks, found {len(notebooks)}")

    web_notebooks = sorted((root / "web" / "public" / "notebooks").glob("week-*/*.ipynb"))
    if len(web_notebooks) != 24:
        fail(f"Expected 24 web notebook assets, found {len(web_notebooks)}")

    print("[OK] Validation passed")
    print(f"weeks={len(weeks)}")
    print("durations=weekday-4h/weekend-2h")
    print(f"web_lessons={168 - missing_lessons}")
    print(f"notebooks={len(notebooks)}")
    print(f"web_notebooks={len(web_notebooks)}")


if __name__ == "__main__":
    main()
