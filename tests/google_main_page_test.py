import allure
from pages.google_main_page import GoogleMainPage
from faker import Faker


@allure.suite("Google Main Page")
class TestGoogleMainPage:
    @allure.feature("Google Main Page Input")
    class TestGoogleMainPageInput:
        Faker.seed()
        faker_item = Faker("ru_RU")
        search_text = faker_item.text(max_nb_chars=40)

        @allure.title("Empty Search Input Test")
        def test_empty_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            assert google_main_page.search_input_is_empty()
            assert google_main_page.search_input_have_not_cross()

        @allure.title("Filled Search Input Test")
        def test_filled_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            assert google_main_page.search_input_is_not_empty()
            assert google_main_page.search_input_have_cross()

        @allure.title("Cleared Search Input Test")
        def test_clear_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.clear_search_input()
            assert google_main_page.search_input_is_empty()
            assert google_main_page.search_input_have_not_cross()
