from playwright.sync_api import expect
from locators import fill_in_address_form as loc
from .base_page import BasePage


class FillAddressForm(BasePage):

    page_url = '/shop/address'

    def __init__(self, page, faker):
        super().__init__(page)

    def fill_in_form_to_delivery(self, faker):
        fullname = self.find(loc.fullname_loc)
        fullname.fill(faker.name())
        email = self.find(loc.email_loc)
        email.fill(faker.email())
        phone = self.find(loc.phone_loc)
        phone.fill(faker.basic_phone_number())
        company_name = self.find(loc.company_name_loc)
        company_name.fill(faker.company())
        vat = self.find(loc.vat_loc)
        vat.fill('12521512')
        street = self.find(loc.street_loc)
        street.fill(faker.street_address())
        street2 = self.find(loc.street2_loc)
        street2.fill('None')
        city = self.find(loc.city_loc)
        city.fill(faker.city())
        zip = self.find(loc.zip_loc)
        zip.fill(faker.zipcode())
        self.find(loc.select_element_loc).select_option('190')
        self.find(loc.state_loc).select_option('108')
        btn_checkout = self.find(loc.btn_checkout_loc)
        btn_checkout.click()

    def check_text_to_confirm_order(self, text):
        expect(self.find(loc.confirm_order_loc)).to_have_text(text)