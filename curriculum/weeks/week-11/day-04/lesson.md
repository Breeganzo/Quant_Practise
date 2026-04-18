# Week 11 Day 04: Position sizing and risk constraints

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Design backtests that avoid common biases and include realistic costs and constraints.

## Continuity and Handoff
- Previous checkpoint: Week 11 Day 03: Transaction costs and slippage
- Previous lesson file: content/week-11/day-03.md
- Today's deliverable: Implement risk constraint layer in backtest flow.
- Next handoff target: Week 11 Day 05: Performance attribution and diagnostics
- Next lesson file: content/week-11/day-05.md

## Theory Concepts

### Concept 1: Volatility-based sizing
Volatility-based sizing should be treated as a measurable component of 'Backtesting architecture and implementation realism'. For this week, emphasize temporal dependence structure and out-of-sample forecast discipline. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Max exposure and concentration limits
Max exposure and concentration limits should be treated as a measurable component of 'Backtesting architecture and implementation realism'. For this week, emphasize temporal dependence structure and out-of-sample forecast discipline. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Stop-loss and drawdown guards
Stop-loss and drawdown guards should be treated as a measurable component of 'Backtesting architecture and implementation realism'. For this week, emphasize temporal dependence structure and out-of-sample forecast discipline. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: EWMA Vol
$$
\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2
$$
Adaptive volatility estimate.

### Formula 2: RMSE
$$
RMSE=\sqrt{\frac{1}{n}\sum_t e_t^2}
$$
Forecast error benchmark.

### Formula 3: First Difference
$$
\Delta x_t=x_t-x_{t-1}
$$
Removes non-stationary level drift.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $\phi$: autoregressive coefficient
- $e_t$: forecast residual
- $\lambda$: EWMA decay

## Real Trading Example
- Instruments: SPY, TLT, GLD
- Macro overlay (FRED): VIXCLS, DGS2
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Simulate sizing rules under stable and stressed conditions.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Position sizing and risk constraints'.

## Step-by-Step Solved Problems
### Solved Problem 1: One-step AR(1) forecast
Given:
- Use c=0.001, phi=0.64, x_t=0.015.
Solution:
1. $x_{t+1}=c+\phi x_t$.
2. Forecast = 0.001 + 0.64*0.015 = 0.010600.
Final answer: Forecasted value = 1.06%.

### Solved Problem 2: EWMA volatility update
Given:
- lambda=0.94, sigma_(t-1)=0.020, r_(t-1)=-0.012.
Solution:
1. $\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$.
2. sigma_t^2 = 0.94*(0.020^2) + 0.06*(0.012^2) = 0.00038464.
3. sigma_t = sqrt(0.00038464) = 0.01961.
Final answer: Updated volatility = 1.96%.

### Solved Problem 3: Compute RMSE
Given:
- Errors are [0.004, -0.006, 0.003, -0.002, 0.005].
Solution:
1. $RMSE=\sqrt{\frac{1}{n}\sum e_t^2}$.
2. Mean squared error = 0.000018.
3. RMSE = sqrt(0.000018) = 0.00424.
Final answer: RMSE = 0.424%.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement risk constraint layer in backtest flow.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
series = build_stationary_series(price_df['Close'])
forecast = walk_forward_arima(series, order=(1, 1, 1))
errors = series.loc[forecast.index] - forecast
rmse = np.sqrt(np.mean(errors**2))
```

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
Which constraint most improves downside behavior?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
