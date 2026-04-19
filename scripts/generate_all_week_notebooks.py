from __future__ import annotations

import argparse
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


def setup_code() -> str:
    return "\n".join(
        [
            "from datetime import date",
            "import warnings",
            "import numpy as np",
            "import pandas as pd",
            "",
            "try:",
            "    import yfinance as yf",
            "except Exception:",
            "    yf = None",
            "",
            "try:",
            "    from pandas_datareader import data as pdr",
            "except Exception:",
            "    pdr = None",
            "",
            "np.set_printoptions(precision=4, suppress=True)",
            "pd.options.display.float_format = '{:.6f}'.format",
            "",
            "def _synthetic_price_frame(tickers, start='2018-01-01', periods=900, seed=7):",
            "    idx = pd.bdate_range(start, periods=periods)",
            "    out = pd.DataFrame(index=idx)",
            "    rng = np.random.default_rng(seed)",
            "    for i, ticker in enumerate(tickers):",
            "        drift = 0.0002 + 0.00005 * (i + 1)",
            "        vol = 0.010 + 0.002 * i",
            "        rets = rng.normal(drift, vol, size=len(idx))",
            "        out[ticker] = 100.0 * np.exp(np.cumsum(rets))",
            "    return out",
            "",
            "def load_market_prices(tickers, start='2018-01-01', end=None):",
            "    end = end or date.today().isoformat()",
            "    tickers = list(tickers)",
            "    if yf is None:",
            "        warnings.warn('yfinance unavailable, using synthetic data')",
            "        return _synthetic_price_frame(tickers, start=start)",
            "",
            "    try:",
            "        raw = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)",
            "        if isinstance(raw.columns, pd.MultiIndex):",
            "            if 'Close' in raw.columns.get_level_values(0):",
            "                close = raw['Close']",
            "            else:",
            "                close = raw.xs('Close', axis=1, level=0, drop_level=True)",
            "        else:",
            "            close = raw.rename(columns={raw.columns[0]: tickers[0]})",
            "        close = close.reindex(columns=tickers)",
            "        close = close.dropna(how='all').ffill().dropna()",
            "        if close.empty:",
            "            raise ValueError('empty market data from Yahoo Finance')",
            "        return close",
            "    except Exception as exc:",
            "        warnings.warn(f'Yahoo download failed ({exc}); using synthetic data')",
            "        return _synthetic_price_frame(tickers, start=start)",
            "",
            "def load_fred_series(series_id, start='2018-01-01', end=None):",
            "    end = end or date.today().isoformat()",
            "    if pdr is None:",
            "        warnings.warn('pandas_datareader unavailable, using synthetic macro data')",
            "        idx = pd.bdate_range(start, end)",
            "        vals = np.linspace(1.0, 1.2, len(idx)) + np.sin(np.arange(len(idx)) / 25) * 0.02",
            "        return pd.Series(vals, index=idx, name=series_id)",
            "",
            "    try:",
            "        ser = pdr.DataReader(series_id, 'fred', start, end)[series_id]",
            "        ser = ser.ffill().dropna()",
            "        if ser.empty:",
            "            raise ValueError('empty FRED series')",
            "        return ser",
            "    except Exception as exc:",
            "        warnings.warn(f'FRED download failed ({exc}); using synthetic macro data')",
            "        idx = pd.bdate_range(start, end)",
            "        vals = np.linspace(1.0, 1.2, len(idx)) + np.sin(np.arange(len(idx)) / 25) * 0.02",
            "        return pd.Series(vals, index=idx, name=series_id)",
        ]
    )


