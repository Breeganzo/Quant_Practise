# Week 01 Day 04: Market structure and asset classes

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Rebuild core quant workflow habits and foundational finance vocabulary.

## Continuity and Handoff
- Previous checkpoint: Week 01 Day 03: Calculus intuition for optimization
- Previous lesson file: content/week-01/day-03.md
- Today's deliverable: Create a comparative table of OHLCV statistics for three instruments.
- Next handoff target: Week 01 Day 05: Risk and performance metrics
- Next lesson file: content/week-01/day-05.md

## Theory Concepts

### Concept 1: Equity, ETF, fixed-income, and derivatives overview
Equity, ETF, fixed-income, and derivatives overview is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Liquidity and bid-ask spread intuition
Liquidity and bid-ask spread intuition is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Trading session and venue effects
Trading session and venue effects is a core part of 'Python setup, math refresh, and market basics'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

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
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 3: Simple Return
$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$
**Plain-English interpretation:** Normalize raw price moves.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $R_f$ | Risk-free rate | annualized decimal | 0.03 |
| $TO_t$ | Portfolio turnover | fraction of portfolio | 0.12 |

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Compare volatility and volume behavior for an ETF versus a single stock.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Market structure and asset classes'.

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
2. Implement today's objective as reusable functions: Create a comparative table of OHLCV statistics for three instruments.
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
1. PM interview question (Week 01 Day 04): Explain Sharpe Ratio and define every symbol clearly.
   - Model answer: "I use Sharpe Ratio to convert raw prices into a decision-ready metric. The formula is $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Market structure and asset classes' matter in live trading systems?
   - Model answer: "Market structure and asset classes matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Market structure and asset classes as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## Reflection Question
Which asset class currently best matches your skill level and why?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
