# Week 17 Quiz

## Instructions
- Attempt each question in interview format first (spoken answer in <60 seconds).
- Then compare with the model answer and self-score for clarity, correctness, and risk awareness.
- Target score: 8/10 or higher.

## Interview Questions and Exact Model Answers
### 1. Real interview question: How would you explain 'Factor investing framework' to a PM in under one minute?
Model answer:
"I present Factor investing framework as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would build factor-score computation pipeline."
### 2. Real interview question: How would you explain 'Cross-sectional regressions' to a PM in under one minute?
Model answer:
"I present Cross-sectional regressions as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would implement weekly cross-sectional regression diagnostics."
### 3. Real interview question: How would you explain 'Information coefficient and decay' to a PM in under one minute?
Model answer:
"I present Information coefficient and decay as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would build IC and decay report with horizon comparison."
### 4. Real interview question: How would you explain 'Portfolio construction for factors' to a PM in under one minute?
Model answer:
"I present Portfolio construction for factors as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would implement decile portfolio builder with turnover tracking."
### 5. Real interview question: How would you explain 'Factor robustness' to a PM in under one minute?
Model answer:
"I present Factor robustness as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would generate factor robustness dashboard."
### 6. Regime-risk question: What assumptions from this week fail first during stress markets?
Model answer:
"The first failures are distribution stability and execution-cost assumptions. In stress regimes, volatility clustering, slippage, and correlation breakdown can invalidate clean backtest behavior. I would widen thresholds, reduce leverage, and require secondary confirmation before new entries."
### 7. Metric-selection question: Which metric from this week would you prioritize for live monitoring, and why?
Model answer:
"I prioritize the metric that directly links expected edge to controllable risk. It must be interpretable, stable across windows, and easy to validate daily. I pair it with a hard risk limit metric so performance and protection are monitored together."
### 8. Implementation question: Give one concrete production guardrail you would enforce.
Model answer:
"I enforce a hard stop on position sizing when realized volatility exceeds a pre-defined threshold relative to the training regime. This prevents model overconfidence during volatility expansion and keeps drawdowns bounded while diagnostics are rerun."
### 9. Communication question: How do you summarize this week's project to non-technical stakeholders?
Model answer:
"I summarize in three lines: objective, measured result, and risk control. I avoid jargon, state one verified number, and explain the decision implication. Then I show the fallback rule if the metric deteriorates."
### 10. Verification question: What is your first check before paper-trading this week's output?
Model answer:
"My first check is full reproducibility: rerun notebook cells end-to-end and verify outputs, data timestamps, and assumptions match documented logic. If any mismatch appears, I block deployment until resolved."
