from locators import search_page as loc
from .base_page import BasePage


class SearchPage(BasePage):

    page_url = '/website/search?search=&order=name+asc'

    def __init__(self, page):
        super().__init__(page)

    def enter_word_to_search_field(self, check_word):
        search_field = self.find(loc.search_field_loc)
        search_field.fill(check_word)
        search_field.press('Enter')

    def check_all_found_words(self, check_word):
        names = [el.inner_text() for el in self.find(loc.all_elements_loc).all()]
        assert all(check_word in element.text for element in names)

    def choose_filter_by_category(self):
        self.page.get_by_role('presentation').hover()
        self.page.wait_for_selector(loc.desks_category_loc, state='visible', timeout=2000)
        self.find(loc.desks_category_loc).click()

    def sign_in(self):
        sign_in_btn = self.find(loc.sign_in_btn_loc)
        sign_in_btn.click()
