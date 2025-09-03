import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_get_picked_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    list_language = driver.find_element(By.XPATH, '//select')
    select = Select(list_language)
    select.select_by_visible_text('Python')
    btn_submit = driver.find_element(By.ID, 'submit-id-submit')
    btn_submit.click()
    text = driver.find_element(By.ID, 'result-text')
    assert text.text == 'Python'


def test_get_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    btn = driver.find_element(By.XPATH, '//button')
    btn.click()
    wait = WebDriverWait(driver, 20)
    text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))
    assert text.text == 'Hello World!'
