export type DayType = "lesson" | "revision" | "project";

export interface DayContinuity {
  previousLabel: string;
  previousLessonPath: string | null;
  todayDeliverable: string;
  nextLabel: string;
  nextLessonPath: string | null;
}

export interface WeekResources {
  notebookPath: string;
  overviewPath: string;
  quizPath: string;
  revisionChecklistPath: string;
  miniProjectPath: string;
}

export interface DayEntry {
  day: number;
  title: string;
  durationHours: number;
  type: DayType;
  lessonPath: string;
  continuity?: DayContinuity;
}

export interface WeekEntry {
  week: number;
  id: string;
  theme: string;
  objective: string;
  days: DayEntry[];
  resources?: WeekResources;
}

export interface CurriculumIndex {
  weeks: WeekEntry[];
}

export interface DailyProgress {
  weekNo: number;
  dayNo: number;
  completed: boolean;
  notes: string;
  updatedAt?: string;
}

export type ProgressMap = Record<string, DailyProgress>;
