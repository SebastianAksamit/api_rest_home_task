import random

import pytest
import requests

from config import endpoints_aws
from utils.helpers import randomize_string


@pytest.fixture
def animal_id():
    animal_body = {
        'name': randomize_string('BAZZ-animal'),
        'kind': randomize_string('Coracias garrulus'),
        'age': random.randint(1, 100)
    }
    create_animal_response = requests.post(endpoints_aws.animals, json=animal_body)
    created_animal_id = create_animal_response.json()['id']
    return created_animal_id
