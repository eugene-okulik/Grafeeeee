from playwright.sync_api import Page
from .base_page import BasePage
from locators import office_design_software as loc


class OfficeDesignSoftware(BasePage):

    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def __init__(self, page: Page):
        super().__init__(page)
        self.adding_element_before = None
        self.initial_quan_value = None

    def button_adding_element(self):
        self.find(loc.btn_add_cart_loc).click()

    def add_limit_quantity(self, clicks):
        for _ in range(clicks):
            self.find(loc.add_quantity_loc).click()

    def get_quantity(self):
        self.initial_quan_value = self.find(loc.quantity_loc).input_value()
        return self.initial_quan_value

    def get_element_text_before(self):
        self.adding_element_before = self.find(loc.adding_element_before_loc)
        return self.adding_element_before.inner_text()

    def click_btn_view_to_cart(self):
        self.find(loc.btn_view_cart_loc).click()

    def add_cart(self):
        self.find(loc.btn_add_cart_loc).click()

    def go_to_cart(self):
        self.find(loc.cart_loc).click()

    def check_indicator_addition_to_cart(self):
        cart_indicator = self.find(loc.cart_indicator_loc)
        cart_indicator_text = cart_indicator.inner_text()
        self.find(lambda x: self.find(
            ".my_cart_quantity.badge.text-bg-primary.position-absolute.top-0.end-0.mt-n1.me-n1.rounded-pill"
        ).text_content() != cart_indicator_text)
        cart_indicator.click()
