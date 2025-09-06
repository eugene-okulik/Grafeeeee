import requests
import allure
from test_api_artem_zolotarev.endpoint.endpoint import Endpoint


class UpdatePostByPut(Endpoint):

    @allure.step('Changes data in post by method put')
    def makes_changes_method_put(self, payload, new_object):
        self.response = requests.put(f'{self.url}/{new_object}', json=payload)
