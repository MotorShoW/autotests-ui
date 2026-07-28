from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    storage = context.storage_state(path='state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверка заголовка
    courses_empty_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_empty_header).to_be_visible()
    expect(courses_empty_header).to_have_text('Courses')

    # Проверка иконки
    courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon).to_be_visible()

    # Проверка блока
    courses_empty_list = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_list).to_be_visible()
    expect(courses_empty_list).to_have_text('There is no results')

    # Проверка описания блока
    courses_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_description).to_be_visible()
    expect(courses_empty_description).to_have_text('Results from the load test pipeline will be displayed here')
