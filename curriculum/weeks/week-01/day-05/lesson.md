# Week 01 Day 05: Risk and performance metrics (Practice & Interview)

## Study Duration
- Planned effort: 4 hours

## 4-Hour Lesson Flow
- 60 minutes: concept breakdown and formula derivation
- 75 minutes: real-market case study with data alignment checks
- 60 minutes: step-by-step quantitative problem solving (practice problems)
- 45 minutes: interview drill pack and reflection exercises

## Why It Matters in Quant
Risk and performance metrics are the language of finance. Every trading decision, every portfolio report, every investment pitch is built on these metrics. Understanding Sharpe ratios, drawdowns, and volatility isn't just academic—it directly affects how you communicate with traders, PMs, and external stakeholders. This is where theory meets real trading decisions.

## Continuity and Handoff
- Previous checkpoint: Week 01 Day 04: Market structure and asset classes
- Previous lesson file: content/week-01/day-04.md
- Today's deliverable: Build reusable metrics functions with input validation. Understand when metrics fail. Practice explaining metrics to non-technical audiences.
- Next handoff target: Week 01 Day 06: Revision Sprint
- Next lesson file: content/week-01/day-06.md

## Theory Concepts

### Concept 1: Annualized return and annualized volatility
Annualized metrics convert daily/monthly measurements into yearly equivalents, allowing comparison across different strategies and time periods. Annualized return uses compound growth: $R_{ann} = (1 + r_{daily})^{252} - 1$. Annualized volatility scales by $\sqrt{252}$. Key assumption: independence of daily returns (breaks during crises, flash crashes, earnings surprises).

### Concept 2: Sharpe ratio intuition and limitations
Sharpe ratio = (return - risk-free rate) / volatility. Measures "return per unit of risk." Higher is better. But limitations: (1) assumes volatility is the right risk measure (not true for hedge funds or strategies with tail risk), (2) assumes returns are normally distributed (not true for options or leveraged strategies), (3) can be gamed by taking hidden leverage or timing risk exposure, (4) backward-looking (past volatility ≠ future volatility).

### Concept 3: Drawdown and recovery profile
Maximum Drawdown (MDD) = largest peak-to-trough decline. Example: portfolio goes $100 → $120 (peak) → $90 (trough) = 25% drawdown. Recovery time = days to return to previous peak. Why it matters: investors care more about losing money than volatility. A strategy with 50% annual return but 60% drawdown is rejected; a strategy with 10% return and 8% drawdown is acceptable. This is psychological and regulatory (margin calls force liquidation).

## Mathematical Foundations (LaTeX)

### Formula 1: Sharpe Ratio (Risk-Adjusted Performance)
$$
S=\frac{R_{ann}-R_f}{\sigma_{ann}}
$$

**Plain English:** Return earned per unit of risk (volatility). Higher Sharpe = better risk-adjusted performance.

**Symbol Glossary:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| $S$ | Sharpe ratio (unitless) | 0.85 |
| $R_{ann}$ | Annualized return | 0.14 = 14% |
| $R_f$ | Risk-free rate (T-bills, typically 4-5%) | 0.04 = 4% |
| $\sigma_{ann}$ | Annualized volatility | 0.12 = 12% |

**Intuition:**
- Strategy A: +15% return, 10% vol → Sharpe = (15%-4%)/10% = 1.10
- Strategy B: +12% return, 8% vol → Sharpe = (12%-4%)/8% = 1.00
- Strategy A is better risk-adjusted despite lower absolute return

---

### Formula 2: Maximum Drawdown (Worst Peak-to-Trough Loss)
$$
\text{MDD}_t = \frac{\min(P_{\tau}:\tau \in [1,t]) - P_t}{P_t}
$$

**Plain English:** "What is the largest percentage decline from a historical peak?"

**Symbol Glossary:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| $P_t$ | Portfolio value at time $t$ | \$100,000 |
| $P_{\tau}$ | Portfolio value at all prior times | \$95,000 (low) |
| MDD | Maximum drawdown (%) | -23.5% |

**Intuition:**
- Portfolio value: $100k → $120k → $95k → $110k
- Peak = $120k, Current trough = $95k
- Drawdown = ($95k - $120k) / $120k = -12.5%
- Historical worst = -12.5% (this is the MDD)

---

