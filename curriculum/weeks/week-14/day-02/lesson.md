# Week 14 Day 02: Yield curve structure

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Develop working fixed-income intuition for pricing, curve dynamics, and interest-rate risk.

## Continuity and Handoff
- Previous checkpoint: Week 14 Day 01: Bond cashflows and pricing mechanics
- Previous lesson file: content/week-14/day-01.md
- Today's deliverable: Create yield-curve plotting utility and slope diagnostics.
- Next handoff target: Week 14 Day 03: Duration and convexity
- Next lesson file: content/week-14/day-03.md

## Theory Concepts

### Concept 1: Spot, forward, and par rates
Spot, forward, and par rates is a core part of 'Fixed income basics for quant workflows'. Start with notation discipline: define weights, constraints, and risk units before solving the allocation problem. Then focus on allocation constraints, risk decomposition, and capital efficiency by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Curve shapes and macro context
Curve shapes and macro context is a core part of 'Fixed income basics for quant workflows'. Start with notation discipline: define weights, constraints, and risk units before solving the allocation problem. Then focus on allocation constraints, risk decomposition, and capital efficiency by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Term premium intuition
Term premium intuition is a core part of 'Fixed income basics for quant workflows'. Start with notation discipline: define weights, constraints, and risk units before solving the allocation problem. Then focus on allocation constraints, risk decomposition, and capital efficiency by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Portfolio Variance
$$
\sigma_p^2=w^\top\Sigma w
$$
**Plain-English interpretation:** Quadratic risk engine.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Evaluate the metric on at least three assets and document which constraint changes the final portfolio most.

### Formula 2: Risk Contribution
$$
RC_i=w_i\frac{(\Sigma w)_i}{\sigma_p}
$$
**Plain-English interpretation:** Per-position risk budget.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Evaluate the metric on at least three assets and document which constraint changes the final portfolio most.

### Formula 3: Duration Shock
$$
\frac{\Delta P}{P}\approx-D_{mod}\Delta y
$$
**Plain-English interpretation:** First-order bond sensitivity.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Evaluate the metric on at least three assets and document which constraint changes the final portfolio most.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $w$ | Portfolio weights | sum to 1 | [0.35,0.25,0.40] |
| $\Sigma$ | Covariance matrix | return^2 | 3x3 matrix |
| $D_{mod}$ | Modified duration | years | 5.8 |

## Real Trading Example
- Instruments: SPY, TLT, GLD, HYG
- Macro overlay (FRED): DGS10, T10YIE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Construct a toy yield curve and interpret steepening/flattening moves.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Yield curve structure'.

## Step-by-Step Solved Problems
### Solved Problem 1: Portfolio expected return
Given:
- w=[0.6,0.4], mu=[0.12,0.08].
Solution:
1. $\mu_p=w^\top\mu$.
2. mu_p = 0.6*0.12 + 0.4*0.08 = 0.104.
Final answer: Portfolio expected return = 10.4%.
Common trap: Ignoring covariance and focusing only on expected return, which underestimates portfolio risk.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Portfolio volatility
Given:
- sigma1=0.20, sigma2=0.12, rho=0.30, w1=0.6, w2=0.4.
Solution:
1. $\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho\sigma_1\sigma_2$.
2. sigma_p^2 = 0.02048.
3. sigma_p = sqrt(0.02048) = 0.1431.
Final answer: Portfolio volatility = 14.31%.
Common trap: Ignoring covariance and focusing only on expected return, which underestimates portfolio risk.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Duration shock
Given:
- Modified duration = 5.8, yield shift = +0.25%.
Solution:
1. $\Delta P/P\approx-D_{mod}\Delta y$.
2. DeltaP/P = -5.8*0.0025 = -0.0145.
Final answer: Approximate bond price change = -1.45%.
Common trap: Ignoring covariance and focusing only on expected return, which underestimates portfolio risk.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Create yield-curve plotting utility and slope diagnostics.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
mu, cov = estimate_moments(asset_returns)
weights = solve_constrained_mv(mu, cov, max_weight=0.35)
risk_budget = risk_contributions(weights, cov)
rebalance_flag = should_rebalance(weights, target_weights, threshold=0.03)
```

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 14 Day 02): Explain Portfolio Variance and define every symbol clearly.
   - Model answer: "I use Portfolio Variance to convert raw prices into a decision-ready metric. The formula is $\sigma_p^2=w^\top\Sigma w$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Yield curve structure' matter in live trading systems?
   - Model answer: "Yield curve structure matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Yield curve structure as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## Reflection Question
Which macro regime tends to produce curve inversion?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
