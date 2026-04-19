# Week 01 Day 05: Risk and performance metrics

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
Rebuild core quant workflow habits and foundational finance vocabulary.

## Continuity and Handoff
- Previous checkpoint: Week 01 Day 04: Market structure and asset classes
- Previous lesson file: content/week-01/day-04.md
- Today's deliverable: Build reusable metrics functions with input validation.
- Next handoff target: Week 01 Day 06: Revision Sprint
- Next lesson file: content/week-01/day-06.md

## Theory Concepts

### Concept 1: Annualized return and annualized volatility
Annualized return and annualized volatility is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Sharpe ratio intuition and limitations
Sharpe ratio intuition and limitations is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Drawdown and recovery profile
Drawdown and recovery profile is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Turnover
$$
TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|
$$
**Plain-English interpretation:** Execution intensity proxy.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 2: Simple Return
$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$
**Plain-English interpretation:** Normalize raw price moves.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Recalculate after a 1 standard deviation shock and explain the intuition in one sentence.

### Formula 3: Log Return
$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$
**Plain-English interpretation:** Additive return representation.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Use two lookback windows and justify which window would be safer for deployment.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50$ |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $R_f$ | Risk-free rate | annualized decimal | 0.03 |
| $TO_t$ | Portfolio turnover | fraction of portfolio | 0.12 |

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Stress windows to inspect: 2020-02 to 2020-04, 2022-01 to 2022-10
- Scenario context: inflation surprise and policy-rate repricing
- Day objective: Compute rolling volatility and drawdown for a benchmark ETF.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Risk and performance metrics'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $110.00 to $111.76.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (111.760-110.000)/110.000 = 0.016000.
Final answer: Simple return = 1.60%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0140.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0140 = 0.2222.
Final answer: Annualized volatility = 22.22%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 22.22%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.2222 = 0.4950.
Final answer: Sharpe ratio = 0.49.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Build reusable metrics functions with input validation.
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

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 01 Day 05): Explain Turnover and define every symbol clearly for an inflation surprise week with simultaneous equity and rate volatility.
   - Model answer: "I use Turnover as a decision bridge from market observations to position sizing. The formula is $TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then cap gross exposure when rolling 20-day volatility exceeds backtest 90th percentile. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify timezone alignment, split/dividend adjustments, and missing-close handling. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Risk and performance metrics' matter in live trading systems?
   - Model answer: "Risk and performance metrics matters because reliable notation and units prevent silent compounding and scaling errors in production PnL reporting. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I cut gross exposure by 30%, rerun diagnostics, and only resume when risk metrics normalize. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Risk and performance metrics in a PM review after CPI surprise where benchmark drawdown accelerated."
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
Which performance metric is easiest to game?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Full notebook rerun completed from clean kernel
- [ ] Reflection logged in progress tracker
