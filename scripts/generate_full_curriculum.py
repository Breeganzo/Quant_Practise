from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


@dataclass(frozen=True)
class DayPlan:
    topic: str
    concepts: tuple[str, str, str]
    worked_example: str
    coding_task: str
    reflection: str


@dataclass(frozen=True)
class WeekPlan:
    theme: str
    objective: str
    weekday_days: tuple[DayPlan, DayPlan, DayPlan, DayPlan, DayPlan]
    revision_focus: tuple[str, str, str]
    project_title: str
    project_problem: str
    project_data: tuple[str, str, str]
    project_steps: tuple[str, str, str, str, str]
    project_metrics: tuple[str, str, str, str]
    admissions_task: str
    interview_task: str


def week_plans() -> list[WeekPlan]:
    return [
        WeekPlan(
            theme="Python setup, math refresh, and market basics",
            objective="Rebuild core quant workflow habits and foundational finance vocabulary.",
            weekday_days=(
                DayPlan(
                    topic="Environment reproducibility and data loading",
                    concepts=(
                        "Virtual environments and dependency locking",
                        "Notebook hygiene and deterministic outputs",
                        "Market data schema (OHLCV) basics",
                    ),
                    worked_example="Load three assets, verify missing values, and create a clean price table.",
                    coding_task="Build a reusable function that loads prices and validates schema assumptions.",
                    reflection="Which part of your setup would most likely break on a new machine?",
                ),
                DayPlan(
                    topic="Algebraic transformations for returns",
                    concepts=(
                        "Simple returns vs log returns",
                        "Compounding and cumulative performance",
                        "Feature scaling for comparability",
                    ),
                    worked_example="Convert a price series to daily returns and cumulative growth index.",
                    coding_task="Implement helper functions for return conversion and scaling.",
                    reflection="When should you avoid log-return communication with stakeholders?",
                ),
                DayPlan(
                    topic="Calculus intuition for optimization",
                    concepts=(
                        "First derivative as local slope",
                        "Second derivative and curvature",
                        "Convexity intuition in risk objectives",
                    ),
                    worked_example="Visualize how a mean-variance objective changes with risk aversion.",
                    coding_task="Plot objective values across different risk-aversion parameters.",
                    reflection="How can noisy market data mislead gradient-based intuition?",
                ),
                DayPlan(
                    topic="Market structure and asset classes",
                    concepts=(
                        "Equity, ETF, fixed-income, and derivatives overview",
                        "Liquidity and bid-ask spread intuition",
                        "Trading session and venue effects",
                    ),
                    worked_example="Compare volatility and volume behavior for an ETF versus a single stock.",
                    coding_task="Create a comparative table of OHLCV statistics for three instruments.",
                    reflection="Which asset class currently best matches your skill level and why?",
                ),
                DayPlan(
                    topic="Risk and performance metrics",
                    concepts=(
                        "Annualized return and annualized volatility",
                        "Sharpe ratio intuition and limitations",
                        "Drawdown and recovery profile",
                    ),
                    worked_example="Compute rolling volatility and drawdown for a benchmark ETF.",
                    coding_task="Build reusable metrics functions with input validation.",
                    reflection="Which performance metric is easiest to game?",
                ),
            ),
            revision_focus=(
                "Rebuild all metric formulas from memory",
                "Review error log and classify mistake types",
                "Retest weak concepts using 10 short recall prompts",
            ),
            project_title="Three-asset risk-return comparison",
            project_problem="Build a mini report comparing risk-adjusted behavior across three liquid assets.",
            project_data=("Yahoo Finance", "Stooq", "FRED macro context"),
            project_steps=(
                "Define objective and assumptions",
                "Ingest and clean price data",
                "Compute return/risk metrics",
                "Visualize volatility and drawdown",
                "Write one-page findings memo",
            ),
            project_metrics=("Annualized return", "Annualized volatility", "Sharpe proxy", "Max drawdown"),
            admissions_task="Create target-program shortlist with tuition, scholarship, and waiver policies.",
            interview_task="Solve 5 basic probability drills and explain each answer aloud.",
        ),
        WeekPlan(
            theme="Probability and statistics for market data",
            objective="Strengthen statistical reasoning needed for quant inference and model validation.",
            weekday_days=(
                DayPlan(
                    topic="Random variables and key distributions",
                    concepts=(
                        "Discrete vs continuous random variables",
                        "Normal, lognormal, and heavy-tail intuition",
                        "Distribution moments and shape",
                    ),
                    worked_example="Compare simulated normal returns with fat-tail synthetic returns.",
                    coding_task="Simulate returns from multiple distributions and compare tail events.",
                    reflection="Why are heavy tails critical for risk systems?",
                ),
                DayPlan(
                    topic="Expectation, variance, and covariance",
                    concepts=(
                        "Expected value as long-run average",
                        "Variance as uncertainty proxy",
                        "Covariance/correlation for co-movement",
                    ),
                    worked_example="Estimate covariance matrix for a small asset universe.",
                    coding_task="Write a covariance diagnostics function with pairwise interpretation.",
                    reflection="What can high correlation hide during market stress?",
                ),
                DayPlan(
                    topic="Sampling and estimation",
                    concepts=(
                        "Population vs sample",
                        "Estimator bias and variance tradeoff",
                        "Central limit theorem intuition",
                    ),
                    worked_example="Estimate mean return stability across different sample lengths.",
                    coding_task="Bootstrap sample means and visualize confidence spread.",
                    reflection="How does small sample size distort confidence?",
                ),
                DayPlan(
                    topic="Confidence intervals and hypothesis testing",
                    concepts=(
                        "Confidence intervals for means",
                        "Null/alternative hypotheses",
                        "P-value interpretation pitfalls",
                    ),
                    worked_example="Test whether strategy mean return differs from zero.",
                    coding_task="Implement one-sided and two-sided tests on synthetic strategy returns.",
                    reflection="Why is statistical significance not equal to economic significance?",
                ),
                DayPlan(
                    topic="Statistical communication for finance decisions",
                    concepts=(
                        "Effect size versus significance",
                        "Practical significance under costs",
                        "Decision thresholds under uncertainty",
                    ),
                    worked_example="Translate a test result into a go/no-go trading research decision.",
                    coding_task="Create a short decision report generator from test outputs.",
                    reflection="How would you explain uncertainty to a non-technical stakeholder?",
                ),
            ),
            revision_focus=(
                "Revisit CLT, confidence intervals, and testing assumptions",
                "Redo one bootstrap exercise without notes",
                "Document top 3 interpretation mistakes in error log",
            ),
            project_title="Bootstrap confidence interval study",
            project_problem="Estimate uncertainty around average returns for multiple assets using resampling.",
            project_data=("Yahoo Finance", "FRED risk-free proxy", "Synthetic stress scenarios"),
            project_steps=(
                "Define estimation target",
                "Build bootstrap sampler",
                "Compute interval estimates",
                "Compare stable vs volatile assets",
                "Summarize implications for portfolio design",
            ),
            project_metrics=("Interval width", "Coverage intuition", "Sampling stability", "Decision confidence"),
            admissions_task="Draft first version of scholarship narrative based on socioeconomic and merit fit.",
            interview_task="Practice 5 statistics interview questions with timed responses.",
        ),
        WeekPlan(
            theme="Linear algebra, optimization, and data engineering",
            objective="Build matrix and optimization intuition while strengthening practical data handling skills.",
            weekday_days=(
                DayPlan(
                    topic="Vectors, matrices, and transformations",
                    concepts=(
                        "Vector space intuition",
                        "Matrix multiplication in factor exposure",
                        "Linear transformations for feature pipelines",
                    ),
                    worked_example="Map asset returns through a synthetic factor-loading matrix.",
                    coding_task="Implement matrix operations and shape checks using NumPy.",
                    reflection="Why do silent shape mismatches cause costly bugs?",
                ),
                DayPlan(
                    topic="Eigenvalues, eigenvectors, and PCA intuition",
                    concepts=(
                        "Variance directions in data",
                        "Principal components as latent factors",
                        "Dimensionality reduction tradeoffs",
                    ),
                    worked_example="Apply PCA to correlated return features and interpret first components.",
                    coding_task="Build PCA diagnostic plots and explained-variance table.",
                    reflection="When can PCA remove useful signal?",
                ),
                DayPlan(
                    topic="Optimization fundamentals",
                    concepts=(
                        "Objective functions and constraints",
                        "Constrained optimization in portfolios",
                        "Regularization and numerical stability",
                    ),
                    worked_example="Solve a constrained minimum-variance allocation toy problem.",
                    coding_task="Code constrained optimization with objective logging.",
                    reflection="What assumptions are hidden inside quadratic optimization?",
                ),
                DayPlan(
                    topic="Pandas data engineering workflow",
                    concepts=(
                        "Index alignment and time-aware joins",
                        "Groupby/rolling windows",
                        "Missing data treatment strategies",
                    ),
                    worked_example="Align multi-asset price data with macro feature releases.",
                    coding_task="Create a reusable data cleaning pipeline function.",
                    reflection="How can forward-fill cause subtle leakage?",
                ),
                DayPlan(
                    topic="SQL basics for quant datasets",
                    concepts=(
                        "Relational schema design",
                        "Filtering, aggregation, and joins",
                        "Time-series query patterns",
                    ),
                    worked_example="Query daily returns and aggregate monthly stats from a SQLite table.",
                    coding_task="Write SQL queries for instrument-level and portfolio-level summaries.",
                    reflection="What makes a schema future-proof for research iteration?",
                ),
            ),
            revision_focus=(
                "Rework one optimization example by hand",
                "Recreate one pandas pipeline from memory",
                "Write and test 3 SQL queries without references",
            ),
            project_title="Market data pipeline prototype",
            project_problem="Build a robust ETL workflow that ingests, cleans, aligns, and stores market data.",
            project_data=("Yahoo Finance", "FRED", "Local SQLite storage"),
            project_steps=(
                "Design schema for prices and features",
                "Ingest and normalize data",
                "Handle missing values and alignment",
                "Store transformed outputs",
                "Validate data quality with checks",
            ),
            project_metrics=("Data completeness", "Alignment errors", "Pipeline runtime", "Validation pass rate"),
            admissions_task="Draft quantitative coursework summary for statement of purpose evidence.",
            interview_task="Practice 3 SQL + 3 Python data-manipulation interview exercises.",
        ),
        WeekPlan(
            theme="Return/risk analytics and exploratory capstone",
            objective="Integrate foundational math and data skills into a complete exploratory market analysis.",
            weekday_days=(
                DayPlan(
                    topic="Return decomposition and compounding effects",
                    concepts=(
                        "Arithmetic vs geometric interpretation",
                        "Volatility drag",
                        "Regime-dependent performance",
                    ),
                    worked_example="Compare cumulative growth under identical mean returns but different volatilities.",
                    coding_task="Implement return decomposition diagnostics in a reusable notebook section.",
                    reflection="How does volatility drag influence long-horizon planning?",
                ),
                DayPlan(
                    topic="Risk distribution diagnostics",
                    concepts=(
                        "Skewness and kurtosis in return data",
                        "Tail event frequency",
                        "Downside-focused metrics",
                    ),
                    worked_example="Evaluate return histograms and downside risk frequencies for multiple assets.",
                    coding_task="Build a downside-risk summary table including semi-variance.",
                    reflection="Why can variance miss path-dependent pain?",
                ),
                DayPlan(
                    topic="Correlation structure and diversification",
                    concepts=(
                        "Rolling correlation behavior",
                        "Diversification under stress",
                        "Clustered risk exposures",
                    ),
                    worked_example="Track rolling correlations during synthetic stress intervals.",
                    coding_task="Generate rolling-correlation heatmaps over time windows.",
                    reflection="When does diversification break down?",
                ),
                DayPlan(
                    topic="Exploratory visualization for strategy intuition",
                    concepts=(
                        "Narrative charting",
                        "Signal sanity checks",
                        "Interpretability of exploratory outputs",
                    ),
                    worked_example="Build a concise dashboard panel of return, drawdown, and volatility views.",
                    coding_task="Produce clean charts with labeled assumptions and caveats.",
                    reflection="How do visuals bias interpretation if scales are inconsistent?",
                ),
                DayPlan(
                    topic="Capstone design and reporting",
                    concepts=(
                        "Problem framing for quant research",
                        "Assumption logging",
                        "Communicating findings with uncertainty",
                    ),
                    worked_example="Draft a one-page executive summary from your exploratory analysis.",
                    coding_task="Create a report template with metric tables and key plots.",
                    reflection="Which assumption in your analysis is weakest?",
                ),
            ),
            revision_focus=(
                "Re-check all key metrics for one asset manually",
                "Stress-test one visualization with alternate scales",
                "Refine assumptions and caveats list",
            ),
            project_title="Capstone 1: Market risk dashboard",
            project_problem="Build an exploratory dashboard for five assets and produce a risk-focused memo.",
            project_data=("Yahoo Finance", "FRED", "Optional benchmark index"),
            project_steps=(
                "Define analysis universe",
                "Compute return and risk metrics",
                "Create visual analytics panels",
                "Stress-test metric robustness",
                "Write and present conclusions",
            ),
            project_metrics=("Coverage breadth", "Risk interpretation quality", "Reproducibility", "Communication clarity"),
            admissions_task="Write first quantified project bullet points for CV based on Capstone 1.",
            interview_task="Present capstone summary in a 3-minute mock explanation.",
        ),
        WeekPlan(
            theme="Supervised ML I: regression and classification",
            objective="Rebuild core supervised learning intuition with finance-aware validation discipline.",
            weekday_days=(
                DayPlan(
                    topic="Supervised learning setup and leakage controls",
                    concepts=(
                        "Feature-target definition",
                        "Temporal train/validation/test splitting",
                        "Data leakage taxonomy",
                    ),
                    worked_example="Build a next-day return direction target with causal features only.",
                    coding_task="Create split utilities for time-aware model evaluation.",
                    reflection="Which feature engineering pattern most often leaks future information?",
                ),
                DayPlan(
                    topic="Linear regression baselines",
                    concepts=(
                        "Bias-variance tradeoff",
                        "Interpretability of coefficients",
                        "Residual diagnostics",
                    ),
                    worked_example="Fit a linear model on synthetic factor-style features.",
                    coding_task="Train and evaluate a baseline regression with residual plots.",
                    reflection="When is a weak but interpretable model preferable?",
                ),
                DayPlan(
                    topic="Logistic regression for directional signals",
                    concepts=(
                        "Log-odds and probabilities",
                        "Decision thresholds",
                        "Class imbalance effects",
                    ),
                    worked_example="Predict positive/negative return sign and tune threshold tradeoffs.",
                    coding_task="Build confusion matrix and threshold sweep diagnostics.",
                    reflection="How do threshold choices impact trading turnover?",
                ),
                DayPlan(
                    topic="Model evaluation metrics",
                    concepts=(
                        "MAE/RMSE for regression",
                        "Precision, recall, F1, AUC for classification",
                        "Economic utility versus statistical metrics",
                    ),
                    worked_example="Compare two classifiers with similar AUC but different precision-recall balance.",
                    coding_task="Implement metric dashboard functions for model comparison.",
                    reflection="Which metric aligns best with your intended strategy objective?",
                ),
                DayPlan(
                    topic="Regularization and generalization",
                    concepts=(
                        "L1/L2 regularization intuition",
                        "Overfitting detection",
                        "Validation-based model selection",
                    ),
                    worked_example="Compare model stability under different regularization strengths.",
                    coding_task="Tune regularization parameters and record out-of-sample behavior.",
                    reflection="How can regularization improve robustness in noisy market data?",
                ),
            ),
            revision_focus=(
                "Recreate full train/validation/test workflow without references",
                "Review one leakage incident and prevention rule",
                "Summarize metric-selection rationale for strategy context",
            ),
            project_title="Directional baseline model",
            project_problem="Build and evaluate a baseline supervised model for next-day direction prediction.",
            project_data=("Price-derived features", "Volume features", "Lagged macro indicator"),
            project_steps=(
                "Define target and feature set",
                "Apply temporal splitting",
                "Train regression and classification baselines",
                "Evaluate statistical and trading-relevant metrics",
                "Write recommendation memo",
            ),
            project_metrics=("AUC", "Precision at threshold", "Stability across folds", "Turnover proxy"),
            admissions_task="Add ML baseline project summary with quantified evaluation metrics.",
            interview_task="Solve 2 regression and 3 classification conceptual interview prompts.",
        ),
        WeekPlan(
            theme="Supervised ML II: trees, ensembles, and diagnostics",
            objective="Advance supervised modeling with non-linear learners and robust model diagnostics.",
            weekday_days=(
                DayPlan(
                    topic="Decision trees and feature interactions",
                    concepts=(
                        "Non-linearity capture",
                        "Tree depth and complexity",
                        "Interpretability via splits",
                    ),
                    worked_example="Train a decision tree and inspect split logic for feature intuition.",
                    coding_task="Fit and visualize shallow vs deep trees with validation scores.",
                    reflection="How does tree depth influence regime sensitivity?",
                ),
                DayPlan(
                    topic="Random forests",
                    concepts=(
                        "Bagging and variance reduction",
                        "Out-of-bag intuition",
                        "Feature importance caveats",
                    ),
                    worked_example="Compare random forest stability across bootstrap samples.",
                    coding_task="Train random forest and analyze feature importance shifts over time.",
                    reflection="Why can feature importance be unstable in correlated predictors?",
                ),
                DayPlan(
                    topic="Gradient boosting intuition",
                    concepts=(
                        "Sequential error correction",
                        "Learning rate and depth tradeoff",
                        "Overfitting controls",
                    ),
                    worked_example="Tune gradient boosting hyperparameters for a balanced precision-recall tradeoff.",
                    coding_task="Run a small boosting hyperparameter grid and log results.",
                    reflection="How do boosting gains change under noisy labels?",
                ),
                DayPlan(
                    topic="Feature engineering and selection",
                    concepts=(
                        "Lagged and rolling features",
                        "Interaction terms",
                        "Feature ablation testing",
                    ),
                    worked_example="Build and compare engineered feature sets for predictive lift.",
                    coding_task="Create feature ablation experiment table.",
                    reflection="Which engineered features seem most fragile across windows?",
                ),
                DayPlan(
                    topic="Model diagnostics and monitoring",
                    concepts=(
                        "Calibration and reliability",
                        "Drift detection basics",
                        "Error slicing by regime",
                    ),
                    worked_example="Analyze model errors during high-volatility periods.",
                    coding_task="Implement drift diagnostics on feature distributions.",
                    reflection="What monitoring trigger would force model retraining?",
                ),
            ),
            revision_focus=(
                "Review tree/forest/boosting differences in one-page summary",
                "Re-run one ablation experiment from scratch",
                "Update model-risk checklist",
            ),
            project_title="Ensemble model comparison",
            project_problem="Compare tree-based models under a consistent validation and monitoring framework.",
            project_data=("Price features", "Volume features", "Regime labels"),
            project_steps=(
                "Create baseline feature set",
                "Train tree/forest/boosting models",
                "Run ablation and stability tests",
                "Evaluate by regime",
                "Document deployment recommendation",
            ),
            project_metrics=("Validation score", "Stability score", "Calibration error", "Drift sensitivity"),
            admissions_task="Draft one paragraph on model governance and robustness for SOP.",
            interview_task="Practice model selection and overfitting explanation questions.",
        ),
        WeekPlan(
            theme="Unsupervised learning and market regimes",
            objective="Use unsupervised methods to detect latent structure and regime behavior in financial data.",
            weekday_days=(
                DayPlan(
                    topic="Unsupervised problem framing",
                    concepts=(
                        "Label-free learning objectives",
                        "Distance metrics and scaling",
                        "Interpretability constraints",
                    ),
                    worked_example="Frame a regime-detection task without labeled outcomes.",
                    coding_task="Prepare normalized feature space for unsupervised analysis.",
                    reflection="How do preprocessing choices distort clustering outcomes?",
                ),
                DayPlan(
                    topic="K-means and hierarchical clustering",
                    concepts=(
                        "Centroid-based clustering",
                        "Cluster validity intuition",
                        "Hierarchical dendrogram interpretation",
                    ),
                    worked_example="Cluster synthetic market states and compare cluster compactness.",
                    coding_task="Run k-means for multiple k values and evaluate silhouette trend.",
                    reflection="What indicates cluster instability across rolling windows?",
                ),
                DayPlan(
                    topic="PCA for regime and factor hints",
                    concepts=(
                        "Dimensionality reduction",
                        "Variance concentration",
                        "Noise filtering tradeoffs",
                    ),
                    worked_example="Use PCA components as regime features and visualize transitions.",
                    coding_task="Project features into principal-component space and label clusters.",
                    reflection="When can PCA hide tail-relevant behavior?",
                ),
                DayPlan(
                    topic="Anomaly detection basics",
                    concepts=(
                        "Outlier scoring",
                        "Isolation-based intuition",
                        "False-positive management",
                    ),
                    worked_example="Detect unusual return/volume combinations in synthetic stress data.",
                    coding_task="Build a simple anomaly score and threshold report.",
                    reflection="How should anomaly alerts feed into risk workflows?",
                ),
                DayPlan(
                    topic="Regime interpretation and actionability",
                    concepts=(
                        "Linking clusters to strategy behavior",
                        "Regime-aware feature gating",
                        "Operational limits of unsupervised signals",
                    ),
                    worked_example="Map cluster labels to momentum and mean-reversion performance differences.",
                    coding_task="Create a regime summary table with strategy implications.",
                    reflection="Which regime label is least actionable and why?",
                ),
            ),
            revision_focus=(
                "Re-derive silhouette and cluster-quality interpretation",
                "Rebuild one PCA-regime chart from memory",
                "List unsupervised failure modes and mitigations",
            ),
            project_title="Regime clustering notebook",
            project_problem="Detect and interpret market regimes using clustering and PCA features.",
            project_data=("Returns", "Rolling volatility", "Volume anomalies"),
            project_steps=(
                "Engineer regime-sensitive features",
                "Run clustering methods",
                "Validate cluster quality",
                "Map regimes to strategy behavior",
                "Write actionable insights",
            ),
            project_metrics=("Silhouette score", "Cluster persistence", "Interpretability", "Strategy differentiation"),
            admissions_task="Create portfolio narrative describing unsupervised regime analysis value.",
            interview_task="Practice 4 unsupervised-learning conceptual questions.",
        ),
        WeekPlan(
            theme="ML pipeline capstone and robustness",
            objective="Integrate supervised and unsupervised components into a robust research pipeline.",
            weekday_days=(
                DayPlan(
                    topic="Pipeline architecture and feature store design",
                    concepts=(
                        "Data/version lineage",
                        "Train-serving consistency",
                        "Feature freshness constraints",
                    ),
                    worked_example="Design a simple feature store schema for daily model updates.",
                    coding_task="Implement feature generation pipeline with reproducible transforms.",
                    reflection="What metadata is required to reproduce a prediction six months later?",
                ),
                DayPlan(
                    topic="Temporal cross-validation and walk-forward tests",
                    concepts=(
                        "Rolling windows",
                        "Expanding windows",
                        "Out-of-sample integrity",
                    ),
                    worked_example="Evaluate model performance under walk-forward simulation.",
                    coding_task="Implement reusable walk-forward evaluation utility.",
                    reflection="Why does random k-fold validation fail for time-series targets?",
                ),
                DayPlan(
                    topic="Thresholding and decision rules",
                    concepts=(
                        "Probability-to-action mapping",
                        "Confidence filtering",
                        "Turnover-aware thresholds",
                    ),
                    worked_example="Compare conservative vs aggressive thresholds for signal generation.",
                    coding_task="Create threshold sweep report including turnover proxy.",
                    reflection="How do threshold choices trade accuracy for implementability?",
                ),
                DayPlan(
                    topic="Explainability and model governance",
                    concepts=(
                        "Local vs global explanations",
                        "Attribution caveats",
                        "Model governance artifacts",
                    ),
                    worked_example="Generate feature-attribution summary for a weekly model run.",
                    coding_task="Build a model card template capturing assumptions and risk controls.",
                    reflection="Which explanation artifacts are most useful for audit readiness?",
                ),
                DayPlan(
                    topic="Capstone packaging and reproducibility",
                    concepts=(
                        "Experiment tracking",
                        "Result reproducibility checklist",
                        "Research report structure",
                    ),
                    worked_example="Prepare a concise report from pipeline experiments.",
                    coding_task="Automate generation of results tables for final capstone memo.",
                    reflection="Which section of your report best demonstrates robustness?",
                ),
            ),
            revision_focus=(
                "Re-run walk-forward split generation",
                "Validate reproducibility checklist for one experiment",
                "Refine model-card documentation",
            ),
            project_title="Capstone 2: Robust signal pipeline",
            project_problem="Build a full signal-generation pipeline with robust validation and governance artifacts.",
            project_data=("Engineered feature store", "Daily return targets", "Regime labels"),
            project_steps=(
                "Assemble feature pipeline",
                "Run walk-forward validation",
                "Tune decision thresholds",
                "Generate explainability artifacts",
                "Deliver model card and report",
            ),
            project_metrics=("Out-of-sample stability", "Threshold efficiency", "Reproducibility", "Governance completeness"),
            admissions_task="Quantify capstone impact and add it to project portfolio index.",
            interview_task="Prepare a 5-minute technical walkthrough of your ML pipeline.",
        ),
        WeekPlan(
            theme="Time-series foundations and stationarity",
            objective="Build practical time-series intuition for forecasting and diagnostic workflows.",
            weekday_days=(
                DayPlan(
                    topic="Stationarity and transformations",
                    concepts=(
                        "Mean/variance stability",
                        "Differencing and detrending",
                        "Log and seasonal transforms",
                    ),
                    worked_example="Diagnose stationarity before and after differencing on a synthetic series.",
                    coding_task="Implement stationarity diagnostic checks and transformation pipeline.",
                    reflection="When can differencing remove useful economic signal?",
                ),
                DayPlan(
                    topic="Autocorrelation and partial autocorrelation",
                    concepts=(
                        "ACF pattern interpretation",
                        "PACF role in lag selection",
                        "Lag memory intuition",
                    ),
                    worked_example="Use ACF/PACF to reason about plausible lag structures.",
                    coding_task="Generate ACF/PACF plots and annotate candidate lags.",
                    reflection="What false patterns can appear in short samples?",
                ),
                DayPlan(
                    topic="AR, MA, and ARMA intuition",
                    concepts=(
                        "Autoregressive process behavior",
                        "Moving-average shock memory",
                        "Model order tradeoffs",
                    ),
                    worked_example="Fit AR and MA models on synthetic data and compare residual structure.",
                    coding_task="Train AR/MA baselines and evaluate one-step forecast errors.",
                    reflection="Which process assumptions are hardest to defend in markets?",
                ),
                DayPlan(
                    topic="ARIMA workflow",
                    concepts=(
                        "Integrated differencing",
                        "Order selection process",
                        "Residual diagnostics",
                    ),
                    worked_example="Build an ARIMA model with iterative diagnostics and refinements.",
                    coding_task="Automate ARIMA candidate comparison table.",
                    reflection="How do you prevent overfitting when tuning ARIMA orders?",
                ),
                DayPlan(
                    topic="Forecast evaluation and communication",
                    concepts=(
                        "Forecast error metrics",
                        "Prediction interval interpretation",
                        "Economic usefulness thresholds",
                    ),
                    worked_example="Compare naive, AR, and ARIMA baselines on holdout periods.",
                    coding_task="Create forecast comparison report with intervals and caveats.",
                    reflection="When is a statistically better forecast still useless for trading?",
                ),
            ),
            revision_focus=(
                "Re-run stationarity workflow on a new series",
                "Summarize ACF/PACF interpretation rules",
                "Review forecast evaluation assumptions",
            ),
            project_title="Time-series baseline forecasting notebook",
            project_problem="Build and compare baseline time-series models with proper diagnostics.",
            project_data=("Synthetic AR data", "Market index returns", "Volatility proxy"),
            project_steps=(
                "Prepare and transform series",
                "Fit baseline models",
                "Run residual diagnostics",
                "Evaluate forecasts",
                "Document practical takeaway",
            ),
            project_metrics=("MAE", "RMSE", "Residual whiteness", "Economic usefulness"),
            admissions_task="Document time-series modeling competency in CV project section.",
            interview_task="Practice ACF/PACF and stationarity conceptual questions.",
        ),
        WeekPlan(
            theme="Volatility modeling and regime shifts",
            objective="Understand volatility dynamics and regime-change handling for risk-aware strategies.",
            weekday_days=(
                DayPlan(
                    topic="Volatility stylized facts",
                    concepts=(
                        "Volatility clustering",
                        "Leverage effect intuition",
                        "Persistence of shocks",
                    ),
                    worked_example="Visualize clustered volatility periods in rolling windows.",
                    coding_task="Compute and plot multiple volatility estimators.",
                    reflection="Why do volatility shocks persist longer than return shocks?",
                ),
                DayPlan(
                    topic="EWMA volatility estimation",
                    concepts=(
                        "Exponential weighting",
                        "Decay parameter interpretation",
                        "Responsiveness vs smoothness tradeoff",
                    ),
                    worked_example="Compare EWMA volatility under fast and slow decay.",
                    coding_task="Implement EWMA estimator with configurable lambda.",
                    reflection="How should lambda change across asset classes?",
                ),
                DayPlan(
                    topic="GARCH intuition",
                    concepts=(
                        "Conditional heteroskedasticity",
                        "ARCH/GARCH terms",
                        "Parameter stability",
                    ),
                    worked_example="Fit a simple GARCH model on synthetic clustered volatility.",
                    coding_task="Estimate GARCH and compare conditional volatility path.",
                    reflection="What does unstable GARCH calibration signal about regime change?",
                ),
                DayPlan(
                    topic="Regime detection and change points",
                    concepts=(
                        "Structural breaks",
                        "Change-point algorithms",
                        "Regime labeling workflows",
                    ),
                    worked_example="Detect breakpoints in a volatility series with synthetic shifts.",
                    coding_task="Implement basic change-point detection and regime labels.",
                    reflection="How should strategy exposure adapt at detected breakpoints?",
                ),
                DayPlan(
                    topic="Volatility-aware decisioning",
                    concepts=(
                        "Volatility targeting",
                        "Adaptive position sizing",
                        "Risk budget adjustments",
                    ),
                    worked_example="Simulate position scaling under different volatility regimes.",
                    coding_task="Build a simple volatility-targeting overlay.",
                    reflection="When can volatility targeting increase hidden risks?",
                ),
            ),
            revision_focus=(
                "Recreate EWMA and GARCH estimates from memory",
                "Compare change-point outputs under different thresholds",
                "Update risk-budget notes for regime transitions",
            ),
            project_title="Volatility regime labeling project",
            project_problem="Build a volatility regime engine and connect labels to risk controls.",
            project_data=("Asset returns", "Rolling vol estimates", "Synthetic regime labels"),
            project_steps=(
                "Estimate multiple volatility measures",
                "Detect potential regime shifts",
                "Create regime labels",
                "Map labels to risk controls",
                "Summarize governance recommendations",
            ),
            project_metrics=("Regime stability", "Detection lag", "Risk-control fit", "Interpretability"),
            admissions_task="Add volatility-risk project insight to statement draft.",
            interview_task="Practice 3 volatility and 2 risk-sizing interview prompts.",
        ),
        WeekPlan(
            theme="Backtesting architecture and implementation realism",
            objective="Design backtests that avoid common biases and include realistic costs and constraints.",
            weekday_days=(
                DayPlan(
                    topic="Backtest design patterns",
                    concepts=(
                        "Vectorized vs event-driven engines",
                        "Research-to-production consistency",
                        "State management in simulation",
                    ),
                    worked_example="Design a minimal event-driven loop for signal and execution simulation.",
                    coding_task="Implement a backtest skeleton with clear interfaces.",
                    reflection="Which part of your architecture is least production-ready?",
                ),
                DayPlan(
                    topic="Data and look-ahead bias controls",
                    concepts=(
                        "Point-in-time data usage",
                        "Survivorship bias",
                        "Timestamp alignment rules",
                    ),
                    worked_example="Show how one-day timestamp misalignment inflates results.",
                    coding_task="Add strict timestamp checks to data pipeline.",
                    reflection="How can survivorship bias distort strategy optimism?",
                ),
                DayPlan(
                    topic="Transaction costs and slippage",
                    concepts=(
                        "Fixed and proportional costs",
                        "Spread and impact proxies",
                        "Turnover sensitivity",
                    ),
                    worked_example="Compare gross vs net returns under increasing turnover.",
                    coding_task="Integrate cost model into backtest calculations.",
                    reflection="Which assumptions make your slippage model unrealistic?",
                ),
                DayPlan(
                    topic="Position sizing and risk constraints",
                    concepts=(
                        "Volatility-based sizing",
                        "Max exposure and concentration limits",
                        "Stop-loss and drawdown guards",
                    ),
                    worked_example="Simulate sizing rules under stable and stressed conditions.",
                    coding_task="Implement risk constraint layer in backtest flow.",
                    reflection="Which constraint most improves downside behavior?",
                ),
                DayPlan(
                    topic="Performance attribution and diagnostics",
                    concepts=(
                        "Signal contribution analysis",
                        "Regime-wise attribution",
                        "Failure mode decomposition",
                    ),
                    worked_example="Break total PnL into signal, sizing, and cost components.",
                    coding_task="Generate attribution report tables for each strategy run.",
                    reflection="What is the primary driver of underperformance in your test?",
                ),
            ),
            revision_focus=(
                "Run bias checklist on one prior notebook",
                "Stress transaction-cost assumptions",
                "Review attribution logic for consistency",
            ),
            project_title="Cost-aware backtest prototype",
            project_problem="Build a realistic backtest with explicit bias controls and cost modeling.",
            project_data=("Signal series", "Daily prices", "Cost assumptions"),
            project_steps=(
                "Design backtest interfaces",
                "Enforce data-integrity checks",
                "Apply execution-cost model",
                "Run strategy and diagnostics",
                "Produce attribution summary",
            ),
            project_metrics=("Net Sharpe proxy", "Turnover", "Cost drag", "Constraint adherence"),
            admissions_task="Prepare one paragraph on research rigor and bias control evidence.",
            interview_task="Practice explaining three common backtest pitfalls and fixes.",
        ),
        WeekPlan(
            theme="Momentum vs mean reversion strategy capstone",
            objective="Evaluate two classic strategy families under unified, realistic testing conditions.",
            weekday_days=(
                DayPlan(
                    topic="Momentum strategy design",
                    concepts=(
                        "Trend persistence hypothesis",
                        "Lookback and holding period tradeoffs",
                        "Signal smoothing",
                    ),
                    worked_example="Build a cross-asset momentum score and rank signals.",
                    coding_task="Implement a momentum signal function with parameter control.",
                    reflection="Which momentum parameter is most sensitive to regime changes?",
                ),
                DayPlan(
                    topic="Mean reversion strategy design",
                    concepts=(
                        "Reversion-to-mean hypothesis",
                        "Z-score normalization",
                        "Entry/exit band selection",
                    ),
                    worked_example="Construct a z-score reversion signal on spread-like data.",
                    coding_task="Implement a mean-reversion signal with adaptive bands.",
                    reflection="How do you detect when mean reversion has structurally broken?",
                ),
                DayPlan(
                    topic="Unified backtest comparison",
                    concepts=(
                        "Comparable assumptions",
                        "Cost-normalized evaluation",
                        "Risk parity of strategy variants",
                    ),
                    worked_example="Run both strategies under identical data and cost assumptions.",
                    coding_task="Create side-by-side strategy comparison table.",
                    reflection="Is any performance gap just a risk-budget mismatch?",
                ),
                DayPlan(
                    topic="Robustness and sensitivity analysis",
                    concepts=(
                        "Parameter sweeps",
                        "Sub-period stability",
                        "Stress scenarios",
                    ),
                    worked_example="Evaluate strategy sensitivity across lookback and threshold ranges.",
                    coding_task="Implement parameter grid with robustness summary outputs.",
                    reflection="Which strategy is more robust after stress tests?",
                ),
                DayPlan(
                    topic="Capstone narrative and decision",
                    concepts=(
                        "Evidence-based selection",
                        "Failure-mode awareness",
                        "Implementation recommendation",
                    ),
                    worked_example="Write a decision memo selecting a strategy for paper trading stage.",
                    coding_task="Generate final capstone report artifact with plots and metrics.",
                    reflection="What would invalidate your selected strategy next month?",
                ),
            ),
            revision_focus=(
                "Re-run one sensitivity experiment",
                "Validate that costs are consistently applied",
                "Review capstone decision assumptions",
            ),
            project_title="Capstone 3: Momentum vs mean reversion",
            project_problem="Compare momentum and mean-reversion families under unified risk and cost rules.",
            project_data=("Liquid ETF universe", "Daily prices", "Transaction-cost assumptions"),
            project_steps=(
                "Design both signal families",
                "Run equivalent backtests",
                "Conduct robustness tests",
                "Perform attribution analysis",
                "Produce decision memo",
            ),
            project_metrics=("Net return profile", "Sharpe proxy", "Drawdown", "Robustness score"),
            admissions_task="Convert capstone outcomes into one polished portfolio case study.",
            interview_task="Prepare strategy-comparison pitch with assumptions and caveats.",
        ),
        WeekPlan(
            theme="Portfolio construction and optimization",
            objective="Transition from single-strategy analysis to portfolio-level construction and risk allocation.",
            weekday_days=(
                DayPlan(
                    topic="Portfolio objective design",
                    concepts=(
                        "Return-risk objective choices",
                        "Constraint sets",
                        "Practical allocation limits",
                    ),
                    worked_example="Formulate objective functions for conservative and aggressive mandates.",
                    coding_task="Implement objective builder for multiple mandate profiles.",
                    reflection="Which constraints are mandatory for realistic deployment?",
                ),
                DayPlan(
                    topic="Mean-variance optimization",
                    concepts=(
                        "Efficient frontier intuition",
                        "Covariance estimation sensitivity",
                        "Weight instability issues",
                    ),
                    worked_example="Compute efficient frontier using sample covariance estimates.",
                    coding_task="Build optimizer with no-short and max-weight constraints.",
                    reflection="Why do optimized weights become unstable with noisy covariances?",
                ),
                DayPlan(
                    topic="Risk parity and equal-risk contribution",
                    concepts=(
                        "Risk contribution decomposition",
                        "Balancing volatility contributions",
                        "Implementation tradeoffs",
                    ),
                    worked_example="Construct a risk-parity portfolio and compare to equal-weight.",
                    coding_task="Implement risk-contribution calculator and rebalance logic.",
                    reflection="When can risk parity overweight low-return assets?",
                ),
                DayPlan(
                    topic="Covariance robustness techniques",
                    concepts=(
                        "Shrinkage intuition",
                        "Rolling covariance windows",
                        "Regime-dependent covariance",
                    ),
                    worked_example="Compare allocations under sample and shrinkage covariance matrices.",
                    coding_task="Integrate shrinkage covariance estimate into optimizer.",
                    reflection="How should covariance model choice change with volatility regime?",
                ),
                DayPlan(
                    topic="Portfolio monitoring and rebalance policy",
                    concepts=(
                        "Drift monitoring",
                        "Rebalance frequency tradeoffs",
                        "Turnover and tax/cost awareness",
                    ),
                    worked_example="Simulate monthly vs quarterly rebalancing outcomes.",
                    coding_task="Build rebalance trigger logic based on drift thresholds.",
                    reflection="Which rebalance policy best balances stability and responsiveness?",
                ),
            ),
            revision_focus=(
                "Re-derive one optimization setup by hand",
                "Compare two covariance models and document effects",
                "Review rebalance-trigger assumptions",
            ),
            project_title="Portfolio allocator comparison",
            project_problem="Compare equal-weight, mean-variance, and risk-parity allocation frameworks.",
            project_data=("Strategy return streams", "Covariance estimates", "Cost assumptions"),
            project_steps=(
                "Define allocation objectives",
                "Implement three allocation methods",
                "Backtest rebalancing policies",
                "Compare risk and turnover profiles",
                "Produce allocator recommendation",
            ),
            project_metrics=("Net return", "Volatility", "Drawdown", "Turnover"),
            admissions_task="Draft a portfolio-construction project paragraph with measured outcomes.",
            interview_task="Practice optimizer and risk-budgeting interview explanations.",
        ),
        WeekPlan(
            theme="Fixed income basics for quant workflows",
            objective="Develop working fixed-income intuition for pricing, curve dynamics, and interest-rate risk.",
            weekday_days=(
                DayPlan(
                    topic="Bond cashflows and pricing mechanics",
                    concepts=(
                        "Coupon and principal cashflows",
                        "Yield-to-maturity intuition",
                        "Price-yield inverse relation",
                    ),
                    worked_example="Price a fixed-coupon bond across multiple yield assumptions.",
                    coding_task="Implement a simple bond pricer for coupon bonds.",
                    reflection="How does reinvestment assumption affect interpretation of yield?",
                ),
                DayPlan(
                    topic="Yield curve structure",
                    concepts=(
                        "Spot, forward, and par rates",
                        "Curve shapes and macro context",
                        "Term premium intuition",
                    ),
                    worked_example="Construct a toy yield curve and interpret steepening/flattening moves.",
                    coding_task="Create yield-curve plotting utility and slope diagnostics.",
                    reflection="Which macro regime tends to produce curve inversion?",
                ),
                DayPlan(
                    topic="Duration and convexity",
                    concepts=(
                        "Macaulay and modified duration",
                        "First-order rate sensitivity",
                        "Convexity correction",
                    ),
                    worked_example="Estimate bond price change under rate shocks using duration/convexity.",
                    coding_task="Build duration-convexity sensitivity calculator.",
                    reflection="When does duration-only approximation fail materially?",
                ),
                DayPlan(
                    topic="Rate-risk scenario analysis",
                    concepts=(
                        "Parallel and non-parallel shifts",
                        "Curve-bucket exposures",
                        "Stress scenario design",
                    ),
                    worked_example="Run parallel and twist scenarios on a small bond basket.",
                    coding_task="Implement scenario engine for curve shocks.",
                    reflection="Which scenario reveals the largest hidden risk?",
                ),
                DayPlan(
                    topic="Fixed-income portfolio interpretation",
                    concepts=(
                        "Carry and roll-down intuition",
                        "Interest-rate hedging basics",
                        "Risk-report communication",
                    ),
                    worked_example="Summarize fixed-income portfolio behavior under changing rates.",
                    coding_task="Generate fixed-income risk report with key sensitivities.",
                    reflection="How would you communicate fixed-income risk to an equity-focused PM?",
                ),
            ),
            revision_focus=(
                "Recompute duration/convexity for one bond from scratch",
                "Review curve scenario assumptions",
                "Summarize fixed-income glossary in one page",
            ),
            project_title="Bond sensitivity analysis",
            project_problem="Build a fixed-income sensitivity dashboard for a small bond portfolio.",
            project_data=("Synthetic bond set", "Yield curve snapshots", "Rate shock scenarios"),
            project_steps=(
                "Price bond set",
                "Compute duration and convexity",
                "Run rate scenarios",
                "Aggregate portfolio risk",
                "Document key exposures",
            ),
            project_metrics=("DV01 proxy", "Convexity impact", "Scenario loss", "Hedge suggestion quality"),
            admissions_task="Add fixed-income competency note to target program fit matrix.",
            interview_task="Practice 5 duration/convexity and curve-shape questions.",
        ),
        WeekPlan(
            theme="Derivatives and options basics",
            objective="Build options intuition for payoffs, Greeks, and hedging workflows.",
            weekday_days=(
                DayPlan(
                    topic="Option payoff structure",
                    concepts=(
                        "Calls and puts",
                        "Long vs short payoff asymmetry",
                        "Moneyness intuition",
                    ),
                    worked_example="Plot payoff diagrams for basic option positions at expiry.",
                    coding_task="Implement payoff calculator for vanilla option strategies.",
                    reflection="Which payoff shape best fits downside protection goals?",
                ),
                DayPlan(
                    topic="Greeks intuition",
                    concepts=(
                        "Delta sensitivity",
                        "Gamma curvature",
                        "Vega and implied volatility exposure",
                    ),
                    worked_example="Track delta and gamma behavior near at-the-money conditions.",
                    coding_task="Create a Greeks approximation table for synthetic option quotes.",
                    reflection="How does gamma risk change near expiry?",
                ),
                DayPlan(
                    topic="Volatility surface basics",
                    concepts=(
                        "Implied volatility",
                        "Smile/skew interpretation",
                        "Vol regime context",
                    ),
                    worked_example="Simulate implied-volatility skew and discuss directional implications.",
                    coding_task="Build implied-vol surface toy visualization.",
                    reflection="Why does skew differ across equities and indices?",
                ),
                DayPlan(
                    topic="Hedging workflow basics",
                    concepts=(
                        "Delta hedging intuition",
                        "Rehedging frequency tradeoff",
                        "Hedging costs and slippage",
                    ),
                    worked_example="Simulate a simple delta-hedging loop on synthetic price paths.",
                    coding_task="Implement discrete hedging simulation and PnL decomposition.",
                    reflection="When can hedging itself create risk concentration?",
                ),
                DayPlan(
                    topic="Options strategy framing",
                    concepts=(
                        "Directional vs volatility bets",
                        "Risk-defined structures",
                        "Scenario-based comparison",
                    ),
                    worked_example="Compare covered call, protective put, and straddle under scenarios.",
                    coding_task="Build strategy scenario matrix with payoff summaries.",
                    reflection="Which strategy aligns with your current risk tolerance and why?",
                ),
            ),
            revision_focus=(
                "Redraw key payoff and Greek intuition charts",
                "Re-run one hedging simulation",
                "Review assumptions in volatility-surface interpretation",
            ),
            project_title="Options risk intuition notebook",
            project_problem="Build an options analytics notebook covering payoffs, Greeks, and hedging outcomes.",
            project_data=("Synthetic option chain", "Underlying paths", "Volatility scenarios"),
            project_steps=(
                "Implement payoff analytics",
                "Estimate and visualize Greeks",
                "Run hedging simulation",
                "Compare strategy scenarios",
                "Summarize practical risk insights",
            ),
            project_metrics=("Hedge error", "Scenario PnL spread", "Risk clarity", "Interpretability"),
            admissions_task="Prepare derivatives-focused portfolio artifact summary.",
            interview_task="Practice options payoff and Greeks interview drills.",
        ),
        WeekPlan(
            theme="Risk engine capstone (VaR/CVaR and stress)",
            objective="Integrate market, model, and scenario risk into a coherent risk engine workflow.",
            weekday_days=(
                DayPlan(
                    topic="Risk framework architecture",
                    concepts=(
                        "Market risk taxonomy",
                        "Model risk awareness",
                        "Operational risk controls",
                    ),
                    worked_example="Design a lightweight risk engine architecture for a multi-strategy book.",
                    coding_task="Draft risk-engine input/output schema and assumptions log.",
                    reflection="Which risk type is easiest to underestimate in early-stage systems?",
                ),
                DayPlan(
                    topic="VaR approaches",
                    concepts=(
                        "Historical VaR",
                        "Parametric VaR",
                        "Monte Carlo VaR intuition",
                    ),
                    worked_example="Compute historical and parametric VaR on synthetic return streams.",
                    coding_task="Implement VaR calculator supporting two methods.",
                    reflection="When do VaR methods diverge the most?",
                ),
                DayPlan(
                    topic="CVaR and tail focus",
                    concepts=(
                        "Expected shortfall intuition",
                        "Tail-risk measurement",
                        "Limitations under sparse extremes",
                    ),
                    worked_example="Compare VaR and CVaR under heavy-tail synthetic data.",
                    coding_task="Add CVaR metrics and tail diagnostics to risk report.",
                    reflection="Why is CVaR often more decision-useful than VaR?",
                ),
                DayPlan(
                    topic="Stress testing framework",
                    concepts=(
                        "Historical stress replay",
                        "Hypothetical scenario design",
                        "Sensitivity stress testing",
                    ),
                    worked_example="Run stress scenarios with correlated shock assumptions.",
                    coding_task="Create stress-testing module with scenario presets.",
                    reflection="Which scenario assumptions are hardest to justify?",
                ),
                DayPlan(
                    topic="Risk governance reporting",
                    concepts=(
                        "Limit breaches and escalation",
                        "Risk dashboards",
                        "Decision documentation",
                    ),
                    worked_example="Compile weekly risk report with VaR, CVaR, and stress outcomes.",
                    coding_task="Generate a risk-governance report artifact for capstone submission.",
                    reflection="What would trigger immediate risk-off action in your framework?",
                ),
            ),
            revision_focus=(
                "Recompute VaR/CVaR with alternative assumptions",
                "Review stress scenario rationale",
                "Validate governance escalation checklist",
            ),
            project_title="Capstone 4: Portfolio risk engine",
            project_problem="Build a risk engine combining VaR, CVaR, stress tests, and reporting controls.",
            project_data=("Portfolio return streams", "Shock scenarios", "Risk limits"),
            project_steps=(
                "Implement VaR/CVaR methods",
                "Integrate stress scenarios",
                "Check limit breaches",
                "Create risk dashboard",
                "Deliver governance memo",
            ),
            project_metrics=("Tail-risk coverage", "Scenario responsiveness", "Limit adherence", "Governance completeness"),
            admissions_task="Write risk-management evidence paragraph for applications.",
            interview_task="Practice explaining VaR limitations and stress-testing design.",
        ),
        WeekPlan(
            theme="Factor models and cross-sectional alpha",
            objective="Develop cross-sectional signal research skills using factor-style workflows.",
            weekday_days=(
                DayPlan(
                    topic="Factor investing framework",
                    concepts=(
                        "Style factors overview",
                        "Cross-sectional ranking intuition",
                        "Risk-adjusted factor design",
                    ),
                    worked_example="Construct simple value and momentum-style factor scores.",
                    coding_task="Build factor-score computation pipeline.",
                    reflection="How do you prevent factor overlap from overstating diversification?",
                ),
                DayPlan(
                    topic="Cross-sectional regressions",
                    concepts=(
                        "Exposure estimation",
                        "Residual return interpretation",
                        "Model specification caveats",
                    ),
                    worked_example="Run cross-sectional regression and interpret exposure coefficients.",
                    coding_task="Implement weekly cross-sectional regression diagnostics.",
                    reflection="Which regression assumption is most fragile in live markets?",
                ),
                DayPlan(
                    topic="Information coefficient and decay",
                    concepts=(
                        "IC measurement",
                        "Signal horizon decay",
                        "Stability diagnostics",
                    ),
                    worked_example="Compute rolling IC for a factor and inspect persistence.",
                    coding_task="Build IC and decay report with horizon comparison.",
                    reflection="What IC level is practically useful after costs?",
                ),
                DayPlan(
                    topic="Portfolio construction for factors",
                    concepts=(
                        "Long-short portfolio assembly",
                        "Neutralization constraints",
                        "Turnover management",
                    ),
                    worked_example="Construct a decile long-short factor portfolio with neutralization.",
                    coding_task="Implement decile portfolio builder with turnover tracking.",
                    reflection="How can neutralization reduce unintended bets?",
                ),
                DayPlan(
                    topic="Factor robustness",
                    concepts=(
                        "Sub-period consistency",
                        "Crowding risk",
                        "Outlier sensitivity",
                    ),
                    worked_example="Stress factor outcomes across calm and volatile periods.",
                    coding_task="Generate factor robustness dashboard.",
                    reflection="What signs indicate factor crowding risk is rising?",
                ),
            ),
            revision_focus=(
                "Rebuild IC/decay calculations from scratch",
                "Review neutralization settings",
                "Document crowding warning indicators",
            ),
            project_title="Cross-sectional factor mini-book",
            project_problem="Design and evaluate a factor-based long-short research portfolio.",
            project_data=("Cross-sectional universe data", "Factor scores", "Risk controls"),
            project_steps=(
                "Build factor features",
                "Estimate signal quality",
                "Construct long-short portfolio",
                "Run robustness checks",
                "Summarize implementation risks",
            ),
            project_metrics=("IC/IR proxy", "Turnover", "Drawdown", "Robustness score"),
            admissions_task="Add factor-research output as advanced quant evidence in portfolio.",
            interview_task="Practice factor-model and IC interpretation questions.",
        ),
        WeekPlan(
            theme="Statistical arbitrage intuition",
            objective="Learn stat-arb foundations including spreads, cointegration, and execution-aware controls.",
            weekday_days=(
                DayPlan(
                    topic="Stat-arb problem framing",
                    concepts=(
                        "Relative-value logic",
                        "Spread construction",
                        "Stationarity requirement",
                    ),
                    worked_example="Create a synthetic spread candidate and inspect mean behavior.",
                    coding_task="Implement spread builder with normalization options.",
                    reflection="Why is spread stationarity central for mean-reversion stat-arb?",
                ),
                DayPlan(
                    topic="Cointegration basics",
                    concepts=(
                        "Common trend vs mean-reverting residual",
                        "Cointegration testing intuition",
                        "Hedge ratio estimation",
                    ),
                    worked_example="Estimate hedge ratio and test cointegration on synthetic pair data.",
                    coding_task="Build cointegration screening utility for candidate pairs.",
                    reflection="How can structural breaks invalidate cointegration assumptions?",
                ),
                DayPlan(
                    topic="Signal generation and execution rules",
                    concepts=(
                        "Z-score entry and exit bands",
                        "Position sizing for spreads",
                        "Stop and timeout rules",
                    ),
                    worked_example="Generate spread z-score signals with practical exit logic.",
                    coding_task="Implement signal engine for pair spread strategy.",
                    reflection="Which exit rule reduces tail risk most effectively?",
                ),
                DayPlan(
                    topic="Backtest and cost-aware evaluation",
                    concepts=(
                        "Pair-level PnL decomposition",
                        "Borrow and financing assumptions",
                        "Execution slippage sensitivity",
                    ),
                    worked_example="Backtest pair strategy with conservative cost assumptions.",
                    coding_task="Add financing and slippage assumptions to spread backtest.",
                    reflection="Where does hidden cost risk often get ignored in pairs strategies?",
                ),
                DayPlan(
                    topic="Failure modes and safeguards",
                    concepts=(
                        "Regime shift risk",
                        "Correlation breakdown",
                        "Portfolio concentration control",
                    ),
                    worked_example="Simulate strategy failure under abrupt regime change.",
                    coding_task="Implement basic safeguard rules and breach alerts.",
                    reflection="Which early-warning indicator should trigger pair deactivation?",
                ),
            ),
            revision_focus=(
                "Re-run cointegration tests on alternate pairs",
                "Audit cost assumptions for realism",
                "Update safeguard checklist",
            ),
            project_title="Pairs trading prototype",
            project_problem="Design a cost-aware stat-arb pairs framework with risk safeguards.",
            project_data=("Candidate pair prices", "Spread diagnostics", "Cost assumptions"),
            project_steps=(
                "Screen candidate pairs",
                "Estimate spread and signal",
                "Backtest with costs",
                "Stress failure scenarios",
                "Deliver go/no-go recommendation",
            ),
            project_metrics=("Spread half-life proxy", "Net return", "Max drawdown", "Safeguard effectiveness"),
            admissions_task="Document statistical-arbitrage project methods and controls for portfolio.",
            interview_task="Practice stat-arb and cointegration technical questions.",
        ),
        WeekPlan(
            theme="Agentic AI for quant research",
            objective="Use agentic workflows to accelerate research while enforcing guardrails for reliability.",
            weekday_days=(
                DayPlan(
                    topic="Agentic workflow design for research",
                    concepts=(
                        "Task decomposition for agents",
                        "Prompt contracts and schema outputs",
                        "Human-in-the-loop checkpoints",
                    ),
                    worked_example="Design an agent pipeline for literature scan and hypothesis generation.",
                    coding_task="Write prompt templates with strict output schema.",
                    reflection="Which tasks should never be fully delegated to an agent?",
                ),
                DayPlan(
                    topic="Research summarization and retrieval",
                    concepts=(
                        "Source ranking",
                        "Evidence extraction",
                        "Citation traceability",
                    ),
                    worked_example="Summarize three papers into a structured research memo format.",
                    coding_task="Create a retrieval-and-summary template with citation slots.",
                    reflection="How do you detect hallucinated references quickly?",
                ),
                DayPlan(
                    topic="Feature idea generation and validation",
                    concepts=(
                        "Hypothesis-to-feature translation",
                        "Feature sanity filters",
                        "Leakage-aware screening",
                    ),
                    worked_example="Convert one macro hypothesis into candidate model features.",
                    coding_task="Build a feature ideation checklist from agent outputs.",
                    reflection="How do you separate novelty from overfitting risk?",
                ),
                DayPlan(
                    topic="Code review and experiment tracking agents",
                    concepts=(
                        "Agent-assisted code QA",
                        "Experiment metadata standards",
                        "Reproducibility enforcement",
                    ),
                    worked_example="Use a review rubric to inspect one strategy notebook for reproducibility gaps.",
                    coding_task="Generate experiment log template with required fields.",
                    reflection="Which experiment metadata fields are mandatory for future audit?",
                ),
                DayPlan(
                    topic="Guardrails and risk management for AI use",
                    concepts=(
                        "Hallucination guardrails",
                        "Data privacy and leakage controls",
                        "Approval gates before deployment",
                    ),
                    worked_example="Design a validation gate that blocks unsupported agent conclusions.",
                    coding_task="Implement an agent-output validation checklist file.",
                    reflection="What validation threshold should block strategy progression?",
                ),
            ),
            revision_focus=(
                "Re-evaluate one agent summary for evidence quality",
                "Review guardrail checklist and tighten thresholds",
                "Update human-approval workflow",
            ),
            project_title="Agent-assisted research memo pipeline",
            project_problem="Build a guarded agentic workflow that generates and validates quant research memos.",
            project_data=("Public research articles", "Internal experiment notes", "Structured validation rubric"),
            project_steps=(
                "Define pipeline stages",
                "Create structured prompts",
                "Generate draft memos",
                "Apply evidence and guardrail checks",
                "Finalize approved memo",
            ),
            project_metrics=("Citation accuracy", "Validation pass rate", "Time saved", "Reproducibility quality"),
            admissions_task="Add AI-assisted research governance statement to portfolio narrative.",
            interview_task="Practice explaining agentic workflows and guardrails in quant context.",
        ),
        WeekPlan(
            theme="Execution, microstructure, and multi-strategy blend",
            objective="Incorporate execution realism and microstructure awareness into a blended strategy portfolio.",
            weekday_days=(
                DayPlan(
                    topic="Market microstructure essentials",
                    concepts=(
                        "Order book dynamics",
                        "Spread and depth",
                        "Latency and queue effects",
                    ),
                    worked_example="Discuss how spread/depth changes alter expected execution quality.",
                    coding_task="Create synthetic microstructure scenarios and expected slippage estimates.",
                    reflection="Which microstructure feature most impacts your strategy style?",
                ),
                DayPlan(
                    topic="Execution cost modeling",
                    concepts=(
                        "Implementation shortfall",
                        "Impact models",
                        "Participation constraints",
                    ),
                    worked_example="Estimate implementation shortfall under different participation rates.",
                    coding_task="Build cost model including spread and impact assumptions.",
                    reflection="What execution assumption is least defensible in your current model?",
                ),
                DayPlan(
                    topic="Strategy blending and diversification",
                    concepts=(
                        "Correlation across alpha sleeves",
                        "Risk budget allocation",
                        "Capacity constraints",
                    ),
                    worked_example="Blend momentum, mean-reversion, and factor sleeves under risk limits.",
                    coding_task="Implement multi-sleeve blend with adjustable risk budgets.",
                    reflection="How does capacity constraint change blend weights?",
                ),
                DayPlan(
                    topic="Rebalancing and execution scheduling",
                    concepts=(
                        "Trade scheduling",
                        "Urgency vs cost tradeoff",
                        "Execution windows",
                    ),
                    worked_example="Compare immediate vs scheduled execution impact assumptions.",
                    coding_task="Create scheduler simulation for rebalance events.",
                    reflection="When should urgency override cost minimization?",
                ),
                DayPlan(
                    topic="Capstone assembly and governance",
                    concepts=(
                        "Blend-level performance attribution",
                        "Execution-risk reporting",
                        "Operational controls",
                    ),
                    worked_example="Compile multi-strategy report with net-of-cost metrics.",
                    coding_task="Generate final blend dashboard for capstone review.",
                    reflection="Which sleeve contributes most net alpha after execution costs?",
                ),
            ),
            revision_focus=(
                "Re-check slippage assumptions against turnover",
                "Review blend risk-budget consistency",
                "Update execution governance checklist",
            ),
            project_title="Capstone 5: Multi-strategy paper portfolio",
            project_problem="Construct a multi-sleeve paper portfolio with microstructure-aware execution assumptions.",
            project_data=("Strategy sleeve signals", "Liquidity proxies", "Cost model inputs"),
            project_steps=(
                "Design sleeve blend",
                "Apply execution-cost assumptions",
                "Backtest net performance",
                "Analyze attribution",
                "Produce governance report",
            ),
            project_metrics=("Net Sharpe proxy", "Cost drag", "Capacity proxy", "Risk-budget adherence"),
            admissions_task="Build consolidated portfolio index linking all major capstones.",
            interview_task="Practice explaining execution-risk tradeoffs for front-office discussions.",
        ),
        WeekPlan(
            theme="Admissions package development",
            objective="Convert technical progress into a competitive, scholarship-focused application package.",
            weekday_days=(
                DayPlan(
                    topic="Program targeting and fit matrix",
                    concepts=(
                        "Program tiering",
                        "Prerequisite fit mapping",
                        "Funding probability assessment",
                    ),
                    worked_example="Build target matrix for US/UK quant masters with funding filters.",
                    coding_task="Create sortable target-program table with fit scores.",
                    reflection="Which programs match your profile most realistically today?",
                ),
                DayPlan(
                    topic="Statement of purpose architecture",
                    concepts=(
                        "Narrative arc",
                        "Evidence-backed claims",
                        "Program-specific customization",
                    ),
                    worked_example="Draft SOP outline connecting projects to career goals.",
                    coding_task="Build SOP section template with evidence placeholders.",
                    reflection="Which claim in your SOP needs stronger proof?",
                ),
                DayPlan(
                    topic="CV and project storytelling",
                    concepts=(
                        "Quantifying impact",
                        "Technical depth signaling",
                        "Role alignment",
                    ),
                    worked_example="Rewrite project bullets using measurable outcomes and tools.",
                    coding_task="Generate CV bullet bank from existing project metadata.",
                    reflection="Which project best demonstrates front-office quant readiness?",
                ),
                DayPlan(
                    topic="Recommendation and supporting documents",
                    concepts=(
                        "Recommender selection strategy",
                        "Evidence packets for recommenders",
                        "Timeline coordination",
                    ),
                    worked_example="Draft recommender brief with achievement highlights.",
                    coding_task="Create recommendation request tracker with deadlines.",
                    reflection="Who can best validate your quant potential and why?",
                ),
                DayPlan(
                    topic="Scholarship optimization workflow",
                    concepts=(
                        "Merit vs need-based pathways",
                        "Funding narrative alignment",
                        "Deadline risk management",
                    ),
                    worked_example="Map scholarship requirements to available project evidence.",
                    coding_task="Build scholarship checklist and submission tracker.",
                    reflection="Which funding application has the highest expected return on effort?",
                ),
            ),
            revision_focus=(
                "Polish SOP paragraph quality and coherence",
                "Validate CV bullets for measurable impact",
                "Review deadline tracker for risk",
            ),
            project_title="Application dossier v1",
            project_problem="Assemble a complete draft admissions package with scholarship-aligned evidence.",
            project_data=("Program requirement matrix", "Project portfolio", "Scholarship criteria"),
            project_steps=(
                "Finalize target list",
                "Draft SOP version 1",
                "Update CV project bullets",
                "Prepare recommendation packets",
                "Complete scholarship tracker",
            ),
            project_metrics=("Completion ratio", "Program-fit score", "Evidence coverage", "Deadline readiness"),
            admissions_task="Complete first full draft set (SOP, CV, target matrix, scholarship list).",
            interview_task="Practice 3 personal-story and 3 technical-fit interview answers.",
        ),
        WeekPlan(
            theme="Quant interview prep I",
            objective="Build speed and accuracy for core quantitative interview domains.",
            weekday_days=(
                DayPlan(
                    topic="Probability drill framework",
                    concepts=(
                        "Conditional probability",
                        "Bayes intuition",
                        "Expected value shortcuts",
                    ),
                    worked_example="Solve coin/card-style probability questions under time constraints.",
                    coding_task="Create a probability drill notebook with timed question sets.",
                    reflection="Which probability pattern still feels slow or error-prone?",
                ),
                DayPlan(
                    topic="Statistics and estimation interview drills",
                    concepts=(
                        "Estimator reasoning",
                        "Bias-variance tradeoff",
                        "Hypothesis interpretation",
                    ),
                    worked_example="Explain confidence interval meaning in interview-friendly language.",
                    coding_task="Generate short stats-question answer templates.",
                    reflection="How can you avoid over-talking while keeping precision?",
                ),
                DayPlan(
                    topic="Python coding speed drills",
                    concepts=(
                        "Array and string patterns",
                        "Complexity awareness",
                        "Edge-case handling",
                    ),
                    worked_example="Solve 3 medium coding problems with clean test coverage.",
                    coding_task="Build a local timed coding drill harness.",
                    reflection="Which coding pattern causes most debugging delays?",
                ),
                DayPlan(
                    topic="SQL and data manipulation interview drills",
                    concepts=(
                        "Joins and aggregations",
                        "Window functions basics",
                        "Data-quality checks",
                    ),
                    worked_example="Solve common SQL interview prompts on synthetic trade tables.",
                    coding_task="Create SQL practice file with expected outputs.",
                    reflection="Which SQL operation do you mis-handle under pressure?",
                ),
                DayPlan(
                    topic="Mock round synthesis",
                    concepts=(
                        "Time management",
                        "Answer structuring",
                        "Error recovery strategy",
                    ),
                    worked_example="Run a mixed 45-minute mock round and self-score.",
                    coding_task="Log mock performance and classify errors by type.",
                    reflection="What one behavior change would improve your next mock score most?",
                ),
            ),
            revision_focus=(
                "Reattempt lowest-scoring question category",
                "Update interview error log",
                "Refine concise answer templates",
            ),
            project_title="Interview drill notebook pack",
            project_problem="Create a reusable set of timed quant interview drills with scoring logs.",
            project_data=("Question bank", "Timed responses", "Error classifications"),
            project_steps=(
                "Assemble mixed-domain question sets",
                "Run timed attempts",
                "Score and classify errors",
                "Refine solution patterns",
                "Build next-week focus plan",
            ),
            project_metrics=("Accuracy", "Speed", "Error recurrence", "Communication clarity"),
            admissions_task="Align interview prep outcomes with application narrative confidence statements.",
            interview_task="Complete one full timed mixed-domain mock round.",
        ),
        WeekPlan(
            theme="Quant interview prep II and strats communication",
            objective="Sharpen front-office communication and strategy discussion readiness.",
            weekday_days=(
                DayPlan(
                    topic="Market intuition drills",
                    concepts=(
                        "Macro-to-market translation",
                        "Regime interpretation",
                        "Risk narrative framing",
                    ),
                    worked_example="Explain how a rate shock may affect equity and fixed-income signals.",
                    coding_task="Create market-scenario note template with impact mapping.",
                    reflection="Which macro-market link is least intuitive for you right now?",
                ),
                DayPlan(
                    topic="Trade idea structuring",
                    concepts=(
                        "Hypothesis articulation",
                        "Catalyst and timing",
                        "Risk and invalidation",
                    ),
                    worked_example="Draft a compact trade thesis with clear invalidation criteria.",
                    coding_task="Build one-page trade idea template.",
                    reflection="How do you separate conviction from overconfidence?",
                ),
                DayPlan(
                    topic="Risk-first communication",
                    concepts=(
                        "Downside framing",
                        "Scenario defense",
                        "Position sizing rationale",
                    ),
                    worked_example="Present a trade idea emphasizing risk controls before return potential.",
                    coding_task="Prepare risk scenario table for one strategy pitch.",
                    reflection="Which risk scenario is hardest for you to defend?",
                ),
                DayPlan(
                    topic="Behavioral and fit interview prep",
                    concepts=(
                        "Story consistency",
                        "Evidence-backed strengths",
                        "Growth narrative",
                    ),
                    worked_example="Answer common fit questions with project-backed examples.",
                    coding_task="Draft STAR-style responses for 5 behavioral prompts.",
                    reflection="Where does your narrative still sound generic?",
                ),
                DayPlan(
                    topic="Final mock panel",
                    concepts=(
                        "Technical clarity",
                        "Executive communication",
                        "Composure under challenge",
                    ),
                    worked_example="Run a full mock panel covering technical and behavioral components.",
                    coding_task="Compile mock feedback and action plan.",
                    reflection="What one communication habit should you change immediately?",
                ),
            ),
            revision_focus=(
                "Re-record one weak mock response",
                "Refine trade thesis invalidation logic",
                "Review narrative consistency across SOP and interview answers",
            ),
            project_title="Strategy pitch deck",
            project_problem="Build and present a concise strategy pitch with risk-first framing.",
            project_data=("Strategy metrics", "Risk scenarios", "Implementation assumptions"),
            project_steps=(
                "Define thesis and edge",
                "Quantify expected behavior",
                "Add risk controls and invalidation",
                "Prepare 10-minute deck",
                "Run mock Q&A",
            ),
            project_metrics=("Pitch clarity", "Risk defense quality", "Q&A resilience", "Narrative consistency"),
            admissions_task="Finalize all application artifacts with polished storytelling.",
            interview_task="Complete two mock interviews and implement feedback revisions.",
        ),
        WeekPlan(
            theme="Final integration and launch-ready portfolio",
            objective="Integrate all learning outputs into a final capstone dossier ready for applications and interviews.",
            weekday_days=(
                DayPlan(
                    topic="Portfolio curation and selection",
                    concepts=(
                        "Signal-to-noise filtering of projects",
                        "Narrative coherence",
                        "Audience-specific packaging",
                    ),
                    worked_example="Select top 4 projects and define positioning for each target audience.",
                    coding_task="Create portfolio index with project links and summaries.",
                    reflection="Which project best demonstrates end-to-end quant maturity?",
                ),
                DayPlan(
                    topic="End-to-end reproducibility pass",
                    concepts=(
                        "Environment and dependency checks",
                        "Notebook rerun integrity",
                        "Result traceability",
                    ),
                    worked_example="Re-run representative notebooks and verify consistency.",
                    coding_task="Build reproducibility checklist and execution log.",
                    reflection="What reproducibility gap would worry an evaluator most?",
                ),
                DayPlan(
                    topic="Final capstone integration",
                    concepts=(
                        "Hypothesis-to-deployment storyline",
                        "Cross-module consistency",
                        "Risk and governance integration",
                    ),
                    worked_example="Assemble a single narrative connecting data, modeling, risk, and execution.",
                    coding_task="Create final capstone report template with linked artifacts.",
                    reflection="Which section needs stronger quantitative evidence?",
                ),
                DayPlan(
                    topic="Presentation polishing",
                    concepts=(
                        "Executive summary writing",
                        "Technical appendix structure",
                        "Visual communication standards",
                    ),
                    worked_example="Refine final report charts and concise summary points.",
                    coding_task="Generate clean chart exports and final tables.",
                    reflection="Does your summary lead with outcomes and evidence?",
                ),
                DayPlan(
                    topic="Launch checklist and next-90-day roadmap",
                    concepts=(
                        "Sustainable learning cadence",
                        "Portfolio maintenance",
                        "Paper-trading progression controls",
                    ),
                    worked_example="Draft next 90-day post-program plan with milestones.",
                    coding_task="Create post-program tracking board with deadlines.",
                    reflection="What will keep your progress compounding after week 24?",
                ),
            ),
            revision_focus=(
                "Final audit of all major project artifacts",
                "Recheck admissions and interview readiness checklist",
                "Document post-program continuity plan",
            ),
            project_title="Capstone 6: Final quant dossier",
            project_problem="Deliver a complete quant dossier combining research, modeling, risk, execution, and communication artifacts.",
            project_data=("All prior project artifacts", "Execution logs", "Application documents"),
            project_steps=(
                "Curate best artifacts",
                "Validate reproducibility",
                "Assemble final report and deck",
                "Run final mock presentation",
                "Publish dossier and action roadmap",
            ),
            project_metrics=("Completeness", "Technical quality", "Communication quality", "Readiness score"),
            admissions_task="Submit final application package checklist for all selected programs.",
            interview_task="Complete final technical+behavioral mock and freeze preparation notes.",
        ),
    ]


