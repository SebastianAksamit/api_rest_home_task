import json
import random
import time

allowed_http_statuses = (
    200, 201, 202, 204, 300, 301, 302, 400, 401, 403, 404, 500, 503, 502,
)


def print_beautified_json(json_as_dict):
    print('\n', json.dumps(json_as_dict, indent=4))


def get_random_http_status_code():
    return random.choice(allowed_http_statuses)


def randomize_string(prefix):
    """
    Adds random suffix to provided prefix (string)
    """
    return f'{prefix}-{time.time()}'
