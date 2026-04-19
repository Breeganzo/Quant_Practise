import { requiresPersistentBackend, supabase } from "./supabase";
import type { DailyProgress, ProgressMap } from "../types";

const LOCAL_KEY_PREFIX = "quant-progress";
const PENDING_WRITES_KEY = "quant-progress-pending-writes";
const MAX_NOTES_LENGTH = 4000;
const RETRY_ATTEMPTS = 3;
const RETRY_BASE_DELAY_MS = 250;
const LOCAL_ONLY_USER_PREFIX = "local-demo-user";

interface PendingWrite {
  userId: string;
  weekNo: number;
  dayNo: number;
  completed: boolean;
  notes: string;
  queuedAt: string;
  retries: number;
}

function progressKey(weekNo: number, dayNo: number): string {
  return `${weekNo}-${dayNo}`;
}

function localStorageKey(userId: string): string {
  return `${LOCAL_KEY_PREFIX}-${userId}`;
}

function isLocalOnlyUser(userId: string): boolean {
  return userId.startsWith(LOCAL_ONLY_USER_PREFIX);
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => {
    window.setTimeout(resolve, ms);
  });
}

function normalizeNotes(notes: string): string {
  return notes.trim().slice(0, MAX_NOTES_LENGTH);
}

function validateProgressWrite(weekNo: number, dayNo: number, notes: string): void {
  if (weekNo < 1 || weekNo > 24) {
    throw new Error(`Invalid week number: ${weekNo}. Expected 1-24.`);
  }
  if (dayNo < 1 || dayNo > 7) {
    throw new Error(`Invalid day number: ${dayNo}. Expected 1-7.`);
  }
  if (notes.length > MAX_NOTES_LENGTH) {
    throw new Error(`Notes are too long. Maximum ${MAX_NOTES_LENGTH} characters.`);
  }
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

function readPendingWrites(): PendingWrite[] {
  const raw = localStorage.getItem(PENDING_WRITES_KEY);
  if (!raw) {
    return [];
  }
  try {
    return JSON.parse(raw) as PendingWrite[];
  } catch {
    return [];
  }
}

function writePendingWrites(queue: PendingWrite[]): void {
  localStorage.setItem(PENDING_WRITES_KEY, JSON.stringify(queue));
}

function queuePendingWrite(write: Omit<PendingWrite, "queuedAt" | "retries">): void {
  const queue = readPendingWrites();
  const index = queue.findIndex(
    (item) =>
      item.userId === write.userId && item.weekNo === write.weekNo && item.dayNo === write.dayNo
  );
  const pending: PendingWrite = {
    ...write,
    queuedAt: new Date().toISOString(),
    retries: 0,
  };
  if (index >= 0) {
    queue[index] = pending;
  } else {
    queue.push(pending);
  }
  writePendingWrites(queue);
}

function removeQueuedWrite(userId: string, weekNo: number, dayNo: number): void {
  const queue = readPendingWrites().filter(
    (item) => !(item.userId === userId && item.weekNo === weekNo && item.dayNo === dayNo)
  );
  writePendingWrites(queue);
}

function toDailyProgress(row: {
  week_no: number;
  day_no: number;
  completed: boolean;
  notes: string | null;
  updated_at: string;
}): DailyProgress {
  return {
    weekNo: row.week_no,
    dayNo: row.day_no,
    completed: row.completed,
    notes: row.notes ?? "",
    updatedAt: row.updated_at,
  };
}

async function withRetry<T>(action: () => Promise<T>, attempts = RETRY_ATTEMPTS): Promise<T> {
  let lastError: unknown;
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      return await action();
    } catch (error) {
      lastError = error;
      if (attempt < attempts) {
        await sleep(RETRY_BASE_DELAY_MS * 2 ** (attempt - 1));
      }
    }
  }
  throw lastError;
}

async function upsertSupabaseProgress(
  userId: string,
  weekNo: number,
  dayNo: number,
  completed: boolean,
  notes: string
): Promise<DailyProgress> {
  const client = supabase;
  if (!client) {
    throw new Error("Supabase client is not initialized.");
  }

  const data = await withRetry(async () => {
    const response = await client
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

    if (response.error) {
      throw response.error;
    }

    return response.data;
  });

  return toDailyProgress(data);
}

export async function flushPendingWrites(userId?: string): Promise<number> {
  if (userId && isLocalOnlyUser(userId)) {
    return 0;
  }

  if (!supabase) {
    return 0;
  }

  const queue = readPendingWrites();
  if (!queue.length) {
    return 0;
  }

  const remaining: PendingWrite[] = [];
  let flushed = 0;

  for (const pending of queue) {
    if (userId && pending.userId !== userId) {
      remaining.push(pending);
      continue;
    }

    try {
      await upsertSupabaseProgress(
        pending.userId,
        pending.weekNo,
        pending.dayNo,
        pending.completed,
        pending.notes
      );
      flushed += 1;
    } catch {
      remaining.push({
        ...pending,
        retries: pending.retries + 1,
      });
    }
  }

  writePendingWrites(remaining);
  return flushed;
}

export async function fetchProgress(userId: string): Promise<ProgressMap> {
  if (isLocalOnlyUser(userId)) {
    return readLocalProgress(userId);
  }

  if (!supabase) {
    if (requiresPersistentBackend) {
      throw new Error("Supabase configuration is required in production mode.");
    }
    return readLocalProgress(userId);
  }

  await flushPendingWrites(userId);

  const { data, error } = await supabase
    .from("daily_progress")
    .select("week_no, day_no, completed, notes, updated_at")
    .eq("user_id", userId);

  if (error) {
    throw error;
  }

  const map: ProgressMap = {};
  for (const row of data ?? []) {
    const item = toDailyProgress(row);
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
  validateProgressWrite(weekNo, dayNo, notes);
  const normalizedNotes = normalizeNotes(notes);

  if (isLocalOnlyUser(userId)) {
    const map = readLocalProgress(userId);
    const item: DailyProgress = {
      weekNo,
      dayNo,
      completed,
      notes: normalizedNotes,
      updatedAt: new Date().toISOString(),
    };
    map[progressKey(weekNo, dayNo)] = item;
    writeLocalProgress(userId, map);
    return item;
  }

  if (!supabase) {
    if (requiresPersistentBackend) {
      throw new Error("Supabase configuration is required in production mode.");
    }
    const map = readLocalProgress(userId);
    const item: DailyProgress = {
      weekNo,
      dayNo,
      completed,
      notes: normalizedNotes,
      updatedAt: new Date().toISOString(),
    };
    map[progressKey(weekNo, dayNo)] = item;
    writeLocalProgress(userId, map);
    return item;
  }

  try {
    const item = await upsertSupabaseProgress(userId, weekNo, dayNo, completed, normalizedNotes);
    removeQueuedWrite(userId, weekNo, dayNo);
    return item;
  } catch {
    queuePendingWrite({
      userId,
      weekNo,
      dayNo,
      completed,
      notes: normalizedNotes,
    });
    throw new Error(
      "Unable to reach Supabase right now. Your update was queued and will retry when the connection is restored."
    );
  }
}
