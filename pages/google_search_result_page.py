import allure
from selene.support.shared import browser
from selene import be, have
from random import randint


class GoogleMainPage:
    url = "https://google.com/search?q={SEARCH_QUERY}"

    @allure.step("Открытие страницы поиска Google")
    def open(self, search_query):
        browser.open(self.url.format(SEARCH_QUERY=search_query))
        return self

