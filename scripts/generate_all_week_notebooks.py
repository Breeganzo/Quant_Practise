from __future__ import annotations

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


def quiz_markdown_for_day(week_no: int, day_no: int) -> str:
    return "\n".join(
        [
            f"## Week {week_no:02d} Day {day_no:02d} Quiz",
            "",
            "Answer these before revealing the solution cell:",
            "1. Write one formula from today in plain language and define each symbol.",
            "2. Use one real ticker from today's examples and state one risk guardrail.",
            "3. In one sentence: why does this concept matter for live trading decisions?",
            "",
            "Then run the next code cell to compare against a reference answer template.",
        ]
    )


def quiz_solution_code_for_day(week_no: int, day_no: int) -> str:
    base_price = 100 + week_no + day_no
    next_price = round(base_price * (1 + 0.008 + 0.0005 * day_no), 3)
    simple_return = (next_price - base_price) / base_price
    gross_return = 1 + simple_return
    return f"""# Quiz reference solution template (auto-generated)
price_t_minus_1 = {base_price:.3f}
price_t = {next_price:.3f}
r_t = (price_t - price_t_minus_1) / price_t_minus_1
gross = 1 + r_t

print('Reference symbols:')
print('  P_(t-1):', price_t_minus_1)
print('  P_t    :', price_t)
print('  r_t    :', round(r_t, 6), '=>', f'{{r_t*100:.2f}}%')
print('  1+r_t  :', round(gross, 6))

print('\\nExpected numeric check:')
print('  simple_return_expected =', {simple_return:.6f})
print('  gross_return_expected  =', {gross_return:.6f})

print('\\nInterview-style answer template:')
print('  Formula in words: return = price change / starting price')
print('  Risk guardrail: reject signals when volatility regime shifts above threshold')
"""


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
        cells.append(new_markdown_cell(lesson_text))
        if day_no <= 5:
            cells.append(
                new_markdown_cell(
                    f"## Week {week_no:02d} Day {day_no:02d} Runnable Example\n"
                    "Run this cell, inspect outputs, then answer the quiz."
                )
            )
            cells.append(new_code_cell(demo_code_for_week(week_no, day_no)))
            cells.append(new_markdown_cell(quiz_markdown_for_day(week_no, day_no)))
            cells.append(new_code_cell(quiz_solution_code_for_day(week_no, day_no)))

    nb = new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
    )

    notebook_path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, notebook_path)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    weeks_root = root / "curriculum" / "weeks"
    notebooks_root = root / "notebooks"

    for week_no in range(1, 25):
        week_id = f"week-{week_no:02d}"
        week_dir = weeks_root / week_id
        nb_path = notebooks_root / week_id / f"{week_id}-learning.ipynb"
        create_week_notebook(week_no, week_dir, nb_path)

    print("Generated notebooks for weeks 01-24.")


if __name__ == "__main__":
    main()
