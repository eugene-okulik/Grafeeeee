import json
import re

from playwright.sync_api import Page, expect, Route


def test_item_title(page: Page):
    def handle_changer(route: Route):
        response = route.fetch()
        body = response.json()
        if body['body']['digitalMat'][0]['familyTypes'][0]['productName']:
            body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
            route.fulfill(
                status=response.status,
                headers=response.headers,
                body=json.dumps(body)
            )
    page.route(re.compile('path=library'), handle_changer)
    page.goto('https://www.apple.com/shop/buy-iphone', wait_until="networkidle")
    page.locator("(//*[@class='rf-hcard-img'])[1]").click()
    expect(page.locator(
        "(//*[@class='rf-digitalmat-overlay-header typography-manifesto'])[1]")).to_have_text('яблокофон 17 про')
