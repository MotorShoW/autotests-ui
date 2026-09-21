from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_title_to_have_text(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')

    def check_dashboard_is_opened(self):
        expect(self.page).to_have_url(self.url)
