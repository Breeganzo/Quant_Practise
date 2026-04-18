# Week 11 Quiz

## Instructions
- Attempt each question in interview format first (spoken answer in <60 seconds).
- Then compare with the model answer and self-score for clarity, correctness, and risk awareness.
- Target score: 8/10 or higher.

## Interview Questions and Exact Model Answers
### 1. Real interview question: How would you explain 'Backtest design patterns' to a PM in under one minute?
Model answer:
"I frame backtest design patterns as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to implement a backtest skeleton with clear interfaces. and log edge cases."
### 2. Real interview question: How would you explain 'Data and look-ahead bias controls' to a PM in under one minute?
Model answer:
"I frame data and look-ahead bias controls as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to add strict timestamp checks to data pipeline. and log edge cases."
### 3. Real interview question: How would you explain 'Transaction costs and slippage' to a PM in under one minute?
Model answer:
"I frame transaction costs and slippage as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to integrate cost model into backtest calculations. and log edge cases."
### 4. Real interview question: How would you explain 'Position sizing and risk constraints' to a PM in under one minute?
Model answer:
"I frame position sizing and risk constraints as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to implement risk constraint layer in backtest flow. and log edge cases."
### 5. Real interview question: How would you explain 'Performance attribution and diagnostics' to a PM in under one minute?
Model answer:
"I frame performance attribution and diagnostics as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to generate attribution report tables for each strategy run. and log edge cases."
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
