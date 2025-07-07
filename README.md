# signi_rest_test_runner

## 📌 Overview
A YAML-driven API test runner with support for variable extraction and assertion validation.

## ✅ Prerequisites
- Python 3.10 or higher
- `pip install -r requirements.txt`
- `uvicorn`, `fastapi`, `httpx`, `pyyaml`, `jinja2`, `jsonpath_ng`

## 🚀 Setup Instructions
```bash
git clone https://github.com/Nash-wa/signi_rest_test_runner.git
cd signi_rest_test_runner
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

🚀 Running the Sample API
uvicorn sample_api.main:app --reload

✅ Running the Test Runner
$env:PYTHONPATH="src"
python -m signi_rest_test_runner.runner test_config.yaml > test_results/output.log

📊 Test Coverage
Login and profile validation (mock endpoints)
Custom hello and status endpoints

❓ Known Issues
API token extraction only works with flat JSON.
No retry mechanism on failure.

✉️ Suggestions
Add HTML report generation
Add retry/backoff logic
