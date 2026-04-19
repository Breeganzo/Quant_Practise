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

export function githubDevUrl(path: string): string {
  const repo =
    (import.meta.env.VITE_REPO_URL as string | undefined) ||
    "https://github.com/Breeganzo/Quant_Practise";
  const cleanRepo = repo.replace(/\/$/, "");
  const cleanPath = path.startsWith("/") ? path.slice(1) : path;

  const match = cleanRepo.match(/^https?:\/\/github\.com\/([^/]+)\/([^/]+)$/i);
  if (!match) {
    return `${cleanRepo}/blob/main/${cleanPath}`;
  }

  const owner = match[1];
  const name = match[2];
  return `https://github.dev/${owner}/${name}/blob/main/${cleanPath}`;
}