def demo_code_for_week(week_no: int, day_no: int) -> str:
    seed = week_no * 100 + day_no

    if week_no <= 4:
        return f"""# Foundation demo: real prices + macro overlay with fallback
np.random.seed({seed})
prices = load_market_prices(['SPY', 'QQQ', 'AAPL'], start='2018-01-01')
returns = prices.pct_change().dropna()
macro = load_fred_series('DGS10', start='2018-01-01').rename('dgs10')
joined = returns.join(macro, how='inner').dropna()

growth = float((1 + joined['SPY']).prod())
ann_return = float((1 + joined['SPY']).prod() ** (252 / joined.shape[0]) - 1)
ann_vol = float(joined['SPY'].std() * np.sqrt(252))
drawdown = float((prices['SPY'] / prices['SPY'].cummax() - 1).min())
rate_corr = float(joined['SPY'].corr(joined['dgs10']))

{{
    'growth_multiple': growth,
    'annualized_return': ann_return,
    'annualized_volatility': ann_vol,
    'max_drawdown': drawdown,
    'spy_rate_corr': rate_corr,
}}
"""

    if week_no <= 8:
        return f"""# ML demo: directional classifier from real SPY features
np.random.seed({seed})
spy = load_market_prices(['SPY'], start='2014-01-01')['SPY']
ret = spy.pct_change()

feat = pd.DataFrame(index=spy.index)
feat['lag_1'] = ret.shift(1)
feat['lag_5'] = ret.rolling(5).mean().shift(1)
feat['vol_20'] = ret.rolling(20).std().shift(1)
feat['macro_rate'] = load_fred_series('DFF', start='2014-01-01').reindex(feat.index).ffill()
target = (ret.shift(-1) > 0).astype(int)
dataset = feat.join(target.rename('target')).dropna()

split = int(0.8 * len(dataset))
train = dataset.iloc[:split]
test = dataset.iloc[split:]

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, roc_auc_score

    model = LogisticRegression(max_iter=500)
    model.fit(train.drop(columns=['target']), train['target'])
    proba = model.predict_proba(test.drop(columns=['target']))[:, 1]
    pred = (proba >= 0.5).astype(int)
    out = {{
        'accuracy': float(accuracy_score(test['target'], pred)),
        'auc': float(roc_auc_score(test['target'], proba)),
    }}
except Exception:
    # fallback classifier if sklearn is unavailable
    pred = (test['lag_1'] > 0).astype(int)
    out = {{
        'accuracy': float((pred.values == test['target'].values).mean()),
        'auc': float('nan'),
    }}

out
"""

    if week_no <= 12:
        return f"""# Time-series demo: AR-style diagnostics on real returns
np.random.seed({seed})
series = load_market_prices(['SPY'], start='2010-01-01')['SPY'].pct_change().dropna()
x_prev = series.shift(1).dropna()
x_curr = series.loc[x_prev.index]

phi = float(np.cov(x_curr.values, x_prev.values, ddof=1)[0, 1] / np.var(x_prev.values, ddof=1))
forecast_next = float(phi * series.iloc[-1])
acf1 = float(series.autocorr(lag=1))
acf5 = float(series.autocorr(lag=5))
rmse_naive = float(np.sqrt(np.mean((series.iloc[1:].values - series.shift(1).dropna().values) ** 2)))

{{
    'ar1_phi': phi,
    'next_return_forecast': forecast_next,
    'acf_lag1': acf1,
    'acf_lag5': acf5,
    'naive_rmse': rmse_naive,
}}
"""

    if week_no <= 16:
        return f"""# Portfolio/risk demo: multi-asset allocation on real prices
np.random.seed({seed})
tickers = ['SPY', 'TLT', 'GLD', 'HYG']
prices = load_market_prices(tickers, start='2012-01-01')
returns = prices.pct_change().dropna()
mu = returns.mean().values * 252
cov = returns.cov().values * 252
vol = np.sqrt(np.diag(cov))

# inverse-volatility heuristic with normalization
inv_vol = 1 / np.maximum(vol, 1e-8)
weights = inv_vol / inv_vol.sum()
port_return = float(weights @ mu)
port_vol = float(np.sqrt(weights @ cov @ weights))
turnover_proxy = float(np.abs(np.diff(weights)).sum())

{{
    'tickers': tickers,
    'weights': [float(round(x, 4)) for x in weights],
    'portfolio_expected_return': port_return,
    'portfolio_volatility': port_vol,
    'turnover_proxy': turnover_proxy,
}}
"""

    if week_no <= 20:
        return f"""# Advanced strategy demo: cross-sectional momentum spread on real assets
np.random.seed({seed})
assets = ['SPY', 'QQQ', 'IWM', 'EFA', 'EEM', 'TLT', 'GLD', 'HYG']
prices = load_market_prices(assets, start='2015-01-01')

mom_63 = prices.pct_change(63).iloc[-1]
next_5 = prices.pct_change().tail(5).mean()
signals = mom_63.dropna().sort_values(ascending=False)

n = max(2, len(signals) // 4)
long_bucket = list(signals.head(n).index)
short_bucket = list(signals.tail(n).index)
spread = float(next_5.loc[long_bucket].mean() - next_5.loc[short_bucket].mean())

{{
    'long_bucket': long_bucket,
    'short_bucket': short_bucket,
    'spread_return_proxy': spread,
    'signal_snapshot': signals.round(4).to_dict(),
}}
"""

    return f"""# Integration demo: readiness tracker anchored to market context
np.random.seed({seed})
spy = load_market_prices(['SPY'], start='2018-01-01')['SPY']
ret = spy.pct_change().dropna()
macro_unrate = load_fred_series('UNRATE', start='2018-01-01').dropna()

ann_return = float((1 + ret).prod() ** (252 / len(ret)) - 1)
ann_vol = float(ret.std() * np.sqrt(252))
sharpe = float((ann_return - 0.03) / max(ann_vol, 1e-8))

quiz_avg = float(np.clip(70 + 10 * sharpe, 60, 95))
mock_scores = np.clip(np.array([72, 78, 81]) + sharpe * 5, 60, 95)
macro_level = float(macro_unrate.iloc[-1]) if not macro_unrate.empty else float('nan')

{{
    'spy_annualized_return': ann_return,
    'spy_annualized_vol': ann_vol,
    'spy_sharpe_proxy': sharpe,
    'latest_unemployment_rate': macro_level,
    'quiz_average': round(quiz_avg, 2),
    'mock_scores': [float(round(x, 2)) for x in mock_scores],
}}
"""


