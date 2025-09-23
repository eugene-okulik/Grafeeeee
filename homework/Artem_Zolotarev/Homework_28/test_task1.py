import re
from playwright.sync_api import Page, expect


def test_authentication(page: Page):
    page.goto(' https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role("textbox", name='Username')
    username.fill('Ivan007')
    password = page.get_by_role('textbox', name='password')
    password.fill('700navI')
    btn_submit = page.get_by_role('button', name='Login')
    btn_submit.click()
    expect(page.get_by_role('generic', name=re.compile('Your username is invalid!')))
