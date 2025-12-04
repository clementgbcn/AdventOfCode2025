# AdventOfCode2025

## Presentation

Advent of Code 2025 solution in Python

Run all the challenges with the command `python -m main -a`

Update the `README.md` `Results` section with `python -m main -r`

## Testing

Run the tests with the command `python -m pytest`

Moreover, you can get the coverage with
```
python -m coverage run -m pytest
python -m coverage html
open htmlcov/index.html
```

# Running Datadog Agent

```
export DD_SERVICE="advent-of-code-2025"
export DD_ENV="prod"
export DD_VERSION=0.1.0
export DD_TRACE_AGENT_URL=http://localhost:8136
export DD_GIT_COMMIT_SHA=$(git rev-parse HEAD)
export DD_GIT_REPOSITORY_URL=$(git config --get remote.origin.url | sed -e 's/:/\//' -e 's/^git@/https:\/\//' -e 's/\.git$//') 
export DD_PROFILING_ENABLE_CODE_PROVENANCE=true
export DD_PROFILING_STACK_V2_ENABLED=true
ddtrace-run -p python -m main -a
```

## Summary
![Results](https://github.com/clementgbcn/AdventOfCode2025/actions/workflows/check_results.yml/badge.svg)


## Results
|   Day | Star   |          Result |   Elapsed Time, ms |
|-------|--------|-----------------|--------------------|
|     1 | 1st    |            1081 |              1.612 |
|     1 | 2nd    |            6689 |              1.719 |
|       |        |                 |                    |
|     2 | 1st    |     24747430309 |              0.389 |
|     2 | 2nd    |     30962646823 |           1245.22  |
|       |        |                 |                    |
|     3 | 1st    |           17443 |              2.468 |
|     3 | 2nd    | 172167155440541 |            144.627 |
|       |        |                 |                    |
|     4 | 1st    |            1389 |             15.971 |
|     4 | 2nd    |            9000 |            285.402 |
