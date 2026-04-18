import { Link } from "react-router-dom";
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
          </article>
        );
      })}
    </section>
  );
}
