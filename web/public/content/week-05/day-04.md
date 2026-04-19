# Week 05 Day 04: Model evaluation metrics

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Rebuild core supervised learning intuition with finance-aware validation discipline.

## Continuity and Handoff
- Previous checkpoint: Week 05 Day 03: Logistic regression for directional signals
- Previous lesson file: content/week-05/day-03.md
- Today's deliverable: Implement metric dashboard functions for model comparison.
- Next handoff target: Week 05 Day 05: Regularization and generalization
- Next lesson file: content/week-05/day-05.md

## Theory Concepts

### Concept 1: MAE/RMSE for regression
MAE/RMSE for regression is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Precision, recall, F1, AUC for classification
Precision, recall, F1, AUC for classification is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Economic utility versus statistical metrics
Economic utility versus statistical metrics is a core part of 'Supervised ML I: regression and classification'. Start with notation discipline: define labels, feature windows, and leakage boundaries before fitting any model. Then focus on causal feature design, leakage control, and robust model validation by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Cross-Entropy
$$
\mathcal{L}_{CE}=-\frac{1}{n}\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
$$
**Plain-English interpretation:** Classification objective.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Use a walk-forward split and verify the metric does not leak future labels into feature construction.

### Formula 2: Ridge Penalty
$$
\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2
$$
**Plain-English interpretation:** Regularized stability control.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Use a walk-forward split and verify the metric does not leak future labels into feature construction.

### Formula 3: Forward Target
$$
y_t=\mathbb{1}[r_{t+1}>0]
$$
**Plain-English interpretation:** Label must stay forward-looking.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Use a walk-forward split and verify the metric does not leak future labels into feature construction.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
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
- Day objective: Compare two classifiers with similar AUC but different precision-recall balance.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Model evaluation metrics'.

## Step-by-Step Solved Problems
### Solved Problem 1: Convert logit to probability
Given:
- Model score z = 0.500.
Solution:
1. $p=\frac{1}{1+e^{-z}}$.
2. p = 1/(1+exp(-0.500)) = 0.622459.
Final answer: Predicted probability = 62.25%.
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

### Solved Problem 4: Position sizing with volatility guardrail
Given:
- Strategy annualized volatility estimate is 0.174.
- Portfolio risk budget target is 0.20.
- Position multiplier rule: scale = target_vol / strategy_vol, clipped to [0.20, 1.00].
Solution:
1. Compute raw scale = target_vol / strategy_vol.
2. raw_scale = 0.20/0.174 = 1.1494.
3. clipped_scale = min(1.00, max(0.20, 1.1494)) = 1.0000.
Final answer: Position multiplier = 1.0000.
Common trap: Ignoring volatility regime shifts and applying static position size in stressed markets.
Interpretation: State how this guardrail changes gross exposure before deployment.
## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement metric dashboard functions for model comparison.
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
1. PM interview question (Week 05 Day 04): Explain Cross-Entropy and define every symbol clearly.
   - Model answer: "I use Cross-Entropy to convert raw prices into a decision-ready metric. The formula is $\mathcal{L}_{CE}=-\frac{1}{n}\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Model evaluation metrics' matter in live trading systems?
   - Model answer: "Model evaluation metrics matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Model evaluation metrics as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## 2-Hour Extension Track (Required)

This section upgrades the day to a full 6-hour study model: 4-hour core lesson + 2-hour required extension.

- **Extension Block A (45 min):** Real-market case expansion.
  - Re-run today's workflow on one additional asset and one stress regime window.
  - Document one regime-specific failure mode and one mitigation rule.
- **Extension Block B (45 min):** Production-quality coding refinement.
  - Add one assertion for data integrity and one assertion for risk limits.
  - Save a short result table with assumptions, metric values, and decision rationale.
- **Extension Block C (30 min):** Interview simulation and review.
  - Deliver a 60-second PM pitch and a 60-second risk-manager response.
  - Include one numeric example from Week 05 Day 04 to prove notation fluency.

Extension completion checks:
- [ ] Stress-regime comparison completed
- [ ] Production guardrail assertions added and passed
- [ ] Interview simulation recorded with one numeric example
## Reflection Question
Which metric aligns best with your intended strategy objective?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
