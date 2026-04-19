# Week 18 Day 04: Backtest and cost-aware evaluation

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
Learn stat-arb foundations including spreads, cointegration, and execution-aware controls.

## Continuity and Handoff
- Previous checkpoint: Week 18 Day 03: Signal generation and execution rules
- Previous lesson file: content/week-18/day-03.md
- Today's deliverable: Add financing and slippage assumptions to spread backtest.
- Next handoff target: Week 18 Day 05: Failure modes and safeguards
- Next lesson file: content/week-18/day-05.md

## Theory Concepts

### Concept 1: Pair-level PnL decomposition
Pair-level PnL decomposition is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Borrow and financing assumptions
Borrow and financing assumptions is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Execution slippage sensitivity
Execution slippage sensitivity is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Spread Z-Score
$$
z_t=\frac{s_t-\mu_s}{\sigma_s}
$$
**Plain-English interpretation:** Stat-arb entry normalization.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 2: Implementation Shortfall
$$
IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}
$$
**Plain-English interpretation:** Execution loss in bps.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 3: Cross-Sectional Z
$$
z_{i,t}=\frac{x_{i,t}-\mu_t}{\sigma_t}
$$
**Plain-English interpretation:** Universe-normalized signal.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $IC$ | Information coefficient | correlation | 0.04 |
| $ADV$ | Average daily volume | shares/day | 12M |
| $IS$ | Implementation shortfall | basis points | 14.2 bps |

## Real Trading Example
- Instruments: SPY, IWM, EFA, EEM
- Macro overlay (FRED): DFF, BAMLH0A0HYM2
- Suggested window: 2018-01-01 to 2026-03-31
- Stress windows to inspect: 2020-03 to 2020-05, 2023-03 to 2023-06
- Scenario context: crowded-factor unwind and liquidity stress
- Day objective: Backtest pair strategy with conservative cost assumptions.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Backtest and cost-aware evaluation'.

## Step-by-Step Solved Problems
### Solved Problem 1: Factor z-score
Given:
- Signal=1.60, mean=0.70, std=0.45.
Solution:
1. $z=\frac{x-\mu}{\sigma}$.
2. z=(1.60-0.70)/0.45 = 2.00.
Final answer: Signal z-score = 2.00.
Common trap: Reporting gross signal performance without implementation costs or capacity constraints.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: IC t-stat
Given:
- Mean IC=0.045, std(IC)=0.018, T=12 months.
Solution:
1. $t=\frac{\bar{IC}}{s/\sqrt{T}}$.
2. t = 0.045/(0.018/sqrt(12)) = 8.66.
Final answer: IC t-stat = 8.66.
Common trap: Reporting gross signal performance without implementation costs or capacity constraints.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Implementation shortfall
Given:
- Arrival=101.20, execution=101.36.
Solution:
1. $IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}$.
2. IS_bps = 10000*(0.16/101.20) = 15.81.
Final answer: Implementation shortfall = 15.81 bps.
Common trap: Reporting gross signal performance without implementation costs or capacity constraints.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Add financing and slippage assumptions to spread backtest.
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

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 18 Day 04): Explain Spread Z-Score and define every symbol clearly for a crowded-factor unwind with liquidity deterioration.
   - Model answer: "I use Spread Z-Score as a decision bridge from market observations to position sizing. The formula is $z_t=\frac{s_t-\mu_s}{\sigma_s}$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then throttle position sizing when estimated implementation shortfall rises above threshold. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify survivorship-bias controls, borrow/shortability flags, and capacity-aware data completeness checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Backtest and cost-aware evaluation' matter in live trading systems?
   - Model answer: "Backtest and cost-aware evaluation matters because signal quality is meaningless unless net-of-cost and capacity-aware in live execution. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I halve position sizes, widen execution limits, and re-open capacity only after slippage improves. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Backtest and cost-aware evaluation in an execution review with rising slippage and crowding risk."
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
Where does hidden cost risk often get ignored in pairs strategies?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Full notebook rerun completed from clean kernel
- [ ] Reflection logged in progress tracker
