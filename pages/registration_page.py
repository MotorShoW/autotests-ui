from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page,
                         'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        self.registration_form = RegistrationFormComponent(page)

        self.title_text = page.get_by_test_id('authentication-ui-course-title-text')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_button = page.get_by_test_id('registration-page-login-link')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_form.fill(email, username, password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()

    def check_registration_button_is_disabled(self):
        expect(self.registration_button).to_be_disabled()
