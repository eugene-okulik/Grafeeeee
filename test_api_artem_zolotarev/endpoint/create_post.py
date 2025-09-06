import requests
import allure
from test_api_artem_zolotarev.endpoint.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step('Create a post')
    def create_new_post(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.json = self.response.json()
        return self.response
