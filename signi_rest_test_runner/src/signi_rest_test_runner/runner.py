import sys
import os

# Add the current file's directory to sys.path if needed
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from signi_rest_test_runner.scenario_loader import load_scenario
# Make sure executor.py exists in the signi_rest_test_runner package.
# If the file is named differently, update the import accordingly.
from signi_rest_test_runner.executor import execute_scenario
from signi_rest_test_runner.validator import validate_response


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m signi_rest_test_runner.runner <test_config.yaml>")
        sys.exit(1)

    scenario_path = sys.argv[1]
    try:
        scenario = load_scenario(scenario_path)
        results = execute_scenario(scenario)

        print("✅ Test execution completed.")
        for result in results:
            print(result)
    except Exception as e:
        print(f"❌ Error during test execution: {e}")

if __name__ == "__main__":
    main()
