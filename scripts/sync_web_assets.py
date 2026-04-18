from __future__ import annotations

import shutil
from pathlib import Path


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    curriculum_index = root / "curriculum" / "curriculum-index.json"
    web_index = root / "web" / "public" / "data" / "curriculum.json"
    if curriculum_index.exists():
        copy_file(curriculum_index, web_index)

    for week_no in range(1, 25):
        week_id = f"week-{week_no:02d}"
        notebook_src = root / "notebooks" / week_id / f"{week_id}-learning.ipynb"
        notebook_dst = root / "web" / "public" / "notebooks" / week_id / f"{week_id}-learning.ipynb"
        if notebook_src.exists():
            copy_file(notebook_src, notebook_dst)

        for day_no in range(1, 8):
            lesson_src = root / "curriculum" / "weeks" / week_id / f"day-{day_no:02d}" / "lesson.md"
            lesson_dst = root / "web" / "public" / "content" / week_id / f"day-{day_no:02d}.md"
            if lesson_src.exists():
                copy_file(lesson_src, lesson_dst)

    print("Synchronized web content and notebook assets.")


if __name__ == "__main__":
    main()