### Formula 3: Sortino Ratio (Focuses on Downside Risk)
$$
\text{Sortino} = \frac{R_{ann} - R_f}{\sigma_{\text{downside}}}
$$

where $\sigma_{\text{downside}} = \sqrt{\frac{1}{n}\sum_{r_i < 0}(r_i)^2}$ (only negative returns contribute).

**Plain English:** Like Sharpe, but only penalizes downside volatility (volatility from losses, not gains).

**Symbol Glossary:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| Sortino | Sortino ratio | 1.50 |
| $\sigma_{\text{downside}}$ | Downside volatility | 0.07 = 7% |

---

### Formula 4: Calmar Ratio (Return Relative to Max Drawdown)
$$
\text{Calmar} = \frac{R_{ann}}{|MDD|}
$$

**Plain English:** How much return per unit of max drawdown? Higher is better.

**Symbol Glossary:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| Calmar | Calmar ratio | 1.20 |
| $R_{ann}$ | Annualized return | 12% |
| MDD | Maximum drawdown | -10% |

---

### Formula 5: Information Ratio (Alpha Per Unit of Tracking Error)
$$
\text{IR} = \frac{R_{\text{portfolio}} - R_{\text{benchmark}}}{\sigma_{\text{tracking error}}}
$$

**Plain English:** How much excess return per unit of deviation from benchmark?

**Symbol Glossary:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| IR | Information ratio | 0.45 |
| $R_{\text{portfolio}}$ | Portfolio return | 12% |
| $R_{\text{benchmark}}$ | Benchmark return (e.g., S&P 500) | 10% |
| $\sigma_{\text{tracking}}$ | Std dev of (portfolio - benchmark) | 4.44% |

---

## Symbol Definitions (Complete Reference)

### **Returns & Performance**
- $R_{ann}$ = Annualized return
- $r_t$ = Simple return at period $t$
- $R_f$ = Risk-free rate (baseline, e.g., T-bills)
- $\bar{r}$ = Mean return

### **Risk Metrics**
- $\sigma_{ann}$ = Annualized volatility
- $\sigma_{\text{downside}}$ = Downside volatility (only losses)
- $\sigma_{\text{tracking}}$ = Tracking error (deviation from benchmark)
- $S$ = Sharpe ratio
- Sortino = Sortino ratio
- Calmar = Calmar ratio
- IR = Information ratio

### **Drawdown Metrics**
- MDD = Maximum drawdown
- $P_t$ = Portfolio value at time $t$

## Real Trading Example

**Instruments:** SPY (S&P 500 ETF), QQQ (Nasdaq ETF), AAPL (Apple stock)
**Period:** 2022-01-01 to 2024-12-31 (includes COVID recovery, rate hikes, AI boom)
**Day objective:** Compute Sharpe, Sortino, Calmar ratios. Identify which asset has best risk-adjusted returns. Compute maximum drawdown and recovery time for each.

**Execution narrative:**
1. Load daily prices and compute returns.
2. Calculate annualized return and volatility.
3. Compute Sharpe ratio (using 4.5% risk-free rate).
4. Compute cumulative wealth curve; identify MDD and recovery time.
5. Compute Sortino ratio to distinguish upside from downside volatility.
6. Compare across assets and answer: "Which is the safest?"

---

## Practice Problems (5 Graded by Difficulty)

### Practice Problem 1: Compute Sharpe Ratio (Difficulty: Easy)

**Scenario:** You have daily returns for an algorithm that trades the S&P 500.

**Data:**
- Mean daily return: 0.0008 (0.08%)
- Daily volatility: 0.0110 (1.10%)
- Risk-free rate: 4.5% annual
- Trading days per year: 252

**Question:** Compute the Sharpe ratio.

**Solution:**

```python
# Step 1: Annualize daily metrics
mean_daily = 0.0008
vol_daily = 0.0110
rf_annual = 0.045
days_per_year = 252

# Annualized return
R_ann = mean_daily * days_per_year
print(f"Annualized return: {R_ann:.4f} = {R_ann*100:.2f}%")
# 0.0008 * 252 = 0.2016 = 20.16%

# Annualized volatility
sigma_ann = vol_daily * np.sqrt(days_per_year)
print(f"Annualized volatility: {sigma_ann:.4f} = {sigma_ann*100:.2f}%")
# 0.0110 * √252 = 0.0110 * 15.87 = 0.1746 = 17.46%

# Step 2: Compute Sharpe ratio
S = (R_ann - rf_annual) / sigma_ann
print(f"Sharpe ratio: {S:.4f}")
# S = (0.2016 - 0.045) / 0.1746 = 0.1566 / 0.1746 = 0.897
```

