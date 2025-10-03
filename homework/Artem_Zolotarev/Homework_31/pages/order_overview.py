from .base_page import BasePage
from locators import order_overview as loc
from playwright.sync_api import expect


class OrderOverview(BasePage):

    page_url = '/shop/cart'

    def __init__(self, page, expected_values):
        super().__init__(page)

    def check_get_added_element(self, expected_values):
        expect(self.find(loc.adding_element_after_loc)).to_have_text(expected_values)

    def check_title_added_element(self, text):
        expect(self.find(loc.order_text_loc)).to_have_text(text)

    def check_quantity_added_element(self, expected_values):
        expect(self.find(loc.order_total_quantity_loc)).to_have_attribute('value', str(expected_values))

    def check_item_text(self, text):
        expect(self.find(loc.check_text_loc)).to_have_text(text)

    def click_button_checkout(self):
        self.find(loc.checkout_loc).click()
