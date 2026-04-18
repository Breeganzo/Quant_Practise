# Week 23 Day 03: Risk-first communication

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Sharpen front-office communication and strategy discussion readiness.

## Continuity and Handoff
- Previous checkpoint: Week 23 Day 02: Trade idea structuring
- Previous lesson file: content/week-23/day-02.md
- Today's deliverable: Prepare risk scenario table for one strategy pitch.
- Next handoff target: Week 23 Day 04: Behavioral and fit interview prep
- Next lesson file: content/week-23/day-04.md

## Theory Concepts

### Concept 1: Downside framing
Downside framing should be treated as a measurable component of 'Quant interview prep II and strats communication'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Scenario defense
Scenario defense should be treated as a measurable component of 'Quant interview prep II and strats communication'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Position sizing rationale
Position sizing rationale should be treated as a measurable component of 'Quant interview prep II and strats communication'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Bayes Update
$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)}
$$
Evidence-driven belief update.

### Formula 2: CAGR
$$
CAGR=\left(\frac{V_T}{V_0}\right)^{1/T}-1
$$
Long-horizon growth target.

### Formula 3: Gap
$$
Gap_j=Target_j-Current_j
$$
Remaining improvement workload.

## Symbol Definitions
- $P_t$: price at time $t$
- $r_t$: simple return
- $\mu$: expected return
- $\sigma$: volatility
- $S$: readiness score
- $EV$: expected value
- $Gap_j$: target gap by skill

## Real Trading Example
- Instruments: SPY, QQQ, TLT
- Macro overlay (FRED): VIXCLS, TEDRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Present a trade idea emphasizing risk controls before return potential.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Risk-first communication'.

## Step-by-Step Solved Problems
### Solved Problem 1: Expected value
Given:
- Win probability=0.58, gain=1.5R, loss=1R.
Solution:
1. $EV=p\cdot Gain-(1-p)\cdot Loss$.
2. EV = 0.58*1.5 - 0.42*1.0 = 0.45R.
Final answer: Expected value = 0.45R per trade.

### Solved Problem 2: Readiness score
Given:
- Weights=[0.45,0.35,0.20], scores=[82,87,80].
Solution:
1. $S=\sum_jw_js_j$.
2. S = 0.45*82 + 0.35*87 + 0.20*80 = 83.35.
Final answer: Readiness score = 83.35/100.

### Solved Problem 3: CAGR target
Given:
- V0=1.00, VT=1.32, T=3 years.
Solution:
1. $CAGR=(V_T/V_0)^{1/T}-1$.
2. CAGR = (1.32/1.00)^(1/3)-1 = 0.0969.
Final answer: Required CAGR = 9.69%.

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Prepare risk scenario table for one strategy pitch.
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

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
Which risk scenario is hardest for you to defend?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
