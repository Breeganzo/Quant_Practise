# Curriculum Enhancement Project Plan

## Objective
Upgrade the full 24-week quant curriculum into a production-ready 6-hour/day learning system with stronger theory depth, executed coding notebooks, realistic daily interview quiz answers, PDF/HTML exports, and GitHub Pages deployment safeguards.

## Scope
- Weekday lesson upgrades for all weeks (days 01-05)
- Notebook generation and execution upgrades for all weeks (days 01-07 + weekly notebook)
- Automated export to PDF/HTML for all weeks
- Web asset sync and production build validation
- CI deployment hardening for GitHub Pages

## Phase Breakdown
1. Phase 1: Baseline audit and quality-gate design.
2. Phase 2: Weekday markdown enhancement and rubric enforcement.
3. Phase 3: Notebook enhancement, execution, and verification.
4. Phase 4: Export, web sync, CI/CD hardening, and release documentation.

## Acceptance Gates
- Each weekday lesson includes the required 6-hour model (4-hour core + 2-hour extension).
- Each weekday lesson includes at least 4 solved problems.
- Daily quiz section includes embedded model answers.
- All week/day notebooks are generated and executable.
- All weeks export to PDF/HTML.
- Web app builds for production and route fallback is preserved.

## Execution Model
- One logical week agent per week.
- Queued parallel execution with controlled concurrency.
- ReAct loop per week: Observe, Reason, Act, Verify.

## Canonical Commands
- /Users/anto/Quant/.venv/bin/python scripts/enhance_weekday_lessons.py --week all
- /Users/anto/Quant/.venv/bin/python scripts/generate_all_week_notebooks.py --week all
- /Users/anto/Quant/.venv/bin/python scripts/run_react_week_pipeline.py --weeks all --workers 8
- /Users/anto/Quant/.venv/bin/python scripts/export_assets.py --week all --write-manifest data/processed/all_weeks_export_manifest.json
- /Users/anto/Quant/.venv/bin/python scripts/sync_web_assets.py
- /Users/anto/Quant/.venv/bin/python scripts/verify_roadmap.py
- cd web && npm ci && npm run build
