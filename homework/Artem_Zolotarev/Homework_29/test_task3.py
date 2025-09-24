from playwright.sync_api import Page, expect


def test_change_color(page: Page):

    page.goto('https://demoqa.com/dynamic-properties')
    color_bnt = page.locator('#colorChange')
    expect(color_bnt).to_have_css('color', 'rgb(220, 53, 69)')
    color_bnt.click()
