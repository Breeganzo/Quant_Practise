# Quant Practice: 24-Week Quant Learning System

This repository contains a complete 6-month quant roadmap with day-level lessons, executable notebooks, and a private login tracker backed by PostgreSQL (Supabase).

Schedule design:

- Weekdays (Day 1-5): 4-hour focused learning blocks
- Weekend Day 6: 2-hour revision and spaced recall
- Weekend Day 7: 2-hour mini-project and reflection

## What Is Included

- Full curriculum for weeks 01-24 in `curriculum/weeks`
- 168 day lesson files (`lesson.md`) with theory, examples, coding, and reflection
- 24 weekly learning notebooks in `notebooks/week-XX/week-XX-learning.ipynb`
- Weekly resource pack per week (overview, quiz, revision checklist, mini-project brief) published to web assets
- React + TypeScript tracker app in `web`
- SQL schema for long-term persistence in `supabase/schema.sql`
- Beginner setup walkthrough in `docs/SUPABASE_SETUP_BEGINNER.md`
- GitHub Pages deployment workflow in `.github/workflows/deploy-pages.yml`

## 1) Python Environment (uv)

1. Install `uv`:
   - `brew install uv`
2. Create/sync environment:
   - `uv sync`

## 2) Regenerate Curriculum and Notebooks

Run these commands from repository root:

- `uv run python scripts/generate_full_curriculum.py`
- `uv run python scripts/generate_all_week_notebooks.py`
- `uv run python scripts/sync_web_assets.py`

Optional validation:

- Validate structure/content consistency:
   - `uv run python scripts/verify_roadmap.py`
- Execute all notebooks:
  - `uv run python scripts/run_notebooks.py --all`
- Export any week to PDF/HTML:
  - `uv run python scripts/export_assets.py --week week-01`

## 3) Supabase Setup (SQL Persistence)

Use the full click-by-click guide:

- `docs/SUPABASE_SETUP_BEGINNER.md`

Quick version:

1. Create a Supabase project.
2. Run `supabase/schema.sql` in Supabase SQL Editor.
3. Enable Email provider under Supabase Authentication.
4. In Supabase Settings -> API, copy:
   - Project URL -> `VITE_SUPABASE_URL`
   - anon public key -> `VITE_SUPABASE_ANON_KEY`
5. Create web env file:
   - `cp web/.env.example web/.env`
6. Fill values in `web/.env`:
   - `VITE_SUPABASE_URL=...`
   - `VITE_SUPABASE_ANON_KEY=...`
   - `VITE_REPO_URL=https://github.com/Breeganzo/Quant_Practise`

Local development allows fallback demo mode without Supabase.
Production deployment to GitHub Pages is Supabase-required.

## 4) Run React Tracker Locally

1. Install web dependencies:
   - `cd web && npm install`
2. Start development server:
   - `npm run dev`

The tracker provides:

- private login
- week/day navigation
- lesson rendering from markdown
- completion + notes persistence in PostgreSQL
- links to lesson and notebook resources

## 5) Deploy to GitHub Pages

Workflow file: `.github/workflows/deploy-pages.yml`

Required repository secrets:

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

See `docs/SUPABASE_SETUP_BEGINNER.md` for exact secret setup path in GitHub UI.

Deployment flow:

1. Push to `main`
2. GitHub Action builds `web`
3. Built app from `web/dist` is deployed to Pages

Vite base path is configured for `Quant_Practise`.

## 6) Persistence Behavior (Dev vs Production)

- Local development (`npm run dev`):
   - if Supabase env vars are set, progress is written to PostgreSQL via Supabase.
   - if Supabase env vars are missing, app runs in local demo mode for quick testing.
- Production build (GitHub Pages):
   - Supabase configuration is mandatory.
   - missing `VITE_SUPABASE_URL` or `VITE_SUPABASE_ANON_KEY` shows a configuration-required screen instead of local fallback.
   - save failures are queued locally and retried automatically when network reconnects.

## 7) Open Notebooks in VS Code or Jupyter

- From VS Code:
   - open any file under `notebooks/week-XX/week-XX-learning.ipynb`.
   - run cells directly in the VS Code Notebook UI.
- From Jupyter locally:
   - `uv run jupyter lab`
   - open `notebooks/week-XX/week-XX-learning.ipynb`.

The web app also links each day to its corresponding weekly notebook and supporting weekly resources.

## 8) Generated Architecture (Canonical vs Mirrored)

- Canonical editable sources:
   - `curriculum/weeks/`
   - `notebooks/`
- Mirrored web assets (do not edit directly):
   - `web/public/content/`
   - `web/public/notebooks/`
   - `web/public/resources/`
   - `web/public/data/curriculum.json`

Always regenerate from canonical sources and then mirror:

- `uv run python scripts/generate_full_curriculum.py`
- `uv run python scripts/generate_all_week_notebooks.py`
- `uv run python scripts/sync_web_assets.py`

## Repository Layout

- `curriculum/`: canonical week/day learning content and capstones
- `notebooks/`: generated weekly notebooks
- `admissions/`: weekly admissions-focused tasks
- `interview/`: weekly interview prep tasks
- `docs/`: setup and onboarding guides
- `scripts/`: generators, notebook execution/export, web content sync
- `supabase/`: SQL schema for persistent progress
- `web/`: React tracker frontend

## Safety Note

This project is for education and simulation-first learning. Do not deploy real capital until your strategy, risk controls, and execution assumptions are tested with robust out-of-sample and stress scenarios.
