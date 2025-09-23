from playwright.sync_api import Page, expect


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('#firstName').fill('Jack')
    page.locator('#lastName').fill('Sparrow')
    page.locator('#userEmail').fill('123@mail.ru')
    page.locator("(//*[@class='custom-control-label'])[2]").check()
    page.locator('#userNumber').fill('9156142142')
    page.locator('#dateOfBirthInput').click()
    page.locator("//select[@class='react-datepicker__month-select']").select_option(value='July')
    page.locator("//select[@class='react-datepicker__year-select']").select_option(value='1995')
    page.locator("//div[@class = 'react-datepicker__day react-datepicker__day--012']").click()
    page.locator('#subjectsInput').fill('a')
    page.locator('#react-select-2-option-2').click()
    page.locator("//label[@for='hobbies-checkbox-1']").check()
    page.locator('#currentAddress').fill('Moscow Patriki 001')
    page.get_by_text('Select State').click()
    page.locator('#react-select-3-option-3').click()
    page.get_by_text('Select City').click()
    page.locator('#react-select-4-option-1').click()
    page.get_by_role('button', name='Submit').click()
    expect(page.get_by_text('Thanks for submitting the form'))
