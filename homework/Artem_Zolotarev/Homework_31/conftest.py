import random
import string
from faker import Faker
import pytest
from pages.desk_categories import DeskCategories
from pages.fill_address_form import FillAddressForm
from pages.login_page import LoginPage
from pages.office_design_software import OfficeDesignSoftware
from pages.order_overview import OrderOverview
from pages.search_page import SearchPage


@pytest.fixture()
def generate_random_pass(length: int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


@pytest.fixture()
def faker():
    return Faker('en_US')


@pytest.fixture()
def office_design_software(page):
    return OfficeDesignSoftware(page)


@pytest.fixture()
def order_overview(page):
    return OrderOverview(page, expected_values=6)


@pytest.fixture()
def fill_address_form(page, faker):
    return FillAddressForm(page, faker)


@pytest.fixture()
def search_page(page):
    return SearchPage(page)


@pytest.fixture()
def page_login_form(page):
    return LoginPage(page)


@pytest.fixture()
def category_desk(page):
    return DeskCategories(page)
