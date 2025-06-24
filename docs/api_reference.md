# API Reference

## EvaluationEngine

```python
engine = EvaluationEngine(
    provider_name="openai",
    validator_names=["exact_match"],
    provider_file="config/providers.yaml",
    profile_name="default",
    profile_file="config/profiles.yaml",
)
```

### evaluate()

```python
result = engine.evaluate(
    request,
    expected,
)
```

Returns

```
EvaluationResult
```

---

## BenchmarkRunner

```python
runner = BenchmarkRunner(engine)
results = runner.run(dataset)
```

---

## BenchmarkEngine

```python
summary = BenchmarkEngine().summarize(...)
```

Returns

```
BenchmarkSummary
```

---

## ComparisonEngine

```python
comparison = ComparisonEngine().compare(...)
```

Returns

```
ModelComparison
```

---

## Reporters

Supported reporters

- JsonReporter
- BenchmarkJsonReporter
- BenchmarkHtmlReporter
- ModelComparisonReporter