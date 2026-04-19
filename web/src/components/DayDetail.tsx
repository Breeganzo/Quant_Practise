import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import rehypeSlug from "rehype-slug";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";

import "katex/dist/katex.min.css";

import { loadLessonMarkdown } from "../lib/content";
import { githubBlobUrl, githubDevUrl, withBase } from "../lib/path";
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

function routeFromLessonPath(lessonPath: string | null | undefined): string | null {
  if (!lessonPath) {
    return null;
  }
  const match = lessonPath.match(/^content\/week-(\d{2})\/day-(\d{2})\.md$/);
  if (!match) {
    return null;
  }
  const week = Number(match[1]);
  const day = Number(match[2]);
  return `/week/${week}/day/${day}`;
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
  const [statusTone, setStatusTone] = useState<"ok" | "error" | "">("");
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

  const dayNotebookPath =
    day.notebookPath ??
    `notebooks/week-${weekNo.toString().padStart(2, "0")}/day-${dayNo.toString().padStart(2, "0")}-learning.ipynb`;
  const webDayNotebookPath = dayNotebookPath;
  const weekId = `week-${weekNo.toString().padStart(2, "0")}`;
  const dayId = `day-${dayNo.toString().padStart(2, "0")}`;
  const sectionPdfBasePath = `pdf/sections/${weekId}`;
  const readingPdfPath = `${sectionPdfBasePath}/${dayId}-reading.pdf`;
  const quizPdfPath = `${sectionPdfBasePath}/${dayId}-quiz.pdf`;
  const interviewPdfPath = `${sectionPdfBasePath}/${dayId}-interview.pdf`;
  const notebookGithubPath = githubBlobUrl(dayNotebookPath);
  const notebookVsCodePath = githubDevUrl(dayNotebookPath);
  const continuity = day.continuity;
  const previousRoute = routeFromLessonPath(continuity?.previousLessonPath);
  const nextRoute = routeFromLessonPath(continuity?.nextLessonPath);

  async function handleSave(): Promise<void> {
    setSaving(true);
    setStatus("");
    setStatusTone("");
    try {
      await onSave(weekNo, dayNo, completed, notes);
      setStatus("Progress saved successfully.");
      setStatusTone("ok");
    } catch (error) {
      setStatus(`Save failed: ${String(error)}`);
      setStatusTone("error");
    } finally {
      setSaving(false);
    }
  }

  return (
    <section className="lesson-layout">
      <article id="lesson-content" className="card lesson-main">
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
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeSlug, rehypeKatex]}
        >
          {markdown}
        </ReactMarkdown>
      </article>

      <aside className="card lesson-side">
        {continuity ? (
          <section className="continuity-panel">
            <h3>Continuity Map</h3>
            <p>
              <strong>Previous checkpoint:</strong> {continuity.previousLabel}
            </p>
            {previousRoute ? (
              <Link to={previousRoute} className="secondary-link">
                Open previous day
              </Link>
            ) : null}
            <p>
              <strong>Today deliverable:</strong> {continuity.todayDeliverable}
            </p>
            <p>
              <strong>Next handoff:</strong> {continuity.nextLabel}
            </p>
            {nextRoute ? (
              <Link to={nextRoute} className="secondary-link">
                Open next day
              </Link>
            ) : null}
          </section>
        ) : null}

        <section className="daily-actions">
          <h3>Daily Study Actions</h3>

          <div className="action-menu">
            <button type="button" className="action-trigger" aria-haspopup="true">
              Daily Reading
            </button>
            <div className="action-menu-panel" role="menu" aria-label="Daily Reading Actions">
              <a className="action-menu-item" href="#lesson-content">
                Read here
              </a>
              <a
                className="action-menu-item"
                href={withBase(readingPdfPath)}
                target="_blank"
                rel="noreferrer"
              >
                Open PDF
              </a>
            </div>
          </div>

          <div className="action-menu">
            <button type="button" className="action-trigger" aria-haspopup="true">
              Daily Quiz
            </button>
            <div className="action-menu-panel" role="menu" aria-label="Daily Quiz Actions">
              <a className="action-menu-item" href="#daily-quiz-realistic-interview-style">
                Read here
              </a>
              <a className="action-menu-item" href={withBase(quizPdfPath)} target="_blank" rel="noreferrer">
                Open PDF
              </a>
            </div>
          </div>

          <div className="action-menu">
            <button type="button" className="action-trigger" aria-haspopup="true">
              Interview Drill
            </button>
            <div className="action-menu-panel" role="menu" aria-label="Interview Drill Actions">
              <a className="action-menu-item" href="#interview-drill">
                Read here
              </a>
              <a
                className="action-menu-item"
                href={withBase(interviewPdfPath)}
                target="_blank"
                rel="noreferrer"
              >
                Open PDF
              </a>
            </div>
          </div>

          <div className="action-menu">
            <button type="button" className="action-trigger" aria-haspopup="true">
              Open Notebook
            </button>
            <div className="action-menu-panel" role="menu" aria-label="Notebook Open Actions">
              <a className="action-menu-item" href={withBase(webDayNotebookPath)} target="_blank" rel="noreferrer">
                Open in app
              </a>
              <a className="action-menu-item" href={notebookGithubPath} target="_blank" rel="noreferrer">
                Open on GitHub
              </a>
              <a className="action-menu-item" href={notebookVsCodePath} target="_blank" rel="noreferrer">
                Open in VS Code
              </a>
            </div>
          </div>
        </section>

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
        {status ? <p className={`status ${statusTone}`}>{status}</p> : null}
      </aside>
    </section>
  );
}
