import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker
import random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()
options = Options()
options.add_experimental_option('detach', True)


def generate_fake_user():
    return {"first name": faker.first_name(), "last name": faker.last_name(), "email": faker.email(),
            "Current Address": faker.address(), "Subjects": ["Maths", "Biology", "Physics", "Chemistry"]}


TEST_DATA = generate_fake_user()


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


def test_registration_form(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.XPATH, '//*[@placeholder="First Name"]')
    first_name.send_keys(TEST_DATA['first name'])
    last_name = driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]')
    last_name.send_keys(TEST_DATA['last name'])
    genders = driver.find_elements(By.XPATH, '//label[@for="gender-radio-1" or @for="gender-radio-2"'
                                             ' or @for="gender-radio-3"]')
    random_choice = random.choice(genders)
    random_choice.click()
    email = driver.find_element(By.XPATH, '//*[@id="userEmail"]')
    email.send_keys(TEST_DATA['email'])
    phone = driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number"]')
    phone.send_keys(str(random.randint(10 ** 9, 10 ** 10 - 1)))
    birthday = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
    birthday.click()
    birthday_month = driver.find_elements(By.CLASS_NAME, 'react-datepicker__month-select')
    random_month = random.choice(birthday_month)
    random_month.click()
    birthday_year = driver.find_elements(By.CLASS_NAME, 'react-datepicker__year-select')
    random_year = random.choice(birthday_year)
    random_year.click()
    birthday_day = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day')
    random_day = random.choice(birthday_day)
    random_day.click()
    address = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    address.send_keys(TEST_DATA['Current Address'])
    subjects = driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
    subjects.send_keys('a')
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'subjects-auto-complete__menu-list')))
    submenu = wait.until((EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-2-option-0"]'))))
    submenu.click()

    hobbies = driver.find_elements(By.XPATH, '//label[@for="hobbies-checkbox-1" or @for="hobbies-checkbox-2"'
                                             ' or @for="hobbies-checkbox-3"]')
    random.choice(hobbies).click()
    state = driver.find_element(By.XPATH, '//*[@class=" css-1wa3eu0-placeholder"]')
    state.click()
    state_element = driver.find_element(By.XPATH, '//*[@id="react-select-3-option-1"]')
    state_element.click()
    city = driver.find_element(By.XPATH, '//*[@class=" css-1wa3eu0-placeholder"]')
    city.click()
    city_element = driver.find_element(By.XPATH, '//*[@id="react-select-4-option-1"]')
    city_element.click()
    submit_btn = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_btn.click()
    modal_body = driver.find_element(By.CLASS_NAME, 'modal-body')
    print(modal_body.text)