def topic_from_lesson(lesson_text: str, week_no: int, day_no: int) -> str:
    default_topic = f"Week {week_no:02d} Day {day_no:02d}"
    for line in lesson_text.splitlines():
        if line.startswith("# Week ") and ":" in line:
            return line.split(":", maxsplit=1)[1].strip()
    return default_topic


def quiz_markdown_for_day(week_no: int, day_no: int, topic: str) -> str:
    return "\n".join(
        [
            f"## Week {week_no:02d} Day {day_no:02d} Quiz",
            "",
            f"Topic: **{topic}**",
            "",
            "Real-world interview questions (answer first, then run the next cell for model answers):",
            "1. PM question: Which formula from today's lesson directly drives a trade decision, and what does each symbol mean?",
            "2. Risk question: Using one real ticker from today's example, what hard guardrail would you enforce before live deployment?",
            "3. Communication question: In one minute, explain why this topic matters for production trading systems.",
            "",
            "Scoring: full credit requires notation correctness, one numeric example, and one explicit risk control.",
        ]
    )


def quiz_solution_code_for_day(week_no: int, day_no: int, topic: str) -> str:
    base_price = 100 + week_no + day_no
    next_price = round(base_price * (1 + 0.008 + 0.0005 * day_no), 3)
    simple_return = (next_price - base_price) / base_price
    gross_return = 1 + simple_return
    phase = "foundations"
    if week_no <= 4:
        phase = "foundations"
    elif week_no <= 8:
        phase = "ml"
    elif week_no <= 12:
        phase = "time_series"
    elif week_no <= 16:
        phase = "portfolio"
    elif week_no <= 20:
        phase = "advanced"
    else:
        phase = "launch"

    scenario_by_phase = {
        "foundations": "inflation surprise week",
        "ml": "post-earnings drift regime",
        "time_series": "volatility-clustering window",
        "portfolio": "cross-asset drawdown phase",
        "advanced": "crowded-factor unwind",
        "launch": "live paper-trade month",
    }
    guardrail_by_phase = {
        "foundations": "cap exposure if rolling volatility breaches training 90th percentile",
        "ml": "freeze entries if calibration error worsens across three checks",
        "time_series": "de-risk when realized volatility exceeds model regime",
        "portfolio": "rebalance when one sleeve contributes over 40% of risk",
        "advanced": "throttle sizing when implementation shortfall exceeds threshold",
        "launch": "halt promotions when max drawdown breaches policy budget",
    }

    scenario = scenario_by_phase[phase]
    guardrail = guardrail_by_phase[phase]
    return f"""# Quiz model answers (auto-generated)
price_t_minus_1 = {base_price:.3f}
price_t = {next_price:.3f}
r_t = (price_t - price_t_minus_1) / price_t_minus_1
gross = 1 + r_t

print('Interview Question 1 (model answer):')
print('  I would use simple return to convert price moves into decision-ready percentages under {scenario}.')
print('  Formula: r_t = (P_t - P_(t-1)) / P_(t-1)')
print('  P_(t-1):', price_t_minus_1)
print('  P_t    :', price_t)
print('  r_t    :', round(r_t, 6), '=>', f'{{r_t*100:.2f}}%')
print('  1+r_t  :', round(gross, 6))

print('\\nInterview Question 2 (model answer):')
print('  For a real ticker like SPY, I would enforce this guardrail before deployment:')
print('  {guardrail}.')

print('\\nInterview Question 3 (model answer):')
print('  Topic:', {topic!r})
print('  This matters because production systems need reproducible metrics, explicit controls,')
print('  and a fallback decision path when stress conditions invalidate baseline assumptions.')

print('\\nNumeric verification:')
print('  simple_return_expected =', {simple_return:.6f})
print('  gross_return_expected  =', {gross_return:.6f})
"""


