import requests


def new_object():
    body = {
        "id": 1,
        "name": 'First object',
        "data": {"color": "white", "size": "big"}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    return response.json()['id']


def get_object():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.json())


get_object()


def get_object_by_id(num: int):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{num}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.json())


get_object_by_id(1)


def post_object():
    body = {
        "id": 1,
        "name": 'First object',
        "data": {"color": "white", "size": "big"}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, 'Status code is incorrect'


def put_object():
    post_id = new_object()
    body = {
        "id": 1,
        "name": 'an updated object using put',
        "data": {"color": "red", "size": "small"}
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{post_id}', json=body)
    assert response.json()['name'] == 'an updated object using put', 'Status code is incorrect'
    print(response.json())
    clear(post_id)


put_object()


def patch_object():
    post_id = new_object()
    body = {
        "name": 'an updated object using patch',
    }
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{post_id}', json=body)
    assert response.json()['name'] == 'an updated object using patch', 'Status code is incorrect'
    print(response.json())
    clear(post_id)


patch_object()


def clear(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')

