# Week 05 Mini Project Brief

## Title
Directional baseline model

## Problem
Build and evaluate a baseline supervised model for next-day direction prediction.

## Data
- Price-derived features
- Volume features
- Lagged macro indicator

## Steps
1. Define target and feature set
2. Apply temporal splitting
3. Train regression and classification baselines
4. Evaluate statistical and trading-relevant metrics
5. Write recommendation memo

## Metrics
- AUC
- Precision at threshold
- Stability across folds
- Turnover proxy

## Common Mistakes to Avoid
- Hidden leakage from future data
- Ignoring transaction and execution effects
- Reporting only best-case outcomes