# Expand to 24 weeks by adding targeted advanced/review variants where needed.
def expanded_week_plans() -> list[WeekPlan]:
    base = week_plans()
    # Weeks covered explicitly above: 1-20 and 21-24 integrated at end -> total 24 entries expected.
    if len(base) != 24:
        raise ValueError(f"Week plan count mismatch: expected 24, got {len(base)}")
    return base


def phase_for_week(week_no: int) -> str:
    if week_no <= 4:
        return "foundations"
    if week_no <= 8:
        return "ml"
    if week_no <= 12:
        return "time_series"
    if week_no <= 16:
        return "portfolio"
    if week_no <= 20:
        return "advanced"
    return "launch"


def concept_explanation(concept: str, week_theme: str, week_no: int) -> str:
    phase_focus = {
        "foundations": "clean data assumptions and stable mathematical transformations",
        "ml": "causal feature design, leakage control, and robust model validation",
        "time_series": "temporal dependence structure and out-of-sample forecast discipline",
        "portfolio": "allocation constraints, risk decomposition, and capital efficiency",
        "advanced": "alpha stability, execution realism, and risk-governed deployment",
        "launch": "decision quality, communication rigor, and reproducible evidence",
    }
    notation_emphasis = {
        "foundations": "define prices, returns, percentages, and all symbols before doing any arithmetic",
        "ml": "define labels, feature windows, and leakage boundaries before fitting any model",
        "time_series": "define time index, lag notation, and forecast horizon before estimating dependence",
        "portfolio": "define weights, constraints, and risk units before solving the allocation problem",
        "advanced": "define universe construction, signal scaling, and execution units before evaluating alpha",
        "launch": "define readiness metrics, scoring weights, and evidence thresholds before making final decisions",
    }
    phase = phase_for_week(week_no)
    return (
        f"{concept} is a core part of '{week_theme}'. "
        f"Start with notation discipline: {notation_emphasis[phase]}. "
        f"Then focus on {phase_focus[phase]} by pairing at least one formula with one real market example (SPY/QQQ/AAPL or phase-relevant assets), "
        "verifying units, and documenting one failure mode that appears in stressed regimes."
    )


