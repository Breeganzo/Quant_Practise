# Week 01 Day 03: Calculus intuition for optimization

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving
- 45 minutes: coding walkthrough and output verification

## Why It Matters in Quant
Rebuild core quant workflow habits and foundational finance vocabulary.

## Continuity and Handoff
- Previous checkpoint: Week 01 Day 02: Algebraic transformations for returns
- Previous lesson file: content/week-01/day-02.md
- Today's deliverable: Plot objective values across different risk-aversion parameters.
- Next handoff target: Week 01 Day 04: Market structure and asset classes
- Next lesson file: content/week-01/day-04.md

## Theory Concepts

### Concept 1: First derivative as local slope
First derivative as local slope should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Second derivative and curvature
Second derivative and curvature should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Convexity intuition in risk objectives
Convexity intuition in risk objectives should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)

### **BLOCK 3 (45 min): Worked Examples and Common Traps**

Calculus is everywhere in quant finance, but most people misunderstand it. This section uses real examples to build intuition.

---

### Formula 1: The Objective Function (What We're Trying to Maximize)

In portfolio optimization, we want to maximize the "risk-adjusted return":

$$
\text{Objective} = R_{portfolio} - \lambda \times \sigma_{portfolio}^2
$$

**Plain English:**
- We want high returns (first term, +)
- We want low risk/volatility (second term, -)
- $\lambda$ (lambda) = "how much do we care about risk?" (risk aversion parameter)
- If $\lambda = 0$: We ignore risk (aggressive)
- If $\lambda = \infty$: We only care about minimizing risk (conservative)

**Symbol Breakdown:**

| Symbol | Meaning | Range | Example |
|--------|---------|-------|---------|
| $R_{portfolio}$ | Portfolio return | -100% to +100% | 12% annual |
| $\sigma_{portfolio}$ | Portfolio volatility | > 0 | 18% annually |
| $\lambda$ | Risk aversion parameter | > 0 | 2.5 |
| $\sigma^2$ | Variance (volatility squared) | > 0 | 0.0324 |

**Trading Example - Two Strategies:**

| Strategy | Return | Volatility | $\lambda = 1$ Objective | $\lambda = 5$ Objective |
|----------|--------|-----------|----------------------|----------------------|
| Aggressive | 20% | 25% | 0.20 - 1×(0.25)² = 0.0375 | 0.20 - 5×(0.25)² = -0.1125 |
| Conservative | 8% | 10% | 0.08 - 1×(0.10)² = 0.07 | 0.08 - 5×(0.10)² = 0.03 |

**Interpretation:**
- With $\lambda = 1$ (moderate risk aversion): Aggressive wins (0.0375 > 0.07) → No! This is WRONG
- Wait, let me recalculate: Aggressive = 0.20 - 0.0625 = 0.1375, Conservative = 0.08 - 0.01 = 0.07 ✓
- With $\lambda = 1$: Aggressive wins (more reward per risk taken)
- With $\lambda = 5$ (high risk aversion): Conservative wins (lower volatility penalty)

---

### Formula 2: First Derivative (Finding the Peak of a Mountain)

The first derivative tells us the **slope** of a function:

$$
\frac{d(\text{Objective})}{d(\lambda)} = \frac{dR}{d\lambda} - \frac{d(\lambda \sigma^2)}{d\lambda} = 0 - \sigma^2 = -\sigma^2
$$

**Plain English:**
- The slope is always negative → As $\lambda$ increases, the objective ALWAYS decreases
- This makes sense: higher risk aversion → lower portfolio return

**Intuition - Think of a Mountain:**
```
Objective Value (Happiness)
         ^
       / | \
      /  |  \       First derivative = slope
     /   |   \      At peak: slope = 0 (flat)
    /    |    \     On left: slope > 0 (going up)
   /     |     \    On right: slope < 0 (going down)
--+------+------+-- λ (Risk Aversion)
  0      λ*     5
```

