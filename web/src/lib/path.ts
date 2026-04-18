export function appBase(): string {
  const base = import.meta.env.BASE_URL || "/";
  return base.endsWith("/") ? base : `${base}/`;
}

export function withBase(relativePath: string): string {
  const clean = relativePath.startsWith("/") ? relativePath.slice(1) : relativePath;
  return `${appBase()}${clean}`;
}

export function githubBlobUrl(path: string): string {
  const repo =
    (import.meta.env.VITE_REPO_URL as string | undefined) ||
    "https://github.com/Breeganzo/Quant_Practise";
  return `${repo.replace(/\/$/, "")}/blob/main/${path}`;
}
