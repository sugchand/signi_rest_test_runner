
# ---- executor.py ----
import httpx
from jinja2 import Template
from jsonpath_ng import parse as jsonpath_parse

context = {}  # Global-like context for storing variables


def render_template(value):
    if isinstance(value, str):
        return Template(value).render(**context)
    elif isinstance(value, dict):
        return {k: render_template(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [render_template(i) for i in value]
    return value


def extract_variables(response, extract):
    body = response.json()
    for key, path in extract.items():
        jsonpath_expr = jsonpath_parse(path)
        match = jsonpath_expr.find(body)
        if match:
            context[key] = match[0].value


def execute_step(step: dict) -> dict:
    request = render_template(step['request'])
    method = request['method'].upper()
    url = request['url']

    client = httpx.Client()
    response = client.request(
        method=method,
        url=url,
        headers=request.get('headers'),
        json=request.get('body')
    )

    if 'extract' in step:
        extract_variables(response, step['extract'])

    return {
        'step': step['name'],
        'request': request,
        'response': {
            'status_code': response.status_code,
            'json': response.json()
        }
    }


def execute_scenario(scenario: dict) -> list:
    return [execute_step(step) for step in scenario['steps']]