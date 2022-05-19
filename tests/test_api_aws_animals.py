import random
import requests
from config import endpoints_aws
from utils.helpers import randomize_string


def test_create_new_animal_and_get_animal_details():
    """
    1. Create new animal by sending POST /animals with JSON
    2. Assert response code 200
    3. Extract created animal ID from response
    4. GET /animals/ID
    5. Assert response code and animal details are correct
    """
    animal_body = {
        'name': randomize_string('XC-animal'),
        'kind': randomize_string('coco'),
        'age': random.randint(1, 100)
    }
    create_animal_response = requests.post(endpoints_aws.animals, json=animal_body)
    assert create_animal_response.status_code == 200
    created_animal_id = create_animal_response.json()['id']

    animal_details_response = requests.get(endpoints_aws.animal_with_id(created_animal_id))
    assert animal_details_response.status_code == 200

    animal_details_response_dict = animal_details_response.json()
    assert animal_details_response_dict['name'] == animal_body['name']
    assert animal_details_response_dict['kind'] == animal_body['kind']
    assert animal_details_response_dict['age'] == animal_body['age']


def test_delete_animal(animal_id):
    delete_animal_response = requests.delete(endpoints_aws.animal_with_id(animal_id))
    assert delete_animal_response.status_code == 204

    animal_details_response = requests.get(endpoints_aws.animal_with_id(animal_id))
    assert animal_details_response.status_code == 404
    assert animal_details_response.json() == ''


def test_create_new_animal_and_actualise_animal_details(animal_id):
    """
    1. Create new animal and extract ID by fixture
    2. Update by sending PUT /animals/ID
    3. Assert response code 202
    4. Get updated details
    5. Assert updated animal details are correct
    """

    update_animal_body = {
        'name': randomize_string('NOD-animal'),
        'kind': randomize_string('giraffe'),
        'age': random.randint(1, 100)
    }

    update_animal_details_response = requests.put(endpoints_aws.animal_with_id(animal_id),
                                                  json=update_animal_body)
    assert update_animal_details_response.status_code == 202

    animal_details_response_after_update = requests.get(endpoints_aws.animal_with_id(animal_id))
    assert animal_details_response_after_update.json()['kind'] == update_animal_body['kind']


def test_create_new_animal_and_check_id_on_list_of_animals(animal_id):
    """
    1. Create new animal and extract ID by fixture
    2. Get details
    3. Assert response code 200
    4. Get list of animals
    5. Verify ID is on the list
    5. Assert result is not empty
    """
    def find_element_in_list(element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return None

    animal_details_response = requests.get(endpoints_aws.animal_with_id(animal_id))
    assert animal_details_response.status_code == 200

    animals_list_response = requests.get(endpoints_aws.animals).text

    animal_id_index = find_element_in_list(animal_id, animals_list_response)

    assert animal_id_index is not None
    # print(f'Index no. {animal_id_index}')
