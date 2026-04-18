# Week 22 Day 03: Python coding speed drills

## Study Duration
- Planned effort: 4 hours

## 5-Block Daily Structure
- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).
- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.
- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.
- **Block 4 (60 min):** Python/pandas implementation and output verification.
- **Block 5 (30 min):** Practice questions, interview drill, and reflection.

## Why It Matters in Quant
Build speed and accuracy for core quantitative interview domains.

## Continuity and Handoff
- Previous checkpoint: Week 22 Day 02: Statistics and estimation interview drills
- Previous lesson file: content/week-22/day-02.md
- Today's deliverable: Build a local timed coding drill harness.
- Next handoff target: Week 22 Day 04: SQL and data manipulation interview drills
- Next lesson file: content/week-22/day-04.md

## Theory Concepts

### Concept 1: Array and string patterns
Array and string patterns is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Complexity awareness
Complexity awareness is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Edge-case handling
Edge-case handling is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Bayes Update
$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)}
$$
**Plain-English interpretation:** Evidence-driven belief update.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.

### Formula 2: CAGR
$$
CAGR=\left(\frac{V_T}{V_0}\right)^{1/T}-1
$$
**Plain-English interpretation:** Long-horizon growth target.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.

### Formula 3: Gap
$$
Gap_j=Target_j-Current_j
$$
**Plain-English interpretation:** Remaining improvement workload.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.

## Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | $110.50 |
| $r_t$ | Simple return | decimal or % | 0.012 = 1.2% |
| $\mu$ | Expected return | annualized decimal | 0.14 |
| $\sigma$ | Volatility (std. dev.) | annualized decimal | 0.18 |
| $S$ | Readiness score | 0 to 100 scale | 83.4 |
| $EV$ | Expected value | R-multiple | 0.45R |
| $Gap_j$ | Target-current skill gap | score points | 7.5 |

## Real Trading Example
- Instruments: SPY, QQQ, TLT
- Macro overlay (FRED): VIXCLS, TEDRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Solve 3 medium coding problems with clean test coverage.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Python coding speed drills'.

## Step-by-Step Solved Problems
### Solved Problem 1: Expected value
Given:
- Win probability=0.58, gain=1.5R, loss=1R.
Solution:
1. $EV=p\cdot Gain-(1-p)\cdot Loss$.
2. EV = 0.58*1.5 - 0.42*1.0 = 0.45R.
Final answer: Expected value = 0.45R per trade.
Common trap: Using one metric in isolation instead of combining expected value, risk limits, and readiness score.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 2: Readiness score
Given:
- Weights=[0.45,0.35,0.20], scores=[82,87,80].
Solution:
1. $S=\sum_jw_js_j$.
2. S = 0.45*82 + 0.35*87 + 0.20*80 = 83.35.
Final answer: Readiness score = 83.35/100.
Common trap: Using one metric in isolation instead of combining expected value, risk limits, and readiness score.
Interpretation: Write one sentence describing how this result would change a real trading decision.

### Solved Problem 3: CAGR target
Given:
- V0=1.00, VT=1.32, T=3 years.
Solution:
1. $CAGR=(V_T/V_0)^{1/T}-1$.
2. CAGR = (1.32/1.00)^(1/3)-1 = 0.0969.
Final answer: Required CAGR = 9.69%.
Common trap: Using one metric in isolation instead of combining expected value, risk limits, and readiness score.
Interpretation: Write one sentence describing how this result would change a real trading decision.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Build a local timed coding drill harness.
3. Add validation tests for leakage, NaNs, and unrealistic outliers.
4. Produce diagnostic plots and summarize one actionable trading rule.
5. Record one failure mode and one mitigation in comments.

Reference implementation sketch:
```python
readiness = score_readiness(quiz_scores, mock_scores, project_rubrics)
posterior = bayes_update(prior=0.55, likelihood=0.72, evidence=0.61)
roadmap = build_90_day_plan(readiness, posterior)
export_launch_checklist(roadmap)
```

## Block 5: Practice, Quiz, and Interview Drill

### Practice Problems
1. Re-derive today's formulas manually and define every variable and unit.
2. Re-run the real trading example with one alternate ticker and compare outputs.
3. Stress-test one assumption and write one explicit risk-control rule.
4. Extend the coding walkthrough with one validation test and one edge-case test.
5. Record one interview-ready explanation in less than 60 seconds.

### Daily Quiz (Realistic Interview Style)
1. In Week 22 Day 03, explain one formula from today's lesson in plain language and define every symbol used.
2. Using one real asset from today's universe, compute the metric and state one risk guardrail you would enforce.
3. Interview drill: In 60 seconds, explain why 'Python coding speed drills' matters for production trading systems.

Answer key template:
- Q1: Formula + symbol table + units.
- Q2: Numeric result + interpretation + guardrail.
- Q3: One concise story linking model, risk, and execution.

### Interview Drill
- Prompt: "Walk me through Python coding speed drills as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.

## Reflection Question
Which coding pattern causes most debugging delays?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
