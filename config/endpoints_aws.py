base_url = 'http://3.91.6.249'

always_ok = f'{base_url}/ok'
animals = f'{base_url}/animals'


def echo_status(status_code):
    return f'{base_url}/echostatus/{status_code}'


def animal_with_id(animal_id):
    return f'{animals}/{animal_id}'
