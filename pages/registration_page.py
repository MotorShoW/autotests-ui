from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page,
                         'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        self.registration_form = RegistrationFormComponent(page)

        self.title_text = Text(page, 'authentication-ui-course-title-text', 'Title')
        self.registration_button = Button(
            page, 'registration-page-registration-button', 'Registration'
        )
        self.login_button = Link(page, 'registration-page-login-link', 'Login')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_form.fill(email, username, password)

    def click_registration_button(self):
        self.registration_button.check_enabled()
        self.registration_button.click()

    def click_login_button(self):
        self.login_button.click()

    def check_registration_button_is_disabled(self):
        self.registration_button.check_disabled()
