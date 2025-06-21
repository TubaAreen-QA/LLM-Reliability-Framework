# Getting Started

## Installation

```bash
git clone https://github.com/<username>/LLM-RELIABILITY-FRAMEWORK.git

cd EvalForge

pip install -r requirements.txt
```

---

## Running a single evaluation

```bash
python cli/main.py \
    --provider fake \
    --prompt "Hello" \
    --expected "Hello" \
    --validators exact_match
```

---

## Running a benchmark

```bash
python cli/benchmark.py \
    --suite config/benchmark_suite.yaml
```

---

## Generating reports

Reports are written to

```
reports/
```

Supported formats

- JSON
- HTML

---

## Running tests

```bash
pytest
```

---

## Repository Structure

```
framework/
providers/
validators/
reporters/
Tests/
robot/
docs/
config/