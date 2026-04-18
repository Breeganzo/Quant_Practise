import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";

import { loadLessonMarkdown } from "../lib/content";
import { githubBlobUrl, withBase } from "../lib/path";
import type { CurriculumIndex, DailyProgress, ProgressMap } from "../types";

interface DayDetailProps {
  curriculum: CurriculumIndex;
  userId: string;
  progress: ProgressMap;
  onSave: (weekNo: number, dayNo: number, completed: boolean, notes: string) => Promise<DailyProgress>;
}

function progressKey(weekNo: number, dayNo: number): string {
  return `${weekNo}-${dayNo}`;
}

export default function DayDetail({
  curriculum,
  userId,
  progress,
  onSave,
}: DayDetailProps): JSX.Element {
  const params = useParams();
  const navigate = useNavigate();

  const weekNo = Number(params.weekNo);
  const dayNo = Number(params.dayNo);

  const week = useMemo(() => curriculum.weeks.find((item) => item.week === weekNo), [curriculum, weekNo]);
  const day = useMemo(() => week?.days.find((item) => item.day === dayNo), [week, dayNo]);

  const currentProgress = progress[progressKey(weekNo, dayNo)];

  const [markdown, setMarkdown] = useState("Loading lesson...");
  const [completed, setCompleted] = useState(Boolean(currentProgress?.completed));
  const [notes, setNotes] = useState(currentProgress?.notes ?? "");
  const [status, setStatus] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (!day) {
      return;
    }
    setCompleted(Boolean(currentProgress?.completed));
    setNotes(currentProgress?.notes ?? "");
  }, [day, currentProgress]);

  useEffect(() => {
    async function run(): Promise<void> {
      if (!day) {
        setMarkdown("Lesson not found.");
        return;
      }
      try {
        const text = await loadLessonMarkdown(day.lessonPath);
        setMarkdown(text);
      } catch (error) {
        setMarkdown(`Unable to load lesson content. ${String(error)}`);
      }
    }
    void run();
  }, [day]);

  if (!week || !day) {
    return (
      <section className="card">
        <h2>Lesson not found</h2>
        <button onClick={() => navigate("/")}>Back to Dashboard</button>
      </section>
    );
  }

  const notebookPath = `notebooks/week-${weekNo.toString().padStart(2, "0")}/week-${weekNo
    .toString()
    .padStart(2, "0")}-learning.ipynb`;
  const lessonRepoPath = `curriculum/weeks/week-${weekNo
    .toString()
    .padStart(2, "0")}/day-${dayNo.toString().padStart(2, "0")}/lesson.md`;

  async function handleSave(): Promise<void> {
    setSaving(true);
    setStatus("");
    try {
      await onSave(weekNo, dayNo, completed, notes);
      setStatus("Progress saved successfully.");
    } catch (error) {
      setStatus(`Save failed: ${String(error)}`);
    } finally {
      setSaving(false);
    }
  }

  return (
    <section className="lesson-layout">
      <article className="card lesson-main">
        <header className="lesson-header">
          <div>
            <h2>
              Week {weekNo.toString().padStart(2, "0")} Day {dayNo.toString().padStart(2, "0")}: {day.title}
            </h2>
            <p>
              Planned duration: {day.durationHours} hour(s) | Track type: {day.type}
            </p>
          </div>
          <Link to="/" className="secondary-link">
            Back to dashboard
          </Link>
        </header>
        <ReactMarkdown>{markdown}</ReactMarkdown>
      </article>

      <aside className="card lesson-side">
        <h3>Progress Controls</h3>
        <p>User: {userId}</p>

        <label className="checkbox-row">
          <input type="checkbox" checked={completed} onChange={(event) => setCompleted(event.target.checked)} />
          Mark this day as completed
        </label>

        <label htmlFor="notes">Notes</label>
        <textarea
          id="notes"
          rows={10}
          value={notes}
          onChange={(event) => setNotes(event.target.value)}
          placeholder="Write summary, blockers, and next actions..."
        />

        <button onClick={handleSave} disabled={saving}>
          {saving ? "Saving..." : "Save Progress"}
        </button>
        {status ? <p className="status">{status}</p> : null}

        <div className="resource-links">
          <h4>Open Resources</h4>
          <a href={githubBlobUrl(lessonRepoPath)} target="_blank" rel="noreferrer">
            Open lesson source (GitHub)
          </a>
          <a href={githubBlobUrl(notebookPath)} target="_blank" rel="noreferrer">
            Open week notebook (GitHub)
          </a>
          <a href={withBase(notebookPath)} target="_blank" rel="noreferrer">
            Open week notebook (local file)
          </a>
          <a href={withBase(day.lessonPath)} target="_blank" rel="noreferrer">
            Open rendered lesson file
          </a>
        </div>
      </aside>
    </section>
  );
}
