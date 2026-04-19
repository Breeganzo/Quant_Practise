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
            <header>
              <h3>
                Week {week.week.toString().padStart(2, "0")}: {week.theme}
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
                    D{day.day}: {day.title} ({day.durationHours}h)
                  </Link>
                );
              })}
            </div>

            <div className="week-resources">
              <h4>Week Resources</h4>
              {week.resources ? (
                <>
                  <a href={withBase(week.resources.notebookPath)} target="_blank" rel="noreferrer">
                    Open week notebook (web)
                  </a>
                  <a href={withBase(week.resources.overviewPath)} target="_blank" rel="noreferrer">
                    Open weekly overview
                  </a>
                  <a href={withBase(week.resources.quizPath)} target="_blank" rel="noreferrer">
                    Open weekly quiz
                  </a>
                  <Link to={`/week/${week.week}/day/6#completion-checklist`}>
                    Open revision checklist (interactive)
                  </Link>
                  <Link to={`/week/${week.week}/day/7#completion-checklist`}>
                    Open mini-project checklist (interactive)
                  </Link>
                  <a href={withBase(week.resources.revisionChecklistPath)} target="_blank" rel="noreferrer">
                    Open revision checklist source
                  </a>
                  <a href={withBase(week.resources.miniProjectPath)} target="_blank" rel="noreferrer">
                    Open mini-project template source
                  </a>
                  <a href={githubBlobUrl(weekNotebookRepoPath)} target="_blank" rel="noreferrer">
                    Open week notebook source (GitHub)
                  </a>
                </>
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
