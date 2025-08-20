import requests
import allure
from test_api_artem_zolotarev.endpoint.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('Delete a post by id')
    def delete_post(self, new_object):
        self.response = requests.delete(f'{self.url}/{new_object}')
