from __future__ import annotations

import shutil
from pathlib import Path


def expected_source_paths(root: Path) -> list[Path]:
    paths: list[Path] = [root / "curriculum" / "curriculum-index.json"]
    for week_no in range(1, 25):
        week_id = f"week-{week_no:02d}"
        week_dir = root / "curriculum" / "weeks" / week_id

        paths.append(root / "notebooks" / week_id / f"{week_id}-learning.ipynb")
        for day_no in range(1, 8):
            paths.append(root / "notebooks" / week_id / f"day-{day_no:02d}-learning.ipynb")
        paths.append(week_dir / "README.md")
        paths.append(week_dir / f"{week_id}-quiz.md")
        paths.append(week_dir / f"{week_id}-revision-checklist.md")
        paths.append(week_dir / f"{week_id}-mini-project-template.md")

        for day_no in range(1, 8):
            paths.append(week_dir / f"day-{day_no:02d}" / "lesson.md")

    return paths


def validate_sources(root: Path) -> None:
    missing = [p for p in expected_source_paths(root) if not p.exists()]
    if missing:
        preview = ", ".join(str(p.relative_to(root)) for p in missing[:12])
        raise SystemExit(f"[FAIL] Missing canonical files before sync: {preview}")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    validate_sources(root)

    curriculum_index = root / "curriculum" / "curriculum-index.json"
    web_index = root / "web" / "public" / "data" / "curriculum.json"
    copy_file(curriculum_index, web_index)

    copied_lessons = 0
    copied_notebooks = 0
    copied_resources = 0
    copied_section_pdfs = 0

    for week_no in range(1, 25):
        week_id = f"week-{week_no:02d}"
        week_dir = root / "curriculum" / "weeks" / week_id

        for notebook_src in sorted((root / "notebooks" / week_id).glob("*.ipynb")):
            notebook_dst = root / "web" / "public" / "notebooks" / week_id / notebook_src.name
            copy_file(notebook_src, notebook_dst)
            copied_notebooks += 1

        resource_pairs = [
            (week_dir / "README.md", root / "web" / "public" / "resources" / week_id / "overview.md"),
            (
                week_dir / f"{week_id}-quiz.md",
                root / "web" / "public" / "resources" / week_id / "quiz.md",
            ),
            (
                week_dir / f"{week_id}-revision-checklist.md",
                root / "web" / "public" / "resources" / week_id / "revision-checklist.md",
            ),
            (
                week_dir / f"{week_id}-mini-project-template.md",
                root / "web" / "public" / "resources" / week_id / "mini-project-template.md",
            ),
        ]
        for src, dst in resource_pairs:
            copy_file(src, dst)
            copied_resources += 1

        for day_no in range(1, 8):
            lesson_src = week_dir / f"day-{day_no:02d}" / "lesson.md"
            lesson_dst = root / "web" / "public" / "content" / week_id / f"day-{day_no:02d}.md"
            copy_file(lesson_src, lesson_dst)
            copied_lessons += 1

        sections_src = root / "exports" / "pdf" / "sections" / week_id
        if sections_src.exists():
            for pdf_src in sorted(sections_src.glob("*.pdf")):
                pdf_dst = root / "web" / "public" / "pdf" / "sections" / week_id / pdf_src.name
                copy_file(pdf_src, pdf_dst)
                copied_section_pdfs += 1

    print(
        "Synchronized web content and notebook assets. "
        f"lessons={copied_lessons} notebooks={copied_notebooks} resources={copied_resources} section_pdfs={copied_section_pdfs}"
    )


if __name__ == "__main__":
    main()
