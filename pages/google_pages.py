import allure
from selene.support.shared import browser
from selene import be, have
from random import randint
from pages.google_page_base import GooglePageBase


class GoogleMainPage(GooglePageBase):
    url = "https://google.com"
    FORM_SEARCH_BUTTON = "//*[@jsname='VlcLAe']//*[@name='btnK']"
    SUGGEST_SEARCH_BUTTON = "//*[@jsname='aajZCb']//*[@name='btnK']"

    @allure.step("Открыть главную страницу Google")
    def open(self):
        browser.open(self.url)
        return self


class GoogleResultsPage(GooglePageBase):
    url = "https://google.com/search?q={SEARCH_QUERY}"
    SEARCH_RESULTS = "#search"

    def __init__(self, search_query):
        self.search_query = search_query

    @allure.step("Открыть страницу результатов поиска Google")
    def open(self, search_query):
        browser.open(self.url.format(SEARCH_QUERY=search_query))
        return self

    @allure.step("Видны результаты поиска")
    def search_results_are_visible(self):
        search_results = browser.element(self.SEARCH_RESULTS)
        search_results.should(be.visible)
        return search_results


