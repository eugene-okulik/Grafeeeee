import pytest
from test_api_artem_zolotarev.endpoint.create_post import CreatePost
from test_api_artem_zolotarev.endpoint.delete_post import DeletePost
from test_api_artem_zolotarev.endpoint.update_method_patch import UpdatePostByPatch
from test_api_artem_zolotarev.endpoint.update_method_put import UpdatePostByPut


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_put_method_endpoint():
    return UpdatePostByPut()


@pytest.fixture()
def update_patch_method_endpoint():
    return UpdatePostByPatch()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


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


@pytest.fixture()
def new_object(create_post_endpoint, delete_post_endpoint):
    payload = {'name': 'First object', 'id': 1, 'data': {'color': 'white', 'size': 'big'}}
    create_post_endpoint.create_new_post(payload)
    post_id = create_post_endpoint.json['id']
    yield post_id
    delete_post_endpoint.delete_post(post_id)
