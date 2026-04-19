import { Link } from "react-router-dom";
import { githubBlobUrl, withBase } from "../lib/path";
import type { CurriculumIndex, ProgressMap } from "../types";

interface LearningDashboardProps {
  curriculum: CurriculumIndex;
  progress: ProgressMap;
}

function keyFor(weekNo: number, dayNo: number): string {
  return `${weekNo}-${dayNo}`;
}

export default function LearningDashboard({
  curriculum,
  progress,
}: LearningDashboardProps): JSX.Element {
  return (
    <section className="dashboard-grid">
      {curriculum.weeks.map((week) => {
        const completedDays = week.days.filter((day) => progress[keyFor(week.week, day.day)]?.completed).length;
        const completionRate = Math.round((completedDays / week.days.length) * 100);
        const weekNotebookRepoPath = `notebooks/${week.id}/${week.id}-learning.ipynb`;

        return (
          <article key={week.id} className="card week-card">
            <header className="week-head">
              <p className="week-kicker">Week {week.week.toString().padStart(2, "0")}</p>
              <h3>
                {week.theme}
              </h3>
              <p>{week.objective}</p>
            </header>

            <div className="week-progress">
              <div className="progress-label">
                <span>{completedDays}/{week.days.length} days complete</span>
                <span>{completionRate}%</span>
              </div>
              <div className="progress-track">
                <div className="progress-fill" style={{ width: `${completionRate}%` }} />
              </div>
            </div>

            <div className="day-links">
              {week.days.map((day) => {
                const item = progress[keyFor(week.week, day.day)];
                const complete = Boolean(item?.completed);
                return (
                  <Link
                    key={`${week.id}-${day.day}`}
                    to={`/week/${week.week}/day/${day.day}`}
                    className={`day-link ${complete ? "complete" : "pending"}`}
                  >
                    <span className="day-index">Day {day.day}</span>
                    <span className="day-title">{day.title}</span>
                    <span className="day-hours">{day.durationHours}h</span>
                  </Link>
                );
              })}
            </div>

            <div className="week-resources">
              <h4>Week Deliverables</h4>
              {week.resources ? (
                <div className="resource-links">
                  <a className="resource-link" href={withBase(week.resources.notebookPath)} target="_blank" rel="noreferrer">
                    Interactive week notebook
                  </a>
                  <a className="resource-link" href={withBase(week.resources.overviewPath)} target="_blank" rel="noreferrer">
                    Weekly overview brief
                  </a>
                  <a className="resource-link" href={withBase(week.resources.quizPath)} target="_blank" rel="noreferrer">
                    Weekly quiz pack
                  </a>
                  <Link className="resource-link" to={`/week/${week.week}/day/6#completion-checklist`}>
                    Revision checklist (interactive)
                  </Link>
                  <Link className="resource-link" to={`/week/${week.week}/day/7#completion-checklist`}>
                    Mini-project checklist (interactive)
                  </Link>
                  <a className="resource-link" href={withBase(week.resources.revisionChecklistPath)} target="_blank" rel="noreferrer">
                    Revision checklist source
                  </a>
                  <a className="resource-link" href={withBase(week.resources.miniProjectPath)} target="_blank" rel="noreferrer">
                    Mini-project template source
                  </a>
                  <a className="resource-link" href={githubBlobUrl(weekNotebookRepoPath)} target="_blank" rel="noreferrer">
                    Open-source notebook source (GitHub)
                  </a>
                </div>
              ) : (
                <p className="resource-muted">Week resource links will appear after curriculum sync.</p>
              )}
            </div>
          </article>
        );
      })}
    </section>
  );
}
