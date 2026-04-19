# Week 09 Day 01: Stationarity and transformations

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Build practical time-series intuition for forecasting and diagnostic workflows.

## Continuity and Handoff
- Previous checkpoint: Week 08 Day 07: Portfolio Project
- Previous lesson file: content/week-08/day-07.md
- Today's deliverable: Implement stationarity diagnostic checks and transformation pipeline.
- Next handoff target: Week 09 Day 02: Autocorrelation and partial autocorrelation
- Next lesson file: content/week-09/day-02.md

## Theory Concepts

### Concept 1: Mean/variance stability
Mean/variance stability is a core part of 'Time-series foundations and stationarity'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Differencing and detrending
Differencing and detrending is a core part of 'Time-series foundations and stationarity'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Log and seasonal transforms
Log and seasonal transforms is a core part of 'Time-series foundations and stationarity'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: First Difference
$$
\Delta x_t=x_t-x_{t-1}
$$
**Plain-English interpretation:** Removes non-stationary level drift.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 2: Autocorrelation
$$
\rho_k=\frac{Cov(x_t,x_{t-k})}{Var(x_t)}
$$
**Plain-English interpretation:** Lag-memory measurement.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 3: AR(1)
$$
x_t=c+\phi x_{t-1}+\epsilon_t
$$
**Plain-English interpretation:** One-step dependence model.
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
- Day objective: Diagnose stationarity before and after differencing on a synthetic series.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Stationarity and transformations'.

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

### Solved Problem 4: Position sizing with volatility guardrail
Given:
- Strategy annualized volatility estimate is 0.179.
- Portfolio risk budget target is 0.20.
- Position multiplier rule: scale = target_vol / strategy_vol, clipped to [0.20, 1.00].
Solution:
1. Compute raw scale = target_vol / strategy_vol.
2. raw_scale = 0.20/0.179 = 1.1173.
3. clipped_scale = min(1.00, max(0.20, 1.1173)) = 1.0000.
Final answer: Position multiplier = 1.0000.
Common trap: Ignoring volatility regime shifts and applying static position size in stressed markets.
Interpretation: State how this guardrail changes gross exposure before deployment.
## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement stationarity diagnostic checks and transformation pipeline.
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
1. PM interview question (Week 09 Day 01): Explain First Difference and define every symbol clearly.
   - Model answer: "I use First Difference to convert raw prices into a decision-ready metric. The formula is $\Delta x_t=x_t-x_{t-1}$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Stationarity and transformations' matter in live trading systems?
   - Model answer: "Stationarity and transformations matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Stationarity and transformations as if you are presenting to a PM who cares about risk-adjusted returns."
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
  - Include one numeric example from Week 09 Day 01 to prove notation fluency.

Extension completion checks:
- [ ] Stress-regime comparison completed
- [ ] Production guardrail assertions added and passed
- [ ] Interview simulation recorded with one numeric example
## Reflection Question
When can differencing remove useful economic signal?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
