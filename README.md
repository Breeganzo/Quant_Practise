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
- React + TypeScript tracker app in `web`
- SQL schema for long-term persistence in `supabase/schema.sql`
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

- Execute all notebooks:
  - `uv run python scripts/run_notebooks.py --all`
- Export any week to PDF/HTML:
  - `uv run python scripts/export_assets.py --week week-01`

## 3) Supabase Setup (SQL Persistence)

1. Create a Supabase project.
2. Open SQL editor and run the script in `supabase/schema.sql`.
3. In Supabase Auth, enable Email/Password sign-in.
4. Create web env file:
   - `cp web/.env.example web/.env`
5. Fill values in `web/.env`:
   - `VITE_SUPABASE_URL=...`
   - `VITE_SUPABASE_ANON_KEY=...`
   - `VITE_REPO_URL=https://github.com/Breeganzo/Quant_Practise`

If Supabase env vars are not set, the app uses local browser storage as fallback demo mode.

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

Deployment flow:

1. Push to `main`
2. GitHub Action builds `web`
3. Built app from `web/dist` is deployed to Pages

Vite base path is configured for `Quant_Practise`.

## Repository Layout

- `curriculum/`: canonical week/day learning content and capstones
- `notebooks/`: generated weekly notebooks
- `admissions/`: weekly admissions-focused tasks
- `interview/`: weekly interview prep tasks
- `scripts/`: generators, notebook execution/export, web content sync
- `supabase/`: SQL schema for persistent progress
- `web/`: React tracker frontend

## Safety Note

This project is for education and simulation-first learning. Do not deploy real capital until your strategy, risk controls, and execution assumptions are tested with robust out-of-sample and stress scenarios.
