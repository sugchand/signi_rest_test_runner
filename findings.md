# Findings & Debugging Log

## Issues Faced

1. ❌ `requirements.txt` not found initially.
   - 🔧 Fixed by manually creating the file using installed packages.

2. ❌ `poetry install` failed.
   - 🔧 Installed dependencies manually using `pip`.

3. ❌ Uvicorn `ModuleNotFoundError: No module named 'sample_api'`
   - 🔧 Created `sample_api/main.py` with FastAPI endpoints.

4. ❌ Test Runner couldn't detect `runner.py`.
   - 🔧 Ensured correct PYTHONPATH (`$env:PYTHONPATH="src"`).
   - 🔧 Ensured `__init__.py` exists.

5. ❌ `ModuleNotFoundError` for `httpx`, `jinja2`, `jsonpath_ng`
   - 🔧 Installed all via pip.

## Observations
- 📂 Project lacks `requirements.txt`, need to generate it.
- 🧪 `runner.py` works once `PYTHONPATH` is correctly set and all dependencies are installed.
Missing modules resolved with pip install and poetry add

PYTHONPATH set to ensure src/ is included in module resolution

Scenario YAML paths clarified and corrected in config

Added better structured example APIs with /hello and /status

Runner now correctly interprets scenario YAML and API base URL
```markdown
# Debugging Findings

## Issues Faced
- Virtual environment was misconfigured.
- PYTHONPATH not set correctly.
- Imports failed due to missing `__init__.py`.
- Initial errors with `ModuleNotFoundError` for httpx, jinja2, jsonpath_ng.
- Relative import (`from .executor`) was needed.
- `test_config.yaml` not in correct path initially.

## Solutions Applied
- Created virtualenv in project root.
- Installed dependencies using `pip install -r requirements.txt`.
- Fixed import errors by adding `__init__.py` and using relative imports.
- Declared PYTHONPATH and executed runner as a module.
- Ensured FastAPI app is up before triggering the runner.