# Week 22 Quiz

## Instructions
- Attempt each question in interview format first (spoken answer in <60 seconds).
- Then compare with the model answer and self-score for clarity, correctness, and risk awareness.
- Target score: 8/10 or higher.

## Interview Questions and Exact Model Answers
### 1. Real interview question: How would you explain 'Probability drill framework' to a PM in under one minute?
Model answer:
"I frame probability drill framework as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to create a probability drill notebook with timed question sets. and log edge cases."
### 2. Real interview question: How would you explain 'Statistics and estimation interview drills' to a PM in under one minute?
Model answer:
"I frame statistics and estimation interview drills as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to generate short stats-question answer templates. and log edge cases."
### 3. Real interview question: How would you explain 'Python coding speed drills' to a PM in under one minute?
Model answer:
"I frame python coding speed drills as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to build a local timed coding drill harness. and log edge cases."
### 4. Real interview question: How would you explain 'SQL and data manipulation interview drills' to a PM in under one minute?
Model answer:
"I frame sql and data manipulation interview drills as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to create sql practice file with expected outputs. and log edge cases."
### 5. Real interview question: How would you explain 'Mock round synthesis' to a PM in under one minute?
Model answer:
"I frame mock round synthesis as a production decision tool, not just a classroom concept. First, I define the core notation and units. Second, I run one real-market example and state the numeric result. Third, I translate the output into a trade action plus one explicit risk guardrail. For implementation, I build reusable code to log mock performance and classify errors by type. and log edge cases."
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
