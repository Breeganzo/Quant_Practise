from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from nbconvert import HTMLExporter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 40
TOP_MARGIN = PAGE_HEIGHT - 40
BOTTOM_MARGIN = 40
LINE_HEIGHT = 14

INLINE_MATH_PATTERN = re.compile(r"\$(.+?)\$")
FRACTION_PATTERN = re.compile(r"\\frac\{([^{}]+)\}\{([^{}]+)\}")
POWER_PATTERN = re.compile(r"\^(\{[^{}]+\}|[A-Za-z0-9+\-])")
SUBSCRIPT_PATTERN = re.compile(r"_(\{[^{}]+\}|[A-Za-z0-9+\-])")

LATEX_REPLACEMENTS = {
    r"\approx": "~",
    r"\cdot": "*",
    r"\times": "x",
    r"\mid": "|",
    r"\ge": ">=",
    r"\le": "<=",
    r"\neq": "!=",
    r"\top": "T",
    r"\Delta": "Delta",
    r"\alpha": "alpha",
    r"\beta": "beta",
    r"\gamma": "gamma",
    r"\lambda": "lambda",
    r"\mu": "mu",
    r"\phi": "phi",
    r"\rho": "rho",
    r"\sigma": "sigma",
    r"\Sigma": "Sigma",
}

SUPERSCRIPT_MAP = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "+": "+",
    "-": "-",
    "n": "n",
    "T": "T",
}

SUBSCRIPT_MAP = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "i": "i",
    "j": "j",
    "t": "t",
    "p": "p",
}


def wrap_line(line: str, max_chars: int = 105) -> list[str]:
    if len(line) <= max_chars:
        return [line]
    words = line.split(" ")
    wrapped: list[str] = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if len(candidate) <= max_chars:
            current = candidate
        else:
            wrapped.append(current)
            current = word
    if current:
        wrapped.append(current)
    return wrapped


def script_token(raw: str) -> str:
    if raw.startswith("{") and raw.endswith("}"):
        return raw[1:-1]
    return raw


def render_script(raw: str, mapping: dict[str, str], prefix: str) -> str:
    token = script_token(raw)
    if not token:
        return ""

    if len(token) == 1:
        return mapping.get(token, f"{prefix}{token}")

    converted = "".join(mapping.get(char, char) for char in token)
    if all(char in mapping for char in token):
        return converted
    return f"{prefix}({token})"


def latex_to_readable(expr: str) -> str:
    text = expr.strip()

    while FRACTION_PATTERN.search(text):
        text = FRACTION_PATTERN.sub(
            lambda match: f"({latex_to_readable(match.group(1))})/({latex_to_readable(match.group(2))})",
            text,
        )

    for command, replacement in LATEX_REPLACEMENTS.items():
        text = text.replace(command, replacement)

    text = POWER_PATTERN.sub(lambda match: render_script(match.group(1), SUPERSCRIPT_MAP, "^"), text)
    text = SUBSCRIPT_PATTERN.sub(lambda match: render_script(match.group(1), SUBSCRIPT_MAP, "_"), text)

    text = text.replace("{", "(").replace("}", ")")
    text = text.replace("\\", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_markdown_line(line: str) -> str:
    normalized = line.rstrip()

    if normalized.startswith("```"):
        return "Code:"

    if normalized.startswith("#"):
        normalized = normalized.lstrip("#").strip()

    normalized = INLINE_MATH_PATTERN.sub(lambda match: latex_to_readable(match.group(1)), normalized)
    normalized = normalized.replace("**", "")
    normalized = normalized.replace("`", "")
    return normalized


def markdown_to_pdf_lines(text: str) -> list[str]:
    out: list[str] = []
    in_math_block = False
    math_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.strip() == "$$":
            if in_math_block:
                expression = " ".join(math_lines).strip()
                out.append(f"Equation: {latex_to_readable(expression)}")
                out.append("")
                math_lines = []
                in_math_block = False
            else:
                in_math_block = True
            continue

        if in_math_block:
            math_lines.append(line)
            continue

        out.append(normalize_markdown_line(line))

    if math_lines:
        expression = " ".join(math_lines).strip()
        out.append(f"Equation: {latex_to_readable(expression)}")

    return out


def write_text_pdf(lines: list[str], output_path: Path, title: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_path), pagesize=A4)
    y = TOP_MARGIN

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(LEFT_MARGIN, y, title)
    y -= LINE_HEIGHT * 1.5

    pdf.setFont("Helvetica", 10)
    for line in lines:
        wrapped = wrap_line(line)
        for segment in wrapped:
            if y < BOTTOM_MARGIN:
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = TOP_MARGIN
            safe = segment.replace("\t", "    ")
            pdf.drawString(LEFT_MARGIN, y, safe)
            y -= LINE_HEIGHT

    pdf.save()


def markdown_to_pdf(md_path: Path, pdf_path: Path) -> None:
    lines = markdown_to_pdf_lines(md_path.read_text(encoding="utf-8"))
    write_text_pdf(lines, pdf_path, title=md_path.name)