def formula_entries(week_no: int, day_no: int) -> list[tuple[str, str, str]]:
    phase = phase_for_week(week_no)
    phase_formulas: dict[str, list[tuple[str, str, str]]] = {
        "foundations": [
            ("Simple Return", r"r_t = \frac{P_t - P_{t-1}}{P_{t-1}}", "Normalize raw price moves."),
            ("Log Return", r"\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)", "Additive return representation."),
            ("Annualized Volatility", r"\sigma_{ann}=\sqrt{252}\,Std(r_t)", "Scale daily uncertainty to annual horizon."),
            ("Sharpe Ratio", r"S=\frac{R_{ann}-R_f}{\sigma_{ann}}", "Risk-adjusted performance score."),
            ("Turnover", r"TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|", "Execution intensity proxy."),
        ],
        "ml": [
            ("Forward Target", r"y_t=\mathbb{1}[r_{t+1}>0]", "Label must stay forward-looking."),
            ("Logistic Probability", r"p=\frac{1}{1+e^{-z}}", "Convert score to probability."),
            ("MSE", r"\mathcal{L}_{MSE}=\frac{1}{n}\sum_i(y_i-\hat{y}_i)^2", "Baseline regression loss."),
            ("Cross-Entropy", r"\mathcal{L}_{CE}=-\frac{1}{n}\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]", "Classification objective."),
            ("Ridge Penalty", r"\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2", "Regularized stability control."),
        ],
        "time_series": [
            ("First Difference", r"\Delta x_t=x_t-x_{t-1}", "Removes non-stationary level drift."),
            ("Autocorrelation", r"\rho_k=\frac{Cov(x_t,x_{t-k})}{Var(x_t)}", "Lag-memory measurement."),
            ("AR(1)", r"x_t=c+\phi x_{t-1}+\epsilon_t", "One-step dependence model."),
            ("EWMA Vol", r"\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2", "Adaptive volatility estimate."),
            ("RMSE", r"RMSE=\sqrt{\frac{1}{n}\sum_t e_t^2}", "Forecast error benchmark."),
        ],
        "portfolio": [
            ("Portfolio Return", r"\mu_p=w^\top\mu", "Expected return from weighted assets."),
            ("Portfolio Variance", r"\sigma_p^2=w^\top\Sigma w", "Quadratic risk engine."),
            ("Risk Contribution", r"RC_i=w_i\frac{(\Sigma w)_i}{\sigma_p}", "Per-position risk budget."),
            ("Duration Shock", r"\frac{\Delta P}{P}\approx-D_{mod}\Delta y", "First-order bond sensitivity."),
            ("CVaR", r"CVaR_\alpha=E[L\mid L\ge VaR_\alpha]", "Tail-risk expectation."),
        ],
        "advanced": [
            ("Cross-Sectional Z", r"z_{i,t}=\frac{x_{i,t}-\mu_t}{\sigma_t}", "Universe-normalized signal."),
            ("Information Coefficient", r"IC_t=Corr(score_{i,t},r_{i,t+1})", "Signal/forward-return linkage."),
            ("IC t-Statistic", r"t_{IC}=\frac{\bar{IC}}{Std(IC)/\sqrt{T}}", "Signal persistence test."),
            ("Spread Z-Score", r"z_t=\frac{s_t-\mu_s}{\sigma_s}", "Stat-arb entry normalization."),
            ("Implementation Shortfall", r"IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}", "Execution loss in bps."),
        ],
        "launch": [
            ("Expected Value", r"EV=p\cdot Gain-(1-p)\cdot Loss", "Decision-quality baseline."),
            ("Readiness Score", r"S=\sum_j w_js_j", "Weighted progress metric."),
            ("Bayes Update", r"P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)}", "Evidence-driven belief update."),
            ("CAGR", r"CAGR=\left(\frac{V_T}{V_0}\right)^{1/T}-1", "Long-horizon growth target."),
            ("Gap", r"Gap_j=Target_j-Current_j", "Remaining improvement workload."),
        ],
    }

    formulas = phase_formulas[phase]
    offset = (day_no - 1) % len(formulas)
    selected = [formulas[offset], formulas[(offset + 1) % len(formulas)], formulas[(offset + 2) % len(formulas)]]
    return selected


