# Week 02 Day 01: Random variables and key distributions

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Strengthen statistical reasoning needed for quant inference and model validation.

## Continuity and Handoff
- Previous checkpoint: Week 01 Day 07: Portfolio Project
- Previous lesson file: content/week-01/day-07.md
- Today's deliverable: Simulate returns from multiple distributions and compare tail events.
- Next handoff target: Week 02 Day 02: Expectation, variance, and covariance
- Next lesson file: content/week-02/day-02.md

## Theory Concepts

### Concept 1: Discrete vs continuous random variables
Discrete vs continuous random variables should be treated as a measurable component of 'Probability and statistics for market data'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Normal, lognormal, and heavy-tail intuition
Normal, lognormal, and heavy-tail intuition should be treated as a measurable component of 'Probability and statistics for market data'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Distribution moments and shape
Distribution moments and shape should be treated as a measurable component of 'Probability and statistics for market data'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Simple Return
$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$
Normalize raw price moves.

### Formula 2: Log Return
$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$
Additive return representation.

### Formula 3: Annualized Volatility
$$
\sigma_{ann}=\sqrt{252}\,Std(r_t)
$$
Scale daily uncertainty to annual horizon.

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
- Day objective: Compare simulated normal returns with fat-tail synthetic returns.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Random variables and key distributions'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $102.00 to $103.22.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (103.224-102.000)/102.000 = 0.012000.
Final answer: Simple return = 1.20%.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0112.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0112 = 0.1778.
Final answer: Annualized volatility = 17.78%.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 17.78%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.1778 = 0.6187.
Final answer: Sharpe ratio = 0.62.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Simulate returns from multiple distributions and compare tail events.
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
Why are heavy tails critical for risk systems?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
