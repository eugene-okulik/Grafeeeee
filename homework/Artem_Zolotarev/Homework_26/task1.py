from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_card(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')
    cards = driver.find_elements(By.CSS_SELECTOR, '[class="oe_product_image_link '
                                                  'd-block h-100 position-relative"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(cards[0]).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    btn_continue = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-secondary')))
    btn_continue.click()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-shopping-cart.fa-stack').click()
    assert 'Customizable Desk' in driver.find_element(By.TAG_NAME, 'h6').text
