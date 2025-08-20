import requests
import allure
from test_api_artem_zolotarev.endpoint.endpoint import Endpoint


class UpdatePostByPatch(Endpoint):

    @allure.step('Changes data in post by method patch')
    def makes_changes_method_patch(self, payload, new_object):
        self.response = requests.patch(f'{self.url}/{new_object}', json=payload)
