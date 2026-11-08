import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check visible dashboard toolbar with text "{title}"')
    def check_visible(self, title):
        self.title.check_visible()
        self.title.check_have_text(title)