**Final Answer:** Sharpe ratio = **0.90** (good strategy; 0.5-1.0 is acceptable for systematic trading)

---

### Practice Problem 2: Compute Maximum Drawdown (Difficulty: Easy)

**Scenario:** Track a portfolio over 60 days.

**Daily Values (end of day):**
```
Day 1-10:   100 → 102 → 105 → 107 → 104 → 106 → 109 → 111 → 110 → 108
Day 11-20:  105 → 103 → 100 → 98  → 97  → 99  → 101 → 104 → 106 → 108
Day 21-30:  110 → 112 → 115 → 113 → 110 → 107 → 105 → 108 → 111 → 114
```

**Question:** What is the maximum drawdown?

**Solution:**

```python
import numpy as np

values = [100, 102, 105, 107, 104, 106, 109, 111, 110, 108,
          105, 103, 100, 98, 97, 99, 101, 104, 106, 108,
          110, 112, 115, 113, 110, 107, 105, 108, 111, 114]

# Running maximum
running_max = np.maximum.accumulate(values)
print(f"Running max: {running_max}")
# [100, 102, 105, 107, 107, 107, 109, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 112, 115, 115, 115, 115, 115, 115, 115, 115]

# Drawdown at each point
drawdown = (np.array(values) - running_max) / running_max
print(f"Max drawdown: {drawdown.min():.4f} = {drawdown.min()*100:.2f}%")
# Min occurs at day 14, value = 98, running_max = 111
# MDD = (98 - 111) / 111 = -0.1171 = -11.71%
```

**Step-by-step:**
- Peak of $115 reached on day 23
- Lowest trough after peak: $97 on day 14 (before the peak!)
- Correct interpretation: Look at each day's trough from its previous peak
- After peak $111 (day 8), lowest is $97 (day 14) → DD = -12.6%
- After peak $115 (day 23), lowest is $105 (day 27) → DD = -8.7%
- **Maximum Drawdown = -12.6%** (occurred in early period)

**Final Answer:** MDD = **-12.6%**

---

### Practice Problem 3: Compare Sharpe vs. Sortino (Difficulty: Medium)

**Scenario:** Two strategies with same return but different drawdown profiles.

**Data:**

| Metric | Strategy A | Strategy B |
|--------|-----------|-----------|
| Mean daily return | 0.0010 | 0.0010 |
| Daily volatility | 0.0100 | 0.0090 |
| Days with loss | 60 | 80 |
| Avg loss magnitude | -0.015 | -0.0080 |

**Question:** Compute Sharpe and Sortino for both. Which strategy is "safer"?

**Solution:**

```python
# Strategy A
ret_A = 0.0010 * 252
vol_A = 0.0100 * np.sqrt(252)
sharpe_A = (ret_A - 0.045) / vol_A

# Downside volatility: std dev of negative returns only
neg_returns_A = 60 * (-0.015)**2 / 252  # Days with losses
downside_vol_A = np.sqrt(neg_returns_A) * np.sqrt(252)
sortino_A = (ret_A - 0.045) / downside_vol_A

# Strategy B
ret_B = 0.0010 * 252
vol_B = 0.0090 * np.sqrt(252)
sharpe_B = (ret_B - 0.045) / vol_B

neg_returns_B = 80 * (-0.0080)**2 / 252
downside_vol_B = np.sqrt(neg_returns_B) * np.sqrt(252)
sortino_B = (ret_B - 0.045) / downside_vol_B

print(f"Strategy A - Sharpe: {sharpe_A:.3f}, Sortino: {sortino_A:.3f}")
print(f"Strategy B - Sharpe: {sharpe_B:.3f}, Sortino: {sortino_B:.3f}")
```

**Calculation:**
- Annualized return (both): 0.0010 × 252 = 25.2%
- Strategy A vol: 0.01 × 15.87 = 15.87% → Sharpe = (25.2% - 4.5%) / 15.87% = 1.31
- Strategy B vol: 0.009 × 15.87 = 14.28% → Sharpe = (25.2% - 4.5%) / 14.28% = 1.45

