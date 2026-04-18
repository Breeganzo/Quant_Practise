-- Supabase schema for lifelong quant-learning progress persistence.
-- Non-destructive and idempotent: safe to run multiple times.

create table if not exists public.user_profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  full_name text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.daily_progress (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  week_no int not null check (week_no >= 1 and week_no <= 24),
  day_no int not null check (day_no >= 1 and day_no <= 7),
  completed boolean not null default false,
  notes text default '',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(user_id, week_no, day_no)
);

create table if not exists public.quiz_scores (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  week_no int not null check (week_no >= 1 and week_no <= 24),
  score numeric(5,2) not null check (score >= 0 and score <= 100),
  created_at timestamptz not null default now(),
  unique(user_id, week_no)
);

create table if not exists public.project_submissions (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  week_no int not null check (week_no >= 1 and week_no <= 24),
  title text not null,
  summary text,
  artifact_url text,
  completed boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique(user_id, week_no)
);

create table if not exists public.revision_logs (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  week_no int not null check (week_no >= 1 and week_no <= 24),
  note text not null,
  created_at timestamptz not null default now()
);

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

do $$
begin
  if not exists (
    select 1
    from pg_trigger t
    join pg_class c on c.oid = t.tgrelid
    join pg_namespace n on n.oid = c.relnamespace
    where n.nspname = 'public'
      and c.relname = 'user_profiles'
      and t.tgname = 'trg_user_profiles_updated_at'
  ) then
    create trigger trg_user_profiles_updated_at
    before update on public.user_profiles
    for each row execute function public.set_updated_at();
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1
    from pg_trigger t
    join pg_class c on c.oid = t.tgrelid
    join pg_namespace n on n.oid = c.relnamespace
    where n.nspname = 'public'
      and c.relname = 'daily_progress'
      and t.tgname = 'trg_daily_progress_updated_at'
  ) then
    create trigger trg_daily_progress_updated_at
    before update on public.daily_progress
    for each row execute function public.set_updated_at();
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1
    from pg_trigger t
    join pg_class c on c.oid = t.tgrelid
    join pg_namespace n on n.oid = c.relnamespace
    where n.nspname = 'public'
      and c.relname = 'project_submissions'
      and t.tgname = 'trg_project_submissions_updated_at'
  ) then
    create trigger trg_project_submissions_updated_at
    before update on public.project_submissions
    for each row execute function public.set_updated_at();
  end if;
end;
$$;

alter table public.user_profiles enable row level security;
alter table public.daily_progress enable row level security;
alter table public.quiz_scores enable row level security;
alter table public.project_submissions enable row level security;
alter table public.revision_logs enable row level security;

do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'user_profiles'
      and policyname = 'user_profiles_owner_only'
  ) then
    create policy "user_profiles_owner_only"
    on public.user_profiles
    for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'daily_progress'
      and policyname = 'daily_progress_owner_only'
  ) then
    create policy "daily_progress_owner_only"
    on public.daily_progress
    for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'quiz_scores'
      and policyname = 'quiz_scores_owner_only'
  ) then
    create policy "quiz_scores_owner_only"
    on public.quiz_scores
    for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'project_submissions'
      and policyname = 'project_submissions_owner_only'
  ) then
    create policy "project_submissions_owner_only"
    on public.project_submissions
    for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);
  end if;
end;
$$;

do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'revision_logs'
      and policyname = 'revision_logs_owner_only'
  ) then
    create policy "revision_logs_owner_only"
    on public.revision_logs
    for all
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);
  end if;
end;
$$;
