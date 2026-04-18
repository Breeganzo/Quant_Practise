# Week 24 Day 01: Portfolio curation and selection

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Integrate all learning outputs into a final capstone dossier ready for applications and interviews.

## Continuity and Handoff
- Previous checkpoint: Week 23 Day 07: Portfolio Project
- Previous lesson file: content/week-23/day-07.md
- Today's deliverable: Create portfolio index with project links and summaries.
- Next handoff target: Week 24 Day 02: End-to-end reproducibility pass
- Next lesson file: content/week-24/day-02.md

## Theory Concepts

### Concept 1: Signal-to-noise filtering of projects
Signal-to-noise filtering of projects should be treated as a measurable component of 'Final integration and launch-ready portfolio'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Narrative coherence
Narrative coherence should be treated as a measurable component of 'Final integration and launch-ready portfolio'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Audience-specific packaging
Audience-specific packaging should be treated as a measurable component of 'Final integration and launch-ready portfolio'. For this week, emphasize decision quality, communication rigor, and reproducible evidence. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)
### Formula 1: Expected Value
$$
EV=p\cdot Gain-(1-p)\cdot Loss
$$
Decision-quality baseline.

### Formula 2: Readiness Score
$$
S=\sum_j w_js_j
$$
Weighted progress metric.

### Formula 3: Bayes Update
$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)}
$$
Evidence-driven belief update.

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
- Day objective: Select top 4 projects and define positioning for each target audience.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Portfolio curation and selection'.

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
2. Implement today's objective as reusable functions: Create portfolio index with project links and summaries.
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
Which project best demonstrates end-to-end quant maturity?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
