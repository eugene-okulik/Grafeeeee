from playwright.sync_api import Page, expect
from locators import desk_categories as loc
from .base_page import BasePage


class DeskCategories(BasePage):

    page_url = '/shop/category/desks-1'

    def __init__(self, page: Page):
        super().__init__(page)
        self.list_prices_before_filtered = None
        self.list_prices_after_filtered = None

    def get_item_by_filter_category_desk(self):
        get_list_elements = self.find(loc.get_list_elements_loc).all()
        for item in get_list_elements:
            assert any(word in item.inner_text().lower() for word in ('desk', 'table')), \
                f'{item.inner_text()} does not include "desk" or "table"'

    def get_prices_before(self):
        get_price_for_each_card = self.find(loc.get_price_for_each_card_loc).all()
        self.list_prices_before_filtered = [float(i.inner_text().replace(',', '')) for i in get_price_for_each_card]

    def click_price_filter(self):
        self.find(loc.filter_price_loc).click()
        self.find(loc.filter_low_to_high_loc).click()

    def get_prices_after(self):
        get_price_after_filtered = self.find(loc.get_price_after_filtered_loc).all()
        self.list_prices_after_filtered = [float(i.inner_text().replace(',', '')) for i in get_price_after_filtered]

    def compare_received_values(self):
        assert self.list_prices_after_filtered == sorted(self.list_prices_before_filtered)

    def get_min_value(self, test_value: str):
        min_value_for_enter = self.find(loc.min_value_for_enter_loc)
        min_value = self.find(loc.min_value_loc)
        min_value.click()
        min_value_for_enter.fill(test_value)
        min_value_for_enter.press('Enter')

    def check_price_of_received_items(self, test_value):
        elements = self.find(loc.elements_loc).all()
        elements_price = [float(el.inner_text().replace(',', '')) for el in elements]
        assert [i > float(test_value) for i in elements_price]

    def go_to_search_result(self):
        cards = (self.find(loc.all_cards_loc)).all()
        all_cards = len(cards)
        search_field = self.find(loc.search_field_loc)
        search_field.fill('table')
        search_field.press('Enter')
        expect(self.find(
            '//div[@class="oe_product_image position-relative h-100 flex-grow-0 overflow-hidden"]')
        ).not_to_have_count(all_cards)

    def switch_to_new_tab_and_get_text(self):
        with self.page.context.expect_event('page') as new_page_event:
            self.find(loc.inner_info_loc).click(modifiers=['Control'])
        new_page = new_page_event.value
        new_page.wait_for_load_state('load')
        new_page.locator(loc.text_loc).wait_for()
        self.text = new_page.locator(loc.text_loc).inner_text()
        new_page.close()

    def get_text_to_check(self):
        return self.text

    def add_item_to_cart(self):
        self.find(loc.element_loc).hover()
        self.find(loc.element_loc).click()
        btn_go_to_cart = self.find(loc.btn_go_to_cart_loc)
        btn_go_to_cart.click()