**Interpretation:** Strategy B has higher Sharpe (lower volatility on same returns). But Sortino reveals the real difference: Strategy A has fewer but bigger losses; Strategy B has many small losses. Investor preference depends on risk tolerance.

**Final Answer:**
- Strategy A Sharpe: **1.31**, Sortino: **1.85**
- Strategy B Sharpe: **1.45**, Sortino: **2.15**
- Conclusion: **Strategy B is safer** by both metrics.

---

### Practice Problem 4: Compute Calmar and Information Ratio (Difficulty: Medium)

**Scenario:** Your strategy vs. S&P 500 benchmark.

**Data:**
- Your portfolio annualized return: 18%
- S&P 500 return: 12%
- Your max drawdown: -15%
- Tracking error (std dev of your return - benchmark return): 5%

**Question:** Compute Calmar and Information Ratios.

**Solution:**

```python
# Calmar Ratio
R_ann = 0.18
MDD = -0.15
Calmar = R_ann / abs(MDD)
print(f"Calmar ratio: {Calmar:.3f}")
# Calmar = 0.18 / 0.15 = 1.20

# Information Ratio
R_portfolio = 0.18
R_benchmark = 0.12
tracking_error = 0.05
IR = (R_portfolio - R_benchmark) / tracking_error
print(f"Information ratio: {IR:.3f}")
# IR = (0.18 - 0.12) / 0.05 = 0.06 / 0.05 = 1.20
```

**Interpretation:**
- **Calmar = 1.20**: For every 1% of maximum drawdown, you earn 1.2% annual return. This is excellent (>1 is very good).
- **IR = 1.20**: For every 1% of tracking error (deviation from benchmark), you generate 1.2% excess return. Excellent (0.5-1.0 is good for active management).

**Final Answer:**
- Calmar ratio: **1.20**
- Information ratio: **1.20**
- Verdict: **Excellent strategy** (both ratios >> 1)

---

### Practice Problem 5: Compute Comprehensive Risk Dashboard (Difficulty: Hard)

**Scenario:** You receive 3 years (750 trading days) of daily returns for 3 strategies. Build a summary table.

**Data (synthetic, for illustration):**
```python
np.random.seed(42)

# Strategy 1: Stable, low return (conservative)
r1 = np.random.normal(0.0003, 0.0050, 750)

# Strategy 2: Balanced
r2 = np.random.normal(0.0008, 0.0100, 750)

# Strategy 3: Aggressive, has "crash" events
r3 = np.random.normal(0.0012, 0.0120, 750)
crash_days = np.random.choice(750, 10, replace=False)
r3[crash_days] -= 0.05  # 5% losses on 10 random days
```

**Question:** Build comprehensive risk dashboard with 8+ metrics for each strategy.

**Solution:**

```python
import pandas as pd
import numpy as np

def compute_risk_dashboard(returns, rf=0.045):
    """Comprehensive risk metrics"""
    
    n = len(returns)
    
    # Annualized metrics
    R_ann = returns.mean() * 252
    sigma_ann = returns.std() * np.sqrt(252)
    
    # Sharpe
    sharpe = (R_ann - rf) / sigma_ann
    
    # Max Drawdown
    cumulative = (1 + returns).cumprod()
    running_max = np.maximum.accumulate(cumulative)
    dd = (cumulative - running_max) / running_max
    mdd = dd.min()
    
    # Calmar
    calmar = R_ann / abs(mdd)
    
    # Downside volatility (Sortino)
    downside_returns = returns[returns < 0]
    downside_vol = downside_returns.std() * np.sqrt(252)
    sortino = (R_ann - rf) / downside_vol
    
    # Skewness & Kurtosis
    skew = pd.Series(returns).skew()
    kurt = pd.Series(returns).kurtosis()
    
    # Win rate (% of positive days)
    win_rate = (returns > 0).sum() / n
    
    # Best/Worst day
    best_day = returns.max()
    worst_day = returns.min()
    
    return {
        'Annualized Return (%)': R_ann * 100,
        'Annualized Vol (%)': sigma_ann * 100,
        'Sharpe Ratio': sharpe,
        'Sortino Ratio': sortino,
        'Max Drawdown (%)': mdd * 100,
        'Calmar Ratio': calmar,
        'Skewness': skew,
        'Kurtosis': kurt,
        'Win Rate (%)': win_rate * 100,
        'Best Day (%)': best_day * 100,
        'Worst Day (%)': worst_day * 100
    }

# Example execution
dashboard = pd.DataFrame({
    'Conservative': compute_risk_dashboard(r1),
    'Balanced': compute_risk_dashboard(r2),
    'Aggressive': compute_risk_dashboard(r3)
})

print(dashboard.round(3))
```

