# Week 07 Day 07: Portfolio Project

## Study Duration
- Planned effort: 6-10 hours/day
- Required minimum: 6 hours for implementation, validation, and communication drills.

## 6-10 Hour Daily Structure
- **Core Block 1 (60 min):** Restate objective, assumptions, and measurable success criteria.
- **Core Block 2 (75 min):** Build/clean data pipeline and verify timestamp integrity.
- **Core Block 3 (75 min):** Implement project logic and validate formulas against spot checks.
- **Core Block 4 (60 min):** Produce diagnostics, stress checks, and fallback pathways.
- **Core Block 5 (45 min):** Deliver interview-style defense with risk controls and escalation.
- **Required Extension Block A (60 min):** Re-run project on alternate assumptions and compare drift.
- **Required Extension Block B (60 min):** Prepare production memo and launch/no-launch decision log.
- **Optional Deep Work (0-4 hours):** Expand tests, improve monitoring, and polish stakeholder narrative.

## Why It Matters in Quant
Project day is where research quality meets execution discipline and communication quality under risk constraints.

## Continuity and Handoff
- Previous checkpoint: Week 07 Day 06: Revision Sprint
- Previous lesson file: content/week-07/day-06.md
- Today's deliverable: Regime clustering notebook
- Next handoff target: Week 08 Day 01: Pipeline architecture and feature store design
- Next lesson file: content/week-08/day-01.md

## Project Blueprint
### Project Title
Regime clustering notebook

### Problem Statement
Detect and interpret market regimes using clustering and PCA features.

### Data Sources
- Returns
- Rolling volatility
- Volume anomalies

### Implementation Steps
1. Engineer regime-sensitive features
2. Run clustering methods
3. Validate cluster quality
4. Map regimes to strategy behavior
5. Write actionable insights

### Evaluation Metrics
- Silhouette score
- Cluster persistence
- Interpretability
- Strategy differentiation

### Execution Standard
- [ ] Notebook/script runs from clean start without hidden state
- [ ] Outputs include at least one diagnostic table and one chart
- [ ] One explicit risk guardrail and fallback action are documented

### Deliverables
- Notebook or script output
- One-page summary memo
- Tracker update with completion and lessons learned

## Mathematical Foundations (LaTeX)
### Formula 1: Logistic Probability
$$
p=\frac{1}{1+e^{-z}}
$$
**Plain-English interpretation:** Convert score to probability.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Use a walk-forward split and verify the metric does not leak future labels into feature construction.

### Formula 2: MSE
$$
\mathcal{L}_{MSE}=\frac{1}{n}\sum_i(y_i-\hat{y}_i)^2
$$
**Plain-English interpretation:** Baseline regression loss.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the same metric on train and out-of-sample windows and explain any degradation.

### Formula 3: Cross-Entropy
$$
\mathcal{L}_{CE}=-\frac{1}{n}\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
$$
**Plain-English interpretation:** Classification objective.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Stress this metric under class imbalance and describe one mitigation you would implement.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50$ |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $\hat{y}$ | Model prediction | class/probability | 0.73 |
| $\lambda$ | Regularization strength | non-negative scalar | 0.10 |
| $TP,FP,FN$ | Confusion matrix counts | integer count | TP=52 |

## Real Trading Example
- Instruments: SPY, XLK, XLF, XLE
- Macro overlay (FRED): DFF, VIXCLS
- Suggested window: 2018-01-01 to 2026-03-31
- Stress windows to inspect: 2020-11 to 2021-03, 2022-06 to 2022-11
- Scenario context: post-earnings dispersion with elevated feature drift
- Day objective: Deliver a capstone-quality notebook and summarize one trade-off under stress assumptions.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Portfolio Project'.

## Step-by-Step Solved Problems
### Solved Problem 1: Convert logit to probability
Given:
- Model score z = 1.400.
Solution:
1. $p=\frac{1}{1+e^{-z}}$.
2. p = 1/(1+exp(-1.400)) = 0.802184.
Final answer: Predicted probability = 80.22%.
Common trap: Using forward labels with backward-filled features, which silently introduces leakage.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Compute precision, recall, F1
Given:
- TP=50, FP=12, FN=18.
Solution:
1. $Precision=\frac{TP}{TP+FP}$.
2. Precision=0.8065.
3. $Recall=\frac{TP}{TP+FN}$.
4. Recall=0.7353.
5. $F1=\frac{2PR}{P+R}$.
6. F1=0.7692.
Final answer: Precision=80.65%, Recall=73.53%, F1=76.92%.
Common trap: Using forward labels with backward-filled features, which silently introduces leakage.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute ridge objective
Given:
- MSE = 0.0410, ||beta||_2^2 = 1.90, lambda = 0.06.
Solution:
1. $\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2$.
2. L = 0.0410 + 0.06*1.90 = 0.1550.
Final answer: Ridge objective = 0.1550.
Common trap: Using forward labels with backward-filled features, which silently introduces leakage.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Ship the project notebook with reproducible outputs, controls, and one escalation rule.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
X_train, X_valid, y_train, y_valid = temporal_split(features, target)
model = fit_logistic_regression(X_train, y_train, l2=0.1)
proba = model.predict_proba(X_valid)[:, 1]
report = classification_report_from_thresholds(y_valid, proba)
```

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. State project objective and one hard failure condition in under 45 seconds.
2. Validate one formula output against a manual spot-check.
3. Show one stress scenario where your decision changes and explain why.
4. Add one edge-case test and one fallback rule to the notebook.
5. Deliver a one-minute PM summary with one risk guardrail.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 07 Day 07): Explain Logistic Probability and define every symbol clearly for a post-earnings momentum regime where feature drift is elevated.
   - Model answer: "I use Logistic Probability as a decision bridge from market observations to position sizing. The formula is $p=\frac{1}{1+e^{-z}}$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then freeze new model entries when calibration error worsens for 3 consecutive windows. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify strict train/validation timestamp split, no forward-filled target leakage, and feature freshness checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Portfolio Project' matter in live trading systems?
   - Model answer: "Portfolio Project matters because model decisions fail quickly without leakage controls, drift monitoring, and threshold governance. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I pause new signals, revert to baseline model, and relaunch only after calibration recovers. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Portfolio Project in a model-risk review after prediction drift and weaker precision."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision under constraints.
  3. Awareness of edge cases, costs, and failure modes.
  4. Clear escalation rule when guardrails are breached.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula, assumptions, and validation checks clearly.
  - Decision: explain one actionable rule, one risk guardrail, and one fallback action.

## Required Extension Track (2+ Hours)
- Re-run today's notebook from a fresh kernel so outputs are reproducible without hidden state.
- Add one additional risk guardrail and verify how it changes trade/no-trade decisions.
- Document one failure mode, one mitigation, and one escalation rule for production use.

Extension completion checks:
- [ ] Notebook restarted and all coding cells rerun successfully
- [ ] At least one extra validation/edge-case test added
- [ ] Risk guardrail and fallback action documented

## Reflection Question
What single risk control would block launch today, and what evidence would clear it?

## Completion Checklist
- [ ] Project notebook runs cleanly from fresh kernel
- [ ] Risk guardrail and fallback action documented
- [ ] Stress scenario comparison completed
- [ ] One-page summary memo finalized
- [ ] Launch/no-launch decision recorded with evidence
