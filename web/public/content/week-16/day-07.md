# Week 16 Day 07: Portfolio Project

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
- Previous checkpoint: Week 16 Day 06: Revision Sprint
- Previous lesson file: content/week-16/day-06.md
- Today's deliverable: Capstone 4: Portfolio risk engine
- Next handoff target: Week 17 Day 01: Factor investing framework
- Next lesson file: content/week-17/day-01.md

## Project Blueprint
### Project Title
Capstone 4: Portfolio risk engine

### Problem Statement
Build a risk engine combining VaR, CVaR, stress tests, and reporting controls.

### Data Sources
- Portfolio return streams
- Shock scenarios
- Risk limits

### Implementation Steps
1. Implement VaR/CVaR methods
2. Integrate stress scenarios
3. Check limit breaches
4. Create risk dashboard
5. Deliver governance memo

### Evaluation Metrics
- Tail-risk coverage
- Scenario responsiveness
- Limit adherence
- Governance completeness

### Execution Standard
- [ ] Notebook/script runs from clean start without hidden state
- [ ] Outputs include at least one diagnostic table and one chart
- [ ] One explicit risk guardrail and fallback action are documented

### Deliverables
- Notebook or script output
- One-page summary memo
- Tracker update with completion and lessons learned

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
- Stress windows to inspect: 2020-02 to 2020-04, 2022-01 to 2022-10
- Scenario context: cross-asset drawdown with correlation spikes
- Day objective: Deliver a capstone-quality notebook and summarize one trade-off under stress assumptions.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull listed FRED series and join strictly by release-aware timestamps (no look-ahead).
3. Compute today's formulas and compare calm vs stress-window behavior.
4. Translate outputs into one explicit trade action and one hard risk guardrail.
5. Validate that the decision is consistent with topic 'Portfolio Project'.

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
2. Implement today's objective as reusable functions: Ship the project notebook with reproducible outputs, controls, and one escalation rule.
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
1. State project objective and one hard failure condition in under 45 seconds.
2. Validate one formula output against a manual spot-check.
3. Show one stress scenario where your decision changes and explain why.
4. Add one edge-case test and one fallback rule to the notebook.
5. Deliver a one-minute PM summary with one risk guardrail.

### Daily Quiz (Realistic Interview Style)
1. PM interview question (Week 16 Day 07): Explain Portfolio Variance and define every symbol clearly for a cross-asset drawdown week with correlation spikes.
   - Model answer: "I use Portfolio Variance as a decision bridge from market observations to position sizing. The formula is $\sigma_p^2=w^\top\Sigma w$. I define each symbol with units first, then compute one concrete value, and finally state what trade action changes because of the result in this regime."
2. Risk manager question: Using one real ticker from this lesson, what hard guardrail would you enforce before live deployment?
   - Model answer: "I would run the workflow on SPY and a stress-sensitive peer, then force rebalance when risk-budget contribution of one sleeve exceeds 40%. If the guardrail triggers, I switch to paper-trade monitoring and block new risk until diagnostics re-pass."
3. Data integrity question: Which checks must pass before you trust the output and place risk?
   - Model answer: "Before trading I verify covariance window consistency, stale-price filtering, and exposure normalization checks. If any check fails, I classify the run as non-tradable and log the incident."
4. Production question: Why does 'Portfolio Project' matter in live trading systems?
   - Model answer: "Portfolio Project matters because portfolio choices are constrained by covariance instability, transaction costs, and risk budgets. In production I need reproducible calculations, explicit control limits, and escalation rules that survive stress windows."
5. Decision question: If your key metric degrades for three consecutive sessions, what is your fallback plan?
   - Model answer: "I de-risk to benchmark weights, rerun stress tests, and re-enable risk only after guardrails pass. I only restore risk after rerun evidence confirms that assumptions are stable again."

Scoring rubric:
- 10/10: correct notation, one numeric example, explicit guardrail, data checks, and escalation path.
- 8/10: mostly correct notation plus a clear guardrail and fallback action.
- 6/10: partial correctness but vague controls or missing data validation.
- Below 6/10: formula recall without decision-quality risk controls.

### Interview Drill
- Prompt: "Walk me through Portfolio Project in an investment committee session after correlation breakdown."
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
