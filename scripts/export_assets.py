from __future__ import annotations

import argparse
import json
from pathlib import Path

from nbconvert import HTMLExporter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 40
TOP_MARGIN = PAGE_HEIGHT - 40
BOTTOM_MARGIN = 40
LINE_HEIGHT = 14


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
    lines = md_path.read_text(encoding="utf-8").splitlines()
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
        lines.extend(source.splitlines())
        lines.append("")

    write_text_pdf(lines, pdf_path, title=nb_path.name)


def export_week(root: Path, week: str) -> None:
    md_week_dir = root / "curriculum" / "weeks" / week
    nb_week_dir = root / "notebooks" / week

    md_output = root / "exports" / "pdf" / week / "markdown"
    nb_pdf_output = root / "exports" / "pdf" / week / "notebooks"
    nb_html_output = root / "exports" / "html" / week

    md_files = sorted(md_week_dir.glob("**/*.md")) if md_week_dir.exists() else []
    nb_files = sorted(nb_week_dir.glob("*.ipynb")) if nb_week_dir.exists() else []

    if not md_files and not nb_files:
        raise SystemExit(f"No markdown or notebooks found for {week}.")

    for md in md_files:
        rel = md.relative_to(md_week_dir)
        markdown_to_pdf(md, md_output / rel.with_suffix(".pdf"))

    for nb in nb_files:
        notebook_to_html_and_pdf(
            nb,
            nb_html_output / f"{nb.stem}.html",
            nb_pdf_output / f"{nb.stem}.pdf",
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Export markdown and notebooks to PDF/HTML.")
    parser.add_argument("--week", type=str, default="week-01", help="Week folder, e.g. week-01")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    export_week(root, args.week)
    print(f"Export completed for {args.week}.")


if __name__ == "__main__":
    main()