def symbol_definitions(week_no: int) -> list[str]:
    phase = phase_for_week(week_no)
    common = [
        ("$P_t$", "Price at time $t$", "USD/share", "$110.50"),
        ("$r_t$", "Simple return", "decimal or %", "0.012 = 1.2%"),
        ("$\\mu$", "Expected return", "annualized decimal", "0.14"),
        ("$\\sigma$", "Volatility (std. dev.)", "annualized decimal", "0.18"),
    ]
    extras = {
        "foundations": [
            ("$R_f$", "Risk-free rate", "annualized decimal", "0.03"),
            ("$TO_t$", "Portfolio turnover", "fraction of portfolio", "0.12"),
        ],
        "ml": [
            ("$\\hat{y}$", "Model prediction", "class/probability", "0.73"),
            ("$\\lambda$", "Regularization strength", "non-negative scalar", "0.10"),
            ("$TP,FP,FN$", "Confusion matrix counts", "integer count", "TP=52"),
        ],
        "time_series": [
            ("$\\phi$", "Autoregressive coefficient", "dimensionless", "0.64"),
            ("$e_t$", "Forecast residual", "return units", "-0.003"),
            ("$\\lambda$", "EWMA decay factor", "0 to 1", "0.94"),
        ],
        "portfolio": [
            ("$w$", "Portfolio weights", "sum to 1", "[0.35,0.25,0.40]"),
            ("$\\Sigma$", "Covariance matrix", "return^2", "3x3 matrix"),
            ("$D_{mod}$", "Modified duration", "years", "5.8"),
        ],
        "advanced": [
            ("$IC$", "Information coefficient", "correlation", "0.04"),
            ("$ADV$", "Average daily volume", "shares/day", "12M"),
            ("$IS$", "Implementation shortfall", "basis points", "14.2 bps"),
        ],
        "launch": [
            ("$S$", "Readiness score", "0 to 100 scale", "83.4"),
            ("$EV$", "Expected value", "R-multiple", "0.45R"),
            ("$Gap_j$", "Target-current skill gap", "score points", "7.5"),
        ],
    }
    rows = common + extras[phase]
    lines = [
        "| Symbol | Meaning | Units | Example |",
        "| --- | --- | --- | --- |",
    ]
    lines.extend(f"| {sym} | {meaning} | {units} | {example} |" for sym, meaning, units, example in rows)
    return lines


