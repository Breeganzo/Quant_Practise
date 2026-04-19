import { createClient } from "@supabase/supabase-js";

type RuntimeConfig = {
  supabaseUrl?: string;
  supabaseAnonKey?: string;
};

const PLACEHOLDER_TOKENS = [
  "YOUR_PROJECT_REF",
  "YOUR_SUPABASE_URL",
  "YOUR_PUBLISHABLE_KEY",
  "YOUR_ANON_KEY",
  "REPLACE_ME",
  "CHANGEME",
];

function normalizeConfigValue(value?: string): string {
  return (value || "").trim();
}

function hasPlaceholderToken(value: string): boolean {
  const normalized = value.toUpperCase();
  return PLACEHOLDER_TOKENS.some((token) => normalized.includes(token));
}

function isValidHttpUrl(value: string): boolean {
  try {
    const parsed = new URL(value);
    return parsed.protocol === "https:" || parsed.protocol === "http:";
  } catch {
    return false;
  }
}

function isValidSupabaseKey(value: string): boolean {
  if (!value) {
    return false;
  }

  // Supabase keys are either JWT-like tokens or newer publishable keys.
  if (value.startsWith("sb_publishable_")) {
    return true;
  }

  const jwtParts = value.split(".");
  return jwtParts.length === 3 && jwtParts.every((part) => part.length > 0);
}

function validateSupabaseConfig(url: string, key: string): string {
  if (!url && !key) {
    return "";
  }
  if (!url || !key) {
    return "Supabase configuration is incomplete. Set both URL and publishable key.";
  }
  if (hasPlaceholderToken(url) || hasPlaceholderToken(key)) {
    return "Supabase configuration still contains placeholder values.";
  }
  if (!isValidHttpUrl(url)) {
    return "Supabase URL is invalid. Expected an absolute http(s) URL.";
  }
  if (!isValidSupabaseKey(key)) {
    return "Supabase publishable key format is invalid.";
  }
  return "";
}

const runtimeConfig =
  typeof window !== "undefined" && (window as { __QUANT_CONFIG__?: RuntimeConfig }).__QUANT_CONFIG__
    ? (window as { __QUANT_CONFIG__?: RuntimeConfig }).__QUANT_CONFIG__
    : {};

const rawSupabaseUrl = normalizeConfigValue(
  runtimeConfig?.supabaseUrl || import.meta.env.VITE_SUPABASE_URL
);
const rawSupabaseAnonKey = normalizeConfigValue(
  runtimeConfig?.supabaseAnonKey || import.meta.env.VITE_SUPABASE_ANON_KEY
);

const supabaseUrl = rawSupabaseUrl.replace(/\/+$/, "");
const supabaseAnonKey = rawSupabaseAnonKey;

export const isProductionBuild = import.meta.env.PROD;
export const requiresPersistentBackend = false;

export const supabaseConfigIssue = validateSupabaseConfig(supabaseUrl, supabaseAnonKey);

export const hasSupabaseConfig = Boolean(
  !supabaseConfigIssue && supabaseUrl && supabaseAnonKey
);

export const supabase = hasSupabaseConfig
  ? createClient(supabaseUrl!, supabaseAnonKey!, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
      },
    })
  : null;
