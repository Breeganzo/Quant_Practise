# Week 07 Day 02: K-means and hierarchical clustering

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Use unsupervised methods to detect latent structure and regime behavior in financial data.

## Continuity and Handoff
- Previous checkpoint: Week 07 Day 01: Unsupervised problem framing
- Previous lesson file: content/week-07/day-01.md
- Today's deliverable: Run k-means for multiple k values and evaluate silhouette trend.
- Next handoff target: Week 07 Day 03: PCA for regime and factor hints
- Next lesson file: content/week-07/day-03.md

## Theory Concepts

### Concept 1: Centroid-based clustering
Centroid-based clustering should be treated as a measurable component of 'Unsupervised learning and market regimes'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Cluster validity intuition
Cluster validity intuition should be treated as a measurable component of 'Unsupervised learning and market regimes'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Hierarchical dendrogram interpretation
Hierarchical dendrogram interpretation should be treated as a measurable component of 'Unsupervised learning and market regimes'. For this week, emphasize causal feature design, leakage control, and robust model validation. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Logistic Probability
$$
p=\frac{1}{1+e^{-z}}
$$
Convert score to probability.

### Formula 2: MSE
$$
\mathcal{L}_{MSE}=\frac{1}{n}\sum_i(y_i-\hat{y}_i)^2
$$
Baseline regression loss.

### Formula 3: Cross-Entropy
$$
\mathcal{L}_{CE}=-\frac{1}{n}\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
$$
Classification objective.

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
- Day objective: Cluster synthetic market states and compare cluster compactness.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'K-means and hierarchical clustering'.

## Step-by-Step Solved Problems
### Solved Problem 1: Convert logit to probability
Given:
- Model score z = -0.100.
Solution:
1. $p=\frac{1}{1+e^{-z}}$.
2. p = 1/(1+exp(--0.100)) = 0.475021.
Final answer: Predicted probability = 47.50%.

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
2. Implement today's objective as reusable functions: Run k-means for multiple k values and evaluate silhouette trend.
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
What indicates cluster instability across rolling windows?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
