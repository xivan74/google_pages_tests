import allure
import pytest

from pages.google_main_page import GoogleMainPage
from faker import Faker


@allure.suite("Главная страница Google")
class TestGoogleMainPage:

    @allure.feature("Поле поиска на главной странице")
    class TestGoogleMainPageInput:
        Faker.seed()
        faker_item = Faker("ru_RU")
        search_text = faker_item.word()

        @allure.title("Тест пустого поля поиска")
        def test_empty_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.search_input_is_empty()
            google_main_page.search_input_has_no_cross()
            google_main_page.search_input_suggest_list_not_visible()

        @allure.title("Тест заполнения поля поиска")
        def test_filled_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.search_input_is_not_empty()
            google_main_page.search_input_has_cross()
            google_main_page.search_input_suggest_list_is_visible()

        @allure.title("Тест очистки поля поиска")
        def test_clear_search_box(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.clear_search_input()
            google_main_page.search_input_is_empty()
            google_main_page.search_input_has_no_cross()
            google_main_page.search_input_suggest_list_not_visible()

        @allure.title("Тест клика в случайную подсказку")
        def test_click_on_suggest_item(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.search_input_suggest_list_is_visible()
            item_text = google_main_page.click_to_any_suggest_list_item()
            google_main_page.search_input_have_correct_text(item_text.lower())

        @allure.title("Тест ховера на случайной подсказке")
        def test_hover_on_suggest_item(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.fill_search_input(text=self.search_text)
            google_main_page.search_input_suggest_list_is_visible()
            item = google_main_page.hover_to_any_suggest_list_item()
            google_main_page.list_item_is_highlighted(item)
            google_main_page.single_list_item_is_highlighted_only()

        @allure.title("Тест появления истории поиска")
        @pytest.mark.skip
        def test_add_item_to_search_history(self):
            google_main_page = GoogleMainPage()
            google_main_page.open()
            google_main_page.click_to_search_input()
            google_main_page.search_input_history_list_not_visible()
            google_main_page.make_search(text=self.search_text)
            google_main_page.search_results_are_visible()
            google_main_page.open()
            google_main_page.click_to_search_input()
            google_main_page.search_input_history_list_is_visible()