def demo_code_for_day(week_no: int, day_no: int) -> str:
    if day_no <= 5:
        return demo_code_for_week(week_no, day_no)

    if day_no == 6:
        seed = week_no * 100 + day_no
        return f"""# Revision sprint demo: rebuild weekly core diagnostics
np.random.seed({seed})
prices = load_market_prices(['SPY', 'QQQ', 'AAPL'], start='2018-01-01')
returns = prices.pct_change().dropna()

summary = pd.DataFrame({{
    'annual_return': returns.mean() * 252,
    'annual_vol': returns.std() * np.sqrt(252),
    'max_drawdown': (prices / prices.cummax() - 1).min(),
}})
summary['sharpe_proxy'] = (summary['annual_return'] - 0.03) / summary['annual_vol'].replace(0, np.nan)
summary = summary.sort_values('sharpe_proxy', ascending=False)

print('Revision diagnostics (best risk-adjusted first):')
summary.round(4)
"""

    seed = week_no * 100 + day_no
    return f"""# Project day demo: mini portfolio report with trade recommendation
np.random.seed({seed})
assets = ['SPY', 'QQQ', 'TLT', 'GLD']
prices = load_market_prices(assets, start='2019-01-01')
returns = prices.pct_change().dropna()

annual_return = returns.mean() * 252
annual_vol = returns.std() * np.sqrt(252)
score = (annual_return - 0.03) / annual_vol.replace(0, np.nan)

report = pd.DataFrame({{
    'annual_return': annual_return,
    'annual_vol': annual_vol,
    'sharpe_proxy': score,
}}).sort_values('sharpe_proxy', ascending=False)

top_asset = report.index[0]
print('Project summary:')
print(report.round(4))
print(f"\\nSuggested focus asset for follow-up research: {{top_asset}}")
"""


def verification_code_for_day(week_no: int, day_no: int, topic: str) -> str:
    seed = week_no * 100 + day_no + 9000
    return f"""# ReAct-style verification: observe -> reason -> act -> verify
np.random.seed({seed})

observe_tickers = ['SPY', 'QQQ', 'TLT']
observe_prices = load_market_prices(observe_tickers, start='2020-01-01')
observe_returns = observe_prices.pct_change().dropna()

if observe_returns.empty:
    raise ValueError('No returns available for verification checks')

ann_vol = float(observe_returns['SPY'].std() * np.sqrt(252))
ann_ret = float((1 + observe_returns['SPY']).prod() ** (252 / len(observe_returns)) - 1)
sharpe_proxy = float((ann_ret - 0.03) / max(ann_vol, 1e-8))

# Risk-first deployment gate used in realistic interview responses.
guardrail = 'de-risk' if ann_vol > 0.30 else 'monitor'
decision = 'deploy-paper-trade' if sharpe_proxy > 0.40 and guardrail == 'monitor' else 'hold-and-review'

verification = {{
    'topic': {topic!r},
    'week': {week_no},
    'day': {day_no},
    'observe_annual_return': ann_ret,
    'observe_annual_vol': ann_vol,
    'reason_sharpe_proxy': sharpe_proxy,
    'act_guardrail': guardrail,
    'verify_decision': decision,
}}

verification
"""


