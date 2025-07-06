# Directory Structure:
# rest_api_test_runner/
# ├── runner.py
# ├── scenario_loader.py
# ├── executor.py
# ├── validator.py
# ├── utils.py
# └── scenarios/example.yaml

# ---- runner.py ----
import sys
from src.signi_rest_test_runner.scenario_loader import load_scenario
from src.signi_rest_test_runner.executor import execute_scenario
from src.signi_rest_test_runner.validator import validate_scenario


if __name__ == '__main__':
    scenario_path = (
        sys.argv[1] if len(sys.argv) > 1 else "scenarios/example.yaml"
    )
    scenario = load_scenario(scenario_path)
    results = execute_scenario(scenario)
    validate_scenario(results)