def render_formula_section(week_no: int, day_no: int) -> list[str]:
    phase = phase_for_week(week_no)
    anchor = {
        "foundations": "Compute this on SPY and QQQ daily closes, then compare how one volatile day changes the metric.",
        "ml": "Use a walk-forward split and verify the metric does not leak future labels into feature construction.",
        "time_series": "Run the formula on rolling windows and inspect whether the value is stable across calm and stress periods.",
        "portfolio": "Evaluate the metric on at least three assets and document which constraint changes the final portfolio most.",
        "advanced": "Measure pre-cost and post-cost values to verify execution frictions do not erase signal edge.",
        "launch": "Translate the metric into a go/no-go decision with explicit thresholds and risk guardrails.",
    }
    lines: list[str] = []
    for idx, (name, latex, interpretation) in enumerate(formula_entries(week_no, day_no), start=1):
        lines.extend(
            [
                f"### Formula {idx}: {name}",
                "$$",
                latex,
                "$$",
                f"**Plain-English interpretation:** {interpretation}",
                "**Notation check:** Identify each symbol and its units before coding this formula.",
                f"**Real-world anchor:** {anchor[phase]}",
                "",
            ]
        )
    return lines


def real_trading_example(week_no: int, day_no: int, day: DayPlan) -> list[str]:
    phase = phase_for_week(week_no)
    universe = {
        "foundations": ("SPY, QQQ, AAPL", "DGS10, UNRATE"),
        "ml": ("SPY, XLK, XLF, XLE", "DFF, VIXCLS"),
        "time_series": ("SPY, TLT, GLD", "VIXCLS, DGS2"),
        "portfolio": ("SPY, TLT, GLD, HYG", "DGS10, T10YIE"),
        "advanced": ("SPY, IWM, EFA, EEM", "DFF, BAMLH0A0HYM2"),
        "launch": ("SPY, QQQ, TLT", "VIXCLS, TEDRATE"),
    }
    tickers, fred = universe[phase]
    return [
        f"- Instruments: {tickers}",
        f"- Macro overlay (FRED): {fred}",
        "- Suggested window: 2018-01-01 to 2026-03-31",
        f"- Day objective: {day.worked_example}",
        "",
        "Execution narrative:",
        "1. Pull market data from Yahoo Finance and align calendars.",
        "2. Pull the listed FRED series and join strictly by release-aware timestamps.",
        "3. Compute today's formulas and compare behavior in stress sub-periods.",
        "4. Translate quantitative results into one explicit trading decision and one risk guardrail.",
        f"5. Validate that the decision is consistent with topic '{day.topic}'.",
    ]


