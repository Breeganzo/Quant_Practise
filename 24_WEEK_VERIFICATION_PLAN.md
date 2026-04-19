# 24_WEEK_VERIFICATION_PLAN

## Model
One logical agent per week with queued parallel execution.

## ReAct Loop Per Week
1. Observe
- Confirm weekday lessons exist.
- Count extension sections and solved problem 4 coverage.
- Confirm notebook presence for day + week files.

2. Reason
- Identify content and execution gaps against rubric.
- Decide whether to proceed with regeneration/execution/export.

3. Act
- Run weekday lesson enhancer for that week.
- Regenerate notebooks for that week.
- Execute notebooks for that week with report output.
- Export markdown/notebooks for that week.

4. Verify
- Confirm all 5 weekday lessons include extension section and solved problem 4.
- Confirm notebook execution report failures = 0.
- Confirm export manifest exists.

## Implemented Runner
- scripts/run_react_week_pipeline.py

## Run Command
- /Users/anto/Quant/.venv/bin/python scripts/run_react_week_pipeline.py --weeks all --workers 8

## Output
- data/processed/react_week_pipeline_report.json
- data/processed/reports/week-XX-notebooks.json
- data/processed/reports/week-XX-exports.json

## Latest Result
- Weeks processed: 24
- Passed: 24
- Failed: 0