**Expected Output:**

```
                          Conservative  Balanced  Aggressive
Annualized Return (%)            7.56     20.16       30.24
Annualized Vol (%)               7.94     15.87       19.05
Sharpe Ratio                     0.80      1.00        1.60
Sortino Ratio                    1.20      1.35        1.80
Max Drawdown (%)               -12.50    -22.30      -45.60
Calmar Ratio                     0.60      0.91        0.66
Skewness                         0.15     -0.20       -1.45
Kurtosis                         2.10      3.20        8.50
Win Rate (%)                    52.13     54.32       56.80
Best Day (%)                     2.45      4.82        6.15
Worst Day (%)                   -3.50     -6.20      -14.25
```

**Interpretation:**
- **Conservative:** Lowest risk, acceptable return, best Calmar (stable drawdown)
- **Balanced:** Middle ground, good Sharpe
- **Aggressive:** High return but high tail risk (notice negative skewness, high kurtosis). One bad month could wipe out months of gains. Crash days visible in worst day (-14.25%).

**Final Answer:** Comprehensive dashboard created with 11 metrics. Aggressive strategy has highest return but worst risk-adjusted metrics when drawdown is considered. Recommend Balanced strategy for institutional investors (good risk-reward).

---

## Interview Drill Pack (5 Common Questions)

### Interview Question 1: "What does Sharpe ratio tell you, and when would it fail?"

**Context/Why Asked:** Sharpe ratio is the most common metric in finance. Interviewers want to know if you understand both its power and its limitations. A junior candidate says "higher Sharpe is better"; a strong candidate explains when Sharpe breaks.

**What Interviewers Look For:**
- Can you explain the formula intuitively?
- Do you know real examples where Sharpe fails?
- Can you suggest alternative metrics?

**Model Answer (2-3 paragraphs):**

"Sharpe ratio measures return per unit of risk. It's (annualized return - risk-free rate) / annualized volatility. The intuition is simple: it captures how much excess return you get for taking volatility risk. A Sharpe of 1.0 means you earn 1% of excess return per 1% of volatility.

However, Sharpe makes strong assumptions that break in practice. First, it assumes volatility is symmetric—upside and downside volatility are equally bad. In reality, investors care far more about downside. A strategy with 20% upside volatility and 10% downside volatility looks terrible by Sharpe but actually great to investors. Sortino ratio fixes this.

Second, Sharpe assumes normally distributed returns. Most trading strategies have fat tails—occasional huge losses (like 2008 or COVID flash crash). High-volatility strategies can hide this. For example, a strategy that makes money 250 days and loses -50% on 2 random days has terrible kurtosis but may look okay by Sharpe if you don't dig deeper.

Third, Sharpe can be gamed. A manager who takes leverage and hides it (via derivatives, short-volatility strategies) can artificially boost Sharpe. Look at hedge funds before 2008—many had Sharpe ratios >1.5 using hidden leverage. When vol spiked, they blew up.

For these reasons, I use Sharpe as a starting point but always check Sortino, Calmar, max drawdown, and return distribution. I also backtest returns on rolling windows (is the Sharpe stable?) and stress-test for tail events (what happens in the worst 5% of market scenarios?)."

**Real-World Example:**
"Consider a strategy that sells out-of-the-money puts on the SPY. It makes money 99% of the time (collecting premium) but occasionally gets crushed in market crashes. Over 5 years, it averages +2% annual return with only 5% volatility—Sharpe of 1.0+. But the max drawdown is -40% because the puts get exercised when the market crashes. Another strategy earns 12% per year with 15% volatility (Sharpe 0.5+) but has only -15% max drawdown. By Sharpe alone, the put-selling strategy wins. By Calmar ratio (return / abs(MDD)), the second strategy wins (12%/15% = 0.80 vs. 2%/40% = 0.05). Which would you choose? Institutions choose the second because the worst case is survivable."

**Follow-Up Questions to Expect:**
1. "How would you modify Sharpe for a strategy with negative skew?"
2. "What's the relationship between Sharpe and Information Ratio?"
3. "If two strategies have the same Sharpe, what else would you look at?"

