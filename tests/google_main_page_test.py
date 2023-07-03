import allure
from pages.google_main_page import GoogleMainPage
from faker import Faker


@allure.suite("Главная страница Google")
class TestGoogleMainPage:
    @allure.feature("Поле поиска на главной странице")
    class TestGoogleMainPageInput:
        Faker.seed()
        faker_item = Faker("ru_RU")
        search_text = faker_item.text(max_nb_chars=40)

        @allure.title("Тест пустого поля поиска")
        def test_empty_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.search_input_is_empty()
            google_main_page.search_input_has_no_cross()

        @allure.title("Тест заполнения поля поиска")
        def test_filled_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.search_input_is_not_empty()
            google_main_page.search_input_has_cross()

        @allure.title("Тест очистки поля поиска")
        def test_clear_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.clear_search_input()
            google_main_page.search_input_is_empty()
            google_main_page.search_input_has_no_cross()
