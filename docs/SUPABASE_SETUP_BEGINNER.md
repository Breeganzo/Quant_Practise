# Supabase Setup (Beginner Guide)

This guide shows exactly where to find your Supabase URL and key, how to run the SQL schema, and how to wire the app locally and on GitHub Pages.

## 1) Create a Supabase Project

1. Go to https://supabase.com and sign in.
2. Click New project.
3. Choose your organization.
4. Set:
   - Name: any project name (for example: quant-practice)
   - Database Password: create and save a strong password
   - Region: choose one close to you
5. Click Create new project.
6. Wait until project status becomes healthy.

## 2) Run the SQL Schema

1. In the Supabase dashboard, open your project.
2. In the left sidebar, click SQL Editor.
3. Click New query.
4. Open this repository file: supabase/schema.sql
5. Paste the SQL into the editor.
6. Click Run.
7. Confirm tables and policies are created (look for no errors in output).

Important safety note:

- The current schema is non-destructive and idempotent.
- It does not drop tables or user data.
- It is safe to re-run if setup is interrupted.

Preflight check before pasting full schema:

1. Run this in SQL Editor first:

```sql
select now();
```

2. If this simple query fails with a network error, fix connectivity first (see troubleshooting section below) and then run the full schema.

## 3) Enable Email/Password Auth

1. In Supabase, go to Authentication.
2. Open Providers.
3. Enable Email.
4. Keep Confirm email enabled or disabled based on your preference.
   - Enabled: users must confirm email.
   - Disabled: users can sign in immediately (easier for local testing).

## 4) Find Your Project URL and Anon Key (Important)

1. In Supabase sidebar, click Settings.
2. Click API.
3. Copy these two values:
   - Project URL -> use as VITE_SUPABASE_URL
   - Project API Keys -> anon public -> use as VITE_SUPABASE_ANON_KEY

Use only the anon public key in the frontend.
Do not put the service_role key in frontend files, GitHub Pages secrets for Vite frontend, or client code.

## 5) Configure Local Environment

From repository root:

```bash
cp web/.env.example web/.env
```

Open web/.env and fill:

```env
VITE_SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
VITE_SUPABASE_ANON_KEY=YOUR_ANON_PUBLIC_KEY
VITE_REPO_URL=https://github.com/Breeganzo/Quant_Practise
```

## 6) Start the Web App and Test Login

```bash
cd web
npm install
npm run dev
```

Then:

1. Open the local URL shown by Vite.
2. Register a new account in the app.
3. Log in.
4. Mark a lesson complete and add a note.
5. Refresh page and confirm progress persists.

## 7) Configure GitHub Pages Secrets

In your GitHub repository:

1. Settings -> Secrets and variables -> Actions.
2. Add these Repository secrets:
   - VITE_SUPABASE_URL
   - VITE_SUPABASE_ANON_KEY
3. Push to main to trigger deploy workflow.

## 8) Production Persistence Rules

- GitHub Pages production build is Supabase-only.
- If `VITE_SUPABASE_URL` or `VITE_SUPABASE_ANON_KEY` is missing in repository secrets,
   the deployed app shows a configuration-required screen instead of local fallback mode.
- During temporary network failures, save attempts are queued in browser storage and retried
   automatically when connectivity returns.

## 9) Quick Troubleshooting

- Error in SQL Editor: Failed to fetch (api.supabase.com)
   - This is usually browser/network related, not SQL syntax.
   - Fix sequence:
      1. Hard refresh the Supabase tab.
      2. Sign out of Supabase, then sign in again.
      3. Open Supabase in an incognito/private window.
      4. Disable ad blockers/privacy extensions for both `supabase.com` and `api.supabase.com`.
      5. Disable VPN/proxy temporarily, or try a different network (for example mobile hotspot).
      6. Run `select now();` in SQL Editor.
      7. If it succeeds, run full `supabase/schema.sql` again.
   - If it still fails, wait 2-5 minutes and retry (temporary service/CDN issues can happen).

- SQL Editor warns about destructive code
   - Use the latest repository version of `supabase/schema.sql`.
   - The current script is non-destructive and safe to re-run.
   - If you still see warning text, inspect for old pasted content and clear editor before re-pasting.

- Error: Invalid API key
  - Confirm you used anon public key, not service_role.

- Error: Failed to fetch or CORS/network issues
  - Verify VITE_SUPABASE_URL value and no trailing spaces.

- Login works but progress not saved
  - Re-run supabase/schema.sql.
  - Check RLS policies were created.
  - Confirm you are logged in with a valid user session.

- App works locally but not on GitHub Pages
  - Confirm both repository secrets are set.
  - Re-run workflow after updating secrets.

- Save shows retry/queued message
   - This means Supabase write failed temporarily.
   - Reconnect to the network and reopen the app; queued writes are retried automatically.