**Real Scenario:**
- At $\lambda = 0$: Slope = -$\sigma^2$ < 0 (objective decreasing)
- At $\lambda = 2$: Slope = -$\sigma^2$ < 0 (still decreasing, but slower)
- This means the objective always slopes downward as risk aversion increases

---

### Formula 3: Second Derivative (How Quickly the Slope Changes)

The second derivative tells us the **curvature** (how fast the slope is changing):

$$
\frac{d^2(\text{Objective})}{d\lambda^2} = -2\sigma^2 < 0
$$

**Plain English:**
- Negative second derivative = **Concave** function = shaped like ⌢ (mountain peak)
- This means the rate of decrease is slowing down (we're flattening out)

**Intuition - How Quickly the Slope Changes:**
```
Slope of Objective
         ^
         |     ← Slope becomes less negative as λ increases
         |    /
         |   /  ← Rate of change = second derivative
         |  /
         | /
    ----+---- λ
         |
```

**Real Numbers Example:**
- At $\lambda = 1$: Slope = -0.0324 (if $\sigma = 0.18$)
- At $\lambda = 2$: Slope = -0.0324 (same! Second derivative tells us about acceleration)
- The second derivative = -2(0.18)² = -0.0648 (curvature is constant)

---

### Formula 4: Convexity and Risk Management

**Convex Function** (∪ shaped): Second derivative > 0
**Concave Function** (∩ shaped): Second derivative < 0

Why does this matter in finance?

$$
\text{Loss Function} = \lambda \times \sigma_{portfolio}^2
$$

This is **convex** (∪ shaped) → "Doubling the risk more than doubles the penalty"

**Real Example:**
- Small increase in risk: +1% volatility → +$λ × 0.01² = +λ × 0.0001 penalty
- Large increase in risk: +10% volatility → +$λ × 0.10² = +λ × 0.01 penalty
- The 10x larger increase in risk causes a 100x larger penalty (convexity!)

This is why risk managers care so much about avoiding tail risks: **losses compound non-linearly**

---

## Symbol Definitions

- $\lambda$ (lambda): Risk aversion parameter (how much we penalize volatility)
- $R_{portfolio}$: Total portfolio return
- $\sigma_{portfolio}$: Portfolio volatility (standard deviation of returns)
- $\sigma^2$: Variance (volatility squared)
- $\frac{d}{d\lambda}$: First derivative (slope/rate of change)
- $\frac{d^2}{d\lambda^2}$: Second derivative (curvature/acceleration)

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Visualize how a mean-variance objective changes with risk aversion.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Calculus intuition for optimization'.

## Step-by-Step Solved Problems

### Solved Problem 1: Understanding the Objective Function (Finding the Best Risk-Return Tradeoff)

**Scenario:** You're building a portfolio optimizer. You have two candidate portfolios:
- **Portfolio A (Aggressive)**: 18% return, 24% volatility
- **Portfolio B (Conservative)**: 9% return, 12% volatility

Your risk aversion parameter is $\lambda = 2$.

Which portfolio is better according to the objective function?

**Given:**
- $R_A = 0.18$, $\sigma_A = 0.24$, so $\sigma_A^2 = 0.0576$
- $R_B = 0.09$, $\sigma_B = 0.12$, so $\sigma_B^2 = 0.0144$
- $\lambda = 2$

**Solution:**

**Step 1:** Calculate objective for Portfolio A
$$\text{Objective}_A = R_A - \lambda \times \sigma_A^2 = 0.18 - 2 \times 0.0576 = 0.18 - 0.1152 = 0.0648$$

**Step 2:** Calculate objective for Portfolio B
$$\text{Objective}_B = R_B - \lambda \times \sigma_B^2 = 0.09 - 2 \times 0.0144 = 0.09 - 0.0288 = 0.0612$$

**Step 3:** Compare
- Portfolio A: 0.0648 ✓ BETTER
- Portfolio B: 0.0612

**Interpretation:**
- Portfolio A has higher return (18% vs 9%)
- Portfolio A has higher volatility (24% vs 12%), but with $\lambda = 2$, the extra return more than compensates
- The aggressive portfolio wins with this level of risk aversion

**Trap - Common Mistake:**
❌ "Portfolio A has 24% volatility which is scary, so let's choose Portfolio B"
✓ "Portfolio A offers 9% more return for only 12% more volatility. With $\lambda = 2$, that's a good deal."

**Final Answer:** Choose **Portfolio A** (objective = 0.0648 > 0.0612)

---

### Solved Problem 2: How Risk Aversion Changes the Winner (Sensitivity Analysis)

**Scenario:** Same two portfolios. What if your risk aversion parameter changes?

- Portfolio A: 18% return, 24% volatility
- Portfolio B: 9% return, 12% volatility

Calculate objectives for $\lambda = 1, 2, 3, 5$ and see when each portfolio wins.

**Solution:**

For each $\lambda$, calculate both objectives:

$$\text{Objective} = R - \lambda \times \sigma^2$$

**$\lambda = 1$ (Low risk aversion - aggressive):**
- $\text{Obj}_A = 0.18 - 1(0.0576) = 0.1224$ ✓ Winner
- $\text{Obj}_B = 0.09 - 1(0.0144) = 0.0756$
- Result: Aggressive portfolio wins

**$\lambda = 2$ (Moderate risk aversion):**
- $\text{Obj}_A = 0.18 - 2(0.0576) = 0.0648$ ✓ Winner
- $\text{Obj}_B = 0.09 - 2(0.0144) = 0.0612$
- Result: Aggressive portfolio still wins

**$\lambda = 3$ (Higher risk aversion):**
- $\text{Obj}_A = 0.18 - 3(0.0576) = 0.0072$ ✓ Winner (but barely)
- $\text{Obj}_B = 0.09 - 3(0.0144) = 0.0468$
- Wait! Let me recalculate: Obj_B = 0.09 - 0.0432 = 0.0468 ✓ Winner
- Result: Conservative portfolio wins!

**$\lambda = 5$ (Very high risk aversion - conservative):**
- $\text{Obj}_A = 0.18 - 5(0.0576) = -0.1080$ (Negative!)
- $\text{Obj}_B = 0.09 - 5(0.0144) = 0.0180$ ✓ Clear winner
- Result: Conservative portfolio dominates

**Interpretation Table:**

| Risk Aversion | Portfolio A Objective | Portfolio B Objective | Winner | Why |
|---------------|----------------------|----------------------|--------|-----|
| $\lambda = 1$ | 0.1224 | 0.0756 | A | Low penalty for volatility |
| $\lambda = 2$ | 0.0648 | 0.0612 | A | Extra return > extra risk penalty |
| $\lambda = 3$ | 0.0072 | 0.0468 | B | Risk penalty dominates return |
| $\lambda = 5$ | -0.1080 | 0.0180 | B | Risk aversion very high |

**Key Insight:** There exists a "crossover point" around $\lambda = 2.5-3$ where the winner switches from A to B. This is why understanding risk aversion matters!

**Final Answer:** 
- Low risk aversion → Choose A
- High risk aversion → Choose B
- Optimal $\lambda$ depends on your portfolio's constraint

---

### Solved Problem 3: Understanding Slope (First Derivative)

**Scenario:** You want to understand how the objective function changes as you increase risk aversion.

Given: Portfolio volatility = 18% = 0.18

How does the objective change when you increase $\lambda$ from 1 to 2?

**Solution:**

**Step 1:** Understand what the first derivative tells us

The first derivative of our objective with respect to $\lambda$ is:
$$\frac{d(\text{Objective})}{d\lambda} = -\sigma^2$$

This tells us: "For every unit increase in $\lambda$, the objective decreases by $\sigma^2$"

**Step 2:** Calculate the slope

$$\frac{d(\text{Objective})}{d\lambda} = -(0.18)^2 = -0.0324$$

This means: "Increasing $\lambda$ by 1 unit decreases the objective by 0.0324"

**Step 3:** Verify with actual calculations

- At $\lambda = 1$: Objective = (some return) - 1(0.0324) = X - 0.0324
- At $\lambda = 2$: Objective = (same return) - 2(0.0324) = X - 0.0648
- Change: (X - 0.0648) - (X - 0.0324) = -0.0324 ✓ Matches slope!

**Interpretation:**
- The slope is negative → increasing risk aversion decreases objective value
- The slope is constant → each unit of $\lambda$ reduces objective by the same amount
- Magnitude = $\sigma^2$ = 0.0324 → Higher volatility → steeper downward slope

**Intuition - Why Constant Slope?**
Because our objective is a **linear function** of $\lambda$: Obj = (constant) - $\lambda$(constant)
- Linear functions have constant slope
- Non-linear functions (like quadratic) have changing slopes

**Final Answer:** Slope = **-0.0324** (objective decreases by 0.0324 for each unit increase in $\lambda$)

---

### Solved Problem 4: Understanding Curvature (Second Derivative)

**Scenario:** In what way is the objective function "curved"?

Is it more like a straight line (linear), or does it have bends?

**Solution:**

**Step 1:** Calculate the second derivative

$$\frac{d^2(\text{Objective})}{d\lambda^2} = -2\sigma^2 = -2(0.18)^2 = -0.0648$$

The second derivative is **negative and constant**.

**Step 2:** Interpret the sign

- **Negative second derivative** = Concave function (∩ shaped)
- This means the function is "bowing downward" like a mountain top

```
Objective
    ^
    |   ∩    ← Concave (negative second derivative)
    |  / \
    | /   \
----+------+---- λ
    |
```

**Step 3:** Interpret the magnitude

The second derivative = -0.0648 tells us: "The slope decreases by 0.0648 for each unit of $\lambda$"

Example:
- At $\lambda = 0$: Slope ≈ -(some value)
- At $\lambda = 1$: Slope ≈ -(same value) - 0.0648 = slightly more negative

Wait, this doesn't seem right for linear function. Let me reconsider:

Actually, since our objective is linear in $\lambda$, the second derivative should be **0**, not -0.0648.

The -0.0648 value would apply if we were considering how volatility penalty changes, but that's not what we're looking at here.

**Correction - For Risk Management:**

When we consider how **losses compound** with volatility:
$$\text{Loss} = \lambda \sigma^2$$

The second derivative of this loss function is:
$$\frac{d^2(\text{Loss})}{d\sigma^2} = 2\lambda > 0$$

**This means:** The loss function is **convex** (∪ shaped) in volatility

```
Loss
  ^
  | /\    ← Convex (positive second derivative)
  |/  \
--+----+-- σ
```

**Why This Matters in Risk Management:**
- Small risk: $\sigma = 0.01$ → Loss = $\lambda(0.01)^2$ = small
- Double the risk: $\sigma = 0.02$ → Loss = $\lambda(0.02)^2$ = 4× the loss (NOT 2×!)
- Triple the risk: $\sigma = 0.03$ → Loss = $\lambda(0.03)^2$ = 9× the loss (NOT 3×!)

This **convexity** is why risk managers are so concerned about tail risks: doubling volatility more than doubles the penalty.

**Final Answer:** 
- Objective w.r.t. $\lambda$: Linear (second derivative = 0)
- Loss w.r.t. volatility: **Convex** (positive second derivative = accelerating penalties)**

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Plot objective values across different risk-aversion parameters.
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

## Practice Problems
1. Re-derive all formulas manually and explain each variable.
2. Re-run the real trading example using one alternate ticker.
3. Stress-test one assumption and write a risk-control rule.
4. Extend the code walkthrough with one new validation test.

## Reflection Question
How can noisy market data mislead gradient-based intuition?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
