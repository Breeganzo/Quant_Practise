# Week 20 Day 03: Strategy blending and diversification

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Incorporate execution realism and microstructure awareness into a blended strategy portfolio.

## Continuity and Handoff
- Previous checkpoint: Week 20 Day 02: Execution cost modeling
- Previous lesson file: content/week-20/day-02.md
- Today's deliverable: Implement multi-sleeve blend with adjustable risk budgets.
- Next handoff target: Week 20 Day 04: Rebalancing and execution scheduling
- Next lesson file: content/week-20/day-04.md

## Theory Concepts

### Concept 1: Correlation across alpha sleeves
Correlation across alpha sleeves should be treated as a measurable component of 'Execution, microstructure, and multi-strategy blend'. For this week, emphasize alpha stability, execution realism, and risk-governed deployment. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Risk budget allocation
Risk budget allocation should be treated as a measurable component of 'Execution, microstructure, and multi-strategy blend'. For this week, emphasize alpha stability, execution realism, and risk-governed deployment. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Capacity constraints
Capacity constraints should be treated as a measurable component of 'Execution, microstructure, and multi-strategy blend'. For this week, emphasize alpha stability, execution realism, and risk-governed deployment. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: IC t-Statistic
$$
t_{IC}=\frac{\bar{IC}}{Std(IC)/\sqrt{T}}
$$
Signal persistence test.

### Formula 2: Spread Z-Score
$$
z_t=\frac{s_t-\mu_s}{\sigma_s}
$$
Stat-arb entry normalization.

### Formula 3: Implementation Shortfall
$$
IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}
$$
Execution loss in bps.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $IC$: information coefficient
- $ADV$: average daily volume
- $IS$: implementation shortfall

## Real Trading Example
- Instruments: SPY, IWM, EFA, EEM
- Macro overlay (FRED): DFF, BAMLH0A0HYM2
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Blend momentum, mean-reversion, and factor sleeves under risk limits.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Strategy blending and diversification'.

## Step-by-Step Solved Problems
### Solved Problem 1: Factor z-score
Given:
- Signal=1.60, mean=0.70, std=0.45.
Solution:
1. $z=\frac{x-\mu}{\sigma}$.
2. z=(1.60-0.70)/0.45 = 2.00.
Final answer: Signal z-score = 2.00.

### Solved Problem 2: IC t-stat
Given:
- Mean IC=0.045, std(IC)=0.018, T=12 months.
Solution:
1. $t=\frac{\bar{IC}}{s/\sqrt{T}}$.
2. t = 0.045/(0.018/sqrt(12)) = 8.66.
Final answer: IC t-stat = 8.66.

### Solved Problem 3: Implementation shortfall
Given:
- Arrival=101.20, execution=101.36.
Solution:
1. $IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}$.
2. IS_bps = 10000*(0.16/101.20) = 15.81.
Final answer: Implementation shortfall = 15.81 bps.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement multi-sleeve blend with adjustable risk budgets.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
factor_scores = compute_factor_scores(universe_frame)
signals = build_long_short_buckets(factor_scores, q=0.2)
execution_cost = estimate_slippage(signals, adv_frame)
net_pnl = backtest_with_costs(signals, returns, execution_cost)
```

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
How does capacity constraint change blend weights?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
