from playwright.sync_api import expect
from .base_page import BasePage
from locators import login_form as loc


class LoginPage(BasePage):

    def validate_login_form_with_empty_pass_field(self, faker):
        email_field = self.find(loc.email_field_loc)
        email_field.fill(faker.email())
        email_field.press('Enter')
        pass_field = self.find(loc.pass_field_loc)
        expect(pass_field).to_have_js_property('validationMessage', 'Please fill out this field.')