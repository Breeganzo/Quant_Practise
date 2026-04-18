import type { CurriculumIndex } from "../types";
import { withBase } from "./path";

export async function loadCurriculum(): Promise<CurriculumIndex> {
  const response = await fetch(withBase("data/curriculum.json"));
  if (!response.ok) {
    throw new Error("Unable to load curriculum index.");
  }
  return (await response.json()) as CurriculumIndex;
}

export async function loadLessonMarkdown(lessonPath: string): Promise<string> {
  const response = await fetch(withBase(lessonPath));
  if (!response.ok) {
    throw new Error(`Unable to load lesson content: ${lessonPath}`);
  }
  return response.text();
}
