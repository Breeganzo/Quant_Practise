export type DayType = "lesson" | "revision" | "project";

export interface DayEntry {
  day: number;
  title: string;
  durationHours: number;
  type: DayType;
  lessonPath: string;
}

export interface WeekEntry {
  week: number;
  id: string;
  theme: string;
  objective: string;
  days: DayEntry[];
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