def create_day_notebook(
    week_no: int,
    day_no: int,
    week_dir: Path,
    notebook_path: Path,
) -> None:
    lesson_path = week_dir / f"day-{day_no:02d}" / "lesson.md"
    lesson_text = lesson_path.read_text(encoding="utf-8")
    topic = topic_from_lesson(lesson_text, week_no, day_no)

    cells = [
        new_markdown_cell(
            f"# Week {week_no:02d} Day {day_no:02d} Learning Notebook\n\n"
            "This day notebook is fully executable and aligned to the lesson content."
        ),
        new_code_cell(setup_code()),
        new_markdown_cell(lesson_text),
        new_markdown_cell(
            f"## Runnable Day Example\n"
            f"Run this example for Week {week_no:02d} Day {day_no:02d}, inspect outputs, then complete the quiz."
        ),
        new_code_cell(demo_code_for_day(week_no, day_no)),
        new_markdown_cell(
            "## ReAct Verification Cell\n"
            "Use this execution cell to validate one trade decision with an explicit risk guardrail."
        ),
        new_code_cell(verification_code_for_day(week_no, day_no, topic)),
        new_markdown_cell(quiz_markdown_for_day(week_no, day_no, topic)),
        new_code_cell(quiz_solution_code_for_day(week_no, day_no, topic)),
    ]

    nb = new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {
                "display_name": "quant-learning-roadmap",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
        },
    )

    notebook_path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, notebook_path)


def create_week_notebook(week_no: int, week_dir: Path, notebook_path: Path) -> None:
    cells = [
        new_markdown_cell(
            f"# Week {week_no:02d} Learning Notebook\n\n"
            "This notebook mirrors the daily lesson plan and includes runnable demo code cells."
        ),
        new_code_cell(setup_code()),
    ]

    for day_no in range(1, 8):
        lesson_path = week_dir / f"day-{day_no:02d}" / "lesson.md"
        lesson_text = lesson_path.read_text(encoding="utf-8")
        topic = topic_from_lesson(lesson_text, week_no, day_no)
        cells.append(new_markdown_cell(lesson_text))
        cells.append(
            new_markdown_cell(
                f"## Week {week_no:02d} Day {day_no:02d} Runnable Example\n"
                "Run this cell, inspect outputs, then answer the quiz."
            )
        )
        cells.append(new_code_cell(demo_code_for_day(week_no, day_no)))
        cells.append(
            new_markdown_cell(
                "## ReAct Verification Cell\n"
                "Validate trade logic with a risk guardrail before reading the model quiz answers."
            )
        )
        cells.append(new_code_cell(verification_code_for_day(week_no, day_no, topic)))
        cells.append(new_markdown_cell(quiz_markdown_for_day(week_no, day_no, topic)))
        cells.append(new_code_cell(quiz_solution_code_for_day(week_no, day_no, topic)))

    nb = new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {
                "display_name": "quant-learning-roadmap",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
        },
    )

    notebook_path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, notebook_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate week/day notebooks for quant curriculum")
    parser.add_argument(
        "--week",
        type=str,
        default="all",
        help="Target week (e.g., week-01) or 'all'",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    weeks_root = root / "curriculum" / "weeks"
    notebooks_root = root / "notebooks"

    target_weeks: list[int]
    if args.week == "all":
        target_weeks = list(range(1, 25))
    else:
        if not args.week.startswith("week-"):
            raise SystemExit("--week must be in format week-XX or 'all'")
        try:
            week_no = int(args.week.split("-")[-1])
        except ValueError as exc:
            raise SystemExit("Invalid week value") from exc
        if week_no < 1 or week_no > 24:
            raise SystemExit("Week must be between week-01 and week-24")
        target_weeks = [week_no]

    for week_no in target_weeks:
        week_id = f"week-{week_no:02d}"
        week_dir = weeks_root / week_id
        nb_path = notebooks_root / week_id / f"{week_id}-learning.ipynb"
        create_week_notebook(week_no, week_dir, nb_path)
        for day_no in range(1, 8):
            day_nb_path = notebooks_root / week_id / f"day-{day_no:02d}-learning.ipynb"
            create_day_notebook(week_no, day_no, week_dir, day_nb_path)

    if len(target_weeks) == 24:
        print("Generated week and day notebooks for weeks 01-24.")
    else:
        print(f"Generated week and day notebooks for {args.week}.")


if __name__ == "__main__":
    main()
