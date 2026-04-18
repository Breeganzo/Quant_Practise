import { FormEvent, useState } from "react";
import { supabase } from "../lib/supabase";

interface AuthPanelProps {
  onAuthSuccess: () => void;
}

export default function AuthPanel({ onAuthSuccess }: AuthPanelProps): JSX.Element {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function handleSignIn(event: FormEvent): Promise<void> {
    event.preventDefault();
    if (!supabase) {
      setError("Supabase is not configured.");
      return;
    }

    setLoading(true);
    setError("");
    setMessage("");

    const { error: signInError } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (signInError) {
      setError(signInError.message);
    } else {
      setMessage("Signed in successfully.");
      onAuthSuccess();
    }

    setLoading(false);
  }

  async function handleSignUp(): Promise<void> {
    if (!supabase) {
      setError("Supabase is not configured.");
      return;
    }

    setLoading(true);
    setError("");
    setMessage("");

    const { error: signUpError } = await supabase.auth.signUp({
      email,
      password,
    });

    if (signUpError) {
      setError(signUpError.message);
    } else {
      setMessage("Sign-up successful. Check your email for confirmation if required.");
    }

    setLoading(false);
  }

  return (
    <section className="card auth-card">
      <h2>Private Login</h2>
      <p>Use your account to persist progress in Supabase for long-term tracking.</p>
      <form onSubmit={handleSignIn} className="auth-form">
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          required
        />

        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          minLength={8}
          required
        />

        <div className="auth-actions">
          <button type="submit" disabled={loading}>
            {loading ? "Signing in..." : "Sign In"}
          </button>
          <button type="button" onClick={handleSignUp} disabled={loading} className="secondary">
            {loading ? "Please wait..." : "Create Account"}
          </button>
        </div>
      </form>
      {message ? <p className="status ok">{message}</p> : null}
      {error ? <p className="status error">{error}</p> : null}
    </section>
  );
}
