# Week 05 Day 02: Linear regression baselines

## Study Duration
- Planned effort: 6-10 hours/day
- Required minimum: 6 hours (core + required extension); optional deep work extends to 10 hours.

## 6-10 Hour Daily Structure
- **Core Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Core Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Core Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Core Block 4 (60 min):** Python/pandas implementation and output verification.
- **Core Block 5 (30 min):** Practice questions, interview drill, and reflection.
- **Required Extension Block A (60 min):** Re-run the real trading example with one alternate ticker and one stress window.
- **Required Extension Block B (60 min):** Restart kernel and rerun all coding cells end-to-end, then add one extra validation test.
- **Optional Deep Work (0-4 hours):** Expand diagnostics, add edge-case tests, and improve interview-ready explanations.

## Why It Matters in Quant
Rebuild core supervised learning intuition with finance-aware validation discipline.

## Continuity and Handoff
- Previous checkpoint: Week 05 Day 01: Supervised learning setup and leakage controls
- Previous lesson file: content/week-05/day-01.md
- Today's deliverable: Train and evaluate a baseline regression with residual plots.
- Next handoff target: Week 05 Day 03: Logistic regression for directional signals
- Next lesson file: content/week-05/day-03.md

## Theory Concepts

### Concept 1: Bias-variance tradeoff
Bias-variance tradeoff is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Interpretability of coefficients
Interpretability of coefficients is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Residual diagnostics
Residual diagnostics is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

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
- Day objective: Fit a linear model on synthetic factor-style features.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Linear regression baselines'.

## Step-by-Step Solved Problems
### Solved Problem 1: Convert logit to probability
Given:
- Model score z = -0.100.
Solution:
1. $p=\frac{1}{1+e^{-z}}$.
2. p = 1/(1+exp(--0.100)) = 0.475021.
Final answer: Predicted probability = 47.50%.
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
2. Implement today's objective as reusable functions: Train and evaluate a baseline regression with residual plots.
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
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 05 Day 02): Explain Logistic Probability and define every symbol clearly for a post-earnings momentum regime where feature drift is elevated.
   - Model answer: "I use Logistic Probability as a decision bridge from market observations to position sizing. The formula is $p=\frac{1}{1+e^{-z}}$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then freeze new model entries when calibration error worsens for 3 consecutive windows. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify strict train/validation timestamp split, no forward-filled target leakage, and feature freshness checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Linear regression baselines' matter in live trading systems?
   - Model answer: "Linear regression baselines matters because model decisions fail quickly without leakage controls, drift monitoring, and threshold governance. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I pause new signals, revert to baseline model, and relaunch only after calibration recovers. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Linear regression baselines in a model-risk review after prediction drift and weaker precision."
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
When is a weak but interpretable model preferable?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Full notebook rerun completed from clean kernel
- [ ] Reflection logged in progress tracker
