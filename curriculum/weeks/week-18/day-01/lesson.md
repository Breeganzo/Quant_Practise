# Week 18 Day 01: Stat-arb problem framing

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Learn stat-arb foundations including spreads, cointegration, and execution-aware controls.

## Continuity and Handoff
- Previous checkpoint: Week 17 Day 07: Portfolio Project
- Previous lesson file: content/week-17/day-07.md
- Today's deliverable: Implement spread builder with normalization options.
- Next handoff target: Week 18 Day 02: Cointegration basics
- Next lesson file: content/week-18/day-02.md

## Theory Concepts

### Concept 1: Relative-value logic
Relative-value logic is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Spread construction
Spread construction is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Stationarity requirement
Stationarity requirement is a core part of 'Statistical arbitrage intuition'. Start with notation discipline: define universe construction, signal scaling, and execution units before evaluating alpha. Then focus on alpha stability, execution realism, and risk-governed deployment by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Cross-Sectional Z
$$
z_{i,t}=\frac{x_{i,t}-\mu_t}{\sigma_t}
$$
**Plain-English interpretation:** Universe-normalized signal.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 2: Information Coefficient
$$
IC_t=Corr(score_{i,t},r_{i,t+1})
$$
**Plain-English interpretation:** Signal/forward-return linkage.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 3: IC t-Statistic
$$
t_{IC}=\frac{\bar{IC}}{Std(IC)/\sqrt{T}}
$$
**Plain-English interpretation:** Signal persistence test.
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
- Day objective: Create a synthetic spread candidate and inspect mean behavior.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Stat-arb problem framing'.

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
2. Implement today's objective as reusable functions: Implement spread builder with normalization options.
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
1. In Week 18 Day 01, explain one formula from today's lesson in plain language and define every symbol used.
2. Using one real asset from today's universe, compute the metric and state one risk guardrail you would enforce.
3. Interview drill: In 60 seconds, explain why 'Stat-arb problem framing' matters for production trading systems.

Answer key template:
- Q1: Formula + symbol table + units.
- Q2: Numeric result + interpretation + guardrail.
- Q3: One concise story linking model, risk, and execution.

### Interview Drill
- Prompt: "Walk me through Stat-arb problem framing as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.

## Reflection Question
Why is spread stationarity central for mean-reversion stat-arb?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
