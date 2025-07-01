# utils.py
import jinja2
import json
from jsonpath_ng.ext import parse as jsonpath_parse
from httpx import Response


def render_template(template: str, context: dict) -> str:
    return jinja2.Template(template).render(**context)


def extract_variables(response: Response, extract_config: dict, context: dict):
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("❌ Failed to parse JSON response during extraction")
        return

    for var_name, jsonpath_expr in extract_config.items():
        matches = jsonpath_parse(jsonpath_expr).find(data)
        if matches:
            context[var_name] = matches[0].value
            print(f"🔧 Extracted '{var_name}' = {context[var_name]}")
        else:
            print(
                f"⚠️  No match found for variable '{var_name}' "
                f"using path '{jsonpath_expr}'"
            )


def apply_assertions(response: Response, assertions: dict, context: dict):
    status_code = assertions.get("status_code")
    if status_code and response.status_code != status_code:
        print(
            f"❌ Assertion failed: expected status {status_code}, "
            f"got {response.status_code}"
        )
    else:
        print("✅ Status code assertion passed")

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("⚠️  Skipping body assertions: response is not JSON")
        return

    for key, expected in assertions.items():
        if key == "status_code":
            continue
        jsonpath_expr = jsonpath_parse(key)
        matches = jsonpath_expr.find(data)
        actual = matches[0].value if matches else None
        if actual != expected:
            print(
                f"❌ Assertion failed: {key} → expected {expected}, "
                f"got {actual}"
            )
        else:
            print(f"✅ Assertion passed: {key} = {expected}")
