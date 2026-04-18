# Week 11 Day 04: Position sizing and risk constraints

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

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
Volatility-based sizing is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Max exposure and concentration limits
Max exposure and concentration limits is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Stop-loss and drawdown guards
Stop-loss and drawdown guards is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: EWMA Vol
$$
\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2
$$
**Plain-English interpretation:** Adaptive volatility estimate.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 2: RMSE
$$
RMSE=\sqrt{\frac{1}{n}\sum_t e_t^2}
$$
**Plain-English interpretation:** Forecast error benchmark.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 3: First Difference
$$
\Delta x_t=x_t-x_{t-1}
$$
**Plain-English interpretation:** Removes non-stationary level drift.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $\phi$ | Autoregressive coefficient | dimensionless | 0.64 |
| $e_t$ | Forecast residual | return units | -0.003 |
| $\lambda$ | EWMA decay factor | 0 to 1 | 0.94 |

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
Common trap: Treating a non-stationary series as stationary and over-trusting one in-sample fit.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: EWMA volatility update
Given:
- lambda=0.94, sigma_(t-1)=0.020, r_(t-1)=-0.012.
Solution:
1. $\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$.
2. sigma_t^2 = 0.94*(0.020^2) + 0.06*(0.012^2) = 0.00038464.
3. sigma_t = sqrt(0.00038464) = 0.01961.
Final answer: Updated volatility = 1.96%.
Common trap: Treating a non-stationary series as stationary and over-trusting one in-sample fit.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute RMSE
Given:
- Errors are [0.004, -0.006, 0.003, -0.002, 0.005].
Solution:
1. $RMSE=\sqrt{\frac{1}{n}\sum e_t^2}$.
2. Mean squared error = 0.000018.
3. RMSE = sqrt(0.000018) = 0.00424.
Final answer: RMSE = 0.424%.
Common trap: Treating a non-stationary series as stationary and over-trusting one in-sample fit.
Interpretation: Write one sentence describing how this result would change a real trading decision.

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

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 11 Day 04): Explain EWMA Vol and define every symbol clearly.
   - Model answer: "I use EWMA Vol to convert raw prices into a decision-ready metric. The formula is $\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Position sizing and risk constraints' matter in live trading systems?
   - Model answer: "Position sizing and risk constraints matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Position sizing and risk constraints as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## Reflection Question
Which constraint most improves downside behavior?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
