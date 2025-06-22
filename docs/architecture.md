# EvalForge Architecture

```
                   CLI
                    │
                    ▼
          EvaluationEngine
                    │
                    ▼
         EvaluationPipeline
                    │
 ┌──────────────────┼──────────────────┐
 ▼                  ▼                  ▼
Prompt Step   Provider Step    Validation Step
                                        │
                                        ▼
                               Scoring Step
                                        │
                                        ▼
                               Reporting Step
                                        │
                                        ▼
                             EvaluationResult
```

## Main Components

- ProviderFactory
- ProviderRegistry
- ValidationEngine
- ScoringEngine
- BenchmarkRunner
- ComparisonEngine
- Reporters

## Configuration

```
providers.yaml
profiles.yaml
pipeline.yaml
benchmark_suite.yaml
```