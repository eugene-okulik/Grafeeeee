import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_hover(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    cards = driver.find_elements(By.CSS_SELECTOR, 'a.oe_product_image_link span img')
    cart_of_cards = driver.find_elements(By.CSS_SELECTOR, 'span.fa.fa-shopping-cart')
    actions.move_to_element(cards[0]).click(cart_of_cards[0]).perform()
    text_card = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           'strong.product-name.product_display_name')))
    assert (cards[0].get_attribute('alt')) in text_card.text
