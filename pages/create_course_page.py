from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)


    def check_visible_create_course_toolbar(self):
        self.create_course_toolbar.check_visible(title='Create course', is_create_course_disabled=True)

    def click_create_course_button(self):
        self.create_course_toolbar.click_create_course_button()

    def check_enabled_create_course_button(self):
        self.create_course_toolbar.check_visible(title='Create course', is_create_course_disabled=False)

    def check_disabled_create_course_button(self):
        self.create_course_toolbar.check_visible(title='Create course', is_create_course_disabled=True)

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.check_visible(title, estimated_time, description, max_score, min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.fill(title, estimated_time, description, max_score, min_score)

    def check_visible_exercises_title(self):
        self.create_exercise_toolbar.check_visible(title='Exercises')

    def click_create_exercise_button(self):
        self.create_exercise_toolbar.click_create_course_button()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises', description='Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        self.create_exercise_form.click_delete_button(index)

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        self.create_exercise_form.check_visible(index, title, description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        self.create_exercise_form.fill(index, title, description)
