import allure
from selene.support.shared import browser
from selene import be, have
from random import randint
from pages.google_page_base import GooglePageBase


class GoogleMainPage(GooglePageBase):
    url = "https://google.com"

    @allure.step("Открыть главную страницу Google")
    def open(self):
        browser.open(self.url)
        return self


class GoogleResultsPage(GooglePageBase):
    url = "https://google.com/search?q={SEARCH_QUERY}"

    def __init__(self, search_query):
        self.search_query = search_query

    @allure.step("Открыть страницу результатов поиска Google")
    def open(self, search_query):
        browser.open(self.url.format(SEARCH_QUERY=search_query))
        return self