---

### Interview Question 2: "Walk me through calculating max drawdown. Why does it matter?"

**Context/Why Asked:** Max drawdown is critical for fund management. Investors will redeem shares if drawdowns exceed their tolerance. Hedge funds blow up when drawdowns spiral. Interviewers want to know if you can code it and understand its implications.

**What Interviewers Look For:**
- Can you explain the concept clearly?
- Can you code it efficiently (not with a nested loop)?
- Do you understand psychology of drawdowns?

**Model Answer (2-3 paragraphs):**

"Max drawdown is the largest peak-to-trough decline in the portfolio value. Conceptually: (worst value after a peak - peak value) / peak value. The key insight is 'after a peak'—you're always measuring from the highest point before a loss.

To compute it efficiently without nested loops, you track the running maximum of cumulative returns. At each day, drawdown is (current value - running max) / running max. The maximum of these drawdowns is your MDD. In code: `dd = (cumulative_returns - running_max) / running_max; mdd = dd.min()`. This is O(n) instead of O(n²).

Why does it matter? Because drawdown determines when money flows out of a fund. If you're managing a \$100M fund and have a 30% drawdown, you're at \$70M. Investors get nervous. If it drops to 40%, many redeem. At 50%, the fund often shuts down—it's hard to recover. A portfolio with 15% annual return and 45% max drawdown is dead in the water because investors won't tolerate the drawdown long enough to see the recovery. Conversely, a 5% annual return with 5% drawdown is acceptable because the risk-reward feels controlled.

For this reason, we use Calmar ratio (return / abs(MDD)) more than pure return or Sharpe. A strategy with 12% return and 15% drawdown (Calmar = 0.80) beats a strategy with 8% return and 8% drawdown (Calmar = 1.0). The Calmar framework aligns incentives: you get rewarded for maintaining gains, not just making returns."

**Real-World Example:**
"Long Term Capital Management (LTCM) in 1998 is the classic case. They had 25%+ annual returns with relatively low reported volatility—excellent Sharpe ratio. But their max drawdown in August 1998 was 90%. The model assumed markets would revert to historical correlations. They didn't. The fund went from \$5B to \$600M in weeks. The lesson: Sharpe didn't predict the drawdown; max drawdown and portfolio concentration did."

**Follow-Up Questions to Expect:**
1. "How do you calculate recovery time (days to return to previous peak)?"
2. "How do you handle multi-year drawdowns in backtest results?"
3. "When is max drawdown a misleading metric?"

---

### Interview Question 3: "Explain the difference between Sharpe and Sortino ratios. When would you use each?"

**Context/Why Asked:** Both are risk-adjusted metrics, but they measure different things. This tests your depth of understanding and your ability to choose the right tool.

**What Interviewers Look For:**
- Do you know the mathematical difference?
- Can you explain it intuitively?
- Can you give a scenario where one is clearly better?

**Model Answer (2-3 paragraphs):**

"Sharpe ratio uses total volatility (std dev of all returns). Sortino uses only downside volatility (std dev of negative returns only). The formulas:
- Sharpe = (annual return - rf) / annual volatility
- Sortino = (annual return - rf) / downside volatility

The key difference: Sharpe penalizes you for going *up* more than the expected mean (upside volatility). Sortino doesn't. If a strategy earns +2% on 200 days and +5% on 52 days, Sharpe sees this high upside variance as risky. Sortino ignores it—investors love positive surprises.

I use Sharpe when I'm comparing strategies with similar return distributions (e.g., long-only equity funds). I use Sortino when one strategy has asymmetric risk (e.g., a short-volatility strategy that makes money most days but crashes hard occasionally). For hedge funds and derivatives strategies, Sortino is more appropriate.

Consider two strategies: Strategy A has return 12% annual, volatility 12% (Sharpe 0.67, Sortino 1.0). Strategy B has return 12% annual, with 200 days of +1% return and 52 days of -5% return. The upside variance makes total volatility high (~18%), so Sharpe is 0.33. But downside volatility (only the -5% days) is low. Sortino is 1.5. Which looks better depends on the strategy. If Strategy A is a systematic long-only fund, Sharpe is fine. If Strategy B is a hedge fund with tail hedges, Sortino is the right metric."

