# Week 03 Day 02: Eigenvalues, eigenvectors, and PCA intuition

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Build matrix and optimization intuition while strengthening practical data handling skills.

## Continuity and Handoff
- Previous checkpoint: Week 03 Day 01: Vectors, matrices, and transformations
- Previous lesson file: content/week-03/day-01.md
- Today's deliverable: Build PCA diagnostic plots and explained-variance table.
- Next handoff target: Week 03 Day 03: Optimization fundamentals
- Next lesson file: content/week-03/day-03.md

## Theory Concepts

### Concept 1: Variance directions in data
Variance directions in data is a core part of 'Linear algebra, optimization, and data engineering'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Principal components as latent factors
Principal components as latent factors is a core part of 'Linear algebra, optimization, and data engineering'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Dimensionality reduction tradeoffs
Dimensionality reduction tradeoffs is a core part of 'Linear algebra, optimization, and data engineering'. Start with notation discipline: define prices, returns, percentages, and all symbols before doing any arithmetic. Then focus on clean data assumptions and stable mathematical transformations by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Log Return
$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$
**Plain-English interpretation:** Additive return representation.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 2: Annualized Volatility
$$
\sigma_{ann}=\sqrt{252}\,Std(r_t)
$$
**Plain-English interpretation:** Scale daily uncertainty to annual horizon.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.

### Formula 3: Sharpe Ratio
$$
S=\frac{R_{ann}-R_f}{\sigma_{ann}}
$$
**Plain-English interpretation:** Risk-adjusted performance score.
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
- Day objective: Apply PCA to correlated return features and interpret first components.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Eigenvalues, eigenvectors, and PCA intuition'.

## Step-by-Step Solved Problems
### Solved Problem 1: Compute simple return
Given:
- Price moves from $104.00 to $105.35.
Solution:
1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.
2. r_t = (105.352-104.000)/104.000 = 0.013000.
Final answer: Simple return = 1.30%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Annualize volatility
Given:
- Daily volatility estimate is 0.0119.
Solution:
1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.
2. sigma_ann = sqrt(252)*0.0119 = 0.1889.
Final answer: Annualized volatility = 18.89%.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: Compute Sharpe ratio
Given:
- Annual return is 14.0%, risk-free rate is 3.0%.
- Use volatility 18.89%.
Solution:
1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.
2. S = (0.14-0.03)/0.1889 = 0.5823.
Final answer: Sharpe ratio = 0.58.
Common trap: Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Build PCA diagnostic plots and explained-variance table.
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
1. PM interview question (Week 03 Day 02): Explain Log Return and define every symbol clearly.
   - Model answer: "I use Log Return to convert raw prices into a decision-ready metric. The formula is $\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Eigenvalues, eigenvectors, and PCA intuition' matter in live trading systems?
   - Model answer: "Eigenvalues, eigenvectors, and PCA intuition matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Eigenvalues, eigenvectors, and PCA intuition as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## Reflection Question
When can PCA remove useful signal?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
