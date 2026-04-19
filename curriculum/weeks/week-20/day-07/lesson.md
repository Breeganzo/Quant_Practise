# Week 20 Day 07: Portfolio Project

## Study Duration
- Planned effort: 6-10 hours/day
- Required minimum: 6 hours for implementation, validation, and communication drills.

## 6-10 Hour Daily Structure
- **Core Block 1 (60 min):** Restate objective, assumptions, and measurable success criteria.
- **Core Block 2 (75 min):** Build/clean data pipeline and verify timestamp integrity.
- **Core Block 3 (75 min):** Implement project logic and validate formulas against spot checks.
- **Core Block 4 (60 min):** Produce diagnostics, stress checks, and fallback pathways.
- **Core Block 5 (45 min):** Deliver interview-style defense with risk controls and escalation.
- **Required Extension Block A (60 min):** Re-run project on alternate assumptions and compare drift.
- **Required Extension Block B (60 min):** Prepare production memo and launch/no-launch decision log.
- **Optional Deep Work (0-4 hours):** Expand tests, improve monitoring, and polish stakeholder narrative.

## Why It Matters in Quant
Project day is where research quality meets execution discipline and communication quality under risk constraints.

## Continuity and Handoff
- Previous checkpoint: Week 20 Day 06: Revision Sprint
- Previous lesson file: content/week-20/day-06.md
- Today's deliverable: Capstone 5: Multi-strategy paper portfolio
- Next handoff target: Week 21 Day 01: Program targeting and fit matrix
- Next lesson file: content/week-21/day-01.md

## Project Blueprint
### Project Title
Capstone 5: Multi-strategy paper portfolio

### Problem Statement
Construct a multi-sleeve paper portfolio with microstructure-aware execution assumptions.

### Data Sources
- Strategy sleeve signals
- Liquidity proxies
- Cost model inputs

### Implementation Steps
1. Design sleeve blend
2. Apply execution-cost assumptions
3. Backtest net performance
4. Analyze attribution
5. Produce governance report

### Evaluation Metrics
- Net Sharpe proxy
- Cost drag
- Capacity proxy
- Risk-budget adherence

### Execution Standard
- [ ] Notebook/script runs from clean start without hidden state
- [ ] Outputs include at least one diagnostic table and one chart
- [ ] One explicit risk guardrail and fallback action are documented

### Deliverables
- Notebook or script output
- One-page summary memo
- Tracker update with completion and lessons learned

## Mathematical Foundations (LaTeX)
### Formula 1: Information Coefficient
$$
IC_t=Corr(score_{i,t},r_{i,t+1})
$$
**Plain-English interpretation:** Signal/forward-return linkage.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 2: IC t-Statistic
$$
t_{IC}=\frac{\bar{IC}}{Std(IC)/\sqrt{T}}
$$
**Plain-English interpretation:** Signal persistence test.
**Notation check:** Identify each symbol and its units before coding this formula.
**Real-world anchor:** Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.

### Formula 3: Spread Z-Score
$$
z_t=\frac{s_t-\mu_s}{\sigma_s}
$$
**Plain-English interpretation:** Stat-arb entry normalization.
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
- Day objective: Deliver a capstone-quality notebook and summarize one trade-off under stress assumptions.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Portfolio Project'.

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
2. Implement today's objective as reusable functions: Ship the project notebook with reproducible outputs, controls, and one escalation rule.
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
1. State project objective and one hard failure condition in under 45 seconds.
2. Validate one formula output against a manual spot-check.
3. Show one stress scenario where your decision changes and explain why.
4. Add one edge-case test and one fallback rule to the notebook.
5. Deliver a one-minute PM summary with one risk guardrail.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 20 Day 07): Explain Information Coefficient and define every symbol clearly for a crowded-factor unwind with liquidity deterioration.
   - Model answer: "I use Information Coefficient as a decision bridge from market observations to position sizing. The formula is $IC_t=Corr(score_{i,t},r_{i,t+1})$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then throttle position sizing when estimated implementation shortfall rises above threshold. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify survivorship-bias controls, borrow/shortability flags, and capacity-aware data completeness checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Portfolio Project' matter in live trading systems?
   - Model answer: "Portfolio Project matters because signal quality is meaningless unless net-of-cost and capacity-aware in live execution. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I halve position sizes, widen execution limits, and re-open capacity only after slippage improves. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Portfolio Project in an execution review with rising slippage and crowding risk."
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
What single risk control would block launch today, and what evidence would clear it?

## Completion Checklist
- [ ] Project notebook runs cleanly from fresh kernel
- [ ] Risk guardrail and fallback action documented
- [ ] Stress scenario comparison completed
- [ ] One-page summary memo finalized
- [ ] Launch/no-launch decision recorded with evidence