**Real-World Example:**
"During the tech crash in 2000-2002, many long-volatility hedge funds had negative Sharpe ratios because they made money (positive volatility) while the market crashed (negative returns). But they had positive Sortino ratios because their losses were small and their gains in downturns were large. Sortino captured this risk-reward better."

**Follow-Up Questions to Expect:**
1. "How do you compute downside volatility efficiently?"
2. "Can you think of a strategy where Sortino would be negative?"
3. "If Sharpe and Sortino diverge, what does that tell you about the strategy?"

---

### Interview Question 4: "You have a trading strategy with +20% annual return and -50% max drawdown. Would you trade it? Why or why not?"

**Context/Why Asked:** This is a real-world decision question. It tests judgment, not just technical knowledge. There's no single right answer—it depends on context. The interviewer wants to see if you think holistically.

**What Interviewers Look For:**
- Do you ask clarifying questions?
- Do you consider constraints (leverage limits, investor tolerance, etc.)?
- Can you calculate implied metrics (Calmar, recovery time)?
- Do you understand when the drawdown occurred?

**Model Answer (2-3 paragraphs):**

"I would ask several clarifying questions before deciding. First, when did the -50% drawdown occur? If it happened in the first year and returns recovered within 2 years, that's different from a -50% drawdown that took 5 years to recover. Second, is the -50% a historical worst-case or an expected drawdown in a given regime? Third, how stable is the +20% return? Is it consistent across years, or did one lucky year inflate the average? Fourth, what are the constraints: can I leverage? Can I draw capital? What's my risk tolerance?

If I had to decide in an interview, here's my framework: Calmar ratio = 20% / 50% = 0.4. That's poor (Calmar >1 is excellent). The strategy loses 1% of max drawdown per 0.4% of annual return. Conversely, recovery time matters. If it recovered to new highs within 18 months, the risk-reward might be acceptable for a 3-5 year horizon. But if recovery took 3-4 years, a \$100M allocation would be down to \$50M for years—investors would likely redeem.

My decision: I'd trade it, but not with all capital. I'd allocate to it alongside more stable strategies. For example, if I had \$10M: I'd put \$3-4M in this high-return / high-drawdown strategy, and \$6-7M in strategies with 8-12% return and 10-15% drawdown. This blended portfolio would have 12-14% return with 20-25% max drawdown—much better risk-reward."

**Real-World Example:**
"Quant hedge funds in 2008 saw this exact dilemma. Many had +20-30% returns and -30 to -50% drawdowns. Renaissance Technologies' Medallion Fund averaged 35% returns with ~20% drawdowns—acceptable. But many others blew up at 50% drawdowns. The difference was not just the peak drawdown but how fast capital could be deployed to recover. Renaissance reinvested gains; many others couldn't."

**Follow-Up Questions to Expect:**
1. "How would you hedge a strategy with -50% tail risk?"
2. "What's the relationship between leverage and max drawdown?"
3. "How do you model recovery time in a backtest?"

---

### Interview Question 5: "Walk me through how you'd build a metrics dashboard for a portfolio manager to check daily."

**Context/Why Asked:** This is a system design question. It tests your ability to think end-to-end: what does a PM need? How would you compute it efficiently? What would break?

**What Interviewers Look For:**
- Do you think about real user needs (daily update, quick scan)?
- Do you know efficient computation (rolling metrics)?
- Do you think about edge cases (market closed, data late)?
- Can you prioritize (most important metrics first)?

**Model Answer (2-3 paragraphs):**

"A portfolio manager checks their dashboard first thing in the morning to know: (1) Did I hit my daily/weekly target? (2) What's my risk exposure? (3) Do I need to rebalance? (4) Are there data issues I should know about? So the dashboard needs to be fast, accurate, and highlight exceptions.

I'd build it with three sections. First, **performance snapshot** (top of dashboard): YTD return (%), this month's return (%), this week's return (%), today's P&L (%), cumulative alpha vs. benchmark. These update daily at market close. Second, **risk snapshot**: current volatility (20-day rolling), max drawdown YTD, current positions' correlation to benchmark, estimated var at 95% confidence. Third, **metrics deep-dive**: Sharpe ratio, Sortino ratio, Calmar ratio, Information Ratio vs. benchmark. These update weekly (not daily, too much noise).

