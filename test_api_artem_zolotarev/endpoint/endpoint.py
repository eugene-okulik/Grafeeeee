import allure


class Endpoint:
    response = None
    url = 'http://objapi.course.qa-practice.com/object'
    json = None

    @allure.step('Checking status code')
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Checking name')
    def check_response_title_is_correct(self, name):
        assert self.response.json()['name'] == name
