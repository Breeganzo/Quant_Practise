import { useEffect, useMemo, useState } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import type { Session } from "@supabase/supabase-js";

import AuthPanel from "./components/AuthPanel";
import DayDetail from "./components/DayDetail";
import LearningDashboard from "./components/LearningDashboard";
import { loadCurriculum } from "./lib/content";
import { fetchProgress, upsertProgress } from "./lib/progress";
import { hasSupabaseConfig, supabase } from "./lib/supabase";
import type { CurriculumIndex, DailyProgress, ProgressMap } from "./types";

export default function App(): JSX.Element {
  const [curriculum, setCurriculum] = useState<CurriculumIndex | null>(null);
  const [session, setSession] = useState<Session | null>(null);
  const [progress, setProgress] = useState<ProgressMap>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const userId = useMemo(() => {
    if (session?.user.id) {
      return session.user.id;
    }
    return "local-demo-user";
  }, [session]);

  useEffect(() => {
    async function boot(): Promise<void> {
      try {
        const content = await loadCurriculum();
        setCurriculum(content);
      } catch (err) {
        setError(String(err));
      }
    }

    void boot();
  }, []);

  useEffect(() => {
    const client = supabase;
    if (!client) {
      setLoading(false);
      return;
    }

    async function loadAuth(): Promise<void> {
      if (!client) {
        return;
      }
      const { data } = await client.auth.getSession();
      setSession(data.session);
      setLoading(false);
    }

    void loadAuth();

    const {
      data: { subscription },
    } = client.auth.onAuthStateChange((_event, currentSession) => {
      setSession(currentSession);
    });

    return () => subscription.unsubscribe();
  }, []);

  useEffect(() => {
    async function loadUserProgress(): Promise<void> {
      try {
        const p = await fetchProgress(userId);
        setProgress(p);
      } catch (err) {
        setError(String(err));
      }
    }

    void loadUserProgress();
  }, [userId]);

  async function handleSaveProgress(
    weekNo: number,
    dayNo: number,
    completed: boolean,
    notes: string
  ): Promise<DailyProgress> {
    const item = await upsertProgress(userId, weekNo, dayNo, completed, notes);
    setProgress((previous) => ({
      ...previous,
      [`${weekNo}-${dayNo}`]: item,
    }));
    return item;
  }

  async function handleSignOut(): Promise<void> {
    if (!supabase) {
      return;
    }
    await supabase.auth.signOut();
  }

  if (loading && hasSupabaseConfig) {
    return <main className="container">Loading authentication...</main>;
  }

  if (!curriculum) {
    return (
      <main className="container">
        <h1>Quant Learning Tracker</h1>
        <p>{error || "Loading curriculum..."}</p>
      </main>
    );
  }

  return (
    <main className="container">
      <header className="top-header card">
        <div>
          <h1>Quant Learning Path Tracker</h1>
          <p>24-week day-by-day learning path with persistent progress and direct lesson links.</p>
        </div>
        <div className="header-actions">
          <span className="badge">User: {userId.slice(0, 12)}</span>
          {hasSupabaseConfig && session ? (
            <button className="secondary" onClick={handleSignOut}>
              Sign Out
            </button>
          ) : null}
        </div>
      </header>

      {!hasSupabaseConfig ? (
        <section className="card warning">
          <h2>Supabase Not Configured</h2>
          <p>
            Configure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY to enable lifelong SQL persistence.
            Until then, this app runs in local demo mode.
          </p>
        </section>
      ) : null}

      {hasSupabaseConfig && !session ? (
        <AuthPanel onAuthSuccess={() => void 0} />
      ) : (
        <Routes>
          <Route path="/" element={<LearningDashboard curriculum={curriculum} progress={progress} />} />
          <Route
            path="/week/:weekNo/day/:dayNo"
            element={
              <DayDetail
                curriculum={curriculum}
                userId={userId}
                progress={progress}
                onSave={handleSaveProgress}
              />
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      )}
    </main>
  );
}