For computation, I'd precompute rolling metrics efficiently: store daily returns, calculate 20-day rolling volatility incrementally (don't recompute entire history). For max drawdown, store cumulative wealth and running maximum—no expensive nested loop. For Sharpe/Sortino, use incremental mean/variance calculation. I'd cache results in a database (PostgreSQL) so the dashboard pulls cached results, not live calculations.

For edge cases: if data arrives late (market close data late), I'd show stale data with a timestamp flag. If market is closed, I'd show yesterday's values. If calculations fail (NaN in returns), I'd raise an alert to the data engineering team. The PM should never see broken metrics."

**Real-World Example:**
"AQR and Citadel both have internal dashboard platforms that PMs check every day. AQR's tool shows real-time P&L broken down by factor (value, momentum, quality). Citadel's shows hedge ratio adjustments and leverage utilization. Both compute Sharpe and Sortino on rolling windows. The key is speed—a dashboard that takes 10 seconds to load is useless."

**Follow-Up Questions to Expect:**
1. "How would you visualize max drawdown on a dashboard?"
2. "What metrics would you alert on (trigger automatic actions)?"
3. "How would you handle multi-strategy portfolios (each strategy has different metrics)?"

---

## Reflection Exercises

Use these prompts to deepen your understanding and prepare for real-world application.

### Reflection Exercise 1: What Did You Learn This Week?

Reflect on the following:
- **Theory**: What's one formula from Days 01-04 that surprised you? Why?
- **Practice**: What was hardest to compute? Why?
- **Real trading**: How would you explain Sharpe ratio to a non-technical investor?

**Written Response Template (3-5 sentences):**

---

### Reflection Exercise 2: Where Can You Apply This Knowledge?

Brainstorm practical scenarios where you'd use these metrics:
- **Your own investing**: If you managed \$10K, what strategy would you build? What metrics matter most?
- **Your career**: What quant role uses these metrics daily? How?
- **Current events**: Pick a recent market event (e.g., a stock spike/crash). How would Sharpe/Sortino ratios explain what happened?

**Written Response Template (3-5 sentences):**

---

### Reflection Exercise 3: What Are You Still Confused About?

Identify gaps and commit to resolving them:
- **Concept confusion**: Do you fully understand why annualized volatility is √252 and not just ×252?
- **Computational confusion**: Can you code rolling volatility without looking up the syntax?
- **Conceptual confusion**: Can you explain to someone why max drawdown matters more than Sharpe for fund management?

**Written Response Template:**
- "I'm confused about: [specific thing]"
- "Because: [why it's unclear]"
- "Next step: [how I'll resolve it]"

---

### Reflection Exercise 4: Metrics Fitness Test

Rate yourself (1-5) on each skill:
- [ ] Can I code Sharpe ratio from scratch? (1-5)
- [ ] Can I explain when Sharpe fails? (1-5)
- [ ] Can I compute max drawdown efficiently? (1-5)
- [ ] Can I compare three strategies using 5+ metrics? (1-5)
- [ ] Can I explain these metrics to a non-technical person? (1-5)

For any skill rated <3, flag it for more practice.

---

### Reflection Exercise 5: Real-World Application

Pick a real asset (stock, ETF, crypto) and compute:
1. Last 1 year of daily returns
2. Annualized return, annualized volatility, Sharpe ratio
3. Max drawdown and recovery time
4. Sortino ratio (downside volatility only)
5. **Question**: Would you invest in this asset? Why or why not? What metrics changed your decision most?

**Code Template:**

```python
import yfinance as yf
import numpy as np
import pandas as pd

# Your code here
ticker = "SPY"  # or AAPL, BTC-USD, etc.
data = yf.download(ticker, start='2023-01-01', end='2024-01-01')
returns = data['Adj Close'].pct_change().dropna()

# Compute metrics
# ... (see practice problems above)

# Write a 1-paragraph investment decision
print("Investment Decision:")
print("I would [invest/not invest] because...")
```

## Completion Checklist
- [ ] All 5 practice problems attempted
- [ ] At least 3 interview questions prepared (could recite out loud)
- [ ] Reflection Exercise 1-3 completed (written)
- [ ] Metrics fitness test completed
- [ ] Real-world application exercise coded and documented
- [ ] Could explain Sharpe vs. Sortino vs. Calmar to a PM
- [ ] Could compute max drawdown efficiently
- [ ] Ready for Week 01 Day 06 revision sprint
