from pages.google_main_page import GoogleMainPage
from faker import Faker


class TestGoogleMainPage:
    Faker.seed()
    faker_item = Faker("ru_RU")
    search_text = faker_item.text(max_nb_chars=40)

    def test_empty_search_box(self):
        google_main_page = GoogleMainPage()
        google_main_page.open()
        assert google_main_page.search_input_is_empty() is True
        assert google_main_page.search_input_have_cross() is False

    def test_filled_search_box(self):
        google_main_page = GoogleMainPage()
        google_main_page.open()
        google_main_page.fill_search_input(text=self.search_text)
        assert google_main_page.search_input_is_empty() is False
        assert google_main_page.search_input_have_cross() is True

    def test_clear_search_box(self):
        google_main_page = GoogleMainPage()
        google_main_page.open()
        google_main_page.fill_search_input(text=self.search_text)
        google_main_page.clear_search_input()
        assert google_main_page.search_input_is_empty() is True
        assert google_main_page.search_input_have_cross() is False

