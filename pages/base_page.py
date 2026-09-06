from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def visit(self):
        self.page.goto(self.url, wait_until='domcontentloaded')

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload(wait_until='domcontentloaded')