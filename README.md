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
|     1 | 1st    |            1081 |              1.565 |
|     1 | 2nd    |            6689 |              1.802 |
|       |        |                 |                    |
|     2 | 1st    |     24747430309 |              0.409 |
|     2 | 2nd    |     30962646823 |           1374.57  |
|       |        |                 |                    |
|     3 | 1st    |           17443 |              2.791 |
|     3 | 2nd    | 172167155440541 |            229.108 |
|       |        |                 |                    |
|     4 | 1st    |            1389 |             21.126 |
|     4 | 2nd    |            9000 |            304.058 |
|       |        |                 |                    |
|     5 | 1st    |             664 |             12.636 |
|     5 | 2nd    | 350780324308385 |              0.401 |
|       |        |                 |                    |
|     6 | 1st    |   4412382293768 |              1.557 |
|     6 | 2nd    |   7858808482092 |              2.085 |
