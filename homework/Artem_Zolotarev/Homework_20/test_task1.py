import pytest
import requests


@pytest.fixture()
def new_object():
    body = {'name': 'First object', "id": 1, "data": {"color": "white", "size": "big"}}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture(scope='session')
def looping_test():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.mark.smoke
@pytest.mark.parametrize('name', ['First object', 123, True])
def test_new_object(name, looping_test, before_after):
    body = {f"name": name, "id": 1, "data": {"color": "red", "size": "small"}}
    response = requests.get(f'http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200


def test_delete_object(new_object, before_after):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.critical
def test_get_object_by_id(new_object, before_after):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.medium
def test_put_object(new_object, before_after):
    body = {"name": "an updated object using put", "id": 1, "data": {"color": "red", "size": "small"}}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object}', json=body)
    assert response.json()['name'] == 'an updated object using put', 'Status code is incorrect'


def test_patch_object(new_object, before_after):
    body = {"name": 'an updated object using patch'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object}', json=body)
    assert response.json()['name'] == 'an updated object using patch', 'Status code is incorrect'