def solved_problems(week_no: int, day_no: int) -> list[tuple[str, list[str], list[str], str]]:
    phase = phase_for_week(week_no)

    if phase == "foundations":
        p0 = 100 + 2 * day_no
        p1 = round(p0 * (1 + 0.011 + 0.001 * day_no), 3)
        r = (p1 - p0) / p0
        sigma_d = 0.0105 + 0.0007 * day_no
        sigma_ann = sigma_d * (252 ** 0.5)
        return [
            (
                "Compute simple return",
                [f"Price moves from ${p0:.2f} to ${p1:.2f}."],
                [
                    r"1. $r_t=\frac{P_t-P_{t-1}}{P_{t-1}}$.",
                    f"2. r_t = ({p1:.3f}-{p0:.3f})/{p0:.3f} = {r:.6f}.",
                ],
                f"Simple return = {r:.2%}.",
            ),
            (
                "Annualize volatility",
                [f"Daily volatility estimate is {sigma_d:.4f}."],
                [
                    r"1. $\sigma_{ann}=\sqrt{252}\cdot\sigma_d$.",
                    f"2. sigma_ann = sqrt(252)*{sigma_d:.4f} = {sigma_ann:.4f}.",
                ],
                f"Annualized volatility = {sigma_ann:.2%}.",
            ),
            (
                "Compute Sharpe ratio",
                ["Annual return is 14.0%, risk-free rate is 3.0%.", f"Use volatility {sigma_ann:.2%}."],
                [
                    r"1. $S=\frac{R_{ann}-R_f}{\sigma_{ann}}$.",
                    f"2. S = (0.14-0.03)/{sigma_ann:.4f} = {(0.11/sigma_ann):.4f}.",
                ],
                f"Sharpe ratio = {(0.11/sigma_ann):.2f}.",
            ),
        ]

    if phase == "ml":
        z = -0.7 + 0.3 * day_no
        p = 1 / (1 + __import__("math").exp(-z))
        tp, fp, fn = 50, 12, 18
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * precision * recall / (precision + recall)
        return [
            (
                "Convert logit to probability",
                [f"Model score z = {z:.3f}."],
                [r"1. $p=\frac{1}{1+e^{-z}}$.", f"2. p = 1/(1+exp(-{z:.3f})) = {p:.6f}."],
                f"Predicted probability = {p:.2%}.",
            ),
            (
                "Compute precision, recall, F1",
                [f"TP={tp}, FP={fp}, FN={fn}."],
                [
                    r"1. $Precision=\frac{TP}{TP+FP}$.",
                    f"2. Precision={precision:.4f}.",
                    r"3. $Recall=\frac{TP}{TP+FN}$.",
                    f"4. Recall={recall:.4f}.",
                    r"5. $F1=\frac{2PR}{P+R}$.",
                    f"6. F1={f1:.4f}.",
                ],
                f"Precision={precision:.2%}, Recall={recall:.2%}, F1={f1:.2%}.",
            ),
            (
                "Compute ridge objective",
                ["MSE = 0.0410, ||beta||_2^2 = 1.90, lambda = 0.06."],
                [r"1. $\mathcal{L}=\mathcal{L}_{MSE}+\lambda\|\beta\|_2^2$.", "2. L = 0.0410 + 0.06*1.90 = 0.1550."],
                "Ridge objective = 0.1550.",
            ),
        ]

    if phase == "time_series":
        phi = 0.64
        x_t = 0.015
        c = 0.001
        forecast = c + phi * x_t
        return [
            (
                "One-step AR(1) forecast",
                [f"Use c={c:.3f}, phi={phi:.2f}, x_t={x_t:.3f}."],
                [r"1. $x_{t+1}=c+\phi x_t$.", f"2. Forecast = {c:.3f} + {phi:.2f}*{x_t:.3f} = {forecast:.6f}."],
                f"Forecasted value = {forecast:.2%}.",
            ),
            (
                "EWMA volatility update",
                ["lambda=0.94, sigma_(t-1)=0.020, r_(t-1)=-0.012."],
                [
                    r"1. $\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$.",
                    "2. sigma_t^2 = 0.94*(0.020^2) + 0.06*(0.012^2) = 0.00038464.",
                    "3. sigma_t = sqrt(0.00038464) = 0.01961.",
                ],
                "Updated volatility = 1.96%.",
            ),
            (
                "Compute RMSE",
                ["Errors are [0.004, -0.006, 0.003, -0.002, 0.005]."],
                [
                    r"1. $RMSE=\sqrt{\frac{1}{n}\sum e_t^2}$.",
                    "2. Mean squared error = 0.000018.",
                    "3. RMSE = sqrt(0.000018) = 0.00424.",
                ],
                "RMSE = 0.424%.",
            ),
        ]

    if phase == "portfolio":
        return [
            (
                "Portfolio expected return",
                ["w=[0.6,0.4], mu=[0.12,0.08]."],
                [r"1. $\mu_p=w^\top\mu$.", "2. mu_p = 0.6*0.12 + 0.4*0.08 = 0.104."],
                "Portfolio expected return = 10.4%.",
            ),
            (
                "Portfolio volatility",
                ["sigma1=0.20, sigma2=0.12, rho=0.30, w1=0.6, w2=0.4."],
                [
                    r"1. $\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho\sigma_1\sigma_2$.",
                    "2. sigma_p^2 = 0.02048.",
                    "3. sigma_p = sqrt(0.02048) = 0.1431.",
                ],
                "Portfolio volatility = 14.31%.",
            ),
            (
                "Duration shock",
                ["Modified duration = 5.8, yield shift = +0.25%."],
                [r"1. $\Delta P/P\approx-D_{mod}\Delta y$.", "2. DeltaP/P = -5.8*0.0025 = -0.0145."],
                "Approximate bond price change = -1.45%.",
            ),
        ]

    if phase == "advanced":
        return [
            (
                "Factor z-score",
                ["Signal=1.60, mean=0.70, std=0.45."],
                [r"1. $z=\frac{x-\mu}{\sigma}$.", "2. z=(1.60-0.70)/0.45 = 2.00."],
                "Signal z-score = 2.00.",
            ),
            (
                "IC t-stat",
                ["Mean IC=0.045, std(IC)=0.018, T=12 months."],
                [r"1. $t=\frac{\bar{IC}}{s/\sqrt{T}}$.", "2. t = 0.045/(0.018/sqrt(12)) = 8.66."],
                "IC t-stat = 8.66.",
            ),
            (
                "Implementation shortfall",
                ["Arrival=101.20, execution=101.36."],
                [r"1. $IS_{bps}=10^4\frac{p_{exec}-p_{arr}}{p_{arr}}$.", "2. IS_bps = 10000*(0.16/101.20) = 15.81."],
                "Implementation shortfall = 15.81 bps.",
            ),
        ]

    return [
        (
            "Expected value",
            ["Win probability=0.58, gain=1.5R, loss=1R."],
            [r"1. $EV=p\cdot Gain-(1-p)\cdot Loss$.", "2. EV = 0.58*1.5 - 0.42*1.0 = 0.45R."],
            "Expected value = 0.45R per trade.",
        ),
        (
            "Readiness score",
            ["Weights=[0.45,0.35,0.20], scores=[82,87,80]."],
            [r"1. $S=\sum_jw_js_j$.", "2. S = 0.45*82 + 0.35*87 + 0.20*80 = 83.35."],
            "Readiness score = 83.35/100.",
        ),
        (
            "CAGR target",
            ["V0=1.00, VT=1.32, T=3 years."],
            [r"1. $CAGR=(V_T/V_0)^{1/T}-1$.", "2. CAGR = (1.32/1.00)^(1/3)-1 = 0.0969."],
            "Required CAGR = 9.69%.",
        ),
    ]


