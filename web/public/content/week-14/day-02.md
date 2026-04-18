# Week 14 Day 02: Yield curve structure

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Develop working fixed-income intuition for pricing, curve dynamics, and interest-rate risk.

## Continuity and Handoff
- Previous checkpoint: Week 14 Day 01: Bond cashflows and pricing mechanics
- Previous lesson file: content/week-14/day-01.md
- Today's deliverable: Create yield-curve plotting utility and slope diagnostics.
- Next handoff target: Week 14 Day 03: Duration and convexity
- Next lesson file: content/week-14/day-03.md

## Theory Concepts

### Concept 1: Spot, forward, and par rates
Spot, forward, and par rates should be treated as a measurable component of 'Fixed income basics for quant workflows'. For this week, emphasize allocation constraints, risk decomposition, and capital efficiency. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Curve shapes and macro context
Curve shapes and macro context should be treated as a measurable component of 'Fixed income basics for quant workflows'. For this week, emphasize allocation constraints, risk decomposition, and capital efficiency. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Term premium intuition
Term premium intuition should be treated as a measurable component of 'Fixed income basics for quant workflows'. For this week, emphasize allocation constraints, risk decomposition, and capital efficiency. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Portfolio Variance
$$
\sigma_p^2=w^\top\Sigma w
$$
Quadratic risk engine.

### Formula 2: Risk Contribution
$$
RC_i=w_i\frac{(\Sigma w)_i}{\sigma_p}
$$
Per-position risk budget.

### Formula 3: Duration Shock
$$
\frac{\Delta P}{P}\approx-D_{mod}\Delta y
$$
First-order bond sensitivity.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $w$: portfolio weights
- $\Sigma$: covariance matrix
- $D_{mod}$: modified duration

## Real Trading Example
- Instruments: SPY, TLT, GLD, HYG
- Macro overlay (FRED): DGS10, T10YIE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Construct a toy yield curve and interpret steepening/flattening moves.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Yield curve structure'.

## Step-by-Step Solved Problems
### Solved Problem 1: Portfolio expected return
Given:
- w=[0.6,0.4], mu=[0.12,0.08].
Solution:
1. $\mu_p=w^\top\mu$.
2. mu_p = 0.6*0.12 + 0.4*0.08 = 0.104.
Final answer: Portfolio expected return = 10.4%.

### Solved Problem 2: Portfolio volatility
Given:
- sigma1=0.20, sigma2=0.12, rho=0.30, w1=0.6, w2=0.4.
Solution:
1. $\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho\sigma_1\sigma_2$.
2. sigma_p^2 = 0.02048.
3. sigma_p = sqrt(0.02048) = 0.1431.
Final answer: Portfolio volatility = 14.31%.

### Solved Problem 3: Duration shock
Given:
- Modified duration = 5.8, yield shift = +0.25%.
Solution:
1. $\Delta P/P\approx-D_{mod}\Delta y$.
2. DeltaP/P = -5.8*0.0025 = -0.0145.
Final answer: Approximate bond price change = -1.45%.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Create yield-curve plotting utility and slope diagnostics.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
mu, cov = estimate_moments(asset_returns)
weights = solve_constrained_mv(mu, cov, max_weight=0.35)
risk_budget = risk_contributions(weights, cov)
rebalance_flag = should_rebalance(weights, target_weights, threshold=0.03)
```

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
Which macro regime tends to produce curve inversion?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
