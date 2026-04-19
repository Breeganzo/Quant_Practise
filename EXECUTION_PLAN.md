# EXECUTION_PLAN

## Implemented Sequence
1. Enhanced weekday lessons across all weeks.
2. Regenerated week and day notebooks.
3. Synchronized canonical content into web public assets.
4. Ran strict roadmap verification checks.
5. Ran parallel week-agent ReAct pipeline (workers=8) for all 24 weeks:
   - lesson enhancement check
   - notebook regeneration
   - notebook execution
   - week export
6. Ran global export manifest pass for all weeks.
7. Re-synced web assets and re-verified roadmap.
8. Built frontend in production mode.

## Evidence Artifacts
- data/processed/lesson_enhancement_report.json
- data/processed/react_week_pipeline_report.json
- data/processed/all_weeks_export_manifest.json
- data/processed/reports/week-01-notebooks.json ... week-24-notebooks.json
- data/processed/reports/week-01-exports.json ... week-24-exports.json

## Automation Added
- scripts/enhance_weekday_lessons.py
- scripts/run_react_week_pipeline.py

## Pipeline Upgrades
- scripts/generate_all_week_notebooks.py:
  - per-week generation option
  - ReAct verification code cell insertion
  - kernel display name alignment
- scripts/run_notebooks.py:
  - JSON report output
  - continue-on-error mode
- scripts/export_assets.py:
  - all-week export mode
  - manifest output
- scripts/verify_roadmap.py:
  - stricter weekday quality enforcement
- .github/workflows/deploy-pages.yml:
  - python/uv setup
  - notebook regeneration
  - asset sync + roadmap validation pre-build

## Frontend Hardening
- web/src/lib/content.ts: timeout + retry fetch strategy
- web/src/components/ErrorBoundary.tsx: global runtime guard
- web/src/main.tsx: ErrorBoundary integration
