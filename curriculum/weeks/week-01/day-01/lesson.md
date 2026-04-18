# Week 01 Day 01: Environment reproducibility and data loading

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
- Previous checkpoint: Program kickoff: environment, data loader, and assumption baseline.
- Today's deliverable: Build a reusable function that loads prices and validates schema assumptions.
- Next handoff target: Week 01 Day 02: Algebraic transformations for returns
- Next lesson file: content/week-01/day-02.md

## Theory Concepts

### Concept 1: Virtual environments and dependency locking
Virtual environments and dependency locking should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 2: Notebook hygiene and deterministic outputs
Notebook hygiene and deterministic outputs should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

### Concept 3: Market data schema (OHLCV) basics
Market data schema (OHLCV) basics should be treated as a measurable component of 'Python setup, math refresh, and market basics'. For this week, emphasize clean data assumptions and stable mathematical transformations. State the formula, verify units, test edge cases, and explain exactly how market regime shifts could break the assumption.

## Mathematical Foundations (LaTeX)

### **BLOCK 1 (45 min): Reset Notation - Prices, Returns, Percentages, and Variables**

Before learning finance formulas, let's establish a common language.

#### **Section 1.1: Time and Indexing**
In quantitative finance, we use subscripts to denote time:
- $P_t$ = Price at time $t$
- $P_{t-1}$ = Price at the previous period (one day ago if daily data)
- $P_{t+1}$ = Price at the next period (tomorrow if daily data)
- $r_t$ = Return earned during period $t$ (from time $t-1$ to time $t$)

**Example Timeline:**
```
Time:        Jan 1    Jan 2    Jan 3    Jan 4
             (t-2)    (t-1)     (t)    (t+1)
Price:       $100     $102     $101    $103
Return:        --      +2%      -1%     +2%
                      (from     (from   (from
                      Jan 1→2) Jan 2→3) Jan 3→4)
```

Notice: The return $r_t$ is earned *during* period $t$, calculated from $P_{t-1}$ to $P_t$.

#### **Section 1.2: Converting Between Decimals and Percentages**

Financial returns are communicated in three equivalent forms:

| Decimal | Percentage | Multiplier |
|---------|-----------|------------|
| 0.01 | 1% | 1.01× |
| -0.05 | -5% | 0.95× |
| 0.10 | 10% | 1.10× |
| -0.20 | -20% | 0.80× |

**Conversion rules:**
- Decimal to percentage: Multiply by 100. Example: 0.016 → 1.6%
- Percentage to decimal: Divide by 100. Example: 2.5% → 0.025
- To "multiply factor": Add 1 to decimal. Example: 0.10 decimal → 1.10 multiplier (10% gain = wealth × 1.10)

**Why three forms?**
- Decimal form: Used in math equations and code
- Percentage form: Used to communicate with stakeholders ("We made 5% today")
- Multiplier form: Used for calculations involving multiple periods (wealth compounds by multiplying)

#### **Section 1.3: Variable Glossary for Asset Prices**

| Symbol | Meaning | Unit | Example |
|--------|---------|------|---------|
| $P_t$ | Asset closing price at end of period $t$ | USD/share or cents | \$110.50 |
| $P_{\text{bid}}$ | Bid price (highest price buyer will pay) | USD/share | \$110.48 |
| $P_{\text{ask}}$ | Ask price (lowest price seller will accept) | USD/share | \$110.52 |
| $O_t$ | Opening price at start of period $t$ | USD/share | \$110.25 |
| $H_t$ | Highest price during period $t$ | USD/share | \$111.00 |
| $L_t$ | Lowest price during period $t$ | USD/share | \$110.10 |
| $V_t$ | Volume (shares traded) during period $t$ | shares/USD | 5,000,000 shares |

**Note on OHLCV data:**
- OHLCV = Open, High, Low, Close, Volume
- Standard market data format provided by data vendors (Yahoo Finance, Bloomberg, etc.)
- For return calculations, we typically use the Close price ($P_t$ or $C_t$)

#### **Section 1.4: Return Variables and Their Meanings**

