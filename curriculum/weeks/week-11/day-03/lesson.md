# Week 11 Day 03: Transaction costs and slippage

## Study Duration
- Planned effort: 6-10 hours/day
- Required minimum: 6 hours (core + required extension); optional deep work extends to 10 hours.

## 6-10 Hour Daily Structure
- **Core Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Core Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Core Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Core Block 4 (60 min):** Python/pandas implementation and output verification.
- **Core Block 5 (30 min):** Practice questions, interview drill, and reflection.
- **Required Extension Block A (60 min):** Re-run the real trading example with one alternate ticker and one stress window.
- **Required Extension Block B (60 min):** Restart kernel and rerun all coding cells end-to-end, then add one extra validation test.
- **Optional Deep Work (0-4 hours):** Expand diagnostics, add edge-case tests, and improve interview-ready explanations.

## Why It Matters in Quant
Design backtests that avoid common biases and include realistic costs and constraints.

## Continuity and Handoff
- Previous checkpoint: Week 11 Day 02: Data and look-ahead bias controls
- Previous lesson file: content/week-11/day-02.md
- Today's deliverable: Integrate cost model into backtest calculations.
- Next handoff target: Week 11 Day 04: Position sizing and risk constraints
- Next lesson file: content/week-11/day-04.md

## Theory Concepts

### Concept 1: Fixed and proportional costs
Fixed and proportional costs is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Spread and impact proxies
Spread and impact proxies is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Turnover sensitivity
Turnover sensitivity is a core part of 'Backtesting architecture and implementation realism'. Start with notation discipline: define time index, lag notation, and forecast horizon before estimating dependence. Then focus on temporal dependence structure and out-of-sample forecast discipline by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: AR(1)
$$
x_t=c+\phi x_{t-1}+\epsilon_t
$$
**Plain-English interpretation:** One-step dependence model.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 2: EWMA Vol
$$
\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2
$$
**Plain-English interpretation:** Adaptive volatility estimate.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.

### Formula 3: RMSE
$$
RMSE=\sqrt{\frac{1}{n}\sum_t e_t^2}
$$
**Plain-English interpretation:** Forecast error benchmark.
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
- Stress windows to inspect: 2020-03 to 2020-06, 2022-09 to 2023-03
- Scenario context: volatility clustering after macro shock
- Day objective: Compare gross vs net returns under increasing turnover.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Transaction costs and slippage'.

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
2. Implement today's objective as reusable functions: Integrate cost model into backtest calculations.
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
1. PM interview question (Week 11 Day 03): Explain AR(1) and define every symbol clearly for a volatility-clustering regime after a macro policy shock.
   - Model answer: "I use AR(1) as a decision bridge from market observations to position sizing. The formula is $x_t=c+\phi x_{t-1}+\epsilon_t$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then de-risk when realized volatility breaks above the model training regime. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify stationarity diagnostics, holiday-gap handling, and rolling-window recalculation checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Transaction costs and slippage' matter in live trading systems?
   - Model answer: "Transaction costs and slippage matters because regime changes break naive stationarity assumptions and invalidate fixed-parameter forecasts. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I switch to shorter lookback controls, reduce leverage, and require stability across two windows. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Transaction costs and slippage in a risk meeting during volatility clustering after policy shock."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision under constraints.
  3. Awareness of edge cases, costs, and failure modes.
  4. Clear escalation rule when guardrails are breached.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula, assumptions, and validation checks clearly.
  - Decision: explain one actionable rule, one risk guardrail, and one fallback action.

## Required Extension Track (2+ Hours)
- Re-run today's notebook from a fresh kernel so outputs are reproducible without hidden state.
- Add one additional risk guardrail and verify how it changes trade/no-trade decisions.
- Document one failure mode, one mitigation, and one escalation rule for production use.

Extension completion checks:
- [ ] Notebook restarted and all coding cells rerun successfully
- [ ] At least one extra validation/edge-case test added
- [ ] Risk guardrail and fallback action documented

## Reflection Question
Which assumptions make your slippage model unrealistic?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Full notebook rerun completed from clean kernel
- [ ] Reflection logged in progress tracker
