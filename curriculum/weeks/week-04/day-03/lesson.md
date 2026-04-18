# Week 04 Day 03: Correlation structure and diversification

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Integrate foundational math and data skills into a complete exploratory market analysis.

## Continuity and Handoff
- Previous checkpoint: Week 04 Day 02: Risk distribution diagnostics
- Previous lesson file: content/week-04/day-02.md
- Today's deliverable: Generate rolling-correlation heatmaps over time windows.
- Next handoff target: Week 04 Day 04: Exploratory visualization for strategy intuition
- Next lesson file: content/week-04/day-04.md

## Theory Concepts

### Concept 1: Rolling correlation behavior
Rolling correlation behavior should be treated as a measurable component of 'Return/risk analytics and exploratory capstone'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Diversification under stress
Diversification under stress should be treated as a measurable component of 'Return/risk analytics and exploratory capstone'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Clustered risk exposures
Clustered risk exposures should be treated as a measurable component of 'Return/risk analytics and exploratory capstone'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Annualized Volatility
$$
\sigma_{ann}=\sqrt{252}\,Std(r_t)
$$
Scale daily uncertainty to annual horizon.

### Formula 2: Sharpe Ratio
$$
S=\frac{R_{ann}-R_f}{\sigma_{ann}}
$$
Risk-adjusted performance score.

### Formula 3: Turnover
$$
TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|
$$
Execution intensity proxy.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $R_f$: risk-free rate
- $TO_t$: portfolio turnover

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Track rolling correlations during synthetic stress intervals.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Correlation structure and diversification'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $106.00 to $107.48.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (107.484-106.000)/106.000 = 0.014000.
Final answer: Simple return = 1.40%.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0126.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0126 = 0.2000.
Final answer: Annualized volatility = 20.00%.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 20.00%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.2000 = 0.5499.
Final answer: Sharpe ratio = 0.55.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Generate rolling-correlation heatmaps over time windows.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
prices = load_prices(['SPY', 'QQQ', 'AAPL'])
returns = prices.pct_change().dropna()
metrics = compute_risk_metrics(returns)
assert metrics['max_drawdown'] <= 0
```

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
When does diversification break down?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
