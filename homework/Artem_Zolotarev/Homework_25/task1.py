import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


def test_id_name(driver):
    input_data = 'some_text'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.NAME, 'text_string')
    search_input.send_keys('some_text')
    search_input.click()
    search_input.send_keys(Keys.ENTER)
    result = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result.text == input_data
