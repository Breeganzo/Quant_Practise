# Week 03 Mini Project Brief

## Title
Market data pipeline prototype

## Problem
Build a robust ETL workflow that ingests, cleans, aligns, and stores market data.

## Data
- Yahoo Finance
- FRED
- Local SQLite storage

## Steps
1. Design schema for prices and features
2. Ingest and normalize data
3. Handle missing values and alignment
4. Store transformed outputs
5. Validate data quality with checks

## Metrics
- Data completeness
- Alignment errors
- Pipeline runtime
- Validation pass rate

## Common Mistakes to Avoid
- Hidden leakage from future data
- Ignoring transaction and execution effects
- Reporting only best-case outcomes
