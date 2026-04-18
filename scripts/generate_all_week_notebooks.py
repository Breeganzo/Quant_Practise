from __future__ import annotations

from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


def setup_code() -> str:
    return "\n".join(
        [
            "import numpy as np",
            "import pandas as pd",
            "np.set_printoptions(precision=4, suppress=True)",
        ]
    )


def demo_code_for_week(week_no: int, day_no: int) -> str:
    seed = week_no * 100 + day_no

    if week_no <= 4:
        return f"""# Foundation demo: synthetic prices and risk metrics
np.random.seed({seed})
idx = pd.bdate_range('2023-01-01', periods=260)
rets = np.random.normal(0.0004, 0.012, size=len(idx))
prices = 100 * np.exp(np.cumsum(rets))
df = pd.DataFrame({{'price': prices}}, index=idx)
df['ret'] = df['price'].pct_change()
summary = {{
    'ann_return': float((1 + df['ret'].dropna()).prod() ** (252 / df['ret'].dropna().shape[0]) - 1),
    'ann_vol': float(df['ret'].dropna().std() * np.sqrt(252)),
    'max_drawdown': float((df['price'] / df['price'].cummax() - 1).min()),
}}
summary
"""

    if week_no <= 8:
        return f"""# ML demo: synthetic classification baseline
np.random.seed({seed})
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

X, y = make_classification(
    n_samples=500,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    random_state={seed}
)
split = 400
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

clf = LogisticRegression(max_iter=500)
clf.fit(X_train, y_train)
proba = clf.predict_proba(X_test)[:, 1]
pred = (proba >= 0.5).astype(int)
{{
    'accuracy': float(accuracy_score(y_test, pred)),
    'auc': float(roc_auc_score(y_test, proba))
}}
"""

    if week_no <= 12:
        return f"""# Time-series demo: autoregressive synthetic signal
np.random.seed({seed})
n = 300
eps = np.random.normal(0, 1, n)
series = np.zeros(n)
for i in range(1, n):
    series[i] = 0.7 * series[i-1] + eps[i]

s = pd.Series(series)
acf1 = float(s.autocorr(lag=1))
acf5 = float(s.autocorr(lag=5))
rolling_std = float(s.rolling(30).std().dropna().mean())
{{'acf_lag1': acf1, 'acf_lag5': acf5, 'rolling_std_mean': rolling_std}}
"""

    if week_no <= 16:
        return f"""# Portfolio/risk demo: constrained allocation intuition
np.random.seed({seed})
n_assets = 5
A = np.random.normal(size=(n_assets, n_assets))
cov = A.T @ A
mu = np.random.uniform(0.05, 0.15, size=n_assets)
raw_w = np.maximum(mu, 0)
weights = raw_w / raw_w.sum()
port_return = float(weights @ mu)
port_vol = float(np.sqrt(weights @ cov @ weights))
{{'weights': weights.round(4).tolist(), 'portfolio_return_proxy': port_return, 'portfolio_vol_proxy': port_vol}}
"""

    if week_no <= 20:
        return f"""# Advanced strategy demo: cross-sectional factor ranking
np.random.seed({seed})
assets = [f'A{{i}}' for i in range(1, 11)]
factor = pd.Series(np.random.normal(0, 1, len(assets)), index=assets, name='factor')
next_ret = pd.Series(np.random.normal(0, 0.02, len(assets)), index=assets, name='next_ret')
ranked = factor.rank(ascending=False)
long = ranked[ranked <= 3].index
short = ranked[ranked >= 8].index
spread = float(next_ret.loc[long].mean() - next_ret.loc[short].mean())
{{'long_bucket': list(long), 'short_bucket': list(short), 'spread_return_proxy': spread}}
"""

    return f"""# Integration demo: readiness tracker snapshot
np.random.seed({seed})
weeks_done = np.random.randint(14, 24)
quiz_avg = np.random.uniform(70, 95)
mock_scores = np.random.uniform(60, 95, size=3)
{{
    'weeks_completed': int(weeks_done),
    'quiz_average': float(round(quiz_avg, 2)),
    'mock_scores': [float(round(x, 2)) for x in mock_scores]
}}
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
            cells.append(new_code_cell(demo_code_for_week(week_no, day_no)))

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