def render_solved_problems(week_no: int, day_no: int) -> list[str]:
    phase = phase_for_week(week_no)
    trap_by_phase = {
        "foundations": "Confusing percentage return with absolute dollar change or forgetting that returns compound multiplicatively.",
        "ml": "Using forward labels with backward-filled features, which silently introduces leakage.",
        "time_series": "Treating a non-stationary series as stationary and over-trusting one in-sample fit.",
        "portfolio": "Ignoring covariance and focusing only on expected return, which underestimates portfolio risk.",
        "advanced": "Reporting gross signal performance without implementation costs or capacity constraints.",
        "launch": "Using one metric in isolation instead of combining expected value, risk limits, and readiness score.",
    }
    lines: list[str] = []
    for idx, (title, given, steps, answer) in enumerate(solved_problems(week_no, day_no), start=1):
        lines.append(f"### Solved Problem {idx}: {title}")
        lines.append("Given:")
        lines.extend(f"- {item}" for item in given)
        lines.append("Solution:")
        lines.extend(steps)
        lines.append(f"Final answer: {answer}")
        lines.append(f"Common trap: {trap_by_phase[phase]}")
        lines.append("Interpretation: Write one sentence describing how this result would change a real trading decision.")
        lines.append("")
    return lines


def coding_walkthrough(week_no: int, day: DayPlan) -> list[str]:
    phase = phase_for_week(week_no)
    snippets = {
        "foundations": [
            "```python",
            "prices = load_prices(['SPY', 'QQQ', 'AAPL'])",
            "returns = prices.pct_change().dropna()",
            "metrics = compute_risk_metrics(returns)",
            "assert metrics['max_drawdown'] <= 0",
            "```",
        ],
        "ml": [
            "```python",
            "X_train, X_valid, y_train, y_valid = temporal_split(features, target)",
            "model = fit_logistic_regression(X_train, y_train, l2=0.1)",
            "proba = model.predict_proba(X_valid)[:, 1]",
            "report = classification_report_from_thresholds(y_valid, proba)",
            "```",
        ],
        "time_series": [
            "```python",
            "series = build_stationary_series(price_df['Close'])",
            "forecast = walk_forward_arima(series, order=(1, 1, 1))",
            "errors = series.loc[forecast.index] - forecast",
            "rmse = np.sqrt(np.mean(errors**2))",
            "```",
        ],
        "portfolio": [
            "```python",
            "mu, cov = estimate_moments(asset_returns)",
            "weights = solve_constrained_mv(mu, cov, max_weight=0.35)",
            "risk_budget = risk_contributions(weights, cov)",
            "rebalance_flag = should_rebalance(weights, target_weights, threshold=0.03)",
            "```",
        ],
        "advanced": [
            "```python",
            "factor_scores = compute_factor_scores(universe_frame)",
            "signals = build_long_short_buckets(factor_scores, q=0.2)",
            "execution_cost = estimate_slippage(signals, adv_frame)",
            "net_pnl = backtest_with_costs(signals, returns, execution_cost)",
            "```",
        ],
        "launch": [
            "```python",
            "readiness = score_readiness(quiz_scores, mock_scores, project_rubrics)",
            "posterior = bayes_update(prior=0.55, likelihood=0.72, evidence=0.61)",
            "roadmap = build_90_day_plan(readiness, posterior)",
            "export_launch_checklist(roadmap)",
            "```",
        ],
    }

    return [
        "1. Build an explicit data-ingestion layer with timestamp and schema checks.",
        f"2. Implement today's objective as reusable functions: {day.coding_task}",
        "3. Add validation tests for leakage, NaNs, and unrealistic outliers.",
        "4. Produce diagnostic plots and summarize one actionable trading rule.",
        "5. Record one failure mode and one mitigation in comments.",
        "",
        "Reference implementation sketch:",
        *snippets[phase],
    ]


def daily_quiz_questions(week_no: int, day_no: int, day: DayPlan) -> list[str]:
    week_label = f"Week {week_no:02d} Day {day_no:02d}"
    formula_name, formula_latex, _ = formula_entries(week_no, day_no)[0]
    return [
        f"1. PM interview question ({week_label}): Explain {formula_name} and define every symbol clearly.",
        f"   - Model answer: \"I use {formula_name} to convert raw prices into a decision-ready metric. "
        f"The formula is ${formula_latex}$. I define each symbol before computing it, verify units, and then interpret "
        "the output as a risk-adjusted trading input rather than a standalone signal.\"",
        "2. Risk manager question: Using one real ticker from this lesson, what risk guardrail would you enforce?",
        "   - Model answer: \"I would run the metric on SPY and one higher-volatility asset, then enforce a volatility or drawdown cap. "
        "If the metric degrades in stressed regimes, I reduce gross exposure and require confirmation from a second risk check.\"",
        f"3. Production question: Why does '{day.topic}' matter in live trading systems?",
        f"   - Model answer: \"{day.topic} matters because it links model logic to real execution constraints. "
        "In production, I need reproducible calculations, explicit guardrails, and decision rules that stay stable when regime conditions change.\"",
        "",
        "Scoring rubric:",
        "- Full credit requires: correct notation, one numeric example, one explicit risk guardrail, and a production decision statement.",
    ]


def interview_drill_prompt(day: DayPlan) -> list[str]:
    return [
        f"- Prompt: \"Walk me through {day.topic} as if you are presenting to a PM who cares about risk-adjusted returns.\"",
        "- What interviewers look for:",
        "  1. Correct notation and units.",
        "  2. Ability to connect theory to a real trade decision.",
        "  3. Awareness of edge cases, costs, and failure modes.",
        "- Model answer framework:",
        "  - Context: define business objective and market regime.",
        "  - Method: state formula and variables clearly.",
        "  - Decision: explain one actionable rule and one risk guardrail.",
    ]


def lesson_path(week_no: int, day_no: int) -> str:
    return f"content/week-{week_no:02d}/day-{day_no:02d}.md"


def day_title(plans: list[WeekPlan], week_no: int, day_no: int) -> str:
    plan = plans[week_no - 1]
    if day_no <= 5:
        return plan.weekday_days[day_no - 1].topic
    if day_no == 6:
        return "Revision Sprint"
    return "Portfolio Project"


def day_deliverable(plans: list[WeekPlan], week_no: int, day_no: int) -> str:
    plan = plans[week_no - 1]
    if day_no <= 5:
        return plan.weekday_days[day_no - 1].coding_task
    if day_no == 6:
        return "Revision checklist with corrected errors and next-week retest priorities."
    return plan.project_title


def continuity_context(plans: list[WeekPlan], week_no: int, day_no: int) -> dict[str, str | None]:
    if week_no == 1 and day_no == 1:
        previous_label = "Program kickoff: environment, data loader, and assumption baseline."
        previous_path = None
    elif day_no == 1:
        previous_label = f"Week {week_no - 1:02d} Day 07: Portfolio Project"
        previous_path = lesson_path(week_no - 1, 7)
    else:
        previous_day = day_no - 1
        previous_label = f"Week {week_no:02d} Day {previous_day:02d}: {day_title(plans, week_no, previous_day)}"
        previous_path = lesson_path(week_no, previous_day)

    if week_no == 24 and day_no == 7:
        next_label = "Program completion: launch your interview-ready quant portfolio and job plan."
        next_path = None
    elif day_no == 7:
        next_label = f"Week {week_no + 1:02d} Day 01: {day_title(plans, week_no + 1, 1)}"
        next_path = lesson_path(week_no + 1, 1)
    else:
        next_day = day_no + 1
        next_label = f"Week {week_no:02d} Day {next_day:02d}: {day_title(plans, week_no, next_day)}"
        next_path = lesson_path(week_no, next_day)

    return {
        "previousLabel": previous_label,
        "previousLessonPath": previous_path,
        "todayDeliverable": day_deliverable(plans, week_no, day_no),
        "nextLabel": next_label,
        "nextLessonPath": next_path,
    }


def continuity_section(continuity: dict[str, str | None]) -> list[str]:
    previous = continuity.get("previousLabel") or "N/A"
    previous_path = continuity.get("previousLessonPath")
    deliverable = continuity.get("todayDeliverable") or "N/A"
    nxt = continuity.get("nextLabel") or "N/A"
    next_path = continuity.get("nextLessonPath")

    lines = [
        "## Continuity and Handoff",
        f"- Previous checkpoint: {previous}",
    ]
    if previous_path:
        lines.append(f"- Previous lesson file: {previous_path}")
    lines.extend(
        [
            f"- Today's deliverable: {deliverable}",
            f"- Next handoff target: {nxt}",
        ]
    )
    if next_path:
        lines.append(f"- Next lesson file: {next_path}")
    return lines


def week_resource_paths(week_no: int) -> dict[str, str]:
    week_id = f"week-{week_no:02d}"
    return {
        "notebookPath": f"notebooks/{week_id}/{week_id}-learning.ipynb",
        "overviewPath": f"resources/{week_id}/overview.md",
        "quizPath": f"resources/{week_id}/quiz.md",
        "revisionChecklistPath": f"resources/{week_id}/revision-checklist.md",
        "miniProjectPath": f"resources/{week_id}/mini-project-template.md",
    }


def day_markdown(
    week_no: int,
    day_no: int,
    week: WeekPlan,
    day: DayPlan,
    continuity: dict[str, str | None],
) -> str:
    concepts_block: list[str] = []
    for idx, concept in enumerate(day.concepts, start=1):
        concepts_block.append(f"### Concept {idx}: {concept}")
        concepts_block.append(concept_explanation(concept, week.theme, week_no))
        concepts_block.append("")

    hour_plan: list[str] = [
        "- **Block 1 (45 min):** Reset notation (prices, returns, percentages, symbols, units).",
        "- **Block 2 (60 min):** Core formulas and compounding intuition with plain-language explanations.",
        "- **Block 3 (45 min):** Hand-calculated solved examples plus common traps.",
        "- **Block 4 (60 min):** Python/pandas implementation and output verification.",
        "- **Block 5 (30 min):** Practice questions, interview drill, and reflection.",
    ]

    practice: list[str] = [
        "1. Re-derive today's formulas manually and define every variable and unit.",
        "2. Re-run the real trading example with one alternate ticker and compare outputs.",
        "3. Stress-test one assumption and write one explicit risk-control rule.",
        "4. Extend the coding walkthrough with one validation test and one edge-case test.",
        "5. Record one interview-ready explanation in less than 60 seconds.",
    ]

    return "\n".join(
        [
            f"# Week {week_no:02d} Day {day_no:02d}: {day.topic}",
            "",
            "## Study Duration",
            "- Planned effort: 4 hours",
            "",
            "## 5-Block Daily Structure",
            *hour_plan,
            "",
            "## Why It Matters in Quant",
            week.objective,
            "",
            *continuity_section(continuity),
            "",
            "## Theory Concepts",
            "",
            *concepts_block,
            "## Mathematical Foundations (LaTeX)",
            *render_formula_section(week_no, day_no),
            "## Symbol Definitions",
            *symbol_definitions(week_no),
            "",
            "## Real Trading Example",
            *real_trading_example(week_no, day_no, day),
            "",
            "## Step-by-Step Solved Problems",
            *render_solved_problems(week_no, day_no),
            "## Coding Walkthrough",
            *coding_walkthrough(week_no, day),
            "",
            "## Block 5: Practice, Quiz, and Interview Drill",
            "",
            "### Practice Problems",
            *practice,
            "",
            "### Daily Quiz (Realistic Interview Style)",
            *daily_quiz_questions(week_no, day_no, day),
            "",
            "### Interview Drill",
            *interview_drill_prompt(day),
            "",
            "## Reflection Question",
            day.reflection,
            "",
            "## Completion Checklist",
            "- [ ] Formula derivations re-worked manually",
            "- [ ] Real trading example reproduced with data checks",
            "- [ ] Solved problems reviewed and understood",
            "- [ ] Coding walkthrough executed and verified",
            "- [ ] Reflection logged in progress tracker",
        ]
    ) + "\n"


