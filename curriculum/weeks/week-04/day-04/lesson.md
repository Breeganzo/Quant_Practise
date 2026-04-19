# Week 04 Day 04: Exploratory visualization for strategy intuition

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
Integrate foundational math and data skills into a complete exploratory market analysis.

## Continuity and Handoff
- Previous checkpoint: Week 04 Day 03: Correlation structure and diversification
- Previous lesson file: content/week-04/day-03.md
- Today's deliverable: Produce clean charts with labeled assumptions and caveats.
- Next handoff target: Week 04 Day 05: Capstone design and reporting
- Next lesson file: content/week-04/day-05.md

## Theory Concepts

### Concept 1: Narrative charting
Narrative charting is a core part of 'Return/risk analytics and exploratory capstone'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Signal sanity checks
Signal sanity checks is a core part of 'Return/risk analytics and exploratory capstone'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Interpretability of exploratory outputs
Interpretability of exploratory outputs is a core part of 'Return/risk analytics and exploratory capstone'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Sharpe Ratio
$$
S=\frac{R_{ann}-R_f}{\sigma_{ann}}
$$
**Plain-English interpretation:** Risk-adjusted performance score.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 2: Turnover
$$
TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|
$$
**Plain-English interpretation:** Execution intensity proxy.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Recalculate after a 1 standard deviation shock and explain the intuition in one sentence.

### Formula 3: Simple Return
$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$
**Plain-English interpretation:** Normalize raw price moves.
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
- Day objective: Build a concise dashboard panel of return, drawdown, and volatility views.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Exploratory visualization for strategy intuition'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $108.00 to $109.62.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (109.620-108.000)/108.000 = 0.015000.
Final answer: Simple return = 1.50%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0133.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0133 = 0.2111.
Final answer: Annualized volatility = 21.11%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 21.11%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.2111 = 0.5210.
Final answer: Sharpe ratio = 0.52.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Produce clean charts with labeled assumptions and caveats.
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
1. PM interview question (Week 04 Day 04): Explain Sharpe Ratio and define every symbol clearly for an inflation surprise week with simultaneous equity and rate volatility.
   - Model answer: "I use Sharpe Ratio as a decision bridge from market observations to position sizing. The formula is $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then cap gross exposure when rolling 20-day volatility exceeds backtest 90th percentile. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify timezone alignment, split/dividend adjustments, and missing-close handling. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Exploratory visualization for strategy intuition' matter in live trading systems?
   - Model answer: "Exploratory visualization for strategy intuition matters because reliable notation and units prevent silent compounding and scaling errors in production PnL reporting. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I cut gross exposure by 30%, rerun diagnostics, and only resume when risk metrics normalize. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Exploratory visualization for strategy intuition in a PM review after CPI surprise where benchmark drawdown accelerated."
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
How do visuals bias interpretation if scales are inconsistent?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Full notebook rerun completed from clean kernel
- [ ] Reflection logged in progress tracker
