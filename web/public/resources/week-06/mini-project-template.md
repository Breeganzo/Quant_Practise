# Week 06 Mini Project Brief

## Title
Ensemble model comparison

## Problem
Compare tree-based models under a consistent validation and monitoring framework.

## Data
- Price features
- Volume features
- Regime labels

## Steps
1. Create baseline feature set
2. Train tree/forest/boosting models
3. Run ablation and stability tests
4. Evaluate by regime
5. Document deployment recommendation

## Metrics
- Validation score
- Stability score
- Calibration error
- Drift sensitivity

## Common Mistakes to Avoid
- Hidden leakage from future data
- Ignoring transaction and execution effects
- Reporting only best-case outcomes