def revision_markdown(week_no: int, week: WeekPlan, continuity: dict[str, str | None]) -> str:
    return "\n".join(
        [
            f"# Week {week_no:02d} Day 06: Revision Sprint",
            "",
            "## Study Duration",
            "- Planned effort: 2 hours",
            "",
            *continuity_section(continuity),
            "",
            "## Revision Plan",
            "- 30 minutes: active recall of weekday concepts",
            "- 40 minutes: rebuild one code workflow from memory",
            "- 30 minutes: error log triage and retest plan",
            "- 20 minutes: update progress tracker and notes",
            "",
            "## Focus Areas",
            *(f"- {item}" for item in week.revision_focus),
            "",
            "## Revision Output",
            "- [ ] Updated error log entries",
            "- [ ] Weak concepts re-tested",
            "- [ ] Next-week risk list prepared",
        ]
    ) + "\n"


def project_markdown(week_no: int, week: WeekPlan, continuity: dict[str, str | None]) -> str:
    return "\n".join(
        [
            f"# Week {week_no:02d} Day 07: Portfolio Project",
            "",
            "## Study Duration",
            "- Planned effort: 2 hours",
            "",
            *continuity_section(continuity),
            "",
            f"## Project Title\n{week.project_title}",
            "",
            "## Problem Statement",
            week.project_problem,
            "",
            "## Data Sources",
            *(f"- {src}" for src in week.project_data),
            "",
            "## Implementation Steps",
            *(f"{idx}. {step}" for idx, step in enumerate(week.project_steps, start=1)),
            "",
            "## Evaluation Metrics",
            *(f"- {metric}" for metric in week.project_metrics),
            "",
            "## Deliverables",
            "- Notebook or script output",
            "- One-page summary memo",
            "- Tracker update with completion and lessons learned",
        ]
    ) + "\n"


def week_readme(week_no: int, week: WeekPlan) -> str:
    day_rows: list[str] = []
    for day_no, day in enumerate(week.weekday_days, start=1):
        day_rows.append(f"| Day {day_no:02d} | {day.topic} | 4h |")
    day_rows.append("| Day 06 | Revision Sprint | 2h |")
    day_rows.append("| Day 07 | Portfolio Project | 2h |")

    return "\n".join(
        [
            f"# Week {week_no:02d}: {week.theme}",
            "",
            "## Weekly Objective",
            week.objective,
            "",
            "## Time Budget",
            "| Day | Focus | Planned Hours |",
            "| --- | --- | --- |",
            *day_rows,
            "",
            "## Weekly Outcome",
            f"- Deliverable: {week.project_title}",
            "- Build one measurable improvement in technical depth and communication.",
            "",
            "## Parallel Tracks",
            f"- Admissions: {week.admissions_task}",
            f"- Interview: {week.interview_task}",
        ]
    ) + "\n"


def week_quiz(week_no: int, week: WeekPlan) -> str:
    qas: list[tuple[str, str]] = []
    for idx, day in enumerate(week.weekday_days, start=1):
        qas.append(
            (
                f"{idx}. Real interview question: How would you explain '{day.topic}' to a PM in under one minute?",
                (
                    f"\"I frame {day.topic.lower()} as a production decision tool, not just a classroom concept. "
                    "First, I define the core notation and units. Second, I run one real-market example and state the numeric result. "
                    "Third, I translate the output into a trade action plus one explicit risk guardrail. "
                    f"For implementation, I build reusable code to {day.coding_task.lower()} and log edge cases.\""
                ),
            )
        )
    qas.extend(
        [
            (
                "6. Regime-risk question: What assumptions from this week fail first during stress markets?",
                "\"The first failures are distribution stability and execution-cost assumptions. In stress regimes, volatility clustering, slippage, and correlation breakdown can invalidate clean backtest behavior. I would widen thresholds, reduce leverage, and require secondary confirmation before new entries.\"",
            ),
            (
                "7. Metric-selection question: Which metric from this week would you prioritize for live monitoring, and why?",
                "\"I prioritize the metric that directly links expected edge to controllable risk. It must be interpretable, stable across windows, and easy to validate daily. I pair it with a hard risk limit metric so performance and protection are monitored together.\"",
            ),
            (
                "8. Implementation question: Give one concrete production guardrail you would enforce.",
                "\"I enforce a hard stop on position sizing when realized volatility exceeds a pre-defined threshold relative to the training regime. This prevents model overconfidence during volatility expansion and keeps drawdowns bounded while diagnostics are rerun.\"",
            ),
            (
                "9. Communication question: How do you summarize this week's project to non-technical stakeholders?",
                "\"I summarize in three lines: objective, measured result, and risk control. I avoid jargon, state one verified number, and explain the decision implication. Then I show the fallback rule if the metric deteriorates.\"",
            ),
            (
                "10. Verification question: What is your first check before paper-trading this week's output?",
                "\"My first check is full reproducibility: rerun notebook cells end-to-end and verify outputs, data timestamps, and assumptions match documented logic. If any mismatch appears, I block deployment until resolved.\"",
            ),
        ]
    )

    return "\n".join(
        [
            f"# Week {week_no:02d} Quiz",
            "",
            "## Instructions",
            "- Attempt each question in interview format first (spoken answer in <60 seconds).",
            "- Then compare with the model answer and self-score for clarity, correctness, and risk awareness.",
            "- Target score: 8/10 or higher.",
            "",
            "## Interview Questions and Exact Model Answers",
            *[
                "\n".join(
                    [
                        f"### {q}",
                        "Model answer:",
                        a,
                    ]
                )
                for q, a in qas
            ],
        ]
    ) + "\n"


def mini_project_brief(week_no: int, week: WeekPlan) -> str:
    return "\n".join(
        [
            f"# Week {week_no:02d} Mini Project Brief",
            "",
            f"## Title\n{week.project_title}",
            "",
            "## Problem",
            week.project_problem,
            "",
            "## Data",
            *(f"- {src}" for src in week.project_data),
            "",
            "## Steps",
            *(f"{idx}. {step}" for idx, step in enumerate(week.project_steps, start=1)),
            "",
            "## Metrics",
            *(f"- {metric}" for metric in week.project_metrics),
            "",
            "## Common Mistakes to Avoid",
            "- Hidden leakage from future data",
            "- Ignoring transaction and execution effects",
            "- Reporting only best-case outcomes",
        ]
    ) + "\n"


def admissions_week_tasks(week_no: int, week: WeekPlan) -> str:
    return "\n".join(
        [
            f"# Admissions Tasks Week {week_no:02d}",
            "",
            f"Primary task: {week.admissions_task}",
            "",
            "## Required Actions",
            "1. Update target program tracker with current week evidence.",
            "2. Add one quantified project outcome to SOP/CV notes.",
            "3. Record scholarship eligibility and upcoming deadline risks.",
            "4. Update recommendation-support evidence package.",
            "5. Log completion in tracker.",
        ]
    ) + "\n"


def interview_week_tasks(week_no: int, week: WeekPlan) -> str:
    return "\n".join(
        [
            f"# Interview Tasks Week {week_no:02d}",
            "",
            f"Primary task: {week.interview_task}",
            "",
            "## Required Actions",
            "1. Complete one timed technical drill set.",
            "2. Solve one coding challenge with explanation-first approach.",
            "3. Record one 3-minute verbal explanation of a weekly concept.",
            "4. Update interview mistake log and mitigation actions.",
            "5. Mark readiness score for the week.",
        ]
    ) + "\n"


def roadmap_markdown(plans: list[WeekPlan]) -> str:
    lines = [
        "# 24-Week Quant Learning Roadmap",
        "",
        "Start date: 20 April 2026",
        "",
        "## Time Commitment",
        "- Monday to Friday: 4 hours/day",
        "- Saturday: 2 hours revision",
        "- Sunday: 2 hours portfolio project",
        "",
        "## Weekly Themes",
        "| Week | Theme | Outcome |",
        "| --- | --- | --- |",
    ]
    for idx, plan in enumerate(plans, start=1):
        lines.append(f"| {idx:02d} | {plan.theme} | {plan.project_title} |")
    return "\n".join(lines) + "\n"


def write_json_index(root: Path, plans: list[WeekPlan]) -> None:
    index: dict[str, list[dict[str, object]]] = {"weeks": []}
    for week_no, plan in enumerate(plans, start=1):
        week_id = f"week-{week_no:02d}"
        day_entries: list[dict[str, object]] = []
        resources = week_resource_paths(week_no)
        week_entry: dict[str, object] = {
            "week": week_no,
            "id": week_id,
            "theme": plan.theme,
            "objective": plan.objective,
            "days": day_entries,
            "resources": resources,
        }
        for day_no in range(1, 8):
            if day_no <= 5:
                title = plan.weekday_days[day_no - 1].topic
                day_type = "lesson"
                duration = 4
            elif day_no == 6:
                title = "Revision Sprint"
                day_type = "revision"
                duration = 2
            else:
                title = "Portfolio Project"
                day_type = "project"
                duration = 2

            continuity = continuity_context(plans, week_no, day_no)
            day_entries.append(
                {
                    "day": day_no,
                    "title": title,
                    "durationHours": duration,
                    "type": day_type,
                    "lessonPath": lesson_path(week_no, day_no),
                    "continuity": continuity,
                }
            )
        index["weeks"].append(week_entry)

    (root / "curriculum" / "curriculum-index.json").write_text(
        json.dumps(index, indent=2), encoding="utf-8"
    )

    web_data = root / "web" / "public" / "data"
    web_data.mkdir(parents=True, exist_ok=True)
    (web_data / "curriculum.json").write_text(json.dumps(index, indent=2), encoding="utf-8")


def build_web_content_copy(root: Path) -> None:
    source_root = root / "curriculum" / "weeks"
    target_root = root / "web" / "public" / "content"
    resources_root = root / "web" / "public" / "resources"
    target_root.mkdir(parents=True, exist_ok=True)
    resources_root.mkdir(parents=True, exist_ok=True)

    for week_no in range(1, 25):
        week_id = f"week-{week_no:02d}"
        src_week = source_root / week_id
        tgt_week = target_root / week_id
        tgt_resources = resources_root / week_id
        tgt_week.mkdir(parents=True, exist_ok=True)
        tgt_resources.mkdir(parents=True, exist_ok=True)

        (tgt_resources / "overview.md").write_text(
            (src_week / "README.md").read_text(encoding="utf-8"), encoding="utf-8"
        )
        (tgt_resources / "quiz.md").write_text(
            (src_week / f"{week_id}-quiz.md").read_text(encoding="utf-8"), encoding="utf-8"
        )
        (tgt_resources / "revision-checklist.md").write_text(
            (src_week / f"{week_id}-revision-checklist.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (tgt_resources / "mini-project-template.md").write_text(
            (src_week / f"{week_id}-mini-project-template.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )

        for day_no in range(1, 8):
            src = src_week / f"day-{day_no:02d}" / "lesson.md"
            tgt = tgt_week / f"day-{day_no:02d}.md"
            tgt.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


def generate_curriculum(root: Path) -> None:
    plans = expanded_week_plans()

    (root / "curriculum" / "roadmap.md").write_text(roadmap_markdown(plans), encoding="utf-8")

    for week_no, plan in enumerate(plans, start=1):
        week_id = f"week-{week_no:02d}"
        week_dir = root / "curriculum" / "weeks" / week_id
        week_dir.mkdir(parents=True, exist_ok=True)

        (week_dir / "README.md").write_text(week_readme(week_no, plan), encoding="utf-8")
        (week_dir / f"{week_id}-quiz.md").write_text(week_quiz(week_no, plan), encoding="utf-8")
        (week_dir / f"{week_id}-mini-project-template.md").write_text(
            mini_project_brief(week_no, plan), encoding="utf-8"
        )
        (week_dir / f"{week_id}-revision-checklist.md").write_text(
            dedent(
                f"""
                # {week_id} Revision Checklist

                - [ ] D1 recall review complete
                - [ ] D3 reinforcement complete
                - [ ] D7 weekly consolidation complete
                - [ ] Error log updated with root causes
                - [ ] Retest plan scheduled for next week
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )

        for day_no, day_plan in enumerate(plan.weekday_days, start=1):
            day_dir = week_dir / f"day-{day_no:02d}"
            day_dir.mkdir(parents=True, exist_ok=True)
            continuity = continuity_context(plans, week_no, day_no)
            (day_dir / "lesson.md").write_text(
                day_markdown(week_no, day_no, plan, day_plan, continuity), encoding="utf-8"
            )

        day6_dir = week_dir / "day-06"
        day6_dir.mkdir(parents=True, exist_ok=True)
        (day6_dir / "lesson.md").write_text(
            revision_markdown(week_no, plan, continuity_context(plans, week_no, 6)),
            encoding="utf-8",
        )

        day7_dir = week_dir / "day-07"
        day7_dir.mkdir(parents=True, exist_ok=True)
        (day7_dir / "lesson.md").write_text(
            project_markdown(week_no, plan, continuity_context(plans, week_no, 7)),
            encoding="utf-8",
        )

        admissions_dir = root / "admissions" / week_id
        admissions_dir.mkdir(parents=True, exist_ok=True)
        (admissions_dir / "tasks.md").write_text(
            admissions_week_tasks(week_no, plan), encoding="utf-8"
        )

        interview_dir = root / "interview" / week_id
        interview_dir.mkdir(parents=True, exist_ok=True)
        (interview_dir / "tasks.md").write_text(
            interview_week_tasks(week_no, plan), encoding="utf-8"
        )

    (root / "admissions" / "README.md").write_text(
        "# Admissions Track\n\nWeekly scholarship and application tasks aligned to curriculum progress.\n",
        encoding="utf-8",
    )
    (root / "interview" / "README.md").write_text(
        "# Interview Track\n\nWeekly technical and communication drills for quant interview readiness.\n",
        encoding="utf-8",
    )

    write_json_index(root, plans)
    build_web_content_copy(root)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    generate_curriculum(root)
    print("Generated full 24-week curriculum content and web index.")


if __name__ == "__main__":
    main()
