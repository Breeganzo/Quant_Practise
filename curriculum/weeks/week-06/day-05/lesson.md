# Week 06 Day 05: Model diagnostics and monitoring

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Advance supervised modeling with non-linear learners and robust model diagnostics.

## Continuity and Handoff
- Previous checkpoint: Week 06 Day 04: Feature engineering and selection
- Previous lesson file: content/week-06/day-04.md
- Today's deliverable: Implement drift diagnostics on feature distributions.
- Next handoff target: Week 06 Day 06: Revision Sprint
- Next lesson file: content/week-06/day-06.md

## Theory Concepts

### Concept 1: Calibration and reliability
Calibration and reliability should be treated as a measurable component of 'Supervised ML II: trees, ensembles, and diagnostics'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Drift detection basics
Drift detection basics should be treated as a measurable component of 'Supervised ML II: trees, ensembles, and diagnostics'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Error slicing by regime
Error slicing by regime should be treated as a measurable component of 'Supervised ML II: trees, ensembles, and diagnostics'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Ridge Penalty
$$
\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2
$$
Regularized stability control.

### Formula 2: Forward Target
$$
y_t=\mathbb{1}[r_{t+1}>0]
$$
Label must stay forward-looking.

### Formula 3: Logistic Probability
$$
p=\frac{1}{1+e^{-z}}
$$
Convert score to probability.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $\hat{y}$: model prediction
- $\lambda$: regularization parameter
- $TP,FP,FN$: confusion counts

## Real Trading Example
- Instruments: SPY, XLK, XLF, XLE
- Macro overlay (FRED): DFF, VIXCLS
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Analyze model errors during high-volatility periods.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Model diagnostics and monitoring'.

## Step-by-Step Solved Problems
### Solved Problem 1: Convert logit to probability
Given:
- Model score z = 0.800.
Solution:
1. $p=\frac{1}{1+e^{-z}}$.
2. p = 1/(1+exp(-0.800)) = 0.689974.
Final answer: Predicted probability = 69.00%.

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

### Solved Problem 3: Compute ridge objective
Given:
- MSE = 0.0410, ||beta||_2^2 = 1.90, lambda = 0.06.
Solution:
1. $\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2$.
2. L = 0.0410 + 0.06*1.90 = 0.1550.
Final answer: Ridge objective = 0.1550.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement drift diagnostics on feature distributions.
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

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
What monitoring trigger would force model retraining?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
