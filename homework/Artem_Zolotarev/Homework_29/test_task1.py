from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    page.keyboard.press('Enter')
    expect(page.locator('#result-text')).to_have_text('Ok')
