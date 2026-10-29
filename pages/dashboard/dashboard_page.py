from playwright.sync_api import Page, expect

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url='https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.students_chart = ChartViewComponent(page, identifier="students", chart_type='bar')
        self.courses_chart = ChartViewComponent(page, identifier="courses", chart_type='pie')
        self.activities_chart = ChartViewComponent(page, identifier="activities", chart_type='line')
        self.scores_chart = ChartViewComponent(page, identifier="scores", chart_type='scatter')

    def check_visible_dashboard_title(self):
        self.dashboard_toolbar.check_visible('Dashboard')

    def check_visible_students_chart(self):
        self.students_chart.check_visible('Students')

    def check_visible_courses_chart(self):
        self.courses_chart.check_visible('Courses')

    def check_visible_activities_chart(self):
        self.activities_chart.check_visible('Activities')

    def check_visible_scores_chart(self):
        self.scores_chart.check_visible('Scores')

    def check_dashboard_is_opened(self):
        expect(self.page).to_have_url(self.url)