def notebook_to_html_and_pdf(nb_path: Path, html_path: Path, pdf_path: Path) -> None:
    html_path.parent.mkdir(parents=True, exist_ok=True)
    exporter = HTMLExporter()
    body, _resources = exporter.from_filename(str(nb_path))
    html_path.write_text(body, encoding="utf-8")

    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    lines: list[str] = [f"Notebook: {nb_path.name}", ""]

    for i, cell in enumerate(nb.get("cells", []), start=1):
        cell_type = cell.get("cell_type", "unknown")
        lines.append(f"Cell {i} [{cell_type}]")
        source = "".join(cell.get("source", []))
        if cell_type == "markdown":
            lines.extend(markdown_to_pdf_lines(source))
        else:
            lines.extend(source.splitlines())
        lines.append("")

    write_text_pdf(lines, pdf_path, title=nb_path.name)


def sanitize_slug(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug


def extract_day_sections(md_path: Path) -> dict[str, list[str]]:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    reading: list[str] = []
    quiz: list[str] = []
    interview: list[str] = []

    current = "reading"
    for line in lines:
        if line.startswith("### Daily Quiz"):
            current = "quiz"
        elif line.startswith("### Interview Drill"):
            current = "interview"

        if current == "reading":
            reading.append(line)
        elif current == "quiz":
            quiz.append(line)
        else:
            interview.append(line)

    return {
        "reading": reading,
        "quiz": quiz,
        "interview": interview,
    }


def export_day_section_pdfs(md_path: Path, section_output_dir: Path) -> dict[str, str]:
    section_output_dir.mkdir(parents=True, exist_ok=True)
    sections = extract_day_sections(md_path)
    day_label = md_path.parent.name if md_path.parent.name.startswith("day-") else md_path.stem
    stem = sanitize_slug(day_label)

    reading_pdf = section_output_dir / f"{stem}-reading.pdf"
    quiz_pdf = section_output_dir / f"{stem}-quiz.pdf"
    interview_pdf = section_output_dir / f"{stem}-interview.pdf"

    write_text_pdf(
        markdown_to_pdf_lines("\n".join(sections["reading"])),
        reading_pdf,
        title=f"{md_path.stem} - Reading",
    )
    write_text_pdf(
        markdown_to_pdf_lines("\n".join(sections["quiz"])),
        quiz_pdf,
        title=f"{md_path.stem} - Quiz",
    )
    write_text_pdf(
        markdown_to_pdf_lines("\n".join(sections["interview"])),
        interview_pdf,
        title=f"{md_path.stem} - Interview Drill",
    )

    return {
        "reading": str(reading_pdf),
        "quiz": str(quiz_pdf),
        "interview": str(interview_pdf),
    }


def export_week(root: Path, week: str) -> None:
    md_week_dir = root / "curriculum" / "weeks" / week
    nb_week_dir = root / "notebooks" / week

    md_output = root / "exports" / "pdf" / week / "markdown"
    section_output = root / "exports" / "pdf" / "sections" / week
    nb_pdf_output = root / "exports" / "pdf" / week / "notebooks"
    nb_html_output = root / "exports" / "html" / week

    md_files = sorted(md_week_dir.glob("**/*.md")) if md_week_dir.exists() else []
    nb_files = sorted(nb_week_dir.glob("*.ipynb")) if nb_week_dir.exists() else []

    if not md_files and not nb_files:
        raise SystemExit(f"No markdown or notebooks found for {week}.")

    for md in md_files:
        rel = md.relative_to(md_week_dir)
        markdown_to_pdf(md, md_output / rel.with_suffix(".pdf"))
        if md.name == "lesson.md" and md.parent.name.startswith("day-"):
            export_day_section_pdfs(md, section_output)

    for nb in nb_files:
        notebook_to_html_and_pdf(
            nb,
            nb_html_output / f"{nb.stem}.html",
            nb_pdf_output / f"{nb.stem}.pdf",
        )


def export_all_weeks(root: Path) -> dict[str, object]:
    weeks_root = root / "curriculum" / "weeks"
    week_dirs = sorted(p for p in weeks_root.glob("week-*") if p.is_dir())

    exported: list[str] = []
    for week_dir in week_dirs:
        export_week(root, week_dir.name)
        exported.append(week_dir.name)

    return {
        "target": "all",
        "weeks_exported": exported,
        "count": len(exported),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Export markdown and notebooks to PDF/HTML.")
    parser.add_argument("--week", type=str, default="week-01", help="Week folder, e.g. week-01 or all")
    parser.add_argument(
        "--write-manifest",
        type=str,
        default="",
        help="Optional JSON manifest output path",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    manifest: dict[str, object]
    if args.week == "all":
        manifest = export_all_weeks(root)
        print("Export completed for all weeks.")
    else:
        export_week(root, args.week)
        manifest = {"target": args.week, "count": 1}
        print(f"Export completed for {args.week}.")

    if args.write_manifest:
        manifest_path = Path(args.write_manifest)
        if not manifest_path.is_absolute():
            manifest_path = root / manifest_path
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"Manifest written to {manifest_path.relative_to(root)}")


if __name__ == "__main__":
    main()
