import type { CurriculumIndex } from "../types";
import { withBase } from "./path";

const FETCH_TIMEOUT_MS = 12000;
const MAX_RETRIES = 2;

async function fetchWithRetry(url: string, attempts = MAX_RETRIES + 1): Promise<Response> {
  let lastError: unknown;

  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    const controller = new AbortController();
    const timer = window.setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
    try {
      const response = await fetch(url, { signal: controller.signal });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      return response;
    } catch (error) {
      lastError = error;
      if (attempt < attempts) {
        await new Promise((resolve) => window.setTimeout(resolve, 250 * attempt));
      }
    } finally {
      window.clearTimeout(timer);
    }
  }

  throw lastError instanceof Error ? lastError : new Error("Unknown fetch failure");
}

export async function loadCurriculum(): Promise<CurriculumIndex> {
  const response = await fetchWithRetry(withBase("data/curriculum.json"));
  return (await response.json()) as CurriculumIndex;
}

export async function loadLessonMarkdown(lessonPath: string): Promise<string> {
  const response = await fetchWithRetry(withBase(lessonPath));
  return response.text();
}
