import { useEffect, useMemo, useState } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import type { Session } from "@supabase/supabase-js";

import AuthPanel from "./components/AuthPanel";
import DayDetail from "./components/DayDetail";
import LearningDashboard from "./components/LearningDashboard";
import { loadCurriculum } from "./lib/content";
import { fetchProgress, flushPendingWrites, upsertProgress } from "./lib/progress";
import {
  hasSupabaseConfig,
  requiresPersistentBackend,
  supabase,
  supabaseConfigIssue,
} from "./lib/supabase";
import type { CurriculumIndex, DailyProgress, ProgressMap } from "./types";

export default function App(): JSX.Element {
  const [curriculum, setCurriculum] = useState<CurriculumIndex | null>(null);
  const [session, setSession] = useState<Session | null>(null);
  const [progress, setProgress] = useState<ProgressMap>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [forceLocalMode, setForceLocalMode] = useState(false);

  const supabaseEnabled = hasSupabaseConfig && !forceLocalMode;

  const userId = useMemo(() => {
    if (session?.user.id) {
      return session.user.id;
    }
    return "local-demo-user";
  }, [session]);

  const overallProgress = useMemo(() => {
    if (!curriculum) {
      return {
        completedDays: 0,
        totalDays: 0,
        completionRate: 0,
      };
    }

    const totalDays = curriculum.weeks.reduce((sum, week) => sum + week.days.length, 0);
    const completedDays = curriculum.weeks.reduce((sum, week) => {
      const completeInWeek = week.days.filter((day) => progress[`${week.week}-${day.day}`]?.completed).length;
      return sum + completeInWeek;
    }, 0);
    const completionRate = totalDays > 0 ? Math.round((completedDays / totalDays) * 100) : 0;

    return {
      completedDays,
      totalDays,
      completionRate,
    };
  }, [curriculum, progress]);

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
    const client = supabaseEnabled ? supabase : null;
    if (!client) {
      setLoading(false);
      return;
    }

    async function loadAuth(): Promise<void> {
      if (!client) {
        return;
      }

      try {
        const { data, error: sessionError } = await client.auth.getSession();
        if (sessionError) {
          setError(`Supabase auth is unavailable (${sessionError.message}). Running in local mode.`);
          setForceLocalMode(true);
          setSession(null);
          return;
        }
        setSession(data.session);
      } catch (err) {
        setError(`Supabase auth failed (${String(err)}). Running in local mode.`);
        setForceLocalMode(true);
        setSession(null);
      } finally {
        setLoading(false);
      }
    }

    void loadAuth();

    const {
      data: { subscription },
    } = client.auth.onAuthStateChange((_event, currentSession) => {
      setSession(currentSession);
    });

    return () => subscription.unsubscribe();
  }, [supabaseEnabled]);

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

  useEffect(() => {
    if (!supabaseEnabled) {
      return;
    }

    function handleReconnect(): void {
      void (async () => {
        try {
          const flushed = await flushPendingWrites(userId);
          if (flushed > 0) {
            const p = await fetchProgress(userId);
            setProgress(p);
          }
        } catch (err) {
          setError(String(err));
        }
      })();
    }

    window.addEventListener("online", handleReconnect);
    return () => {
      window.removeEventListener("online", handleReconnect);
    };
  }, [supabaseEnabled, userId]);

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

  if (loading && supabaseEnabled) {
    return <main className="container">Loading authentication...</main>;
  }

  if (requiresPersistentBackend && !supabaseEnabled) {
    return (
      <main className="container">
        <section className="card warning">
          <h1>Supabase Configuration Required</h1>
          <p>
            This production build requires VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY. Configure
            repository secrets and redeploy.
          </p>
        </section>
      </main>
    );
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
      <header className="top-header card premium-hero">
        <div className="hero-copy">
          <p className="hero-eyebrow">Quant Research Academy</p>
          <h1>Institution-Grade Quant Learning Path</h1>
          <p>
            24-week desk-style curriculum with applied modeling, risk, execution, and interview
            preparation.
          </p>
          <div className="hero-metrics">
            <span className="metric-pill">
              <strong>{overallProgress.completedDays}</strong> / {overallProgress.totalDays} days completed
            </span>
            <span className="metric-pill">{overallProgress.completionRate}% program complete</span>
            <span className="metric-pill">6-10h daily cadence</span>
          </div>
        </div>
        <div className="header-actions">
          <span className={`badge ${supabaseEnabled ? "badge-ok" : "badge-muted"}`}>
            {supabaseEnabled ? "Cloud progress active" : "Local mode active"}
          </span>
          <span className="badge badge-muted">User: {userId.slice(0, 12)}</span>
          {supabaseEnabled && session ? (
            <button className="secondary" onClick={handleSignOut}>
              Sign Out
            </button>
          ) : null}
        </div>
      </header>

      {!supabaseEnabled && !requiresPersistentBackend && (supabaseConfigIssue || forceLocalMode) ? (
        <section className="card mode-note">
          <p>
            Progress is currently stored locally for this browser session.
            {supabaseConfigIssue ? ` Config issue: ${supabaseConfigIssue}` : ""}
            {forceLocalMode ? " Auth fallback mode is active." : ""}
          </p>
        </section>
      ) : null}

      {supabaseEnabled && !session ? <AuthPanel onAuthSuccess={() => void 0} /> : null}

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
    </main>
  );
}
