import { createClient } from "@supabase/supabase-js";

type RuntimeConfig = {
  supabaseUrl?: string;
  supabaseAnonKey?: string;
};

const runtimeConfig =
  typeof window !== "undefined" && (window as { __QUANT_CONFIG__?: RuntimeConfig }).__QUANT_CONFIG__
    ? (window as { __QUANT_CONFIG__?: RuntimeConfig }).__QUANT_CONFIG__
    : {};

const supabaseUrl = (runtimeConfig?.supabaseUrl || import.meta.env.VITE_SUPABASE_URL || "").trim();
const supabaseAnonKey = (
  runtimeConfig?.supabaseAnonKey || import.meta.env.VITE_SUPABASE_ANON_KEY || ""
).trim();

export const isProductionBuild = import.meta.env.PROD;
export const requiresPersistentBackend = false;

export const hasSupabaseConfig = Boolean(supabaseUrl && supabaseAnonKey);

export const supabase = hasSupabaseConfig
  ? createClient(supabaseUrl!, supabaseAnonKey!, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
      },
    })
  : null;
