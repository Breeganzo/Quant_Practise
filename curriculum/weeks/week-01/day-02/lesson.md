# Week 01 Day 02: Algebraic transformations for returns

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
- Previous checkpoint: Week 01 Day 01: Environment reproducibility and data loading
- Previous lesson file: content/week-01/day-01.md
- Today's deliverable: Implement helper functions for return conversion and scaling.
- Next handoff target: Week 01 Day 03: Calculus intuition for optimization
- Next lesson file: content/week-01/day-03.md

## Theory Concepts

### Concept 1: Simple returns vs log returns
Simple returns vs log returns should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Compounding and cumulative performance
Compounding and cumulative performance should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Feature scaling for comparability
Feature scaling for comparability should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)

### Formula 1: Simple Return (One Period)
$$
r_t = \frac{P_t}{P_{t-1}} - 1 = \frac{P_t - P_{t-1}}{P_{t-1}}
$$

**What does this mean?**
- Calculate your percentage profit/loss from holding an asset for one period
- Start with shares bought at price $P_{t-1}$ (yesterday's or previous period's price)
- Sell at price $P_t$ (today's price)
- Your return = (profit) / (initial investment)

**Symbol Glossary:**
| Symbol | Meaning | Example |
|--------|---------|---------|
| $r_t$ | Simple return (decimal or %) | 0.0160 = 1.60% |
| $P_t$ | Asset price at END of period $t$ | $111.76 |
| $P_{t-1}$ | Asset price at END of period $t-1$ (one period ago) | $110.00 |
| $t$ | Time index (day 1, day 2, etc.) | Today = period 5 |

**Intuition:**
- If you buy at \$100 and sell at \$110: $r = (110-100)/100 = 0.10 = 10\%$ profit
- If you buy at \$100 and sell at \$95: $r = (95-100)/100 = -0.05 = -5\%$ loss
- The fraction $(P_t - P_{t-1}) / P_{t-1}$ directly answers: "What % did I gain/lose?"

**Alternative form (Gross Return):**
$$
1 + r_t = \frac{P_t}{P_{t-1}}
$$
- $1 + r_t$ tells you the multiple on your investment
- Example: $1 + 0.10 = 1.10$ means your wealth multiplied by 1.10 (10% gain)

---

### Formula 2: Compounding Over Multiple Periods
$$
\text{Total Wealth After } n \text{ Periods} = (1 + r_1) \times (1 + r_2) \times \cdots \times (1 + r_n)
$$

**What does this mean?**
- When returns happen over multiple days/months, you need to multiply the gross returns, not add them
- This is because each period's gain/loss is calculated on the *new* wealth, not the original

**Symbol Glossary:**
| Symbol | Meaning | Example |
|--------|---------|---------|
| $r_i$ | Simple return in period $i$ | Day 1: 2%, Day 2: -1%, Day 3: 3% |
| $1 + r_i$ | Wealth multiplier for period $i$ | 1.02, 0.99, 1.03 |
| Product | Total multiplication effect | 1.02 × 0.99 × 1.03 = 1.0403 |

**Intuition - Why Multiply, Not Add?**
- Day 1: Buy at \$100, sell at \$102 → 2% gain, wealth = \$102
- Day 2: Buy at \$102, sell at \$100.98 → **-1% on \$102** (not on \$100), wealth = \$100.98
- Day 3: Buy at \$100.98, sell at \$104.01 → **3% on \$100.98** (not on original \$100), wealth = \$104.01
- Total return = (\$104.01 - \$100) / \$100 = 4.01% NOT 2% + (-1%) + 3% = 4%
- Proof: 1.02 × 0.99 × 1.03 = 1.0403 = 4.03% (compounding compounds!)

**Long-term example:**
- Annual return of 10% per year for 5 years
- NOT: 10% + 10% + 10% + 10% + 10% = 50%
- INSTEAD: $1.10^5 = 1.6105 = 61.05\%$ (compound growth is powerful!)

---

### Formula 3: Log Return (Additive Return Representation)
$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

**What does this mean?**
- A mathematical transformation of simple return that has a useful property: log returns ADD over time (unlike simple returns which multiply)
- Useful for: statistical modeling, optimization, communication

**Symbol Glossary:**
| Symbol | Meaning | Example |
|--------|---------|---------|
| $\ell_t$ | Log return (must add over time) | 0.0158 (compare to simple 1.6%) |
| $\ln$ | Natural logarithm (base $e \approx 2.718$) | $\ln(1.016) \approx 0.0158$ |
| Relationship | $\ell_t = \ln(1 + r_t)$ | Log return ≈ simple return if return is small |

**Intuition - Why Log Returns?**
- Simple returns multiply: 1.02 × 0.99 × 1.03
- Log returns add: 0.0198 + (-0.0101) + 0.0296 = 0.0393
- For statistics, addition is easier than multiplication!
- Log returns are *almost* equal to simple returns for small changes (within 1% they're very close)

**When to use:**
- ✓ Quantitative analysis, statistical models, machine learning
- ✓ Academic papers and research
- ✗ Explaining returns to clients/stakeholders (use simple return %)

---

### Formula 4: Annualized Volatility (Scale Daily to Yearly)
$$
\sigma_{ann}=\sqrt{252}\,\sigma_d
$$

**What does this mean?**
- Daily volatility (measured on 1-day returns) scaled to an annualized (yearly) basis
- Assumes ~252 trading days per year (standard market calendar)

**Symbol Glossary:**
| Symbol | Meaning | Example |
|--------|---------|---------|
| $\sigma_{ann}$ | Annualized volatility (yearly uncertainty) | 0.18 = 18% yearly |
| $\sigma_d$ | Daily volatility (daily uncertainty) | 0.0113 = 1.13% daily |
| $\sqrt{252}$ | Scaling factor (15.87) | $\sqrt{252} = 15.87$ |

**Intuition - Why $\sqrt{252}$?**
- Variance (volatility squared) scales linearly with time: $\text{Var}_{\text{year}} = 252 \times \text{Var}_{\text{day}}$
- Volatility (standard deviation) scales with square root of time
- If daily vol = 1%, then yearly vol ≈ 1% × 15.87 = 15.87%
- This assumes daily returns are independent (not true during crises, but reasonable long-term)

---

### Formula 5: Sharpe Ratio (Risk-Adjusted Performance)
$$
S=\frac{R_{ann}-R_f}{\sigma_{ann}}
$$

**What does this mean?**
- How much excess return (above risk-free rate) per unit of risk (volatility)
- Higher Sharpe = better risk-adjusted performance

**Symbol Glossary:**
| Symbol | Meaning | Example |
|--------|---------|---------|
| $S$ | Sharpe ratio (dimensionless) | 0.80 is good |
| $R_{ann}$ | Annualized return (yearly %) | 0.14 = 14% per year |
| $R_f$ | Risk-free rate (treasury return) | 0.03 = 3% per year |
| $\sigma_{ann}$ | Annualized volatility (yearly %) | 0.18 = 18% per year |
| Numerator | "Excess return" beyond risk-free | 0.14 - 0.03 = 0.11 = 11% |

**Intuition:**
- Risk-free return: Invest in Treasury bonds, get 3% with zero risk
- Risky investment: Get 14% but with 18% volatility
- Excess reward: 14% - 3% = 11% above risk-free
- Per unit of risk: 11% / 18% = 0.61 (you earn 0.61% excess per 1% of volatility taken)
- Higher ratio means more reward per unit of risk (better deal)

**Real comparison:**
- Strategy A: 12% return, 15% volatility → Sharpe = (0.12 - 0.03) / 0.15 = 0.60
- Strategy B: 15% return, 25% volatility → Sharpe = (0.15 - 0.03) / 0.25 = 0.48
- Despite higher return, Strategy A is better risk-adjusted (more return per unit of risk)

## Symbol Definitions (Summary)
- $P_t$: Price at time $t$ (e.g., today's closing price)
- $P_{t-1}$: Price at time $t-1$ (e.g., yesterday's closing price)
- $r_t$: Simple return in period $t$ (decimal, e.g., 0.016 for 1.6%)
- $\ell_t$: Log return in period $t$ (decimal, used for math/statistics)
- $\sigma_d$: Daily volatility (daily standard deviation of returns)
- $\sigma_{ann}$: Annualized volatility (yearly standard deviation of returns)
- $\mu$: Expected return (mean of returns)
- $R_{ann}$: Annualized return (average yearly return)
- $R_f$: Risk-free rate (return from Treasury bonds)
- $S$: Sharpe ratio (risk-adjusted performance metric)
- $t$: Time index (period number: day 1, day 2, etc.)

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Convert a price series to daily returns and cumulative growth index.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Algebraic transformations for returns'.

## Step-by-Step Solved Problems

### Solved Problem 1: Compute Simple Return (One-Day Holding)

**Real Trading Scenario:**
You buy 100 shares of Apple at the open on Day 1 at \$104.00/share.
At the close of Day 1, Apple is trading at \$105.35/share.
What is your daily return?

**Given:**
- $P_{t-1} = \$104.00$ (opening price)
- $P_t = \$105.35$ (closing price)
- Number of shares: 100 (doesn't matter for return calculation!)

**Solution:**

**Step 1:** Calculate the simple return formula
$$r_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{\$105.35 - \$104.00}{\$104.00}$$

**Step 2:** Plug in numbers
$$r_t = \frac{\$1.35}{\$104.00} = 0.012980$$

**Step 3:** Convert to percentage
$$r_t = 0.012980 \times 100\% = 1.30\%$$

**Interpretation:**
- You made a 1.30% profit on your initial investment
- In dollar terms: 100 shares × \$1.35 = \$135 profit on a \$10,400 investment
- Verification: \$135 / \$10,400 = 0.01298 = 1.30% ✓

**Gross return check:**
$$1 + r_t = 1 + 0.01298 = 1.01298 = \frac{P_t}{P_{t-1}} = \frac{105.35}{104.00} = 1.01298$$ ✓

**Final Answer:** Simple return = **1.30%**, Gross return = **1.01298**

---

### Solved Problem 2: Compute Compound Return Over 3 Days

**Real Trading Scenario:**
You hold an equity position for 3 consecutive trading days. Daily returns:
- Day 1: +2.0%
- Day 2: -1.5%
- Day 3: +1.8%

What is your total return over the 3 days?

**Given:**
- $r_1 = 0.020$ (Day 1 return)
- $r_2 = -0.015$ (Day 2 return)
- $r_3 = 0.018$ (Day 3 return)

**Wrong approach (TRAP - DO NOT DO THIS):**
$$\text{Total return} = r_1 + r_2 + r_3 = 0.020 - 0.015 + 0.018 = 0.023 = 2.3\%$$ ❌

This is WRONG because each day's return compounds on the new wealth, not the original!

**Correct approach (Multiply Gross Returns):**

**Step 1:** Convert each return to gross return (multiply factor)
- Day 1: $1 + r_1 = 1 + 0.020 = 1.020$
- Day 2: $1 + r_2 = 1 - 0.015 = 0.985$
- Day 3: $1 + r_3 = 1 + 0.018 = 1.018$

**Step 2:** Multiply gross returns together
$$\text{Total Wealth Multiplier} = 1.020 \times 0.985 \times 1.018 = 1.02316$$

**Step 3:** Convert back to simple return
$$r_{\text{total}} = 1.02316 - 1 = 0.02316 = 2.316\%$$

**Why the difference?**
- Simple sum: 2.3%
- Correct compounding: 2.316%
- The extra 0.016% = 0.016% comes from compounding (the gain on gains)

**Numerical proof:**
- Start with \$10,000
- Day 1: \$10,000 × 1.020 = \$10,200
- Day 2: \$10,200 × 0.985 = \$10,047
- Day 3: \$10,047 × 1.018 = \$10,231.60
- Total return: (\$10,231.60 - \$10,000) / \$10,000 = 0.02316 = 2.316% ✓

**Final Answer:** Compound return over 3 days = **2.316%** (NOT 2.3%)

---

### Solved Problem 3: Annualize Daily Volatility

**Real Trading Scenario:**
You compute the daily volatility (standard deviation of daily returns) for Apple over the past year.
The daily volatility is 1.19%.
What is the annualized volatility?

**Given:**
- $\sigma_d = 0.0119$ (daily volatility as decimal)
- Trading days per year: 252 (standard market convention)

**Solution:**

**Step 1:** Apply annualization formula
$$\sigma_{ann} = \sqrt{252} \times \sigma_d$$

**Step 2:** Calculate the scaling factor
$$\sqrt{252} = 15.8745$$

**Step 3:** Multiply daily volatility by scaling factor
$$\sigma_{ann} = 15.8745 \times 0.0119 = 0.1889$$

**Step 4:** Convert to percentage
$$\sigma_{ann} = 0.1889 \times 100\% = 18.89\%$$

**Intuition - Why $\sqrt{252}$?**
- Daily volatility compounds roughly as: if each day has 1% std dev, after 252 days we'd expect $\sqrt{252} \approx 15.87$ times that variability
- This assumes daily returns are independent (reasonable for most stocks, breaks down in crises)

**Sanity check:**
- Daily volatility = 1.19% makes sense (daily moves are usually small)
- Yearly volatility = 18.89% makes sense (yearly moves are much larger)
- Ratio: 18.89% / 1.19% = 15.87 ≈ √252 ✓

**Final Answer:** Annualized volatility = **18.89%** (or 0.1889 in decimal form)

---

### Solved Problem 4: Calculate Sharpe Ratio

**Real Trading Scenario:**
A quantitative strategy has these annual metrics:
- Average annual return: 14.0%
- Annual volatility: 18.89%
- Current Treasury (risk-free) rate: 3.0%

What is the Sharpe ratio, and is this strategy attractive?

**Given:**
- $R_{ann} = 0.14$ (annual return)
- $\sigma_{ann} = 0.1889$ (annual volatility)
- $R_f = 0.03$ (risk-free rate)

**Solution:**

**Step 1:** Calculate excess return
$$R_{ann} - R_f = 0.14 - 0.03 = 0.11 = 11\%$$

**Interpretation:** The strategy beats the risk-free rate by 11 percentage points.

**Step 2:** Divide excess return by volatility
$$S = \frac{0.11}{0.1889} = 0.5823$$

**Step 3:** Interpret the result

| Sharpe Ratio | Interpretation |
|--------------|-----------------|
| < 0 | Worse than risk-free (avoid) |
| 0 - 0.4 | Poor risk-adjusted return |
| 0.4 - 0.8 | Acceptable (this strategy) |
| 0.8 - 1.5 | Good |
| > 1.5 | Excellent |

**Comparison to alternatives:**
- Treasury bonds: Sharpe = (0.03 - 0.03) / 0 = undefined, but no risk
- S&P 500 historically: Sharpe ≈ 0.45
- This strategy: Sharpe = 0.58 → *slightly better than market average*

**Final Answer:** Sharpe ratio = **0.58** (reasonably attractive, slightly outperforms broad market on risk-adjusted basis)

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Implement helper functions for return conversion and scaling.
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
When should you avoid log-return communication with stakeholders?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
