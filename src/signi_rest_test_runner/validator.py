# ---- validator.py ----
def validate_scenario(results: list):
    for result in results:
        step_name = result['step']
        response = result['response']
        expected = result.get('assert', {})

        print(f"Validating step: {step_name}")

        if 'status_code' in expected:
            assert response['status_code'] == expected['status_code'], \
                (
                    f"{step_name}: Expected {expected['status_code']} "
                    f"but got {response['status_code']}"
                )

        if 'body' in expected:
            for key, val in expected['body'].items():
                actual = response['json'].get(key)
                assert actual == val, (
                    f"{step_name}: Expected body.{key} = {val}, got {actual}"
                )