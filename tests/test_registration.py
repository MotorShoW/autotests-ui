import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit()
    registration_page.fill_registration_form(
        email='user.name@gmail.com',
        username='username',
        password='password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_is_opened()
    dashboard_page.check_dashboard_title_to_have_text()
