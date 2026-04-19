# Week 19 Quiz

## Instructions
- Attempt each question in interview format first (spoken answer in <60 seconds).
- Then compare with the model answer and self-score for clarity, correctness, and risk awareness.
- Target score: 8/10 or higher.

## Interview Questions and Exact Model Answers
### 1. Real interview question: How would you explain 'Agentic workflow design for research' to a PM in under one minute?
Model answer:
"I present Agentic workflow design for research as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would write prompt templates with strict output schema."
### 2. Real interview question: How would you explain 'Research summarization and retrieval' to a PM in under one minute?
Model answer:
"I present Research summarization and retrieval as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would create a retrieval-and-summary template with citation slots."
### 3. Real interview question: How would you explain 'Feature idea generation and validation' to a PM in under one minute?
Model answer:
"I present Feature idea generation and validation as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would build a feature ideation checklist from agent outputs."
### 4. Real interview question: How would you explain 'Code review and experiment tracking agents' to a PM in under one minute?
Model answer:
"I present Code review and experiment tracking agents as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would generate experiment log template with required fields."
### 5. Real interview question: How would you explain 'Guardrails and risk management for AI use' to a PM in under one minute?
Model answer:
"I present Guardrails and risk management for AI use as a decision workflow for liquidity stress and crowding unwind. Step one: define notation, units, and assumptions clearly. Step two: show one numeric result on a real ticker and state its decision impact. Step three: enforce a guardrail (throttle sizing when implementation shortfall worsens) and explain the fallback path if it fails. For implementation, I would implement an agent-output validation checklist file."
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
