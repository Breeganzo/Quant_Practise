# Week 03 Day 06: Revision Sprint

## Study Duration
- Planned effort: 6-10 hours/day
- Required minimum: 6 hours across recall, rebuild, rerun, and retest blocks.

## 6-10 Hour Daily Structure
- **Core Block 1 (60 min):** Recall formulas, notation, and units without notes.
- **Core Block 2 (75 min):** Rebuild one weekday workflow from memory and compare with reference output.
- **Core Block 3 (60 min):** Rerun at least two notebooks from a clean kernel and capture mismatches.
- **Core Block 4 (60 min):** Diagnose root causes and update safeguards in code/comments.
- **Core Block 5 (45 min):** Interview drill, quiz, and escalation-rule rehearsal.
- **Required Extension Block A (60 min):** Re-test on one alternate ticker universe and one stress window.
- **Required Extension Block B (60 min):** Produce a remediation log with before/after evidence.
- **Optional Deep Work (0-4 hours):** Add robustness tests, monitor drift controls, and harden reporting.

## Why It Matters in Quant
Revision day converts fragile understanding into deployment-ready reliability by forcing recall, rebuild, and guardrail validation.

## Continuity and Handoff
- Previous checkpoint: Week 03 Day 05: SQL basics for quant datasets
- Previous lesson file: content/week-03/day-05.md
- Today's deliverable: Revision checklist with corrected errors and next-week retest priorities.
- Next handoff target: Week 03 Day 07: Portfolio Project
- Next lesson file: content/week-03/day-07.md

## Revision Plan
- 90 minutes: active recall of weekday concepts and manual formula rewrite.
- 90 minutes: rebuild one weekday code workflow from memory.
- 90 minutes: restart kernel and rerun at least two day notebooks end-to-end.
- 90 minutes: error-log triage, retest plan, and guardrail refinement.
- Optional 0-4 hours: deepen weak areas with extra interview drill and code hardening.

## Focus Areas
- Rework one optimization example by hand
- Recreate one pandas pipeline from memory
- Write and test 3 SQL queries without references

## Mathematical Foundations (LaTeX)
### Formula 1: Simple Return
$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$
**Plain-English interpretation:** Normalize raw price moves.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 2: Log Return
$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$
**Plain-English interpretation:** Additive return representation.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Recalculate after a 1 standard deviation shock and explain the intuition in one sentence.

### Formula 3: Annualized Volatility
$$
\sigma_{ann}=\sqrt{252}\,Std(r_t)
$$
**Plain-English interpretation:** Scale daily uncertainty to annual horizon.
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
- Day objective: Rebuild two weekday workflows and compare decision outputs after a clean rerun.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Revision Sprint'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $112.00 to $113.90.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (113.904-112.000)/112.000 = 0.017000.
Final answer: Simple return = 1.70%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0147.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0147 = 0.2334.
Final answer: Annualized volatility = 23.34%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 23.34%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.2334 = 0.4714.
Final answer: Sharpe ratio = 0.47.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Rebuild one workflow from memory, rerun from clean kernel, and document one corrected failure mode.
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
1. Re-derive two key formulas from this week with units and constraints.
2. Rebuild one weekday notebook workflow from memory and verify output parity.
3. Replay one stress regime and document one changed decision rule.
4. Add one extra validation test that would have caught a prior mistake.
5. Record a 60-second explanation of one corrected failure mode.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 03 Day 06): Explain Simple Return and define every symbol clearly for an inflation surprise week with simultaneous equity and rate volatility.
   - Model answer: "I use Simple Return as a decision bridge from market observations to position sizing. The formula is $r_t = \frac{P_t - P_{t-1}}{P_{t-1}}$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then cap gross exposure when rolling 20-day volatility exceeds backtest 90th percentile. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify timezone alignment, split/dividend adjustments, and missing-close handling. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Revision Sprint' matter in live trading systems?
   - Model answer: "Revision Sprint matters because reliable notation and units prevent silent compounding and scaling errors in production PnL reporting. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I cut gross exposure by 30%, rerun diagnostics, and only resume when risk metrics normalize. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Revision Sprint in a PM review after CPI surprise where benchmark drawdown accelerated."
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
Which failure mode still appears after reruns, and what concrete control will prevent it next week?

## Completion Checklist
- [ ] Updated error log entries
- [ ] Weak concepts re-tested
- [ ] Two notebooks rerun from fresh kernel
- [ ] Next-week risk list prepared
- [ ] Interview drill recorded with one fallback action
