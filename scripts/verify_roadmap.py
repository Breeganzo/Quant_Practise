from __future__ import annotations

import json
from pathlib import Path


REQUIRED_WEEKDAY_SECTIONS = [
    "## 5-Block Daily Structure",
    "## Mathematical Foundations (LaTeX)",
    "## Symbol Definitions",
    "## Real Trading Example",
    "## Step-by-Step Solved Problems",
    "## Coding Walkthrough",
]

REQUIRED_ALL_DAYS_SECTIONS = ["## Continuity and Handoff"]

REQUIRED_WEEK_RESOURCE_KEYS = [
    "notebookPath",
    "overviewPath",
    "quizPath",
    "revisionChecklistPath",
    "miniProjectPath",
]

REQUIRED_CONTINUITY_KEYS = [
    "previousLabel",
    "previousLessonPath",
    "todayDeliverable",
    "nextLabel",
    "nextLessonPath",
]


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
    content_issues: list[str] = []
    checked_weekday_lessons = 0

    for week in weeks:
        week_no = week.get("week")
        days = week.get("days", [])
        if len(days) != 7:
            fail(f"Week {week_no} does not have 7 days")

        resources = week.get("resources")
        if not isinstance(resources, dict):
            content_issues.append(f"week-{week_no:02d} missing resources block")
        else:
            for key in REQUIRED_WEEK_RESOURCE_KEYS:
                path_value = resources.get(key)
                if not isinstance(path_value, str) or not path_value.strip():
                    content_issues.append(f"week-{week_no:02d} missing resource key: {key}")
                    continue
                resource_path = root / "web" / "public" / path_value
                if not resource_path.exists():
                    content_issues.append(
                        f"week-{week_no:02d} resource path missing on web/public: {path_value}"
                    )

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
                continue

            notebook_path = day.get("notebookPath")
            if not isinstance(notebook_path, str) or not notebook_path.strip():
                content_issues.append(
                    f"week-{week_no:02d} day-{day_no:02d} missing notebookPath"
                )
            else:
                day_nb = root / "web" / "public" / notebook_path
                if not day_nb.exists():
                    content_issues.append(
                        f"week-{week_no:02d} day-{day_no:02d} day notebook missing: {notebook_path}"
                    )

            continuity = day.get("continuity")
            if not isinstance(continuity, dict):
                content_issues.append(f"week-{week_no:02d} day-{day_no:02d} missing continuity block")
            else:
                for key in REQUIRED_CONTINUITY_KEYS:
                    if key not in continuity:
                        content_issues.append(
                            f"week-{week_no:02d} day-{day_no:02d} continuity missing key: {key}"
                        )

                previous_path = continuity.get("previousLessonPath")
                if week_no == 1 and day_no == 1:
                    if previous_path is not None:
                        content_issues.append(
                            "week-01 day-01 continuity previousLessonPath should be null"
                        )
                else:
                    if not isinstance(previous_path, str):
                        content_issues.append(
                            f"week-{week_no:02d} day-{day_no:02d} continuity previousLessonPath invalid"
                        )
                    else:
                        prev_path = root / "web" / "public" / previous_path
                        if not prev_path.exists():
                            content_issues.append(
                                f"week-{week_no:02d} day-{day_no:02d} previous lesson missing: {previous_path}"
                            )

                next_path = continuity.get("nextLessonPath")
                if week_no == 24 and day_no == 7:
                    if next_path is not None:
                        content_issues.append("week-24 day-07 continuity nextLessonPath should be null")
                else:
                    if not isinstance(next_path, str):
                        content_issues.append(
                            f"week-{week_no:02d} day-{day_no:02d} continuity nextLessonPath invalid"
                        )
                    else:
                        nxt_path = root / "web" / "public" / next_path
                        if not nxt_path.exists():
                            content_issues.append(
                                f"week-{week_no:02d} day-{day_no:02d} next lesson missing: {next_path}"
                            )

                today_deliverable = continuity.get("todayDeliverable")
                if not isinstance(today_deliverable, str) or not today_deliverable.strip():
                    content_issues.append(
                        f"week-{week_no:02d} day-{day_no:02d} continuity todayDeliverable is empty"
                    )

            lesson_text = lesson_path.read_text(encoding="utf-8")
            for section in REQUIRED_ALL_DAYS_SECTIONS:
                if section not in lesson_text:
                    content_issues.append(
                        f"week-{week_no:02d} day-{day_no:02d} missing section: {section}"
                    )

            if day_no <= 5:
                checked_weekday_lessons += 1
                for section in REQUIRED_WEEKDAY_SECTIONS:
                    if section not in lesson_text:
                        content_issues.append(
                            f"week-{week_no:02d} day-{day_no:02d} missing section: {section}"
                        )
                if "$$" not in lesson_text:
                    content_issues.append(
                        f"week-{week_no:02d} day-{day_no:02d} missing LaTeX block delimiters ($$)"
                    )
                solved_problem_count = lesson_text.count("### Solved Problem")
                if solved_problem_count < 3:
                    content_issues.append(
                        f"week-{week_no:02d} day-{day_no:02d} has {solved_problem_count} solved problems (expected >=3)"
                    )

    if duration_issues:
        fail("Duration mismatches: " + "; ".join(duration_issues[:10]))

    if missing_lessons:
        fail(f"Missing lesson markdown files in web/public/content: {missing_lessons}")

    if content_issues:
        fail("Content quality issues: " + "; ".join(content_issues[:20]))

    weekly_notebooks = sorted((root / "notebooks").glob("week-*/week-*-learning.ipynb"))
    if len(weekly_notebooks) != 24:
        fail(f"Expected 24 weekly learning notebooks, found {len(weekly_notebooks)}")
    daily_notebooks = sorted((root / "notebooks").glob("week-*/day-*-learning.ipynb"))
    if len(daily_notebooks) != 24 * 7:
        fail(f"Expected 168 daily learning notebooks, found {len(daily_notebooks)}")

    web_weekly_notebooks = sorted(
        (root / "web" / "public" / "notebooks").glob("week-*/week-*-learning.ipynb")
    )
    if len(web_weekly_notebooks) != 24:
        fail(f"Expected 24 web weekly notebook assets, found {len(web_weekly_notebooks)}")
    web_daily_notebooks = sorted(
        (root / "web" / "public" / "notebooks").glob("week-*/day-*-learning.ipynb")
    )
    if len(web_daily_notebooks) != 24 * 7:
        fail(f"Expected 168 web daily notebook assets, found {len(web_daily_notebooks)}")

    print("[OK] Validation passed")
    print(f"weeks={len(weeks)}")
    print("durations=weekday-4h/weekend-2h")
    print(f"web_lessons={168 - missing_lessons}")
    print(f"weekday_lessons_with_quality_checks={checked_weekday_lessons}")
    print(f"weekly_notebooks={len(weekly_notebooks)}")
    print(f"daily_notebooks={len(daily_notebooks)}")
    print(f"web_weekly_notebooks={len(web_weekly_notebooks)}")
    print(f"web_daily_notebooks={len(web_daily_notebooks)}")


if __name__ == "__main__":
    main()
