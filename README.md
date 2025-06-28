A modular LLM Evaluation Framework built using Python and Robot Framework.

LLM RELIABILITY FRAMEWORK - LRF

> A modular LLM Evaluation Framework for validating, benchmarking, and comparing Large Language Models.

## Features

- Provider abstraction
- Validation engine
- Weighted scoring
- Configurable evaluation pipeline
- Benchmark execution
- Model comparison
- JSON and HTML reporting
- Robot Framework integration
- GitHub Actions CI

## Installation

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Run Evaluation

```bash
python cli/main.py \
    --provider fake \
    --prompt "Hello" \
    --expected "Hello"
```

## Documentation

- docs/getting_started.md
- docs/api_reference.md
- docs/architecture.md

## License

MIT