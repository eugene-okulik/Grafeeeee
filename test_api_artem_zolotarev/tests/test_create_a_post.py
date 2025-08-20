import pytest
from test_api_artem_zolotarev.conftest import update_put_method_endpoint, update_patch_method_endpoint

TEST_DATA = [
    {'name': 'first object', 'id': 1, 'data': {'color': 'red', 'size': 'small'}},
    {'name': 'second object', 'id': 1, 'data': {'color': 'white', 'size': 'big'}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_new_object(create_post_endpoint, looping_test, data, before_after):
    create_post_endpoint.create_new_post(data)
    create_post_endpoint.check_response_status_code_is_correct()


def test_delete_object(delete_post_endpoint, new_object, before_after):
    delete_post_endpoint.delete_post(new_object)
    delete_post_endpoint.check_response_status_code_is_correct()


@pytest.mark.critical
def test_put_object(update_put_method_endpoint, new_object, before_after):
    payload = {"name": 'updated object by put method',
               'id': 100, 'data': {'color': 'white', 'size': 'medium'}}
    update_put_method_endpoint.makes_changes_method_put(payload, new_object)
    update_put_method_endpoint.check_response_title_is_correct(payload['name'])


@pytest.mark.medium
def test_patch_object(update_patch_method_endpoint, new_object, before_after):
    payload = {'name': 'an updated object using patch'}
    update_patch_method_endpoint.makes_changes_method_patch(payload, new_object)
    update_patch_method_endpoint.check_response_title_is_correct(payload['name'])
