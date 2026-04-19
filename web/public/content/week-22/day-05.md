# Week 22 Day 05: Mock round synthesis

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
- Previous checkpoint: Week 22 Day 04: SQL and data manipulation interview drills
- Previous lesson file: content/week-22/day-04.md
- Today's deliverable: Log mock performance and classify errors by type.
- Next handoff target: Week 22 Day 06: Revision Sprint
- Next lesson file: content/week-22/day-06.md

## Theory Concepts

### Concept 1: Time management
Time management is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 2: Answer structuring
Answer structuring is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

### Concept 3: Error recovery strategy
Error recovery strategy is a core part of 'Quant interview prep I'. Start with notation discipline: define readiness metrics, scoring weights, and evidence thresholds before making final decisions. Then focus on decision quality, communication rigor, and reproducible evidence by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), verifying units, and documenting one failure mode that appears in stressed regimes.

## Mathematical Foundations (LaTeX)
### Formula 1: Gap
$$
Gap_j=Target_j-Current_j
$$
**Plain-English interpretation:** Remaining improvement workload.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.

### Formula 2: Expected Value
$$
EV=p\cdot Gain-(1-p)\cdot Loss
$$
**Plain-English interpretation:** Decision-quality baseline.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.

### Formula 3: Readiness Score
$$
S=\sum_j w_js_j
$$
**Plain-English interpretation:** Weighted progress metric.
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
- Day objective: Run a mixed 45-minute mock round and self-score.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Mock round synthesis'.

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

### Solved Problem 4: Position sizing with volatility guardrail
Given:
- Strategy annualized volatility estimate is 0.209.
- Portfolio risk budget target is 0.20.
- Position multiplier rule: scale = target_vol / strategy_vol, clipped to [0.20, 1.00].
Solution:
1. Compute raw scale = target_vol / strategy_vol.
2. raw_scale = 0.20/0.209 = 0.9569.
3. clipped_scale = min(1.00, max(0.20, 0.9569)) = 0.9569.
Final answer: Position multiplier = 0.9569.
Common trap: Ignoring volatility regime shifts and applying static position size in stressed markets.
Interpretation: State how this guardrail changes gross exposure before deployment.
## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Log mock performance and classify errors by type.
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
1. PM interview question (Week 22 Day 05): Explain Gap and define every symbol clearly.
   - Model answer: "I use Gap to convert raw prices into a decision-ready metric. The formula is $Gap_j=Target_j-Current_j$. I define each symbol before computing it, verify units, and then interpret the output as a risk-adjusted trading input rather than a standalone signal."
2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?
   - Model answer: "I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check."
3. Production question: Why does 'Mock round synthesis' matter in live trading systems?
   - Model answer: "Mock round synthesis matters because it links model logic to real execution constraints. In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change."

Scoring rubric:
- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.

### Interview Drill
- Prompt: "Walk me through Mock round synthesis as if you are presenting to a PM who cares about risk-adjusted returns."
- What interviewers look for:
  1. Correct notation and units.
  2. Ability to connect theory to a real trade decision.
  3. Awareness of edge cases, costs, and failure modes.
- Model answer framework:
  - Context: define business objective and market regime.
  - Method: state formula and variables clearly.
  - Decision: explain one actionable rule and one risk guardrail.

## 2-Hour Extension Track (Required)

This section upgrades the day to a full 6-hour study model: 4-hour core lesson + 2-hour required extension.

- **Extension Block A (45 min):** Real-market case expansion.
  - Re-run today's workflow on one additional asset and one stress regime window.
  - Document one regime-specific failure mode and one mitigation rule.
- **Extension Block B (45 min):** Production-quality coding refinement.
  - Add one assertion for data integrity and one assertion for risk limits.
  - Save a short result table with assumptions, metric values, and decision rationale.
- **Extension Block C (30 min):** Interview simulation and review.
  - Deliver a 60-second PM pitch and a 60-second risk-manager response.
  - Include one numeric example from Week 22 Day 05 to prove notation fluency.

Extension completion checks:
- [ ] Stress-regime comparison completed
- [ ] Production guardrail assertions added and passed
- [ ] Interview simulation recorded with one numeric example
## Reflection Question
What one behavior change would improve your next mock score most?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
