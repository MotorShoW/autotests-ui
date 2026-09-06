from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page,
                         'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        self.title_text = page.get_by_test_id('authentication-ui-course-title-text')
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_button = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()

    def check_registration_button_is_disabled(self):
        expect(self.registration_button).to_be_disabled()
