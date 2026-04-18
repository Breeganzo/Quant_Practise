import { supabase } from "./supabase";
import type { DailyProgress, ProgressMap } from "../types";

const LOCAL_KEY_PREFIX = "quant-progress";

function progressKey(weekNo: number, dayNo: number): string {
  return `${weekNo}-${dayNo}`;
}

function localStorageKey(userId: string): string {
  return `${LOCAL_KEY_PREFIX}-${userId}`;
}

function readLocalProgress(userId: string): ProgressMap {
  const raw = localStorage.getItem(localStorageKey(userId));
  if (!raw) {
    return {};
  }
  try {
    return JSON.parse(raw) as ProgressMap;
  } catch {
    return {};
  }
}

function writeLocalProgress(userId: string, map: ProgressMap): void {
  localStorage.setItem(localStorageKey(userId), JSON.stringify(map));
}

export async function fetchProgress(userId: string): Promise<ProgressMap> {
  if (!supabase) {
    return readLocalProgress(userId);
  }

  const { data, error } = await supabase
    .from("daily_progress")
    .select("week_no, day_no, completed, notes, updated_at")
    .eq("user_id", userId);

  if (error) {
    throw error;
  }

  const map: ProgressMap = {};
  for (const row of data ?? []) {
    const item: DailyProgress = {
      weekNo: row.week_no,
      dayNo: row.day_no,
      completed: row.completed,
      notes: row.notes ?? "",
      updatedAt: row.updated_at,
    };
    map[progressKey(item.weekNo, item.dayNo)] = item;
  }
  return map;
}

export async function upsertProgress(
  userId: string,
  weekNo: number,
  dayNo: number,
  completed: boolean,
  notes: string
): Promise<DailyProgress> {
  if (!supabase) {
    const map = readLocalProgress(userId);
    const item: DailyProgress = {
      weekNo,
      dayNo,
      completed,
      notes,
      updatedAt: new Date().toISOString(),
    };
    map[progressKey(weekNo, dayNo)] = item;
    writeLocalProgress(userId, map);
    return item;
  }

  const { data, error } = await supabase
    .from("daily_progress")
    .upsert(
      {
        user_id: userId,
        week_no: weekNo,
        day_no: dayNo,
        completed,
        notes,
      },
      {
        onConflict: "user_id,week_no,day_no",
      }
    )
    .select("week_no, day_no, completed, notes, updated_at")
    .single();

  if (error) {
    throw error;
  }

  return {
    weekNo: data.week_no,
    dayNo: data.day_no,
    completed: data.completed,
    notes: data.notes ?? "",
    updatedAt: data.updated_at,
  };
}
