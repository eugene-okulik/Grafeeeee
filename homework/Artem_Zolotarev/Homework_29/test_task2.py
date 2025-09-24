from playwright.sync_api import Page, expect, BrowserContext


def test_is_enabled(page: Page, context: BrowserContext):

    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    clicker = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        clicker.click()

    new_page = new_page_event.value
    expect(new_page.locator('#result-text')).to_have_text('I am a new page in a new tab')
    expect(clicker).to_be_enabled()