| Symbol | Meaning | Range | Example |
|--------|---------|-------|---------|
| $r_t$ | Simple return (decimal) | (-1, +∞) | 0.016 |
| $r_t (\%)$ | Simple return (percent) | (-100%, +∞%) | 1.6% |
| $1 + r_t$ | Gross return or wealth multiplier | (0, +∞) | 1.016 |
| $\ell_t$ | Log return (decimal) | (-∞, +∞) | 0.0158 |
| $R_{ann}$ | Annualized return (yearly %) | depends on period | 14% |
| $\bar{r}$ | Mean return (average of all periods) | depends on data | 0.05% |
| $\sigma_t$ | Volatility (standard deviation of returns) | > 0 | 1.5% daily |

**Key insight:** 
- Simple return $r_t$ can never go below -1 (you can't lose more than 100%)
- Log return $\ell_t$ can go to negative infinity mathematically, but is easier for statistics
- Gross return $1 + r_t$ should always be positive (else you've gone bankrupt)

---

### Formula 1: Simple Return (One-Period Percentage Change)

$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$

**Plain English:** "What percentage did my investment change?"

**Symbol Breakdown:**
- $r_t$ = Your profit/loss as a fraction of what you started with
- $P_t$ = Price TODAY (end of period)
- $P_{t-1}$ = Price YESTERDAY (end of previous period)
- Numerator $P_t - P_{t-1}$ = Absolute dollar profit/loss
- Denominator $P_{t-1}$ = Your initial investment

**Mathematical Intuition:**
- If I invest \$100 and it becomes \$102: $r = (102-100)/100 = 0.02 = 2\%$
- If I invest \$100 and it becomes \$95: $r = (95-100)/100 = -0.05 = -5\%$
- The denominator normalizes by initial wealth (why we can compare investments of different sizes)

**Trading Example:**
- You buy Apple at \$102.00
- Next day Apple closes at \$103.22
- Your return: $r = (103.22 - 102.00) / 102.00 = 0.01196 = 1.196\%$

**Related Formula: Gross Return**
$$1 + r_t = \frac{P_t}{P_{t-1}}$$

The gross return tells you the multiplication factor. In the example: $1 + 0.01196 = 1.01196$ means your wealth multiplied by 1.01196.

---

### Formula 2: Log Return (For Mathematical Convenience)

$$
\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

**Plain English:** "The logarithmic return—a mathematical transformation that makes statistics easier."

**Symbol Breakdown:**
- $\ell_t$ = Log return (will be close to, but slightly different from simple return)
- $\ln$ = Natural logarithm (base $e \approx 2.71828$)
- The argument $P_t / P_{t-1}$ = Gross return

**Why Use Log Returns?**
- **Property**: Log returns ADD over time (simple returns multiply)
- Example: Day 1 +2%, Day 2 +3% → Total is NOT +5% (it's +5.06% due to compounding)
- But: log(1.02) + log(1.03) = log(1.02 × 1.03) = addition works!
- **For statistics**: It's much easier to add returns than to multiply them repeatedly

**Trading Example:**
- Stock goes from \$100 to \$102: Simple return = 2%, Log return = ln(1.02) = 0.01980 ≈ 1.98%
- For small returns, the two are nearly identical
- For large returns, they diverge: Stock goes from \$100 to \$150: Simple = 50%, Log = ln(1.50) = 40.5%

**When to use each:**
- ✓ Simple return: Communicating to stakeholders, regulatory reporting, client statements
- ✓ Log return: Statistical analysis, time-series models, academic research, optimization

---

### Formula 3: Annualized Volatility (Scale Daily Variance to Yearly)

$$
\sigma_{ann}=\sqrt{252}\,\sigma_d
$$

**Plain English:** "Take the daily volatility and scale it up to a yearly basis."

**Symbol Breakdown:**
- $\sigma_{ann}$ = Annualized volatility (yearly standard deviation)
- $\sigma_d$ = Daily volatility (daily standard deviation)
- $\sqrt{252}$ = Scaling factor (252 trading days per year)
- $\sqrt{}$ = Square root (because variance scales linearly, but std dev scales as square root)

**Why $\sqrt{252}$?**
- If each day has independent return distribution with std dev = $\sigma_d$
- Then over 252 days: $\text{Var}_{\text{annual}} = 252 × \text{Var}_{\text{daily}}$
- Taking square root: $\sigma_{\text{annual}} = \sqrt{252} × \sigma_{\text{daily}} = 15.87 × \sigma_{\text{daily}}$

**Sanity Check:**
- Daily volatility = 1% → Yearly volatility = 15.87%
- Daily volatility = 2% → Yearly volatility = 31.74%
- Does this make sense? Yes! Daily moves are small but compound over a year.

---

## Symbol Definitions (Complete Reference)

### **Price & Market Data**
- $P_t$ = Price (close) at time $t$ (units: USD/share or similar)
- $O_t$ = Opening price (units: USD/share)
- $H_t$ = High price during period (units: USD/share)
- $L_t$ = Low price during period (units: USD/share)
- $V_t$ = Volume (units: shares traded)

### **Returns**
- $r_t$ = Simple return (decimal, dimensionless)
- $r_t (\%)$ = Simple return as percentage
- $\ell_t$ = Log return (decimal, dimensionless)
- $1 + r_t$ = Gross return / wealth multiplier
- $\bar{r}$ = Average return / mean return
- $R_{ann}$ = Annualized return (yearly, units: %)

### **Risk & Volatility**
- $\sigma_d$ = Daily volatility / daily standard deviation
- $\sigma_{ann}$ = Annualized volatility / yearly standard deviation
- $\sigma$ = Standard deviation (generic)
- $\text{Var}$ = Variance (standard deviation squared)

### **Risk-Adjusted Returns**
- $R_f$ = Risk-free rate (Treasury return, units: %)
- $S$ = Sharpe ratio (dimensionless)
- $\mu$ = Expected return / drift

### **Other**
- $t$ = Time index (period number: day 1, day 2, etc.)
- $TO_t$ = Turnover at time $t$ (fraction of portfolio replaced)

## Real Trading Example
- Instruments: SPY, QQQ, AAPL
- Macro overlay (FRED): DGS10, UNRATE
- Suggested window: 2018-01-01 to 2026-03-31
- Day objective: Load three assets, verify missing values, and create a clean price table.

Execution narrative:
1. Pull market data from Yahoo Finance and align calendars.
2. Pull the listed FRED series and join strictly by release-aware timestamps.
3. Compute today's formulas and compare behavior in stress sub-periods.
4. Translate quantitative results into one explicit trading decision and one risk guardrail.
5. Validate that the decision is consistent with topic 'Environment reproducibility and data loading'.

## Step-by-Step Solved Problems

### Solved Problem 1: Read and Understand Notation

**Scenario:** You're given a dataset with the following:
- $P_{t-2} = \$100.00$ (Apple close price 2 days ago)
- $P_{t-1} = \$102.00$ (Apple close price yesterday)
- $P_t = \$103.22$ (Apple close price today)

Interpret the notation and identify: What is $P_t$? What is $P_{t-1}$? What does $r_t$ represent?

**Solution:**

**Step 1:** Identify the time subscripts
- $P_t$ = $103.22 = TODAY's closing price
- $P_{t-1}$ = $102.00 = YESTERDAY's closing price
- $P_{t-2}$ = $100.00 = TWO DAYS AGO closing price

**Step 2:** Interpret return notation
- $r_t$ = The return earned TODAY (from yesterday's close to today's close)
- $r_t$ = $(P_t - P_{t-1}) / P_{t-1}$ = $(103.22 - 102.00) / 102.00$ = 1.196%
- $r_{t-1}$ = The return earned YESTERDAY (from two days ago to yesterday)
- $r_{t-1}$ = $(P_{t-1} - P_{t-2}) / P_{t-2}$ = $(102.00 - 100.00) / 100.00$ = 2.00%

**Step 3:** Key insight about subscript meaning
The subscript $t$ refers to the END of the period. The return $r_t$ is earned DURING period $t$, from $P_{t-1}$ (start of period) to $P_t$ (end of period).

**Interpretation table:**

| Symbol | Value | Meaning |
|--------|-------|---------|
| $P_t$ | \$103.22 | Today's price (end of today's period) |
| $P_{t-1}$ | \$102.00 | Yesterday's price (end of yesterday's period = start of today's period) |
| $r_t$ | 1.196% | Return earned today |
| $r_{t-1}$ | 2.00% | Return earned yesterday |

**Final Answer:** $P_t = \$103.22$ (today), $P_{t-1} = \$102.00$ (yesterday), $r_t$ = 1.196% (today's return)

---

### Solved Problem 2: Convert Between Decimal, Percentage, and Multiplier Forms

**Scenario:** A portfolio manager tells you "We had a +1.5% day." Represent this in:
1. Decimal form
2. Percentage form
3. Multiplier (gross return) form

**Given:** Simple return = 1.5%

**Solution:**

**Step 1:** Percentage to decimal (divide by 100)
$$r_t = 1.5\% = \frac{1.5}{100} = 0.015$$

**Step 2:** Percentage form (already given)
$$r_t = 1.5\%$$

**Step 3:** Decimal to multiplier (add 1)
$$1 + r_t = 1 + 0.015 = 1.015$$

**Verification:** If you had \$1,000,000 yesterday, today you have $1,000,000 × 1.015 = \$1,015,000. Profit = \$15,000 = 1.5% of \$1,000,000 ✓

**Conversion summary:**

| Form | Value | When to Use |
|------|-------|-----------|
| Percentage | 1.5% | Communicating with stakeholders |
| Decimal | 0.015 | Formulas and code |
| Multiplier | 1.015 | Calculating compounded returns |

---

### Solved Problem 3: Compute Simple Return and Identify Components

**Scenario:** A stock goes from \$110.00 (yesterday) to \$111.76 (today).

Compute:
1. The simple return $r_t$
2. The gross return $1 + r_t$
3. Your dollar profit if you owned 1,000 shares

**Given:**
- $P_{t-1} = \$110.00$
- $P_t = \$111.76$
- Shares owned: 1,000

**Solution:**

**Step 1:** Compute simple return
$$r_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{111.76 - 110.00}{110.00} = \frac{1.76}{110.00} = 0.01600$$

**Convert to percentage:**
$$r_t = 0.01600 × 100 = 1.60\%$$

**Step 2:** Compute gross return
$$1 + r_t = 1 + 0.01600 = 1.01600$$

Interpretation: Your wealth multiplied by 1.01600.

**Step 3:** Calculate dollar profit
$$\text{Dollar profit} = \text{Shares} × (P_t - P_{t-1}) = 1,000 × 1.76 = \$1,760$$

**Verification:** 
- Started with: 1,000 × \$110.00 = \$110,000
- Ended with: 1,000 × \$111.76 = \$111,760
- Profit: \$111,760 - \$110,000 = \$1,760 ✓
- Return: \$1,760 / \$110,000 = 0.01600 = 1.60% ✓

**Final Answer:**
- Simple return = **1.60%** (or 0.01600)
- Gross return = **1.01600**
- Dollar profit = **\$1,760**

---

### Solved Problem 4: Annualize Volatility from Daily Volatility

**Scenario:** The daily volatility (standard deviation of daily returns) for a stock is 1.12%. What is the annualized volatility?

**Given:**
- $\sigma_d = 0.0112$ (daily volatility)
- Trading days per year = 252 (standard)

**Solution:**

**Step 1:** Apply annualization formula
$$\sigma_{ann} = \sqrt{252} × \sigma_d$$

**Step 2:** Calculate the square root of 252
$$\sqrt{252} = 15.8745...$$

**Step 3:** Multiply by daily volatility
$$\sigma_{ann} = 15.8745 × 0.0112 = 0.17779$$

**Step 4:** Convert to percentage
$$\sigma_{ann} = 0.17779 × 100 = 17.79\%$$

**Sanity check:**
- Daily volatility = 1.12% (reasonable for most stocks)
- Yearly volatility = 17.79% (reasonable, yearly swings are much bigger)
- Ratio = 17.79 / 1.12 = 15.88 ≈ √252 ✓

**Intuition:** If every single day has 1.12% volatility, then:
- After 1 day: variance ≈ 1.12%
- After 252 days (1 year): variance compounds, std dev scales by √252 ≈ 15.87

**Final Answer:** Annualized volatility = **17.79%** (or 0.1779 in decimal form)

## Coding Walkthrough
1. Build an explicit data-ingestion layer with timestamp and schema checks.
2. Implement today's objective as reusable functions: Build a reusable function that loads prices and validates schema assumptions.
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
Which part of your setup would most likely break on a new machine?

## Completion Checklist
- [ ] Formula derivations re-worked manually
- [ ] Real trading example reproduced with data checks
- [ ] Solved problems reviewed and understood
- [ ] Coding walkthrough executed and verified
- [ ] Reflection logged in progress tracker
